class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr != None:
            currStr += f"{str(curr.value)} ->"
            curr = curr.next
        return currStr

    # return node w/node
    # runtime: O(n) where n = number of nodes
    def find(self,value):
        curr = self.head
        while curr != None:
            if curr.value == value:
                return curr
            curr = curr.next
        return None

    # delete node with given value then returns that node
    # runtime: O(n) where n is number of nodes
    # O(1) if curr.value is self.head
    def delete(self,value):
        curr = self.head

        # sprecial case if we need to delete the head
        if curr.value == value:
            self.head = curr.next
            curr.next = None
            return curr

        prev = None

        while curr != None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next

    # insert node at head of list
    # runtime: O(1)
    def insert_at_head(self,node):
        node.next = self.head
        self.head = node

    # overwrite node or insert node at head
    # runtime: O(n)
    def insert_at_head_or_overwrite(self,node):
        existingNode = self.find(node.value) # O(n)
        if existingNode != None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node) # O(1)