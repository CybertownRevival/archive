#!/usr/bin/perl -w


#################################################################
# This Script is to control transfers in CT
# some functions bastardized from other routines.. lol
# Coolkama 24 march 2003
##################################################################


# Contains shared functions for all registration pages.
        &get_date;
        &parse_form;

# where the script logs are stored:
my $logfilepath = "/services/http/80/cgi-bin/cybertown/logs/";
my $logfilename = "bank_transfers.log";
my $transerrmess = "";
my $cmd_path = "/services/commserv/2000/bin/raudp -r 192.168.0.51:2035 -BSIROOT /services/commserv/2000";

my $MEM_NNM = $FORM{'MEM_NNM'};
my $TO_NNM = $FORM{'TO_NNM'};
my $TO_AMT = $FORM{'TO_AMT'};
my $FROM_HOM = $FORM{'FROM_HOM'};
my $TKT = $FORM{'TKT'};

# we want fingerprints:
#Turn the IP address into a readable domain name.
my $realip = $ENV{'REMOTE_ADDR'};
my $ip = $ENV{'REMOTE_HOST'};
my $n = `nslookup $ip | grep Name`; chop($n);
my $host=substr($n, rindex($n, " ")+1);    
my $period1=rindex($host,'.');
my $period2=rindex($host,'.',$period1-1);

my $remote_user =$ENV{'REMOTE_USER'};
my $remote_ident =$ENV{'REMOTE_IDENT'};

