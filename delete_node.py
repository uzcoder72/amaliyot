# Linked List


# Node => data , next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def show_all_nodes(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def add_first_node(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def last_add_node(self, new_data):
        node = Node(new_data)
        if self.head is None:
            self.head = node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def insert_node(self, prev_node, new_data):
        if prev_node is None:
            raise Exception('The previous node is empty')
        node = Node(new_data)
        node.next = prev_node.next
        prev_node.next = node
    def delete_node(self, key):
        current_node = self.head

        if current_node is not None:
            if current_node.data == key:
                self.head = current_node.next
                current_node = None
                return

        previous_node = None
        while current_node is not None:
            if current_node.data == key:
                break
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            print("The key was not found in the list.")
            return

        previous_node.next = current_node.next
        current_node = None


node1 = Node('dushanba')
node2 = Node('seshanba')
node3 = Node('chorshanba')

llist = LinkedList()
llist.head = node1
node1.next = node2
node2.next = node3
# llist.add_first_node('Yakshanba')
llist.last_add_node('payshanba')
llist.last_add_node('shanba')
llist.insert_node(node3.next, 'juma')
llist.show_all_nodes()
print("After deleting 'juma':")
llist.delete_node('juma')
llist.show_all_nodes()
# llist.head.next = node2
# llist.head.next.next = node3
