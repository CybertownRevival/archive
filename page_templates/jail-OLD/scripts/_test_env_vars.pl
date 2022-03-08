#!/usr/bin/perl

                      print "Content-type: text/html\n\n";
                      print "\n";

                      foreach $key (sort keys(%ENV)) {
                          print "$key = $ENV{$key} <br>";
                      }
			print "back=". $ENV{'HTTP_REFERER'};
exit(0);

