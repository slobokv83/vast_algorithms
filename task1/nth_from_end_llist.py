# Simple Python program to find n'th node from end

# Linked list starts with the Head and ends with None
# each element of the list (Node) consists of data and next
# with next incrementing, position (pointer of the list) is incrementig also

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
     
class LinkedList:
    def __init__(self):
        self.head = None
 
    # createNode and and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Function to get the nth node from the end of a linked list
    def nth_from_end(self, n):
        temp = self.head # used temp variable
         
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
         
        # print count
        if n > length: # if entered location is greater
                       # than length of linked list
            print('Location is greater than the length of LinkedList')
            return
        temp = self.head
        for _ in range(0, length - n):
            temp = temp.next
        return temp.data
 
if __name__ == "__main__":
    llist = LinkedList()

    # Use push() to construct below list
        # 35->15->4->20
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)
    llist.push(7)
    llist.push(8)

    print("The Nth element from the end:", llist.nth_from_end(7))