# get MEM_NNM's current Balance
my $cmd = "/services/commserv/2000/bin/raudp -r 192.168.0.51:2035 -BSIROOT /services/commserv/2000 DB G M NNM $MEM_NNM MON";
$SIG{ALRM} = \&timed_out;
eval {  
            alarm(16);  
            $response = `$cmd` || '';  
            alarm(0);  
};  
my ($code, $RES) = split(/\n/, $response);
chomp($code); chomp($RES);  
if ($code eq '0') {
	#convert MEM_NNM's hex balance to decimal
	$fromcash = hex($RES);
	
	if ($fromcash >= $TO_AMT) {
	
		# get TO_NNM's current Balance
		my $cmd = "/services/commserv/2000/bin/raudp -r 192.168.0.51:2035 -BSIROOT /services/commserv/2000 DB G M NNM $TO_NNM MON";
		$SIG{ALRM} = \&timed_out;
		eval {  
            alarm(16);  
            $response = `$cmd` || '';  
            alarm(0);  
		};  
		my ($code, $RES) = split(/\n/, $response);
		chomp($code); chomp($RES);  
		if ($code eq '0') {
			#convert TO_NNM's hex balance to decimal
			$tocash = hex($RES);
			# create new balance for MEM_NNM
			$fromcashnew = $fromcash - $TO_AMT;
			# create new balance for TO_NNM
			$tocashnew = $tocash + $TO_AMT;
			
			# convert new MEM_NNM balance to hex
			$fromcashnewh = sprintf("%x",$fromcashnew);
			# make sure hex value of MEM_NNM's balance is 8 digits long (text)
			if (length($fromcashnewh) < 8) {
				my $additions = 8 - length($fromcashnewh);
				for (my $i = 1;$i<=$additions;$i++) {
					$fromcashnewh = '0'.$fromcashnewh;
				}
			}	
			# convert new TO_NNM balance to hex
			$tocashnewh = sprintf("%x",$tocashnew);
			# make sure hex value of TO_NNM's balance is 8 digits long (text)
			if (length($tocashnewh) < 8) {
				my $additions = 8 - length($tocashnewh);
				for (my $i = 1;$i<=$additions;$i++) {
					$tocashnewh = '0'.$tocashnewh;
				}
			}	
			
			# do actual database debit amount from client (MEM_NMM)
			my $cmd = '/services/commserv/2000/bin/raudp -r 192.168.0.51:2035 -BSIROOT /services/commserv/2000 DB U M NNM ';
			$SIG{ALRM} = \&timed_out;
			$cmd .=  $MEM_NNM;  
         $cmd .= ' MON ';  
			$cmd .=  $fromcashnewh;           
			eval {  
            alarm(16);  
            $response = `$cmd` || '';  
            alarm(0);  
			};  
			my ($code, $RES) = split(/\n/, $response);
			chomp($code); chomp($RES);  
			if ($code eq '0') {
				# do actual database credit amount to client (TO_NMM)
				$cmd = '/services/commserv/2000/bin/raudp -r 192.168.0.51:2035 -BSIROOT /services/commserv/2000 DB U M NNM ';
				$cmd .=  $TO_NNM;  
	         $cmd .= ' MON ';  
				$cmd .=  $tocashnewh;           
				$SIG{ALRM} = \&timed_out;
				eval {  
            	alarm(16);  
	            $response = `$cmd` || '';  
            	alarm(0);  
				};  
				my ($code, $RES) = split(/\n/, $response);
				chomp($code); chomp($RES);  
				if ($code eq '0') {			
					# Done show success!
          					&success_html_output;
          					$transerrmess = "Success";
          					$tranmess2 = "Closing balance $MEM_NNM $fromcashnew - $TO_NNM $tocashnew";
	        					&write_text_file;       					
				}
				else {
					# Failed to complete credit part of transfer, need to roll back the debit that occured to MEM_NMM
					# convert old MEM_NNM balance to hex
					$fromcashoh = sprintf("%x",$fromcash);
					# make sure hex value of MEM_NNM's balance is 8 digits long (text)
					if (length($fromcashoh) < 8) {
						my $additions = 8 - length($fromcashoh);
						for (my $i = 1;$i<=$additions;$i++) {
							$fromcashoh = '0'.$fromcashoh;
						}
					}			
					$cmd = '/services/commserv/2000/bin/raudp -r 192.168.0.51:2035 -BSIROOT /services/commserv/2000 DB U M NNM ';
					$cmd .=  $MEM_NNM;
	         	$cmd .= ' MON ';
					$cmd .=  $fromcashoh;
					$SIG{ALRM} = \&timed_out;
					eval {  
            		alarm(16);
	         	   $response = `$cmd` || '';
            		alarm(0);
					};
					my ($code, $RES) = split(/\n/, $response);
					chomp($code); chomp($RES);
					if ($code eq '0') {
							# Rolled back successfully but still need to show transfer failed
							$transerrmess = "The system was unable to credit $TO_NNM at this time.";
							&failure_html_output;
							$tranmess2 = "Closing balance $MEM_NNM $fromcash - $TO_NNM $tocash";
							&write_text_file;
					}
					else {
							# Failed to roll back! client has lost money.
							$transerrmess = "The system was unable to credit $TO_NNM.<br><b> Also the system was unable to credit you your funds back.</b>";
							&failure_html_output;
							$tranmess2 = "Closing balance $MEM_NNM $fromcashnew - $TO_NNM $tocash";
							&write_text_file;
					}
				}
			}
			else {
				# failed to initiate transfer
				$transerrmess = "The system was unable to debit funds from your account at this time.";
				&failure_html_output;
				$tranmess2 = "Closing balance $MEM_NNM $fromcash - $TO_NNM $tocash";
				&write_text_file;
			}		
		}
		else {
			# Failed to get TO_NNM's Balance
			$transerrmess = "$TO_NNM nick seems to be invalid... Tut Tut....";
			&failure_html_output;
			$tranmess2 = "Closing balance $MEM_NNM $fromcash - $TO_NNM $tocash";
			&write_text_file;
		}
	}
	else {
		# Client doesn't have enough funds to transfer that amount to someone
		$transerrmess = "You have insuffient funds to be able to complete that transfer.";	
		&failure_html_output;
		$tranmess2 = "Closing balance $MEM_NNM $fromcash - $TO_NNM $tocash";		
		&write_text_file;
	}
}
else {
	# Client doesn't have enough funds to transfer that amount to someone
	$transerrmess = "$MEM_NNM nick seems to be invalid... Tut Tut.... ($result)";	
	&failure_html_output;
	$tranmess2 = "Closing balance $MEM_NNM $fromcash - $TO_NNM $tocash";	
	&write_text_file;
}

exit;


####################
sub write_text_file {
####################
      $textfile = $logfilepath . $logfilename;

      $month = $mon + 1; #$mon starts at 0 for some reason

      if ( ! open (HITME, ">> $textfile") )
      {
        print "<font color=000000>";
          print "Opening file $textfile failed\n";
        print "</font>\n";
      }

        chmod 0666, $textfile;
        flock (HITME,2);

        print HITME "$MEM_NNM ($fromcash) TO $TO_NNM ($tocash) AMOUNT $TO_AMT |";
        print HITME " $transerrmess |";
        print HITME " $tranmess2 |";
        print HITME "  Submitted: $hour:$min:$sec, $month/$mday/$year,";
        print HITME " $realip ";
        print HITME "";        
        print HITME "\n";
        flock(HITME,8);
        close HITME;
}

