AAAA-check
==========

A repository of simple programs to check for the existence of IPv6 addresses (AAAA records) in DNS.

----

aaaa-check.py 
-------------

A *very* simple program that loops forever to check whether manually input domain names
have IPv6 addresses (AAAA records).  Created out of the need to check whether domain names entered
into a web site had AAAA records.  The cleaner way to do this would be to build it into the 
website itself - and that may happen - but in the meantime I could copy domain names from the
web page and paste them into the terminal window where I had this app running.

To terminate the program simply do a Ctrl+C

Requires the dnspython library available from 
   http://www.dnspython.org/ or 
   https://github.com/rthalley/dnspython
