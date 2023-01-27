#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:33:06 2023

@author: sam
"""

def merge_sort(items):
 
    n = len(items)
    temporary_storage = [None] * n
    size_of_subsections = 1
    while size_of_subsections < n:
        for i in range(0, n, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2
    return items

#the below merges the split cells back together and then sorts them 
def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0
    
    #this is the only section that needed to be changed. 
    #the if statement was changed to be len(items[i_1]) > len(items[i_2])
    #this makes it so the merge sort is comparing the lengths of the items in the list
    while i_1 < end_1 or i_2 < end_2:
        if i_1 < end_1 and i_2 < end_2:
            if len(items[i_1]) > len(items[i_2]):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
            else:  # the_list[i_2] >= items[i_1]
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
            i_t += 1
        elif i_1 < end_1:
            for i in range(i_1, end_1):
                temporary_storage[i_t] = items[i_1]
 
            i_1 += 1
            i_t += 1
        else:  # i_2 < end_2
            for i in range(i_2, end_2):
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
                i_t += 1
    for i in range(i_t):
        items[start_1 + i] = temporary_storage[i]
                
#defining three unordered lists of words                 
list1 = ["fear","heard","signifies","suboptimal","community","mobilization","policy","early","nine","tenfold"] 
list2 = ["feverish","as","well","musing","individual","conglomerate","turbulent","tumultuous","free","zenith"]
list3 = ["a","you","please","me","they","exotic","mystical","subliminal","no","sir","eleventh","grace","peace","prosperity","wisdom"]

#calling the merge_sort sorting method to order the words from largest to smallest 

print(f"List 1\n{merge_sort(list1)}\n") 
print(f"List 2\n{merge_sort(list2)}\n")  
print(f"List 3\n{merge_sort(list3)}\n")              
            