####################
sub success_html_output {
####################
print <<EOT;




































































<!-- bank/phase3.tmpl -->
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title>CityCash Transfer</title>
<meta name="Author" content="Coolkama, Simioni and Halogen">

</head>
<body bgcolor="#000000" text="lime">
<table border="0" cellpadding="0" cellspacing="0" width="575" align="center">
      <!-- fwtable fwsrc="confirm.png" fwbase="confirm.jpg" fwstyle="Dreamweaver" fwdocid = "742308039" fwnested="0" -->
      <tr> 
        <td><img src="spacer.gif" width="55" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="208" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="141" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="11" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="106" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="6" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="48" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="1" border="0" alt=""></td>
      </tr>
      <tr> 
        <td colspan="7"><img name="confirm_r1_c1" src="/places/bank/images/top.jpg" width="575" height="171" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="171" border="0" alt=""></td>
      </tr>
      <tr> 
        <td><img name="confirm_r2_c1" src="/places/bank/images/left.jpg" width="55" height="182" border="0" alt=""></td>
        <td colspan="5"> 
          <table border="0" cellspacing="10" align="center">
            <tr> 
              <td><font face="Arial, Helvetica, sans-serif" size="-1"> <font color="#FFFFFF">Transfer 
                from:</font><br>
                <font color="#ffff00">$MEM_NNM</font><br>
                <font color="#FFFFFF">New balance:</font><br>
                <font color="#ffff00">$fromcashnew</font><br>
                <font color="#FFFFFF">The Sum of:</font><br>
                <font color="#ffff00">$TO_AMT</font></font> </td>
              <td><font face="Arial, Helvetica, sans-serif" size="-1"> <font color="#FFFFFF">Transfer 
                to:</font><br>
                <font color="#ffff00">$TO_NNM</font><br>
                <br>
                <br>
                <font color="#FFFFFF">The Sum of:</font><br>
                <font color="#ffff00">$TO_AMT</font></font> </td>
            </tr>
          </table>
          <p align="center"><font face="Arial, Helvetica, sans-serif" color="#FFFFFF" size="-1">T</font><font face="Arial, Helvetica, sans-serif" color="#FFFFFF"><font size="-1">ransaction 
            Completed!</font></font></p>
        </td>
        <td><img name="confirm_r2_c7" src="/places/bank/images/right.jpg" width="48" height="182" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="182" border="0" alt=""></td>
      </tr>
      <tr> 
        <td colspan="7"><img name="confirm_r3_c1" src="/places/bank/images/bottombar.jpg" width="575" height="21" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="21" border="0" alt=""></td>
      </tr>
      <tr> 
        <td rowspan="2" colspan="2"><img name="confirm_r4_c1" src="/places/bank/images/bottomleft.jpg" width="263" height="81" border="0" alt=""></td>
        
    <td><a href="print?TPL=bank/phase1"><img name="confirm_r4_c3" src="/places/bank/images/new.jpg" width="141" height="24" border="0" alt=""></a></td>
        <td rowspan="2"><img name="confirm_r4_c4" src="/places/bank/images/bottomdivider.jpg" width="11" height="81" border="0" alt=""></td>
        
    <td><a href="javascript:window.close();"><img name="confirm_r4_c5" src="/places/bank/images/close.jpg" width="106" height="24" border="0" alt=""></a></td>
        <td rowspan="2" colspan="2"><img name="confirm_r4_c6" src="/places/bank/images/bottomright.jpg" width="54" height="81" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="24" border="0" alt=""></td>
      </tr>
      <tr> 
        <td><img name="confirm_r5_c3" src="/places/bank/images/underbuttonleft.jpg" width="141" height="57" border="0" alt=""></td>
        <td><img name="confirm_r5_c5" src="/places/bank/images/underbuttonright.jpg" width="106" height="57" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="57" border="0" alt=""></td>
      </tr>
    </table> 
    <!--#define variable="SUCC" value="YES" --> 
</body>
</html>

EOT
}

