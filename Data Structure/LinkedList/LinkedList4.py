from CircularDoublyLinkedList import *

LL3 = CircularDoublyLinkedList()
Node1 = Node("I use Arch BTW")
Node2 = Node("Abo obaidah amk")
Node3 = Node(6.2)
Node4 = Node(8)
Node5 = Node(1)
Node6 = Node(4.7)

LL3.Add_at_front(Node1.data)
LL3.Add_at_front(Node2.data)
LL3.Add_at_any_index(LL3.head,Node3.data)
LL3.Add_at_any_index(LL3.head.next,Node4.data)
LL3.Add_at_the_end(Node5.data)
LL3.Add_at_the_end(Node6.data)


print("Before Deletion:")
LL3.print_list()
LL3.delete(Node3.data) 
print("\n")
print(f"after {Node3.data} deletion:")
LL3.print_list()
print("\n")
LL3.search(Node2.data) 



#neglect it طنشها
#print(eval("LL3.head"+".next"*2+".data"))