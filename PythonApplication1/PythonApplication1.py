

# time complexity : o (n^2)
def bubbleSort(my_list):
    index_length = len(my_list) - 1
    sorted = False

    while not sorted:
        sorted = True

        for x in range(0, index_length):
            if my_list[x] > my_list[x + 1]:
                sorted = False
                # swap of the elements  
                my_list[x], my_list[x + 1] =  my_list[x + 1], my_list[x]
        
    return my_list



# time complexity : worst case O(n)
def linear_search(my_list2, target): 
    for x in range(0, len(my_list2)):
        if my_list2[x] == target:
            return x 
       
    return -1

# time complexity: worst case o(n^2)
def selection_sort(my_list4):
    length = len(my_list4) - 1
    
    for i in range(0, length):
        min_idx = i
        
        for j in range(i + 1, len(my_list4)):
            if my_list4[j] < my_list4[min_idx]:
                min_idx = j
                
        my_list4[i], my_list4[min_idx] = my_list4[min_idx], my_list4[i]  
    return my_list4
    


# time complexity : worst case O(log n)
def binary_search(my_list3, target3):
    left = 0
    right = len(my_list3) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if my_list3[mid] == target3:
            return mid
        elif my_list3[mid] < target3:
            left = mid + 1
        else:
            right = mid - 1
    return -1
            
def prac():
    for _ in range(5):
        print(f'Hello {5}')


def main():
    res = 1 % 10
    print(res)

    
main()