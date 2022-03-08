<!-- #ifdef variable="loginerror002" -->
<!-- #if variable="T_MPL" == value="jail" -->
<HTML>
<HEAD>
<meta http-equiv="Content-Type" content="text/html">
<title><$g_title></title>

<meta http-equiv="refresh" content="0; URL=http://www.cybertown.com/jail/">
<SCRIPT LANGUAGE="JavaScript">

<!-- "hide me!"

function checker (what)
{
startpoint=0;
alllen=document.cookie.length;
if(alllen>0)
{
temlen=document.cookie.indexOf(';',startpoint)
if(temlen>-1)
{
mycookies=document.cookie.substring(startpoint,temlen);
}
else
{
mycookies=document.cookie.substring(startpoint,alllen);
}

set_cookie =''+mycookies+"; path=/; domain=.cybertown.com; expires=Friday, 30-Apr-90 23:59:59 GMT;";
document.cookie ='' + set_cookie + '';
}
document.cookie ='BLAXXUN='+what+'; path=/';
}

checker('<$NNM>');
// scriptend-->
</script>

</head>
</html>
<!-- #endif variable="T_MPL" -->
<!-- #endif variable="loginerror002" -->



<!-- #ifdef variable="T_MCO" value="mothership" -->
<!-- #include virtual="<$g_Templates>mothership/login.tmpl" -->
<!-- #endif variable="T_MCO" -->

<!-- #ifndef variable="T_MCO" value="mothership" -->
<HTML>
<HEAD>
<meta http-equiv="Content-Type" content="text/html">
<title><$g_title></title>
<!-- #ifndef variable="T_IWOS" -->
  <base target="_top">
<!-- #endif variable="T_IWOS" -->
<!-- #include virtual="<$g_Templates>common/loadinfo.tmpl" -->
<script language=javascript>
function checksubmit()
{
 if ( document.loginform.NNM.value.length > 0 && document.loginform.PWD.value.length > 0 )
  document.loginform.submit();

}
</script>
</HEAD>

<!-- #include virtual="<$g_Templates>common/body2.tmpl" -->

<!-- #ifndef variable="T_IWOS" -->
  <!-- #define variable="TARGET" value="_top"-->
<!-- #endif variable="T_IWOS" -->
<!-- #ifdef variable="T_IWOS" -->
  <!-- #define variable="TARGET" value="_self"-->
<!-- #endif variable="T_IWOS" -->

<div align=center>


<table border=0 width=90%><tr>
<td width=150 align=left>
<!-- #ifndef variable="imm" -->
<!-- #ifdef variable="ID" -->

<!-- #ifdef variable="plc" value="club"-->
                                <A HREF="<$selfurl>?NNM=Visitor&login=true&plc=club&DTY=CL&ac=<$ac>&ID=<$ID>">
<!-- #endif variable="plc" -->

<!-- #ifndef variable="plc" value="club"-->
                                <A HREF="<$selfurl>?NNM=Visitor&login=true&ID=<$ID>&ac=<$ac>">
<!-- #endif variable="plc" -->

<!-- #endif variable="ID" -->



<!-- #ifndef variable="ID" -->

<!-- #ifdef variable="plc" -->
<!-- #ifndef variable="plc" value="club"-->
                                <A HREF="<$selfurl>?NNM=Visitor&login=true&plc=<$plc>ac=<$ac>">
<!-- #endif variable="plc" -->
<!-- #endif variable="plc" -->

<!-- #ifndef variable="plc" -->
                                <A HREF="place<$g_exe>?NNM=Visitor&login=true&ac=<$ac>">
<!-- #endif variable="plc" -->
<!-- #endif variable="ID" -->
                                        <IMG HEIGHT=55 WIDTH=98 SRC="<$g_Images>/images/login/visitor.jpg"  BORDER=0  ALT="Visitor"></A>
                <!-- #endif variable="imm" -->
