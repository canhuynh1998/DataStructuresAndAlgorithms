'''
Quick Sort Algorithm Implementation

Time: O(NlogN) best-average, O(N^2) worst when the input array is sorted
Space O(logN) recursive method
'''
import random
def QuickSort(array):
    _helper(array, 0, len(array) - 1)
    return array

def _helper(array, start, end):
    if start > end:
        return 
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        if array[pivot] < array[left] and array[pivot] > array[right]:
            swap(array, left, right)
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1
    
    swap(array, pivot, right)   # now left > right so the correct position of value at pivot index is right
    leftSmaller = right - 1 - start < end - (right + 1) #get better in time complexity
    
    if leftSmaller:
        _helper(array, start, right - 1)
        _helper(array, right + 1, end)
    else:
        _helper(array, right + 1, end)
        _helper(array, start, right - 1)

def swap(array, start, end):
    array[start], array[end] = array[end], array[start]

if __name__ == "__main__":
    testArr = [random.randint(0,11) for _ in range(10)]
    correctArr = testArr.copy()

    assert QuickSort(testArr) == sorted(correctArr)
    print('Correct !')
