#!/usr/bin/perl
use Data::Dumper;
{
	# process
	# this package defines a process object
	#
	package process;

	# new - create a process object
	sub new {
		my ($class, $name, $state) = @_;
		my $self = { name => $name, state => $state };
		return bless $self, $class;
	}

	# link method - get or set the link to the next process
	# Usage:
	# 	$next = $proc->link;
	# Or:
	# 	$proc->link( $other_proc );
	sub link {
		my $process = shift;
		return @_ ? ($process->{link} = shift) : $process->{link};
	}

	sub run {
		my $process = shift;
		return "process name: ".$process->{name}.", process state: ". $process->{state};
	}

	# ... and a fewer other routines ...
}

# Create the idle process. Its state contains a program that 
# loops forever, giving up its slice immediately each time.
$idle = new process("Idle", $idle_state);

# Create the boot process, wich loads some program in from disk, 
# initializes and queues the process state for that program, and then exits.
$boot = new process("Boot", $boot_state);

# Set up the circular link
$idle->link($boot);
$boot->link($idle);

# and get ready to run, as if we just finished a slice for $idle.
$pred = $boot;
$current_process = $idle;
$quit_cause = $SLICE_OVER;

# here the scheduler - it never exits
while (1) {
	if ( $quit_cause == $SLICE_OVER ) {
		# Move to the next process.
		$pred = $current_process;
		$current_process = $current_process->link;
	} elsif ( $quit_cause == $IO_BLOCK ) {
		# The current process has issued some I/O.
		# Remove it form the list, and move on to the next.
		$next_process = $pred->link( $current_process->link );
		# Add current_process to a list for the I/O device.
		IO_wait($current_process);
		$current_process = $next_process;
	} elsif ( $quit_cause == $IO_COMPLETE ) {
		# Some I/O has completed - add the process 
		# waiting for it back into the list.
		# If the current process is idle, progress to 
		# the new process immediately.
		# Otherwise, continue the current process 
		# until the end of its slice.
		$io_process->link( $current_process );
		$pred = $pred->link( $io_process );
	} elsif ( $quit_cause == $QUIT ) {
		# This process has completed - remove it from the list.
		$next_process  = new process( $current_process->link );
		$current_process = $next_process;
	} elsif ( $quit_cause == $FORK ) {
		# Fork a new process. Put it at the end of the list.
		$new_process = new process( $current_process->process_info );
		$new_process->link( $current_process );
		$pred = $pred->link( $new_process );
	}

	# run the current process
	$quit_cause = $current_process->run;
	print Dumper $quit_cause;
}
