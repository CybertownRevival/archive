#!/usr/bin/perl

#########################################
#       REMOVE OBJECTS FOR MALL         #
#########################################
#########################################
#    Scripts written by: Lee Clagett    #
#              Copyright 2000           #
#########################################
# This script is to be used by          #
# mpsl.net, and no one else.            #
# The use of this script on another     #
# website is srictly prohibited         #
#########################################

if ($ENV{'REQUEST_METHOD'} eq 'GET') {
@pairs = split(/&/, $ENV{'QUERY_STRING'});
}
elsif ($ENV{'REQUEST_METHOD'} eq 'POST') {
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
}
else {
&error('request_method');
}
foreach $pair (@pairs) {
($name, $value) = split(/=/, $pair);
$name =~ tr/+/ /;
$name =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$value =~ tr/+/ /;
$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$value =~ s/\n/\s/g;
if ($name && $value) { $FORM{$name} = $value; }
}
print "Content-type: text/html\n\n";
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time); 

######################################################
# Easily Editable variables. Pretty Self Explanatory #
######################################################

$http_long = "http://www.cybertown.com/places/shopping/removes";
$http_short = "/";
$absolute = "/services/http/80/htdocs/places/shopping/removes";
$punished_path = "punish";
$holds_path = "holds";
$remove_path = "remove";
$this_file = "cgi-bin/cybertown/templates/shopping/remove.pl";
$hold_file = "cgi-bin/news/mall/other/psupload.cgi";
$background = "http://www.virtualsolarsystem.com/uranus/katana_blade/christmas.gif";

#################################
# GIVE MALL DEPS CERTAIN RIGHTS #
#################################---------------------------------#
# Returns $dep with 1 if a name matches deputy list, returns 0 if #
# doesn't. A bit sloppy                                           #
#-----------------------------------------------------------------#

@names = ("008","Lanneret","Paden","tiffers","LSS","WolfDance","denmeister","katana_blade","frankster200");
$t = "0";
foreach $d (@names) {
if($FORM{'name'} eq $d) {
if($t != 5) {
$dep = "1";
$t = 5;
} else {
$dep = "0";
}
}
}

################################
# SET-UP COMMANDS TO DO THINGS #
################################-------------------------------------#
# Re-directs to sub-routines depending on what the variable task has #
# for a value                                                        #
#--------------------------------------------------------------------#

if($FORM{'task'} eq "read") {
 if($FORM{'name'} eq "") {
  print "<b>ERROR:</b><br>Not logged into CT or clicked incorrect link";
 } else {
  &read;
 }
} elsif($FORM{'task'} eq "post") {
 if($FORM{'name'} eq "") {
  print "<b>ERROR:</b><br>Not logged into CT or clicked incorrect link";
 } else {
  &post;
 }
} elsif($FORM{'task'} eq "post2") {
 if($FORM{'name'} eq "") {
  print "<b>ERROR:</b><BR>Not logged into CT or clicked incorrect link";
 } else {
  &post2;
 }
} elsif($FORM{'task'} eq "admin") {
  &admin;
} elsif($FORM{'task'} eq "admin2") {
  &admin2;
} elsif($FORM{'task'} eq "hold") {
&hold;
} elsif($FORM{'task'} eq "hold2") {
&hold2;
} elsif($FORM{'task'} eq "punish") {
&punish;
} elsif($FORM{'task'} eq "punishfind") {
&punishfind;
} elsif($FORM{'task'} eq "punishadd") {
&punishadd;
} elsif($FORM{'task'} eq "punishadd2") {
&punishadd2;
} else {
 print "<b>ERROR:</b><br>No Command Given";
}

