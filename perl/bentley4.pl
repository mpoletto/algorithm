#! /usr/bin/perl

# Bentley4, the linear algorithm

# maximum of two numbers
sub max {
    my ($x, $y) = @_;
    return $x > $y ? $x : $y;
}

# Bentley's algorithm 4, the linear algorithm
sub bentley4 {                           # @_ is Bentley's array X
    my ($maxsofar, $maxendinghere);
    for ($i = 0; $i < @_; $i++) {
        $maxendinghere = max(0.0, $maxendinghere + $_[$i]);
        $maxsofar = max($maxsofar, $maxendinghere);
    }
    return $maxsofar;
}

# pad: for making test data, return an array of $n copies of the number $i
sub pad {
    my ($i, $n) = @_;
    my @a = ();
    for ($c = 0; $c < $n; $c++) {
	push(@a, $i); 
    }
    return @a;
}

# main program
print "Algorithm 4, the linear algorithm\n";
@ex = (31, -41, 59, 26, -53, 58, 97, -93, -23, 84); # Bentley's example
print "Bentley's test data: @ex\n";
print "The maximum segment sum of Bentley's data is ",bentley4(@ex),"\n";

# print "The mss. of 3 0 ... 0 4 with 10 0's is ", bentley4(3,pad(0,10),4),"\n";
# print "The mss. of 3 0 ... 0 4 with 100 0's is ", bentley4(3,pad(0,100),4),"\n";
# print "The mss. of 3 0 ... 0 4 with 200 0's is ", bentley4(3,pad(0,200),4),"\n";
# print "The mss. of 3 0 ... 0 4 with 400 0's is ", bentley4(3,pad(0,400),4),"\n";
# print "The mss. of 3 0 ... 0 4 with 1000 0's is ", bentley4(3,pad(0,1000),4),"\n";
# print "The mss. of 3 0 ... 0 4 with 2000 0's is ", bentley4(3,pad(0,2000),4),"\n";
# print "The mss. of 3 0 ... 0 4 with 4000 0's is ", bentley4(3,pad(0,4000),4),"\n";
# print "The mss. of 3 0 ... 0 4 with 10000 0's is ", bentley4(3,pad(0,10000),4),"\n";
# print "The mss. of 3 0 ... 0 4 with 20000 0's is ", bentley4(3,pad(0,20000),4),"\n";
# print "The mss. of 3 0 ... 0 4 with 40000 0's is ", bentley4(3,pad(0,40000),4),"\n";
# print "The mss. of 3 0 ... 0 4 with 100000 0's is ", bentley4(3,pad(0,100000),4),"\n";



