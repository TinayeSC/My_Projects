
#Bubble Sort is O(n2)
def bubble_sort(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(1, i + 1):
            if arr[j - 1] > arr[j]:
return arr

#Quick Sort is O(log n)
def quick_sort(arr, low, high):
    if low < high:
        mid = partition(arr, low, high)
        arr = quick_sort(arr, low, mid - 1)
        arr = quick_sort(arr, mid + 1, high)
return arr

#This is the partition method that is used to select the pivot point and move the elements around:
def partition(arr, low, high):
    # The pivot point is the first item in the subarray
    pivot = arr[low]
    # Loop through the array. Move items up or down the array so that they
    # are in the proper spot with regards to the pivot point
    while low < high:
        # Can we find a number smaller than the pivot point:
        # Keep moving the high marker down the array until we find this
        # or until high==low
        while low < high and arr[high] >= pivot:
high -= 1
        if low < high:
            # Found a smaller number, swap it into position
            arr[low] = arr[high]
            # Now look for a number larger than the pivot point
 
while low < high and arr[low] <= pivot:
            low += 1
        if low < high:
            # Found one! Move it into position
            arr[high] = arr[low]
# Move the pivot back into the array and return its index
arr[low] = pivot
return low

#Merge Sort is O(n log(n))
 
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
    while i_1 < end_1 or i_2 < end_2:
        if i_1 < end_1 and i_2 < end_2:
            if items[i_1] < items[i_2]:
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

#Python includes its own sort() method, which uses the Timsort algorithm.
my_list = [54,26,93,17,77,31,44,55,20]
my_list.sort()
print(my_list)

#linear search is O(n)
def sequential_search(item, arr):
    # If item is not found, return None
    # Iterate over list. If we find our item, break loop
    # and return index
    for i in range(len(arr)):
        if arr[i] == item:
            return i


#Binary search is O(log n) 
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


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)