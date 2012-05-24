#!/usr/bin/env python

import dns.resolver
import dns.exception

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