###############
# SHOW REMOVE #
###############--------------------------------------------------#
# This is the sub-routine for the main part of the Remove Board, #
# displaying all removed and to be removed objects               #
#----------------------------------------------------------------#
sub read {

#-------------------------------------------------------------#
# Uses the path variable from above, and gets the appropriate #
# directory                                                   #
#-------------------------------------------------------------#
opendir(DATA,"$absolute/$remove_path");

#-----------------------------------------------#
# Gets a directory listing for every html file. #
#-----------------------------------------------#
@data = grep(/\.html$/,readdir(DATA));
closedir(DATA);

#--------------------------------------------------------------------#
# Prints the top part of the page, with the options to other parts.  #
# NOTE: The holds option is disabled at this point, it starts with a #
# comment.                                                           #
#--------------------------------------------------------------------#
print <<END;
<html><head><title>Remove Objects</title></head>
<body bgcolor="black" background="$background" LINK="#00FF00" VLINK="#FFFF00" ALINK="#FFFFFF" TEXT="#D0DBF7">
<center>
<font size="+2"><b>Shopping Mall Remove Requests</b></font></center>
<center>
<form name="form" action="$http_short$this_file" method="post">
<input type="hidden" name="name" value="$FORM{'name'}">
<input type="radio" name="task" value="post">Remove Request
END
#&nbsp;&nbsp;&nbsp;&nbsp;<input type="radio" name="task" value="hold">Upload Hold

#------------------------------------------#
# Options that only the deputies will see. #
#------------------------------------------#
if ($dep != 1 ) {
} else {
print <<END;
&nbsp;&nbsp;&nbsp;&nbsp;<input type="radio" name="task" value="admin">Admin
&nbsp;&nbsp;&nbsp;&nbsp;<input type="radio" name="task" value="punish">Punished Creators
END
}

#----------------------------#
# Completes the options part #
#----------------------------#
print <<END;
&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value=" GO "></form>
</center><table border="0" width="100%"><tr bgcolor="red">
<td>Object</td><td>Location</td><td>Creator</td><td width="10">Removed</td></tr>
END

#-----------------------------------------------------------------#
# Sorts the data in alpabetical order. NOTE: The filenames of the #
# html files are done by date so alpabetical order is by date.    #
#-----------------------------------------------------------------#
@data2 = sort { lc($b) cmp lc($a) } @data;

#------------------------------------------------------------------#
# Outputs all the Objects List. Each html file contains the proper #
# coding needed, so the entire file is outputted.                  #
#------------------------------------------------------------------#
foreach $a (@data2) {
 open(REM,"$absolute/$remove_path/$a");
 my @rem = <REM>;
 print @rem;
 print "</tr>";
}
print "</table></body></html>";
}


##############################
# REQUESTING A REMOVE PART I #
##############################--------------------------------#
# This little sub-routine the generates the html file for the #
# object requested to be removed. This first part just        #
# generates the required options and such for the hold.       #
#-------------------------------------------------------------#

sub post {
print <<END;
<html><head><title>Remove Objects</title></head>
<body bgcolor="black" background="$background" LINK="#00FF00" VLINK="#FFFF00" ALINK="#FFFFFF" TEXT="#D0DBF7">
<center>
<font size="+2"><b>Shopping Mall Remove Requests</b></font></center>
<form name="form" method="post" action="$http_short$this_file">
<input type="hidden" name="name" value="$FORM{'name'}">
<input type="hidden" name="task" value="post2">
<table border="0" width="100%">
<tr bgcolor="red"><td>Nickname</td><td>Store</td><td>Object Name</td></tr>
<tr><td>$FORM{'name'}</td><td>
 <select name="store">
 <option value="Antique Shop">Antique Shop
 <option value="Appliance Shop">Appliance Shop
 <option value="Aquatics Shop">Aquatics Shop
 <option value="Bargain Outlet">Bargain Outlet
 <option value="Bedroom Showcase">Bedroom Showcase
 <option value="Car Dealer">Car Dealer
 <option value="Carpet Shop">Carpet Shop
 <option value="Collectibles">Collectibles
 <option value="Electronics Store">Electronics Store
 <option value="Fine Art Shop">Fine Art Shop
 <option value="Furniture Store">Furniture Store
 <option value="Garden Store">Garden Store
 <option value="Gift Shop">Gift Shop
 <option value="Grocery Store">Grocery Store
 <option value="Holiday Shop">Holiday Shop
 <option value="Kitchen Store">Kitchen Store
 <option value="Large Item Shop">Large Item Shop
 <option value="Novelty Store">Novelty Store
 <option value="Office Store">Office Store
 <option value="Poster Shop">Poster Shop
 <option value="Pet Shop">Pet Shop
 <option value="Space Port">Space Port
 <option value="Toy Store">Toy Store
 <option value="Weapons Display">Weapons Display
 </select></td>
<td><input type="text" name="object"></td></tr></table><center>
<input type="submit" value=" Post "> <input type="button" value="Cancel" onClick="history.back()">
</form>
END
}

