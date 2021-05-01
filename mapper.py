#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line       = line.strip()   
    key_value  = line.split(",")   
    key_in     = key_value[0]   
    value_in   = key_value[1]    

    #print key_in
    if (value_in.isdigit()):					
    	print( '%s\t%s' % (key_in, value_in) )  
    elif (value_in == "ABC"):
    	print( '%s\t%s' % (key_in, value_in) )  

