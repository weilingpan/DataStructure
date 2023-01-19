class ListNode:
    def __init__(self, data=None, next=None): 
        self.data = data
        self.next = next

    def has_value(self, value) -> bool:
        if self.data == value:
            return True
        return False

class SingleLinkedList:
    def __init__(self): 
        self.head = None
        self.tail = None

    def add_item(self, new_item):
        if not isinstance(new_item, ListNode):
            new_item = ListNode(new_item)
        
        if self.head is None:
            self.head = new_item
            self.tail = new_item #特別留意
        else:
            #TODO: 要留意是否是 multi nodes，目前只支援 single node
            self.tail.next = new_item
            self.tail = self.tail.next
        print(f'After adding ... --> head: {self.head.__dict__}, tail: {self.tail.__dict__}')

    def display(self) -> list:
        first_node = self.head
        display_node = first_node # first node
        
        res_lst = []
        while display_node is not None:
            res_lst.append(display_node.data)
            display_node = display_node.next # next node
        return res_lst


if __name__ == '__main__':
    print(f'========== Initiate nodes and check the value is in node or not ==========')
    node = ListNode() #{'data': None, 'next': None}
    node1 = ListNode(8) #{'data': 8, 'next': None}
    node2 = ListNode(13) #{'data': 13, 'next': None}
    node3 = ListNode('my node') #{'data': 'my node', 'next': None}
    node4 = ListNode(99) #{'data': 99, 'next': None}
    print(node1.has_value(5)) #False
    print(node2.has_value(13)) #True
    print(node3.has_value(13)) #False

    print(f'========== Manage our list nodes ==========')
    # multi-nodes #TODO: 如何在SingleLinkedList加入multi nodes? 目前只支援加入單一 node
    #node1.next = node2
    #print(node1.__dict__) #{'data': 8, 'next': <__main__.ListNode object at 0x00000229F7649F70>}

    # single linked list
    # 1. Initiate my list
    my_lst = SingleLinkedList() #{'head': None, 'tail': None}
    print(my_lst.display()) #[]

    # 2. Add 8 to list
    my_lst.add_item(node4)
    print(my_lst.display()) #[99]
    my_lst.add_item(node2)
    print(my_lst.display()) #[99, 13]
    my_lst.add_item(node3)
    print(my_lst.display()) #[99, 13, 'my node']
