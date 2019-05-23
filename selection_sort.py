#! /usr/bin/python
# Write an algorithm for selection sort

def selection_sort(arr):
    
    for i in range(len(arr)):
        min_index = i
    
        for j in range(1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
                
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
            
    return arr
    
  
if __name__ == '__main__':
    tests = [[[10, 4, 5, 9, 1, 3], [1, 3, 4, 5, 9, 10]],
              [[11, 13, 2], [2, 11, 13]],
              [[], []]
            ]
          
    for l, expected in tests:
        assert selection_sort(l) == expected
