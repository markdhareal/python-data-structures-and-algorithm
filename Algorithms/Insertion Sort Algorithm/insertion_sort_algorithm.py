# INSERTION SORT ALGORITHM

def insertion_sort(elements):
    size = len(elements)
    for i in range(1, size):
        current_number = elements[i]
        left_side = i - 1
        while left_side >= 0 and current_number < elements[left_side]:
            elements[left_side+1], elements[left_side] = elements[left_side], elements[left_side+1]
            left_side -= 1
    
    return elements

if __name__ == "__main__":

    elements = [22,9,8,6,80,1,0]

    print(insertion_sort(elements))