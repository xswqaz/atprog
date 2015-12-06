#!/usr/bin/perl


print "Content-type: text/html\n\n";
print "<html><body><pre>";

print "<form action=\"atedit.cgi\" method=\"post\">";


my @result=`/root/tool/listprog`;
#my @result=`/root/tool/listprog`;
#my @result=`atq`;

foreach my $line (@result) {
        chomp($line);

	my( $id, $line ) = split(/ /,$line,2);	

        print "<input type=\"checkbox\" name=\"id\" value=\"$id\">$line<br>";
}

print "<input type=text name=url size=50><br>";

print "<input type=\"submit\" name=func value=add>&nbsp;";
print "<input type=\"submit\" name=func value=del>&nbsp;";
print "acd<input type=\"checkbox\" name=acd value=1 checked=\"checked\"></form>";

print "</pre></body></html>\n";

