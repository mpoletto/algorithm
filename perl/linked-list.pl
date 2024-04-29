#!/usr/bin/perl
use Modern::Perl;
use Data::Dumper;

my $list = undef;
foreach (reverse 1..5) {
    # print $_, "\n";
    $list = [$list, $_ * $_];
}

sub prynt {
    my ($list) = @_;
    use constant NEXT => 0;
    use constant VAL => 1;
    print $list->[VAL] // 'undef', "\n";
    print $list->[NEXT][VAL] // 'undef', "\n";
    print $list->[NEXT][NEXT][VAL] // 'undef', "\n";
    print $list->[NEXT][NEXT][NEXT][VAL] // 'undef', "\n";
    print $list->[NEXT][NEXT][NEXT][NEXT][VAL] // 'undef', "\n";
}
print "original\n";
prynt($list);

my $first = $list->[1];
my $second = $list->[0][1];
$list->[1] = $second;
$list->[0][1] = $first;
print "exchanged 1 and 2\n";
prynt($list);

$list->[NEXT] = [ $list->[NEXT], 49 ];
print "included 49\n";
prynt($list);