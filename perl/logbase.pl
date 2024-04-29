#!/usr/bin/perl

use Benchmark;
use Data::Dumper;
use constant pi => 3.14159265358979;

sub volume_var {
	my ($r, $n) = @_;

	my $denom;
	if ($n % 2) {
		$denom = sqrt(pi) * factorial (2 * (int($n / 2)) + 2) / 
				 factorial(int($n / 2) + 1) / (4 ** (int($n / 2) + 1)); 
	} else {
		$denom = factorial($n / 2);
	}
	return ($r ** $n) * (pi ** ($n / 2)) / $denom;
}

sub volume_novar {
	my ($r, $n) = @_;
	if ($n % 2) {
		return ($r ** $n) * (pi ** ($n / 2)) / 
				(sqrt(pi) * factorial(2 * (int($n / 2)) + 2) / 
				factorial(int($n / 2) + 1) / (4 ** (int($n / 2) + 1)));
	} else {
		return ($r ** $n) * (pi ** ($n / 2)) / factorial($n / 2);
	}
}

sub factorial {
	my $n = shift // die "Usage: $0 N\n";
	
	my $f = 1;
	my $i = 1;
	$f *= ++$i while $i < $n;
	return $f;
}

sub logbase1 {
	my ($base, $numbers) = @_;
	my $result;

	for (my $i = 0; $i < @$numbers; $i++) {
		push @result, log ($numbers->[$i]) / log ($base);
	}
	return @result;
}

sub logbase2 {
	my ($base, $numbers) = @_;
	my @result;
	my $logbase = log $base;
	for (my $i = 0; $i < @$numbers; $i++) {
		push @result, log ($numbers->[$i]) / $logbase;
	}
	return @result;
}

# $x = log(10)/log(3);
# print $x;

# print "factorial: ", factorial(10/2);

@numbers = (1..1000);

timethese (10000, { 
	no_temp => 'logbase1(10, \@numbers)', 
	temp => 'logbase2(10, \@numbers)'
	});

timethese (10000, { 
	no_temp => 'volume_var(10000, 10000)', 
	temp => 'volume_novar(10000, 10000)'
	});
