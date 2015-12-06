#!/usr/bin/perl

#use strict;
#use CGI;

#my $q = new CGI;
#my $submitdel = $q->param('submitdel');
#my $submitadd = $q->param('submitadd');

read(STDIN, $formdata, $ENV{'CONTENT_LENGTH'});

#print "Content-type: text/html\n\n";

foreach $data(split(/&/,$formdata)) {
	($key, $value) = split(/=/,$data);
	$hash{$key} = $value;
}

if ($hash{func} eq "add") {
    if ( $hash{url} ne "" ) {
        $hash{url} =~ s/\+/ /g;
        $hash{url} =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack('C', hex($1))/eg;
        $hash{url} =~ s/\t//g;

	system("wget $hash{url}");
	@tvpid = split(/\//, $hash{url});

	if ( $hash{acd} eq "1" ) {
        	system("/root/tool/atprog $tvpid[3]");
	} else {
        	system("/root/tool/atprog $tvpid[3] 1");
	}	
    }
}

if ($hash{func} eq "del") {
    if ( $hash{id} ne "" ) {
        system("/usr/bin/atrm $hash{id}");
    }
}

print "Location: /atlist.cgi\n\n";


