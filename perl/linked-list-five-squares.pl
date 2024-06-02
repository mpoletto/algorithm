#!/usr/bin/perl
use Data::Dumper;
use constant NEXT => 0;
use constant VAL => 1;

$list = undef;
foreach (reverse 1..5) {
	$list = [ $list, $_ * $_ ];
}

$one = $list;
$four = $one->[NEXT];
$nine = $four->[NEXT];
$sixteen = $nine->[NEXT];
$tfive = $sixteen->[NEXT];

print "1) ", $one->[VAL], "\n";
print "4) ", $four->[VAL], "\n";
print "9) ", $nine->[VAL], "\n";
print "16) ", $sixteen->[VAL], "\n";
print "25) ", $tfive->[VAL], "\n";

$val = $list;
for ($i = 0; $i < 5; $i++) {
	print $val->[VAL], "\n";
	$val = $val->[NEXT];
}

print Dumper $list;
print Dumper $list->[1];
print Dumper $list->[0][1];
print Dumper $list->[0][0][1];
print Dumper $list->[0][0][0][1];
print Dumper $list->[0][0][0][0][1];
