# LINEAR SEARCH ALGORITHM

# This will implement the linear search algorithm
def linear_search(item, elements):

    isExisting = False
    iteration = 0
    
    for i in range(len(elements)):
        # It will count the iteration
        iteration = iteration + 1

        # This will check the elements one-by-one
        if item == elements[i]:
            isExisting = True
            print(f"Item {item} is found at index {i}")
            break

    if not isExisting:
        print(f"Item is not existing")

    print(f"Iteration: {iteration}")



if __name__ == "__main__":
    elements = [3,9,10,25,1]
    
    search_item = int(input("Search: "))

    linear_search(search_item,elements)