###############################
# REQUESTING A REMOVE PART II #
###############################----------------------------------#
# This is the very confusing thing I made when I first started   #
# programming really. Probably a better way to write. Just makes #
# the file name by date, so that they can be sorted by newest at #
# top.                                                           #
#----------------------------------------------------------------#
sub post2 {
if($yday < 100) {
 if($yday > 9) {
  $yday2 = "0$yday";
 } elsif($yday < 10) {
  $yday2 = "00$yday";
 }
} else {
 $yday2 = "$yday";
} 

if($hour < 10) {
 $hour2 = "0$hour";
} else {
 $hour2 = "$hour";
}

if($min < 10) {
 $min2 = "0$min";
} else {
 $min2 = "$min";
}

if($sec < 10) {
 $sec2 = "0$sec";
} else {
 $sec2 = "$sec";
}

#--------------------------------------------------------------#
# Below is actually what is put into the html file. As I said, #
# all the information needed.                                  #
#--------------------------------------------------------------#
open(DATA,">$absolute/$remove_path/$year$yday2$hour2$min2$sec2.html");
print DATA <<END;
<tr>
<!-- COLOR -->
<td bgcolor="#aaaa00">
<!-- END COLOR -->

<!-- OBJECT -->
$FORM{'object'}</td>
<!-- END OBJECT -->

<!-- LOCATION -->
<td>$FORM{'store'}</td>
<!-- END LOCATION -->

<!-- CREATOR -->
<td>$FORM{'name'}</td>
<!-- END CREATOR -->

<!-- REMOVED -->
<td>No</td>
<!-- END REMOVED -->
END
close(DATA);
print <<END;
<html><head><title>Remove Objects</title></head>
<body bgcolor="black" background="$background" LINK="#00FF00" VLINK="#FFFF00" ALINK="#FFFFFF" TEXT="#D0DBF7">
<center>
<font size="+2"><b>Shopping Mall Remove Requests</b></font></center>
<BR><BR>Request Added!
<form name="form" method="post" action="$http_short$this_file">
<input type="hidden" name="name" value="$FORM{'name'}">
<input type="hidden" name="task" value="read">
<center><input type="submit" value="Back to Remove Requests"></center>
</form>
END
}

#########
# ADMIN #
#########------------------------------------------------------------#
# Displays the same list as before. Just this time there are check   #
# boxes for the user to check to designate which objects have been   #
# removed. If an already removed object is checked, nothing happens. #
# How everything is read and such, is the same from the beginning    #
#--------------------------------------------------------------------#

sub admin {
opendir(DATA,"$absolute/$remove_path");

@data = grep(/\.html$/,readdir(DATA));
closedir(DATA);

#Print Top
print <<END;
<html><head><title>Remove Objects</title></head>
<body bgcolor="black" background="$background" LINK="#00FF00" VLINK="#FFFF00" ALINK="#FFFFFF" TEXT="#D0DBF7">
<center>
<font size="+2"><b>Shopping Mall Remove Requests $hour</b></font></center>
<form name="form" action="$http_short$this_file" method="post">
<input type="hidden" name="name" value="$FORM{'name'}">
<input type="hidden" name="task" value="admin2">
<center><input type="submit" value="Update"></center>
<table border="0" width="100%"><tr bgcolor="red">
<td>Object</td><td>Location</td><td>Creator</td><td width="10">Removed</td></tr>
END
@data2 = sort { lc($b) cmp lc($a) } @data;

#Print Info
foreach $a (@data2) {
 open(REM,"$absolute/$remove_path/$a");
 my @rem = <REM>;
 print @rem;
 print "<td width=\"5\"><input type=\"checkbox\" name=\"$a\" value=\"checked\"></td></tr>";
}
print "</table></form></body></html>";
}


