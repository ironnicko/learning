class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = node(data)
            return        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node(data)
    
    def prepend(self, data):
        current_node = self.head
        new_node = node(data)
        new_node.next = current_node
        self.head = new_node
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def delete_data(self, data):
        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            current_node = None
        previous_node = None
        while current_node and current_node.data != data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return 

        previous_node.next = current_node.next
        current_node = None

    def delete_index(self, index):
        if self.len() <= index: return print("Index too big")
        current_node = self.head
        if index == 0:
            self.head = current_node.next
            current_node = None 
            return
        previous_node = None
        count = 0
        while current_node and count != index:
            previous_node = current_node
            current_node = current_node.next
            count += 1
        previous_node.next = current_node.next
        current_node = None

    def insert_after_node(previous_node, data):
        if not previous_node:
            print("Previous Node not found")
        new_node = node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node


    def len(self):
        if not self.head:
            return 0
        current_node = self.head
        count = 1
        while current_node.next:
            current_node = current_node.next
            count += 1
        return count

if __name__ == "__main__":
    driver = linkedlist()
    driver.append(2)
    driver.append(3)
    driver.append(6)
    driver.prepend(4)
    driver.delete_data(3)
    driver.delete_index(1)
    driver.display()
    print("Len " + str(driver.len()))