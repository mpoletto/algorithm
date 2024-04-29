#!/usr/bin/perl
use Benchmark qw(:all);
use FindBin qw($RealBin);
use lib "$RealBin";
use BinarySearch;

@ary = ('apple', 'banana', 'cherry', 'date', 'elderberry', 'fig');
@ary2 = ('apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'teste', 'welcome');

timethis ($count, "code");

# Use Perl code in strings...
timethese($count, {
    'binary_search' => binary_search(@ary, 'date'),
    'binary_search2' => binary_search(@ary2, 'date'),
});
# ... or use subroutine references.
# timethese($count, {
#     'Name1' => sub { ...code1... },
#     'Name2' => sub { ...code2... },
# });
# cmpthese can be used both ways as well
cmpthese($count, {
    'binary_search' => binary_search(@ary, 'date'),
    'binary_search2' => binary_search(@ary2, 'date'),
});
# cmpthese($count, {
#     'Name1' => sub { ...code1... },
#     'Name2' => sub { ...code2... },
# });
# ...or in two stages
$results = timethese($count,
    {
        'binary_search' => binary_search(@ary, 'date'),
        'binary_search2' => binary_search(@ary2, 'date'),
    },
'none'
);
cmpthese( $results ) ;
$t = timeit($count, binary_search(@ary, 'date'));
print "$count loops of other code took:",timestr($t),"\n";
$t = countit($time, binary_search(@ary, 'date'));
$count = $t->iters ;
print "$count loops of other code took:",timestr($t),"\n";
# enable hires wallclock timing if possible
use Benchmark ':hireswallclock';