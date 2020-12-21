'''
Merge Sort Algorithm Implementation 

Time: O(NlogN)
Space: O(N)
'''
import random

def MergeSort(array):
    if len(array) <= 1:
        return array
    temp = array[:]
    _helper(array, temp, 0, len(array) - 1)
    return array

def _helper(main, temp, start, end):
    if start == end:
        return
    mid = (start + end) // 2
    '''
    We want to eventually return the main array so we put temp at the parameter of the main array
    At every recursive call, it will change so that we don't lose our reference to the main array
    '''
    _helper(temp, main, start, mid)     #dividing left half
    _helper(temp, main, mid+1, end)     #dividing right half
    _merge(main, temp, start, mid, end)

def _merge(main, temp, start, mid, end):
    left, index = start, start
    right = mid + 1

    while left <= mid and right <= end:
       #Merging elements
        if temp[left] < temp[right]:
            main[index] = temp[left]
            left += 1
        else:
            main[index] = temp[right]
            right += 1
        index += 1

    while left <= mid:
        # Merging the rest of the left sub array into the resulting array
        main[index] = temp[left]
        index += 1
        left += 1
    
    while right <= end:
        # Merging the rest of the right sub array into the resulting array
        main[index] = temp[right]
        index += 1
        right += 1



if __name__ == "__main__":
    testArr = [random.randint(0,11) for _ in range(10)]
    correctArr = testArr.copy()

    assert MergeSort(testArr) == sorted(correctArr)
    print('Correct !')