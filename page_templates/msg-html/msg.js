<!-- msg/msg.js -->
<!--- dynamic javascript for messaging --->

<!-- #include file="<$g_Templates>/common/getframe.html" -->

<script language="javascript">

var url_prt   = "<$g_cgiRoot>/print<$g_exe>?";
var url_msg   = "<$g_cgiRoot>/msg<$g_exe>?";
var par_del   = "ac=delete&ID=";
var par_mdel  = "ac=mdelete&ID=";
var par_cre   = "ac=create&TYP=I&PDT=<$PDT>&PKE=<$PKE>&";

var par_ibox = "TPL=msg/listmessages&INBOX=OWNSDA&OWN=<$MEM_ID><$VIS_ID>&TYP=I<$g_SessionID>&";
var par_obox = "TPL=msg/listmessages&OUTBOX=OWNSDA&OWN=<$MEM_ID><$VIS_ID>&TYP=O<$g_SessionID>&";
var par_rbox = "TPL=msg/listmessages&ALERTS=OWNSDA&OWN=<$MEM_ID><$VIS_ID>&TYP=N<$g_SessionID>&";
var par_fbox = "TPL=msg/listmessages&FILTER=OWNSDA&TYP=T<$g_SessionID>&";
var par_tbox = "TPL=msg/listmessages&THREAD=OWNSDA&OWN=<$MEM_ID><$VIS_ID><$g_SessionID>&";
var par_sbox = "TPL=msg/messages&OWN=<$MEM_ID><$VIS_ID><$g_SessionID>&";

var par_icre = "TPL=msg/listmessages&INBOX=OWNSDA&OWN=<$MEM_ID><$VIS_ID>&NEXT_TYP=I<$g_SessionID>&";
var par_ocre = "TPL=msg/listmessages&OUTBOX=OWNSDA&OWN=<$MEM_ID><$VIS_ID>&NEXT_TYP=O<$g_SessionID>&";
var par_rcre = "TPL=msg/listmessages&ALERTS=OWNSDA&OWN=<$MEM_ID><$VIS_ID>&NEXT_TYP=N<$g_SessionID>&";
var par_xcre = "TPL=msg/sendclose&T_PDT=<$PDT>&T_PKE=<$PKE><$g_SessionID>&";
var par_pcre = "TPL=member/info&DTY=M<$g_SessionID>&";

var par_send = "TPL=msg/createmessage&T_LB=<$T_LB>&PDT=<$PDT>&PKE=<$PKE><$g_SessionID>";
var par_lbud = "TPL=msg/listbuddy&OWN=<$MEM_ID><$VIS_ID>&T_LB=buddylist<$g_SessionID>";
var par_ibud = "TPL=msg/updatebuddy&TYP=INSERT&INSERT_NNM=NNM&INSERT_ID=ID&OWN=<$MEM_ID><$VIS_ID><$g_SessionID>";
var par_dbud = "TPL=msg/updatebuddy&TYP=DELETE&DELETE_ID=ID&OWN=<$MEM_ID><$VIS_ID><$g_SessionID>";
var par_prof = "TPL=member/info&DTY=M<$g_SessionID>";

var url_ibox = url_prt + par_ibox;
var url_obox = url_prt + par_obox;
var url_rbox = url_prt + par_rbox;
var url_fbox = url_prt + par_fbox;
var url_tbox = url_prt + par_tbox;
var url_sbox = url_prt + par_sbox;
var url_send = url_prt + par_send;
var url_lbud = url_prt + par_lbud;
var url_ibud = url_prt + par_ibud;
var url_dbud = url_prt + par_dbud;
var url_prof = url_prt + par_prof;

var mem_id = "<$MEM_ID><$VIS_ID>";
var cgi_rt = "<$g_cgiRoot>";
var ses_id = "<$g_SessionID>";
var ext_ex = "<$g_exe>";

var security_warning  = "Use this form only in real security problem situations. False reports will result in being excluded from the community.";
var security_deftext  = "I have a security problem. Please contact me.";
var broadcast_warning = "Use this form only for broadcast messages to all online users.";
var broadcast_deftext = "";

</script>

<script language="javascript" src="<$g_HTMLRoot>/common/msg.js" type="text/javascript">
</script>
