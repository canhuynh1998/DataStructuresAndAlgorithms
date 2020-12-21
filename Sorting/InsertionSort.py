'''
Insertion Sort Algorithms Implementation

Time: O(N^2)
Space: O(1) in-place
'''

import random

def swap(start, end, array):
    array[start], array[end] = array[end], array[start]

def Insertion(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j -= 1
    return array

if __name__ == "__main__":
    testArr = [random.randint(0,11) for _ in range(10)]
    correctArr = testArr.copy()

    assert Insertion(testArr) == sorted(correctArr)
    print('Correct!!')