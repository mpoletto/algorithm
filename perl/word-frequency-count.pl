#! /usr/bin/perl
use Data::Dumper;
# word frequency count

while(<>) {                              # iterate over lines in named file
    # print "$. $_";                       # print line number and line
    tr/A-Za-z/ /cs;                      # remove punctuation
    # exit 0 if $. > 10;                   # stop after 10 lines
    foreach $word (split(' ', lc $_)) {  # each word in line, lc is lowercase
	    $freq{$word}++;                  # increment frequency count for word
    }
}

print Dumper(\%freq);

foreach $word (sort keys %freq) {        # sort words found
    print "$word $freq{$word}\n";        # print word with its frequency
}