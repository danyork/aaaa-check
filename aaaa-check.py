#!/usr/bin/env python
#
# aaaa-check.py
#
# Copyright 2012 Dan York
# License: BSD
#
# A *very* simple program that loops forever to check whether manually input domain names
# have IPv6 addresses (AAAA records).  Created out of the need to check whether domain names entered
# into a web site had AAAA records.  The cleaner way to do this would be to build it into the 
# website itself - and that may happen - but in the meantime I could copy domain names from the
# web page and paste them into the terminal window where I had this app running.
#
# To terminate the program simply do a Ctrl+C
#
# Requires the dnspython library available from 
#   http://www.dnspython.org/ or 
#   https://github.com/rthalley/dnspython
#

import dns.resolver

while 1:
    try: 
        answer = dns.resolver.query(raw_input("Domain name = "), "AAAA")
        print answer[0]
    except dns.resolver.NoAnswer:
        print "No AAAA"
    except dns.resolver.NXDOMAIN:
        print "No such domain"
    except KeyboardInterrupt:
        print "\nGoodbye!"
	exit()
