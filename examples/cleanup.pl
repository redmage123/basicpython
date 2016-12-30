#!/usr/bin/env perl 
#===============================================================================
#
#         FILE: cleanup.pl
#
#        USAGE: ./cleanup.pl  
#
#  DESCRIPTION: i
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: YOUR NAME (), 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: Thursday 16 October 2014 10:17:35  IST
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use utf8;


my $team;
my $salary;
my $line;
my $name;
my $output;
my $position;

open(FH,"ALbb.salaries.2003.csv") or die ("ERROR: $!");
open(WFH,">ALbb.salaries.2003.formattted.csv") or die ("ERROR: $!");


for (my $i=0;$i<4;$i++) {
    $line =<FH>;
}



while (<FH>) {

        if (($team,$name,$salary,$position) = /^([a-zA-Z\s]+),(\".*?\"),\"(.*)\",(.*)$/) {
            $salary =~ s/,//g;
        $output = sprintf ("%s,%s,%s,%s\n", $team,$name,$salary,$position);
        printf(WFH $output);
    } else {
        print (WFH $_);
    }
}
close(FH);
close(WFH);
