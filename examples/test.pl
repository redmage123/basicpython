#!/usr/bin/env perl 
#===============================================================================
#
#         FILE: test.pl
#
#        USAGE: ./test.pl  
#
#  DESCRIPTION: 
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: YOUR NAME (), 
# ORGANIZATION: 
#      VERSION: 1.0
#      CREATED: Thursday 16 October 2014 10:51:30  IST
#     REVISION: ---
#===============================================================================

use strict;
use warnings;
use utf8;


my $foo;

$foo = "24,000,000";


$foo =~ s/,//g;
print $foo,"\n";
