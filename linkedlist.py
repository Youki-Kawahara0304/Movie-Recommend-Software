class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
        
    def get_next_node(self):
        return self.next_node

class LinkedList:
    def __init__(self, value = None):
        self.head_node = Node(value)

    def insert_beginning(self, new_node_value):
        new_node = Node(new_node_value, self.head_node)
        self.head_node = new_node
    
    def search_by_value(self, value):
        current_node = self.head_node
        while current_node: 
            sub = current_node.get_value()
            print(sub.get_value())

            if current_node.get_value() == value:
               
                return current_node
            current_node = current_node.get_next_node()
        



        





