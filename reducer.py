#!/usr/bin/env python3
import sys

prev_show	= None		
total_views = 0			
print_flag  = 0 		

for line in sys.stdin:
    line       = line.strip()      
    key_value  = line.split('\t')   

     
    curr_show  = key_value[0]         
    value_in   = key_value[1]         

    if (prev_show != curr_show):
        if (print_flag == 1):
            print('%s\t%s' % (prev_show, total_views))
            print_flag = 0
            total_views = 0
        if (value_in != "ABC"):					
            (total_views) = int(value_in)		
    else:										
        if (value_in != "ABC"):					
            (total_views) = int(total_views)	
            (value_in)    = int(value_in)		
            (total_views) = (total_views) + (value_in)	
    if (value_in == "ABC"):
        print_flag = 1
    prev_show = curr_show	


