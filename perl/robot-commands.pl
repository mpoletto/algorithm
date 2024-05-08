#!/usr/bin/perl

@control_commands  = ();

push( @control_commands, "rotate shoulder until above table" );
push( @control_commands, "open elbow until hand at table level" );
push( @control_commands, "open fingers" );
push( @control_commands, "close elbow 45 degrees" );
$i = 0;
while ( $command = shift( @control_commands ) ) {
	print $command, "\n";
	unshift( @control_commands, "teste ". ++$i ) unless $i > 10;
}
