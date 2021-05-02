#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line       = line.strip()   
    key_value  = line.split(",")   
    show     = key_value[0]   
    channel   = key_value[1]   

    #print show
    if (channel.isdigit()):					
    	print( '%s\t%s' % (show, channel) )  
    elif (channel == "ABC"):
    	print( '%s\t%s' % (show, channel) )

