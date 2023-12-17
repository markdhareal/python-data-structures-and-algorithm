# SELECTION SORT ALGORITHM

def selection_sort(elements):
    size = len(elements)
    
    for i in range(size-1):
        # Assign the current minimum based on i
        current_minimum = i
        for j in range(current_minimum+1, size):
            # if the condition is true, the new value of current minimum will be base on j
            if elements[current_minimum] > elements[j]:
                current_minimum = j
        
        # Swapping
        elements[current_minimum], elements[i] = elements[i], elements[current_minimum]

    return elements 


if __name__ == "__main__":

    elements = [88,9,1,0,4,2,90,77]

    print(selection_sort(elements))