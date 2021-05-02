#!/usr/bin/env python3
import sys

prev_show	= None		
total_channel = 0			
print_flag  = 0 		

for line in sys.stdin:
    line       = line.strip()      
    key_value  = line.split('\t')   

     
    curr_show  = key_value[0]         
    channel   = key_value[1]         

    if (prev_show != curr_show):
        if (print_flag == 1):
            print('%s\t%s' % (prev_show, total_channel))
            print_flag = 0
            total_channel = 0
        if (channel != "ABC"):					
            (total_channel) = int(channel)		
    else:										
        if (channel != "ABC"):					
            (total_channel) = int(total_channel)	
            (channel)    = int(channel)		
            (total_channel) = (total_channel) + (channel)	
    if (channel == "ABC"):
        print_flag = 1
    prev_show = curr_show	

