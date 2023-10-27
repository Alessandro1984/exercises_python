# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:06:45 2023

@author: bramucci
"""

def steigung_funktion(werte):
    x1 = werte[0]
    y1 = werte[1]
    x2 = werte[2]
    y2 = werte[3]
    delta_x = x2 - x1
    delta_y = y2 - y1
    
    if delta_x == 0:
        print("Die Steigung ist nicht definiert.")
    else:    
        steigung = delta_y / delta_x
        return steigung
    
    
test_list = [1,1,3,4]
    
x = steigung_funktion([4, 4, 8, 4])

print(steigung_funktion([4, 4, 8, 4]))