class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    # insert node at the begining of the linked list
    def insert_at_the_begining(self, newData):
        node = Node(newData)
        node.next = self.head
        self.head = node
    
    # insert node at the end of the linked list
    def insert_at_the_end(self, newData):
        if self.head is None:
            node = Node(newData)
            self.head = node
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(newData)
    
    # print all the elements of the linked list
    def print(self):
        if self.head is None:
            print('No elements in the linked list')
        
        dataToPrint = ''
        itr = self.head
        while itr:
            dataToPrint += str(itr.data) + '--->'
            itr = itr.next
        
        print(dataToPrint)
    
    # create a linked list from an array
    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_the_begining(data)
    
    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
            
        return count
        
    # remove element at the given position
    def remove_at(self, position):
        if position < 0 or position > self.length():
            raise Exception('Invalid index')
        
        # check for head
        if position == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        while position - 2 > 0:
            itr = itr.next
            position -= 1
        
        itr.next = itr.next.next
    
    # insert element at the given position
    def insert_at(self, position, data):
        if position < 0 or position > self.length():
            raise Exception('Invalid index')
        
        # check for head
        if position == 0:
            self.insert_at_the_begining(data)
            return
        
        itr = self.head
        while position - 2 > 0:
            itr = itr.next
            position -= 1
        
        node = Node(data)
        node.next = itr.next
        itr.next = node
  
        
# main
if __name__ == '__main__':
    li = LinkedList()
    li.insert_values([20, 10, 5])
    li.insert_at(3, 15)
    print(f'Length of the original Linked list is {li.length()}')
    print('Before deleting: ')
    li.print()
    li.remove_at(3)
    print('After deleting 3rd node from the begining: ')
    li.print()
