class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        ptr = self.head
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def begining(self, newdata):
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

    def ending(self, newdata):
        new_node = Node(newdata)
        if self.head == None:
            self.head = new_node
            return

        last_ptr = self.head
        while last_ptr.next:
            last_ptr = last_ptr.next
        last_ptr.next = new_node

    def between(self, prenode, newdata):
        if prenode == None:
            return
        new_node = Node(newdata)
        new_node.next = prenode.next
        prenode.next = new_node

    def rm_node(self, rmvalue):
        ptr = self.head
        while ptr:
            if ptr.data == rmvalue:
                break
            pre_node = ptr
            ptr = ptr.next
        if ptr:
            pre_node.next = ptr.next
        else:
            print(f'找不到資料={rmvalue}')

    def length(self):
        ptr = self.head
        cnt = 0
        while ptr:
            cnt += 1
            ptr = ptr.next
        return cnt

if __name__ == '__main__':
    link = LinkedList()
    link.head = Node(5)
    node2 = Node(15)
    node3 = Node(25)

    link.head.next = node2
    node2.next = node3
    link.print_list()

    print(f'新增至begining')
    link.begining(1)
    link.print_list()

    print(f'新增至ending')
    link.ending(100)
    link.print_list()

    print(f'新增至between')
    link.between(node2, -50)
    link.print_list()

    print(f'移除某個node')
    link.rm_node(15)
    link.print_list()

    print(f'計算長度:{link.length()}')
