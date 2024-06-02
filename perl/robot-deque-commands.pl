#!/usr/bin/perl
use Data::Dumper;

my @control_commands  = ();	# no previous commands
my $delay_until = time;		# no command in progress

# Central loop - process robot commands in detail.
$i = 0;
while ( $i < 1 ) { # only terminate on an EXIT command
	# Check for new command input.
	if ( command_available() ) {
		push( @control_commands, get_command(1) );
	}
	if ( $delay_until <= time and $command = shift( @control_commands ) ) {
		if ( ! ref $command ) {
			# Parse the high-level text command.
			# When the command has been parsed into internal form, 
			# it will be put at the front of the deque for immediate 
			# processing (since it is the details of the current 
			# command that have been determined).
			unshift( @control_commands, [ $intcmd, $arg1, $arg2 ] );
		} else { 
			$op = $command->[0];
			# Process an internal command.
			PROCESS_COMMAND();
		}
	}
	$i++;
}

sub command_available() {
	@command = (
		'Put the elbow up on to the table.', 
		'Open the fingers', 
		'Put the opened fingers close to the cup of glass', 
		'Close the fingers tightened on the cup of  glass', 
		'Get up the cup of glass close to the mouth'
	);
	return \@command;
}

sub get_command() {
	$key = shift;
	$c = command_available()->[$key];
	print Dumper $c;
	return $c
	#exit();
}

sub PROCESS_COMMAND() {
}
