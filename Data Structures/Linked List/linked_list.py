# LINKED LIST DATA STRUCTURE

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_the_end(self,data):
        node = Node(data,None)

        if self.head is None:
            self.head = node
            return
        
        iteration = self.head
        while iteration.next:
            iteration = iteration.next

        iteration.next = node

    def get_length(self):
        counter = 0
        iterator = self.head

        while iterator:
            counter += 1
            iterator = iterator.next
        return counter
         
    def print_list(self):
        current_node = self.head

        if current_node is None:
            print("Linked List is Empty")
            return

        while current_node:
            print(current_node.data, end=" --> ")
            current_node = current_node.next

        print()

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_the_end(0)
    linked_list.insert_at_the_end(90)
    linked_list.insert_at_the_end(2)
    linked_list.insert_at_the_beginning(1)
    linked_list.insert_at_the_end(3)
    linked_list.print_list()

    print("Length: ",linked_list.get_length())