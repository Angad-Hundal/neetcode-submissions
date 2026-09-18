
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    

    def insert(self, node: Node):
        # check if already in cache
        # remove it 
        # remove from the list
        # append it to the last
        # append the new value

        prev = self.right.prev
        next = self.right

        prev.next = node
        node.prev = prev

        node.next = next
        next.prev = node
    

    def remove(self, node: Node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.val

        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        if self.capacity < len(self.cache):
            left = self.left.next

            self.remove(left)

            del self.cache[left.key]
        
