#!/usr/bin/perl
# $index = binary_search(\@array, $word)
# @array is a list of lowercase strings in alphabetical order.
# $word is the target word that might be in the list.
# binary_search() returns the array index such that $array[$index] is $word.

package BinarySearch;
use Exporter;
our @ISA=qw( Exporter );
our @EXPORT=qw( binary_search );

sub binary_search {
    my ($arrayref, $word) = @_;
    my ($low, $high) = (0, @$arrayref - 1);
    while ($low <= $high) {
        my $try = int(($low + $high) / 2);
        $low = $try+1, next if $arrayref->[$try] lt $word;
        $high = $try-1, next if $arrayref->[$try] gt $word;
        return $try;
    }
    return;
}
# my @array = ('apple', 'banana', 'cherry', 'date', 'elderberry', 'fig');
# my $index = binary_search(\@array, @ARGV);
# print $index."\n";

1;