</td>
<td align=center>
<CENTER><image src="/banners/bestchat.gif"><BR><FONT FACE="arial" SIZE="-1" COLOR="#00DD00">Chosen by YAHOO! as coolest chat site for 2001</FONT><CENTER>
<CENTER><FONT COLOR="#80FF00" SIZE="+2">E</FONT><FONT COLOR="#80FF00" SIZE="+1">NTER</FONT><FONT COLOR="#80FF00" SIZE="+2"> C</FONT><FONT COLOR="#80FF00" SIZE="+1">YBERTOWN</FONT>
<br>
<img src="<$g_HTMLRoot>/places/enter/images/enter.jpg" width=381 height=139 border=0 alt="Enter Now!">
</CENTER>
</td>

<td width=150 align=right>
<!-- #ifndef variable="imm" -->
<!--A HREF="register<$g_exe>"-->
<IMG HEIGHT=14 WIDTH=85 SRC="<$g_Images>/images/login/immigrate.gif" BORDER=0 ALT="Immigrate"><!--/a-->
<br>
<!-- #ifdef variable="T_IWOS" -->
  <A HREF="register<$g_exe>?T_IWOS=1">
<!-- #endif variable="T_IWOS" -->
<!-- #ifndef variable="T_IWOS" -->
  <A HREF="register<$g_exe>">
<!-- #endif variable="T_IWOS" -->
<IMG HEIGHT=83 WIDTH=84 SRC="<$g_Images>/images/login/register.gif" BORDER=0 ALT="Immigrate Today!"></a>
<!-- #endif variable="imm" -->
</td>
</tr></table>

<!-- testing -->

<!-- #ifdef variable="ID" -->
<form action="<$selfurl>" method="POST" target="<$TARGET>" name=loginform>
<input type="hidden" name="TKT" value="<$TKT>">
        <input type="HIDDEN" name="ID" value="<$ID>">

<!-- #ifdef variable="plc" value="club" -->
        <input type="HIDDEN" name="plc" value="club">
        <input type="HIDDEN" name="DTY" value="CL">
<!-- #endif variable="plc" -->


<!-- #endif variable="ID" -->



<!-- #ifndef variable="ID" -->

<!-- #ifdef variable="plc" -->
<form action="<$selfurl>" method="POST" target="<$TARGET>" name=loginform>
        <input type="hidden" name="TKT" value="<$TKT>">
        <input type="HIDDEN" name="plc" value="<$plc>">
<!-- #endif variable="plc" -->


<!-- #ifndef variable="plc" -->
<form action="place<$g_exe>" method="POST" target="<$TARGET>" name=loginform>
        <input type="hidden" name="TKT" value="<$TKT>">
<!-- #endif variable="plc" -->

<!-- #endif variable="ID" -->



<input type="HIDDEN" name="ac" value="<$ac>">
<input type="HIDDEN" name="login" value="true">

<table border="0" width=100%>
        <tr align="center">
                
<td align="center" width=100 valign=top><INPUT NAME="forgot" TYPE="Image" SRC="<$g_Images>/images/login/resend.jpg"
                ALT="forgot your password" align="middle" border=0></INPUT>
        </td>
        <td width=120 align="left" valign=top><small>
                If you forgot your Password,
                click <A HREF="register<$g_exe>?ac=forgot">here</a> and we will
          <A HREF="register<$g_exe>?ac=forgot">email</A> it to you. <font color="red"><b><blink>NEVER, EVER</blink> give your password to anyone else, no matter who they claim to be or what jobs they offer you!</b></font></small>
        </td>
<td width=30>&nbsp;</td>
<td>
<input type=hidden name="T_IN" value="<$T_IN>">
<table border="0">
<tr align="center">
<td align="center">Nickname</td>
<td align="center"><input type="text" name="NNM" size="16" value="<$NNM>" maxlength="16" tabindex="1"></td>
</tr>
<tr align="center">
<td align="center">Password</td>
<td align="center">
<input type="password" name="PWD" size="16" value="<$PWD>" maxlength="16" tabindex="2"
onchange="checksubmit()">
</td>
<tr align=center>
<td align="center" colspan=2><input type="submit" value="Enter " tabindex="3"> <input type=submit name="cancel3" value="Cancel">
</td>
</tr>
</table>

