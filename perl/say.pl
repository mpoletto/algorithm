#!/usr/bin/perl
#use Modern::Perl;
$_ = 'My name is Someone.';
say if /My name is/;
s/Someone/Anyone/;
tr/A-Z/a-x/;
say;
