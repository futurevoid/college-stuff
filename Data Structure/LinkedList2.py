from CircularLinkedList import *

LL2 = LinkedList()
Node1 = LL2.Add_at_front("I use Arch BTW")
Node2 = LL2.Add_at_front("Abo obaidah amk")
Node3 = LL2.Add_at_any_index(LL2.head,6.2)
Node4 = LL2.Add_at_any_index(LL2.head.next,8)
Node5 = LL2.Add_at_the_end(1)
Node6 = LL2.Add_at_the_end(4.7)

print("Before Deletion:")
LL2.print_list()
LL2.delete(4.7) 
print("\n")
print("after deletion:")
LL2.print_list()
LL2.search("Abo obaidah amk") 
