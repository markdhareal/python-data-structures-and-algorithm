# BINARY SEARCH ALGORITHM

def binary_search(item, elements):
    lower_bound = 0
    upper_bound = len(elements) - 1
    isExisting = False

    while lower_bound <= upper_bound:

        mid_index = (upper_bound + lower_bound) // 2
        mid_number = elements[mid_index]

        if item == mid_number:
            isExisting = True
            print(f"Item {item} is found at index {mid_index}")
            break
        elif item < mid_number:
            upper_bound = mid_index - 1
        else:
            lower_bound = mid_index + 1

    if not isExisting:
        print(f"Item is not existing")

if __name__ == "__main__":

    elements = [1,2,4,7,9,10,11,22]

    search_item = int(input("Search: "))

    binary_search(search_item, elements)