class Node:

	def __init__(self,value):
		self.value = value
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def cs2c(self): # function to convert a singly linked list to circular
		temp = self.head
		c = 0 
		while(temp):
			c += 1
			temp = temp.next
		temp = self.head
		for i in range(int(c)-1):
			temp = temp.next
		temp.next = self.head

		# Printing the linked list
		temp = self.head
		c = 0
		while(temp and c < 18): # this will print linked list twi e as there are 9 elements in the linked list.
			print(temp.value)
			temp = temp.next
			c += 1


# defining elements of linked list
LinkedListObj = LinkedList() # creating object of linked list
LinkedListObj.head = Node(1) # defining head
first_node = Node(2) # second element in linked list
second_node = Node(3) 
third_node = Node(4)
forth_node = Node(99)
fifth_node = Node(3)
sixth_node = Node(44)
seventh_node = Node(2)
eight_node = Node(7)
ninth_node = Node(77)

# linking linked list0
LinkedListObj.head.next = first_node 
first_node.next = second_node
second_node.next = third_node
third_node.next = forth_node
forth_node.next = fifth_node
fifth_node.next = sixth_node
sixth_node.next = seventh_node
seventh_node.next = eight_node
eight_node.next = ninth_node

LinkedListObj.cs2c()