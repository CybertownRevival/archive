#!/usr/bin/perl

require "pr_utils.pl";

# Configuration Variables

$mailprog = '/usr/sbin/sendmail';
#mailprog = '/usr/lib/sendmail';


# filename: will be displayed after sending form
$okfilename = "http://www.cybertown.com/problem_report/pr_ok.html";
$errorfilename = "http://www.cybertown.com/problem_report/pr_error.html";

@required = ('problem_description','nnm','form_url');
@reg_fields = ('email','nnm','problem_description','when_and_frequency','actions_before_error','OS','Other_OS','CPU_speed','RAM','Other_RAM','BROWSER','Other_Browser','Blaxxun_contact','graphics_accel_manufacturer','Other_graphics_accel','graphics_accel_model','graphics_accel_ram');

&get_date;
&parse_form;
&check_required;
$success = &send_mail($FORM{'mail_recipient'},$FORM{'mail_subject'});
$success && &send_verification($FORM{'email'});
$success?print "Location: $okfilename\n\n":print "Location: $errorfilename\n\n";

