# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i # What our second loop will use for its first index
        smallest_index = cur_index # How we will designate as the smallest
        #number and restart loops if smaller numbers are found while using the second loop
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)): # Compares
            if arr[smallest_index]>arr[j]:
        # (hint, can do in 3 loc)



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr