#!/usr/bin/perl


read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
  ($name, $value) = split(/=/, $pair);
  $value =~ tr/+/ /;
  $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
  $value =~ s/~!/ ~!/g;
  $FORM{$name} = $value;
}

if( !open(RAUDP, "/services/commserv/2000/bin/raudp -r www2:2035 -BSIROOT /services/commserv/2000 DB G M NNM $FORM{'NNM'} RGK PWD |")){$rgk_error = "Cannot run:   $!\n";}
else{  
  @rgk = <RAUDP>;
  $reg = $rgk[1];
  $pwd = $rgk[2];
  chop($reg);
  chop($pwd);
}
close(RAUDP);




print "Content-type:text/html\n\n";
print <<HTMLHead;

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2//EN">
<HTML>
<HEAD>
   <TITLE>Cybertown</TITLE>
   <META HTTP-EQUIV="Author" CONTENT"Christopher Raymond">
   <META HTTP-EQUIV="Description" CONTENT="">
   <META HTTP-EQUIV="KeyWords" CONTENT="">
   <META NAME="Author" CONTENT="Christopher Raymond">
   <META NAME="keywords" CONTENT="">
   <META NAME="description" CONTENT="">
   <!--//KeyWords//--!>
</HEAD>
<BODY TEXT="#00DDDD" BGCOLOR="#000000" LINK="#00FFFF" VLINK="#00FFFF" ALINK="#00FF00" BACKGROUND="">
<CENTER>

<br><br> 
<FONT face="arial" size=+1><b>The password for your child's Cybertown account</b><br><br></font> 
<FONT face="arial">
<br> 

HTMLHead
;

 print"<table align=center cellpadding=2 border=0>\n";
 print"<tr><td align=\"right\"><FONT face=\"arial\">Nickname:          </td><td><FONT face=\"arial\"><b>$FORM{'NNM'}</td>\n";
 print"<tr><td align=\"right\"><FONT face=\"arial\">Immigration Code: </td><td><FONT face=\"arial\"><b>$FORM{'RGK'}</td>\n";

if( $reg ne "" && $FORM{'RGK'} eq $reg){
 print"<tr><td align=\"right\"><FONT face=\"arial\">Password:          </td><td><FONT face=\"arial\"><b>$pwd</td>\n";
 print"</td></tr></table>\n";
}else{
 print"<tr><td align=\"right\"><FONT face=\"arial\">Password:          </td><td><FONT face=\"arial\"><b>unavailable</td>\n";
 print"</td></tr></table>\n";
 print"<br><FONT face=\"arial\">Most likely your child's account has been activated.  Please contact <a href=\"mailto:help\@cybertown.com\" >Cybertown Help</a> to request your child's password.\n";
 print"<FONT face=\"arial\">Please supply the email address your child used to register for Cybertown, and your child's Cybertown nickname. \n";
}

print"</td></tr></table>\n";
print <<EndHTML;

</CENTER>
</BODY>
</HTML>
EndHTML
;