</td>
<td width=30>&nbsp;</td>
        <td width=120 align="right" valign=top><small>
                If you want to
                <A HREF="register<$g_exe>?ac=chpass">change</a> your Password,
                click <A HREF="register<$g_exe>?ac=chpass">here</a>.
		<font color="yellow"><b><blink>ALWAYS</blink> make your password something <blink>VERY HARD</blink> for anyone to guess, and use it for Cybertown exclusively!</b></font></small>
        </td>
        <td align="center" width=100 valign=top><INPUT NAME="chpass" TYPE="Image" SRC="<$g_Images>/images/login/change_enter.jpg"
                ALT="change password" align="middle" border=0></INPUT>
        </td>
                
        </tr>

</table>

<br>
<!-- #ifdef variable="loginerror001" -->
        <blockquote><font color="#FF0000"><p>Login failed, please try again!</p></font></blockquote>
<!-- #endif variable="loginerror001" -->

<!-- #ifdef variable="loginerror002" -->
        <blockquote><font color="#FF0000"> Sorry <$NNM>, you have been excluded
        from the community under the <a href="http://www.cybertown.com/UBP2090.html" target="_blank">UBP</a> until <$EXD_MON>/<$EXD_MDAY>/<$EXD_YEAR>. Re-entry under any other nickname, whether created prior to or after your date of exclusion will result in a permanent ban.
        <br>
        <script language="JavaScript">
	var days = 0;
	var difference = 0;
	ctday = new Date(<$CT_YEAR>, <$CT_MON>,<$CT_MDAY>,01, 01, 01);
	exdate = new Date(<$EXD_YEAR>, <$EXD_MON>, <$EXD_MDAY>,01, 01, 01);
	difference = exdate - ctday;
	days = Math.round(difference/(1000*60*60*24));
	document.write("You have "+days+" days left to your ban<br>");
	</script>
        
        </font></blockquote>
<!-- #endif variable="loginerror002" -->
<!-- #ifdef variable="loginerror003" -->
        <blockquote><font color="#FF0000"><p>Sorry <$NNM>, there are already too many members loged in
        in the community.
        <br>
        Please try again later.</font></blockquote>
<!-- #endif variable="loginerror003" -->



        <input type="hidden" name="backurl" value="<$pbackurl>">
</form>
</p>

<form method=post action="register<$g_exe>">
<input type="hidden" name="TKT" value="<$TKT>">
        <input type=hidden name="backurl" value="<$pbackurl>">
        <input type=hidden name="NNM" value="<$NNM>">
        <input type=hidden name="GHDEBUG" value="1">
        <!--input type=submit name="forgot" value="Resend">
        <input type=submit name="chpass" value="Change"-->


        

   



<font color=#ff0000>
<!-- #ifdef variable="forgotok001" -->
Your Password will be sent to you if you request it with your Nickname and your email
<br>
mailto: <a href="mailto:Help@cybertown.com?subject=forgotten password">Help@cybertown.com</a>
<!-- #endif variable="forgotok001" -->
</font>

</form>




<p>
<b>Immigration or Login Problems?</b> Check the
<a href="javascript:loadInfo('<$g_HTMLRoot>/help/quickhelp.html')" target="_self">Quick Help</a>!<br><br>
<font size=+1 color="#FFFF00">
<strong>Please note:</strong>
to enter the site your browser must accept cookies. 
</font>
<small>
<font color="#FFFF00">
<br>Netscape 4.x: menu 'edit-preferences-advanced-accept cookies' IE 4.x: menu 'view-internet options-advanced-accept cookies'
</font>
</small>
</p>
</div>

<!-- #include virtual="<$g_Templates>common/focusform.tmpl" -->
<img src="http://tracking.ym0.net/im3.asp?A=11821&P=14032" length=0 width=0>
</BODY>
</HTML>
<!-- #endif variable="T_MCO" -->
