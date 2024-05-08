#!/usr/bin/perl
use Modern::Perl;
use Data::Dumper qw(Dumper);
my %flintstones_birthday = ('Fred' => 'May, 5th', 'Wilma' => 'October, 26th', 'Pebbles' => 'October, 8th', 'Barney' => undef, 'Betty' => '');

print "\n";
print "foreach:\n";
foreach my $key (keys %flintstones_birthday) {
	print $flintstones_birthday{$key}, "\n" if $flintstones_birthday{$key};
}

print "\n";
print "while each:\n";
while (my ($key, $value) = each(%flintstones_birthday)) {
	print $key, ": ";
	print $value, "\n" if defined;
}

print "\n";
print "for:\n";
for my $name (keys %flintstones_birthday) {
	print $name, ": ", $flintstones_birthday{$name}, "\n" if $flintstones_birthday{$name};
}

# print Dumper \@ARGV;
my $name = shift or die "Give a name, please\n";
my $test_name = 0;
for my $name_key (keys %flintstones_birthday) { 
	if ($name eq $name_key) {
		$test_name = 1;
	}
}
if (!$test_name) {
	print "This name isn't in the list\n";
	exit 1;
}
if (!exists $flintstones_birthday{$name}) {
	print "We don't have the birthday for $name\n";
	exit 1;
}
print $flintstones_birthday{$name}, "\n";


print "Enter a name\n";
chomp( my $name_from_stdin = <STDIN> );
print $name_from_stdin, "\n";