###########
# ADMIN II#
###########---------------------------------------------------------#
# This is the part the removes the Yellow line, and adds Yes to the #
# Checked column.                                                   #
#-------------------------------------------------------------------#
sub admin2 {

opendir(DATA,"$absolute/$remove_path");

@dataf = grep(/\.html$/,readdir(DATA));
closedir(DATA);

@dataf2 = sort { lc($b) cmp lc($a) } @dataf;
foreach $b (@dataf2) {
 if ($FORM{$b} eq "checked") {
 use LWP::Simple; 
  $read = get("$http_long/$remove_path/$b");
  open(STUFF,">$absolute/$remove_path/$b");
  $bottom = "$read";
  $top = "$read";
  $middle = "$read";

  $top =~ s/^.*<!-- END COLOR -->//s;
  $top =~ s/<!-- COLOR -->//s;
  $top =~ s/<!-- END COLOR -->//s;
  $top =~ s/<!-- REMOVED -->.*$//s;
  $top =~ s/<!-- REMOVED -->//s;
   
  print STUFF <<END;
<tr><td>
$top
<!-- REMOVED -->
<td>Yes</td>
<!-- END REMOVED -->
END
 }
}
print <<END;
<html><head><title>Remove Objects</title></head>
<body bgcolor="black" background="$background" LINK="#00FF00" VLINK="#FFFF00" ALINK="#FFFFFF" TEXT="#D0DBF7">
<center>
<font size="+2"><b>Shopping Mall Remove Requests</b></font></center>
<br>Updated Successfully!
<br><br><form name="form" action="$http_short$this_file" method="post">
<input type="hidden" name="name" value="$FORM{'name'}">
<input type="hidden" name="task" value="admin">
<input type="submit" value="Back to Remove Requests">
</form>
</body></html>
END
}

################
# HOLD OBJECTS #
################-----------------------------------------------------#
# This whole thing just uses a simple upload script. I know you have #
# one already in use of some sort. So I won't say much about this    #
# here.                                                              #
#--------------------------------------------------------------------#
sub hold {
print <<END;
<html><head><Title>Upload Holds</title>
<script language="javascript">
<!-- Hide
function check() {
 if(document.form.ONAME.value == "") {
    alert("Please enter a name for your Object");
    return false;
}
if(document.form.FILE1.value == "") {
    alert("Please choose a VRML-File");
    return false;
} else {
 if((document.form.FILE1.value.indexOf(".wrl")<4)&&(document.form.FILE1.value.indexOf(".wrz")<5)) {
    alert("Please use only .wrl or .wrz files");
    return false;
}
}
if(document.form.FILE2.value == "") {
    return true;
} else {
if((document.form.FILE2.value.indexOf(".jpg")<4)&&(document.form.FILE2.value.indexOf(".gif")<5)) {
    alert("Please use only .jpg or .gif files");
    return false;
}
}
if(document.form.FILE3.value == "") {
    alert("Please choose a Thumbnail-File");
    return false;
} else {
 if((document.form.FILE3.value.indexOf(".jpg")<4)&&(document.form.FILE3.value.indexOf(".gif")<5)) {
    alert("Please use only .jpg or .gif files");
    return false;
}
}
   return true;
}
// -->
</script>
</head>
<body bgcolor="black" background="$background" LINK="#00FF00" VLINK="#FFFF00" ALINK="#FFFFFF" TEXT="#D0DBF7">
<center><font size="+2"><b>Shopping Mall Hold Uploads</b></font></center>
<br><font color="yellow">Please read everything before attempting to upload holds.</font>
<BR><BR><b>TECH INFO:</b>When you upload holds through this service, note that it does not automatically upload to cybertown's servers. Rather it uploads
to another website in which 008 controls. Because of this objects will not be uploaded right away, and will have to wait until 008 uploads 
them himself to the mall. 
<br><br><b>OTHER INFO:</b>There are two types of holds in the mall. All will be assumed personal holds unless I get an inbox from a CL, CD, or 
NL (more info under Colony Event Holds). Please put in the name in parenthesis how many you want. If none is put, it will be assumed 1, and only 1 will be
uploaded.
<br><br><b>Colony Event Holds:</b> These holds are for objects that are going to be used in a Colony, hood, or block game. The first thing that must be 
done is that your CL, CD, or NL must put a message in my inbox telling me who will be creating objects for an event, and what the event is. If this 
does not happen, your holds will be assumed personal. If a CL, CD, or NL does inbox me, you can get up to 30 objects at 10 CC's price per instance. 
Nothing special needs to be on the thumbnail, and where the object ends up, doesn't matter. I would like that you put 0 CC's on the object's thumbnail 
though.

<br><br><b>Personal Holds:</b> The second type of hold is a personal hold. A personal hold will cost 1000 CC's per instance. Up to 10 instances allowed. 
You do not need to put any special markings on the thumb, and where the object ends up does not matter.
<form method="POST" name="form" action="$http_short$hold_file" ENCTYPE="multipart/form-data"  onSubmit="return check()">
<input type="hidden" name="NAME" value="$FORM{'name'}">
<table border="0" width="100%">
<tr><td>Nickname:</td><td>$FORM{'name'}</td></tr>
<tr><td>Object Name:</td><td><input type="text" name="ONAME"></td></tr>
<tr><td>VRML File:</td><td> 
<input type="file" name="FILE1">
</td></tr>
<tr><td>Texture: </td><td>
<input type="file" name="FILE2">
</td></tr>
<tr><td>Thumbnail:</td><td>
<input type="file" name="FILE3">
</td></tr></table>
<font size="2">By clicking the upload button you understand all the extra rules set in place, as well as ones set on upload page in mall.

<br><br><input type="submit" value="UPLOAD">
</form>
</body>
</html>
END
}

