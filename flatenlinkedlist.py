# this is hard question in strivers sde sheet
class Node:
    def __init__(self, x=0, nextNode=None, childNode=None):
        self.data = x
        self.next = nextNode
        self.child = childNode

head = Node(5)
head.child = Node(14)
head.next = Node(10)
head.next.child = Node(4)
head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)
head.next.next.next = Node(7)
head.next.next.next.child = Node(17)


# the above test case is copied from the strivers website 
# i am going to flatten this linked list but not sorting this because i do not know how to apply merge sort on lls 
# this is not optimal opproch to solve this problem the optimal way is to merge the linked list(merge algo from merge sort!!!)
h = head
temp = head 
while temp:
    x = temp.next 
    curdown = temp.child
    curleft = temp
    while curdown:
        curleft.next = curdown 
        curleft = curleft.next 
        curdown = curdown.child 
    curleft.next = x
    temp = x 
while h:
    print(h.data)
    h = h.next
    
        
#successfully done this     