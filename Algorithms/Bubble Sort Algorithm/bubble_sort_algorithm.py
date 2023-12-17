# BUBBLE SORT ALGORITHM

def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1,0,-1):
        for j in range(i):
            # Check if the current element is greater than to the next one.
            # If yes, swap them
            if elements[j] > elements[j+1]:
                # Swapping
                temporary_container = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temporary_container
    
    return elements

if __name__ == "__main__":
    elements = [12,9,13,4,0,40]

    print(bubble_sort(elements))