#################
# HOLDS PART II #
#################

sub hold2 {
print <<END;
<html><head><Title>Upload Holds</title></head>
<body bgcolor="black" background="$background" LINK="#00FF00" VLINK="#FFFF00" ALINK="#FFFFFF" TEXT="#D0DBF7">
<center><font size="+2"><b>Shopping Mall Hold Uploads</b></font></center>
Object uploaded succesfully!
<center><form action="$http_short$this_file" method="post">
<input type="hidden" name="name" value="$FORM{'name'}">
<input type="hidden" name="task" value="read">
<input type="submit" value="Back to Remove Board">
</form>
END
}

#####################
# PUNISHED CREATORS #
#####################------------------------------------------------#
# Very similar to what I have done in the past. There is a separate  #
# folder for each offence. (1st Offence Folder, 2nd Offence Folder,  #
# etc). Each folder contains a text file with a creators name on it  #
# This reads that file, and outputs whats in the file line by line.  #
# Each line contains data for the next column. All of this data was  #
# created by hand, and there is no part of the script that generates #
# these files.                                                       # 
#--------------------------------------------------------------------#
sub punish {
print <<END;
<html><head><Title>Upload Holds</title></head>
<body bgcolor="black" background="$background" LINK="#00FF00" VLINK="#FFFF00" ALINK="#FFFFFF" TEXT="#D0DBF7">
<center><font size="+2"><b>Punished Creators</b></font></center>
<font size="+1">Breaking of Rules Procedures</font>
<br>Check here. If it is a first time offender, give the creator a warning using the message below as a guide. Then post a message in the mall's inbox, or 008's inbox regarding the incident. If it is
a repeat offender, report the incident to 008 in his inbox, or the mall inbox. 008 will handle it from there.
<BR><BR><font size="+1">Warning Message</font>
<br><font color="green">Subject: Warning From Mall</font>
<br><table border="0" width="100%"><tr><td><font color="green">Message:</font></td><td><font color="green">You are being warned for < RULE BROKEN >. Please read the mall rules at www.mpsl.net/mall/rules.shtml 
for more info. If you break this or any other mall rules again you will face fines, or even a ban from uploading. Please make sure that you read everything
on this page, and to make sure that this does not happened again.</font></td></tr></table>
<br><font size="+1">1st Offence</font>
<table border="0" width="100%"><tr bgcolor="red"><td>Name</td><td>Date</td></tr>
END

#--- CREATORS WARNED ----#
opendir("ONE","$absolute/$punished_path/1");
@one = grep(/\.txt$/,readdir(ONE));
close(ONE);

foreach $a (@one) {
open("ONE1","$absolute/$punished_path/1/$a");
@one1 = <ONE1>;
print "<tr><td><a href=\"$http_short$this_file?task=punishfind&level=1&cname=$one1[0]&name=$FORM{'name'}\" target=\"detail\">$one1[0]</td><td>$one1[1] $one1[2], $one1[3]</td></tr>";
}

#--- SECOND OFFENCE ----#
print <<END;
</table><br><br><font size="+1">2nd Offence</font>
<table border="0" width="100%"><tr bgcolor="red"><td>Name</td><td>Date</td><td>Fine Amount</td></tr>
END

opendir("TWO","$absolute/$punished_path/2");
@two = grep(/\.txt$/,readdir(TWO));
close(TWO);

foreach $a (@two) {
open("TWO1","$absolute/$punished_path/2/$a");
@two1 = <TWO1>;
print "<tr><td><a href=\"$http_short$this_file?task=punishfind&level=2&cname=$two1[0]&name=$FORM{'name'}\" target=\"detail\">$two1[0]</td><td>$two1[1] $two1[2], $two1[3]</td><td>$two1[5]</td></tr>";
}

#--- THIRD OFFENCE ----#
print <<END;
</table><br><br><font size="+1">3rd Offence</font>
<table border="0" width="100%"><tr bgcolor="red"><td>Name</td><td>Date</td><td>Fine Amount</td></tr>
END

opendir("THR","$absolute/$punished_path/3");
@thr = grep(/\.txt$/,readdir(THR));
close(THR);

foreach $a (@thr) {
open("THR1","$absolute/$punished_path/3/$a");
@thr1 = <THR1>;
print "<tr><td><a href=\"$http_short$this_file?task=punishfind&level=3&cname=$thr1[0]&name=$FORM{'name'}\" target=\"detail\">$thr1[0]</td><td>$thr1[1] $thr1[2], $thr1[3]</td><td>$thr1[5]</td></tr>";
}

#--- FOURTH OFFENCE ----#
print <<END;
</table><br><br><font size="+1">4th Offence</font>
<table border="0" width="100%"><tr bgcolor="red"><td>Name</td><td>Date</td><td>Fine Amount</td></tr>
END

opendir("FOU","$absolute/$punished_path/4");
@fou = grep(/\.txt$/,readdir(FOU));
close(FOU);

foreach $a (@fou) {
open("FOU1","$absolute/$punished_path/4/$a");
@fou1 = <FOU1>;
print "<tr><td><a href=\"$http_short$this_file?task=punishfind&level=4&cname=$fou1[0]&name=$FORM{'name'}\" target=\"detail\">$fou1[0]</td><td>$fou1[1] $fou1[2], $fou1[3]</td><td>$fou1[5]</td></tr>";
}

#--- FIFTH OFFENCE ----#
print <<END;
</table><br><br><font size="+1">5th Offence - BANNING FROM UPLOADING</font>
<table border="0" width="100%"><tr bgcolor="red"><td>Name</td><td>Date</td></tr>
END

opendir("FIF","$absolute/$punished_path/5");
@fif = grep(/\.txt$/,readdir(FIF));
close(FIF);

foreach $a (@fif) {
open("FIF1","$absolute/$punished_path/5/$a");
@fif1 = <FIF1>;
print "<tr><td><a href=\"$http_short$this_file?task=punishfind&level=5&cname=$fif1[0]&name=$FORM{'name'}\" target=\"detail\">$fif1[0]</td><td>$fif1[1] $fif1[2], $fif1[3]</td></tr>";
}

print <<END;
</td></tr></table>
</body></html>
END
}

#######################
# BOTTOM PART DISPLAY #
#######################----------------------------------------------#
# This part just displays what was selected by the user in the top   #
# frame. It displays the information in the bottom frame, message    #
# board style.                                                       #
#--------------------------------------------------------------------#
sub punishfind {
open("INFO","$absolute/$punished_path/$FORM{'level'}/$FORM{'cname'}.txt");
@info = <INFO>;
close(INFO);
$level = $FORM{'level'} + 1;
print <<END;
<html><head><Title>Upload Holds</title></head>
<body bgcolor="black" background="$background" LINK="#00FF00" VLINK="#FFFF00" ALINK="#FFFFFF" TEXT="#D0DBF7">
$info[0]
<br>$info[1] $info[2], $info[3]
<BR><br><br>$info[4]
</body></html>
END
}