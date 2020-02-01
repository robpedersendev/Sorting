# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i # What our second loop will use for its first index
        smallest_index = cur_index # How we will designate as the
        # smallest number and restart loops if smaller numbers are
        #  found while using the second loop
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)): # This loop will run
            # through the remaining items in loop between where the
            # loop starts and ends
            if arr[smallest_index]>arr[j]: # If the value of the item
                # at the current index is larger then the index of where
                # [j] is
                smallest_index = j # Update the smallest index
        # (hint, can do in 3 loc)
        temp = arr[smallest_index] # Create temp variable to hold the
        #number at the index of arr[smallest_number]
        arr[smallest_index]=arr[cur_index] # Overwrite the smallest
        #index value with the value of the index of cur_index in the array
        arr[cur_index]=temp # Overwrite the value of arr[cur_index] with
        #the value of temp



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap_flag = True
    while swap_flag is True:
        swap_flag = False
        for j in arr:
            if arr[j]> arr[j+1]:
                ##swap numbers
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1]=temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr