#! /usr/bin/perl

# Bentley1, the cubic algorithm

# maximum of two numbers
sub max {
    my ($x, $y) = @_;
    return $x > $y ? $x : $y;
}

# Bentley's algorithm 1, the cubic algorithm
sub bentley1 {                           # @_ is Bentley's array X
    my ($sum, $maxsofar);
    for ($l = 0; $l < @_; $l++) {
        for ($u = $l; $u < @_; $u++) {   # @_ in scalar context is length of X
            $sum = 0;
            for ($i = $l; $i <= $u; $i++) {
                $sum += $_[$i];    # $sum now contains the sum of @X[l..u]
            }
            $maxsofar = max($sum, $maxsofar);
            print $l, " ", $u, " ", $sum, " ", $maxsofar, "\n";
        }
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
print "Algorithm 1, the cubic algorithm\n";
@ex = (31, -41, 59, 26, -53, 58, 97, -93, -23, 84); # Bentley's example
print "Bentley's test data: @ex\n";
print "The maximum segment sum of Bentley's data is ",bentley1(@ex),"\n";


#print "The mss. of 3 0 ... 0 4 with 10 0's is ", bentley1(3,pad(0,10),4),"\n";
#print "The mss. of 3 0 ... 0 4 with 100 0's is ", bentley1(3,pad(0,100),4),"\n";
#print "The mss. of 3 0 ... 0 4 with 200 0's is ", bentley1(3,pad(0,200),4),"\n";
#print "The mss. of 3 0 ... 0 4 with 400 0's is ", bentley1(3,pad(0,400),4),"\n";
#print "The mss. of 3 0 ... 0 4 with 1000 0's is ", bentley1(3,pad(0,1000),4),"\n";
