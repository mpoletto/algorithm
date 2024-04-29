#!/usr/bin/perl

sub get_names {
    my ($names) = @_;

    foreach (@$names) {
        print @$names, "\n";
    }
}

@names = ('Felipe', 'Joana', 'Alice');

get_names(\@names);