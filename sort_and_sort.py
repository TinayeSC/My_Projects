#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:54:18 2023

@author: sam
"""

def binary_search(item, arr):
    low, high = 0, len(arr) - 1
    # Keep iterating until low and high cross
    # Returns None if item not found
    while high >= low:
        # Find midpoint
        mid = (low + high) // 2
        # If item is found at midpoint, return
        if arr[mid] == item:
            print(arr[mid])
            return mid
        # Else, if item at midpoint is less than item,
        # search the second half of the list
        elif arr[mid] < item:
            low = mid + 1
        # Else, search first half
        else:
            high = mid - 1
            
def sequential_search(item, arr):
    # If item is not found, return None
    # Iterate over list. If we find our item, break loop
    # and return index
    for i in range(len(arr)):
        if arr[i] == item:
            return i

following_array = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

#from my understanding, if the array was ordered from smallest to largest
# then a binary search would be useful
#as a result, I believe that the sequential search is likely the better choice
index = (sequential_search(9, following_array))
print(f"The number 9 occurs at the index {index} ")

# Insertion sort in Python from programiz.com


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key



print("\nUsing Insertion Sort:")
insertionSort(following_array)
print(following_array)

#as i mentioned before, the binary search is very effecient for ordered lists
#in the real world this has many applications. probably has use in catalouging grocery stores,
#libraries, and other places where items are ordered and their order is recorded on some device
print("\n")
print("Number Searched for:\nIndex:")
print(binary_search(9,following_array)) 