####################
sub failure_html_output {
####################
print <<EOT;

<!-- bank/phase3.tmpl -->
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title>CityCash Transfer</title>
<meta name="Author" content="Coolkama, Simioni and Halogen">

</head>
<body bgcolor="#000000" text="lime">
    <table border="0" cellpadding="0" cellspacing="0" width="575" align="center">
      <!-- fwtable fwsrc="confirm.png" fwbase="confirm.jpg" fwstyle="Dreamweaver" fwdocid = "742308039" fwnested="0" -->
      <tr> 
        <td><img src="spacer.gif" width="55" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="208" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="141" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="11" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="106" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="6" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="48" height="1" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="1" border="0" alt=""></td>
      </tr>
      <tr> 
        <td colspan="7"><img name="confirm_r1_c1" src="/places/bank/images/top.jpg" width="575" height="171" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="171" border="0" alt=""></td>
      </tr>
      <tr> 
        <td><img name="confirm_r2_c1" src="/places/bank/images/left.jpg" width="55" height="182" border="0" alt=""></td>
        <td colspan="5"> 
          
      <div align="center">
        <p><font color="#ff0000"><b><font face="Arial, Helvetica, sans-serif">There has been a problem during this transfer,<br>
        $transerrmess<br>
        </font></b></font></p>
        <p><font color="#ff0000"><b><font face="Arial, Helvetica, sans-serif">Please 
          go back and try again</font></b></font></p>
        </div>
        </td>
        <td><img name="confirm_r2_c7" src="/places/bank/images/right.jpg" width="48" height="182" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="182" border="0" alt=""></td>
      </tr>
      <tr> 
        <td colspan="7"><img name="confirm_r3_c1" src="/places/bank/images/bottombar.jpg" width="575" height="21" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="21" border="0" alt=""></td>
      </tr>
      <tr> 
        
    <td rowspan="2" colspan="2"><img name="confirm_r4_c1" src="/places/bank/images/bottomlefterror.jpg" width="263" height="81" border="0" alt=""></td>
        
    <td><img name="confirm_r4_c3" src="/places/bank/images/blank.jpg" width="141" height="24" border="0" alt=""></td>
        <td rowspan="2"><img name="confirm_r4_c4" src="/places/bank/images/bottomdivider.jpg" width="11" height="81" border="0" alt=""></td>
        
    <td><a href="javascript:history.go(-1);"><img name="confirm_r4_c5" src="/places/bank/images/back.jpg" width="106" height="24" border="0" alt=""></a></td>
        <td rowspan="2" colspan="2"><img name="confirm_r4_c6" src="/places/bank/images/bottomright.jpg" width="54" height="81" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="24" border="0" alt=""></td>
      </tr>
      <tr> 
        <td><img name="confirm_r5_c3" src="/places/bank/images/underbuttonleft.jpg" width="141" height="57" border="0" alt=""></td>
        <td><img name="confirm_r5_c5" src="/places/bank/images/underbuttonright.jpg" width="106" height="57" border="0" alt=""></td>
        <td><img src="spacer.gif" width="1" height="57" border="0" alt=""></td>
      </tr>
    </table>
<!--#define variable="SUCC" value="NO" --> 
</body>
</html>

EOT
}

#######################
sub get_date {
#######################
    @days = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday');
   @months = ('January','February','March','April','May','June','July',
              'August','September','October','November','December');

    ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    if ($hour < 10) { $hour = "0$hour"; }
    if ($min < 10) { $min = "0$min"; }
    if ($sec < 10) { $sec = "0$sec"; }

    $date = "$days[$wday], $months[$mon] $mday, 19$year at $hour\:$min\:$sec";
}

#######################
sub parse_form {
#######################
#if ($ENV{'REQUEST_METHOD'} eq 'POST') {
    # Get the input
#    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
 
#}
#else # the GET
#{
	$buffer=$ARGV[0];
#}
#PRINT "$ENV{'REQUEST_METHOD'}";
#PRINT "$buffer";
    # Split the name-value pairs
    @pairs = split(/&/, $buffer);


    foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
 
	$name =~ tr/+/ /;
	$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

	# Foil one form of hackery.
	$value =~ s/<!--(.|\n)*-->//g;

	if ($FORM{$name} && ($value)) {
	    $FORM{$name} = "$FORM{$name}, $value";
	}
	elsif ($value) {
	    $FORM{$name} = $value;
	}
    }
}