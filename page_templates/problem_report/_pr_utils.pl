### This is a set of common perl subroutines

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
	$year += 1900;
    $date = "$days[$wday], $months[$mon] $mday, $year at $hour\:$min\:$sec";
}

#######################
sub parse_form {
#######################
### DO NOT check for 'POST' (not necessary!)
###    if ($ENV{'REQUEST_METHOD'} eq 'POST') {
###      # Get the input
###	read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
###      # Split the name-value pairs
###	@pairs = split(/&/, $buffer);
###    }
###    else {
###	&reg_error('request_method');
###    }

    # Get the input
    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
 
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

#######################
sub check_required {
#######################
    foreach $require (@required) {
	if (!($FORM{$require}) || $FORM{$require} eq ' ') {
	    push(@ERROR,$require);
	}
    }

    if (@ERROR) {
	&reg_error('missing_fields', @ERROR);
    }
}

#######################
sub send_mail {
#######################
    my($mail_recipient, $mail_subject) = @_;
    open(MAIL,"|$mailprog -t -f$FORM{'email'}") || return undef;

    print MAIL "To: $mail_recipient\n";
    if($FORM{'email'}) {
	print MAIL "From: $FORM{'email'} ($FORM{'realname'})\n";
    }
    else {
	print MAIL "From: Unknown (unknown sender)\n"
	}

    print MAIL "Subject: $mail_subject\n\n";

    print MAIL "$mail_subject\n";
    print MAIL "Submitted by $FORM{'realname'} ($FORM{'email'})\n";
    print MAIL "on $date\n";
    print MAIL "-------------------------------------------------------\n\n";


    foreach $key (@reg_fields) {
	# Print the name and value pairs in FORM array to mail.
	print MAIL "$key:\n\n$FORM{$key}\n---------------------------------------------------\n\n";
    }

    print MAIL "-------------------------------------------------------\n";

   # Send Any Environment Variables To Recipient.
    foreach $env_report (@env_report) {
	if($ENV{$env_report}) {
	    print MAIL "$env_report: $ENV{$env_report}\n";
	}
    }

    close (MAIL);
	
	
}

####################################
# end of sub send_mail
####################################



#######################
sub send_verification {
#######################
    my($mail_recipient) = @_;
    open(MAIL,"|$mailprog -t -fsupport\@cybertown.com") || return undef;

    print MAIL "To: $mail_recipient\n";
   
   
	print MAIL "From: support\@cybertown.com (Cybertown Technical Support)\n";


    print MAIL "Subject: Cybertown Technical Problem Report\n\n";

   
    print MAIL "-------------------------------------------------------\n\n";


print MAIL <<"END_MAIL";

Thank you for reporting your technical problem;
Your email has been sent to the Cybertown Support Team.

To help in solving your problem as quickly as possible, we have
listed the most frequent technical problems, and their solutions,
at http://www.colonycity.com/problem_report/top13.html.

We want you to have the best possible experience in Cybertown,
and we will look into your problem as soon as possible. Due to 
the volume of email we receive, however, we may not be able to 
send you a personal reply


Sincerely,
Cybertown Support Team



END_MAIL

    print MAIL "-------------------------------------------------------\n";



    close (MAIL);
	
	
}

################################
### end of sub send_verification
################################









#######################
sub reg_error {
#######################
    my ($error,@error_fields) = @_;

    print "Content-type: text/html\n\n";

    if ($error eq 'request_method') {
	print "<html><head><title>Error: Request Method</title>\n";
	print "</head>\n <body bgcolor=#FAE8BA>";
	print "<center>";
	print "   <h1>Error: Request Method</h1>\n  </center>\n\n";
	print "Bad request method\n";
	print "<p><hr size=7 width=75%><p>\n";
	print "<ul>";
	print "<li><a href=\"$ENV{'HTTP_REFERER'}\">Back to the Submission Form</a>\n";
	print "</ul>\n";
	print "</body></html>\n";
    }

    elsif ($error eq 'missing_fields') {
	print "<html><head> <title>Error: Missing Fields</title></head>";
	print "<body bgcolor=#000000 text=#00ff00 link=#FFFFFF alink=#00ff00 vlink=#FFFFFF><center>\n";
	print "   <h1>Error: Missing Fields</h1>";
	print "The following fields were left blank in your submission form:<p>\n";

      # Print Out Missing Fields in a List.
	print "<ul>";
	foreach $missing_field (@error_fields) {
	    print "<li>$missing_field\n";
	}
	print "</ul>\n";

      # Provide Explanation for Error and Offer Link Back to Form.
	print "<p><hr size=7 width=75\%><p>\n";
	print "Please <a href=$FORM{form_url}>go back</a> and finish the form.\n";
	print "The above fields must be filled out before you can successfully submit the form.\n\n";
	print "</body></html>\n";
    }
    elsif ($error eq 'not_registered') {
	print "<html><head><title>Error: Not Registered</title>\n";
	print "</head>\n <body bgcolor=#FAE8BA>";
	print "<center>";
	print "   <h1>Error: Not Registered</h1>\n  </center>\n\n";
	print "<p>You do not appear to have registered to download cyberhub.";
	print "<p><hr size=7 width=75%><p>\n";
	print "Please return to the download form, and make sure that\n";
	print "you have entered your registration number correctly.\n";
	print "If you continue to have troubles, plese contact\n";
	print "<a href=\"mailto:$mailto\">Black Sun</a> for further assistance.\n";
	print "<ul>";
	print "<li><a href=\"$ENV{'HTTP_REFERER'}\">Back to the Submission Form</a>\n";
	print "</ul>\n";
	print "</body></html>\n";
    }

    elsif ($error eq 'registration_timeout') {
	print "<html><head><title>Error: Registration Timeout</title>\n";
	print "</head>\n <body bgcolor=#FAE8BA>";
	print "<center>";
	print "<h1>Error: Registration Timeout</h1>\n  </center>\n\n";
	print "<p>Your registration has timed out.\n";
	print "<p><hr size=7 width=75%><p>\n";
	print "Registrations are only valid for one hour after the initial\n";
	print "download attempt. You must return to the Black Sun Product\n";
	print "registration page and re-register.\n";
	print "<p>If you continue to have troubles, plese contact\n";
	print "<a href=\"mailto:$mailto\">Black Sun</a> for further assistance.\n";
	print "<ul>";
	print "<li><a href=\"$ENV{'HTTP_REFERER'}\">Back to the Submission Form</a>\n";
	print "</ul>\n";
	print "</body></html>\n";
    }

    exit;
}
#######################

1;

