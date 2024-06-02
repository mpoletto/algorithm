#!/usr/bin/perl

@control_commands  = ();

push( @control_commands, "rotate shoulder until above table" );
push( @control_commands, "open elbow until hand at table level" );
push( @control_commands, "open fingers" );
push( @control_commands, "close elbow 45 degrees" );
$i = 0;
while ( $command = shift( @control_commands ) ) {
	print $#control_commands, $command, "\n";
	# "Efficiency Tip: push-shift Versus unshift-pop. push and shift can be 100 times faster than
	# unshift and pop. Perl grows an array by ever larger amounts when it is extended at the end but
	# grows it only by small amounts when it is extended at the front"
	unshift( @control_commands, "teste ". ++$i ) unless $i > 10;
}
