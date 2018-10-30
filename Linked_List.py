class  Node: # defining a class to create a new node.

 	def __init__(self,value): # constructor that allots the value at the npde and also initiatilises next to none.
 		self.value = value # value at a node will be accessed by .value.
 		self.next = None # next value to that node.

class LinkedList: # defining a class to handle everything (all the functions) related to the linked list.

	def __init__(self): # constructor that initialises head to none
		self.head = None

	def print_llist(self):  # function to print all the elements of linked list.
		temp = self.head # storing value of head in temp.
		while(temp): # exrecuting loop till we r getting value of temp
			print(temp.value) 
			temp = temp.next # setting pointer to the next node

	def new_head(self,value): #  function to add a new node at the head of linked list
		newhead = Node(value) # creating node
		newhead.next = self.head # assigning next of new head the value of old head
		self.head = newhead #assigning new head
	
	def new_end(self,value): # funvtion to a new element at end of node
		newend = Node(value) #creating node for value
		temp = self.head 
		# running a counter c to reach the end of node
		c = 0
		while(temp != None): # c=1 for first element c=2 for second element and so on
			c +=1
			temp = temp.next
		# adding nee value at the end of list
		temp = self.head
		for i in range(int(c)-1):
			temp = temp.next
		temp.next = newend

	def middle_insertion(self,prev_node_index,value): # function to add node in between linked list
		temp = self.head
		newnode = Node(value)
		for i in range(int(prev_node_index)): # for loop that takes us to the node in linked list after which we have to add a new node
			temp = temp.next
		newnode.next = temp.next
		temp.next = newnode

	def delete_head(self): # deleting head of linked list
		self.head = self.head.next

	def delete_end(self): # deletig head of linked list
		temp = self.head 
		# running a counter c to reach the end of node
		c = 0
		while(temp != None):
			c +=1
			temp = temp.next
		# deleting last node
		temp = self.head
		for i in range(int(c)-2): # for loops takes us to second last element of the linked list.  we get c = length of linked list. -2 done as for loop starting with 0
			temp = temp.next
		temp.next = None

	def delete_middle(self,prev_node_index): # deleting element present in between th list index of element to be deleted = prev_node_index + 1
		#defining two temporary variable to get hold on two consecutive values in linked list.
		temp = self.head
		temp1 = temp.next
		for i in range(int(prev_node_index)-1): # for loop will take us to the element at index just before the element to be deleted. 
			temp = temp.next
			temp1 = temp1.next
		temp.next = temp1.next

	def length_linkedlist(self): # function to display length of linked list.
		c = 0
		temp = self.head
		while(temp):
			c += 1
			temp = temp.next
		print(c)

	def find_element(self,element): # function to find an element in the linked list.
		temp = self.head
		c = 0
		while(temp):
			
			if temp.value == element: 
				print("Element found at {} th index.".format(c))
			else:
				print("Element not found {} th index.".format(c))
			c += 1
			temp = temp.next

	def element_at_node(self,node_index): # function to display present at the nth index in linked list.
		temp = self.head
		for i in range(int(node_index)):
			temp = temp.next
		print("Element at {} index = {} ".format(node_index,temp.value))

	def element_from_last(self,node_index): # function to find element at nth node from last
		temp = self.head
		c = 0
		while(temp):
			c += 1
			temp = temp.next
		
		temp = self.head

		for i in range(int(c) - int(node_index) - 1): # element index from top = (length(i.e. 'c')) - (node from back) - (1)
			temp = temp.next
		print("Element  at {} index from Bottom is {}".format(node_index,temp.value))

	def print_middle_element(self): # function to print middle element of linked list.
		temp = self.head
		c = 0
		while(temp):
			c += 1
			temp = temp.next
		temp = self.head
		for i in range(int(c/2)): # if c== odd number then rounding it off to lower integer number
			temp = temp.next
		print("Middle Element = {}".format(temp.value))
# defining elements of linked list
LinkedListObj = LinkedList() # creating object of linked list
LinkedListObj.head = Node(1) # defining head
first_node = Node(2) # second element in linked list
second_node = Node(3) # last element

# linking linked list
LinkedListObj.head.next = first_node 
first_node.next = second_node

#printing linked list
LinkedListObj.print_llist()

#adding new elemnt at start of linked list
LinkedListObj.new_head(0)

#again printing linked list to see the applied changes
print("New Linked List")
LinkedListObj.print_llist()

#adding new element at the end of linked list
LinkedListObj.new_end(4)

#again printing linked list to see the applied changes
print("New Linked List")
LinkedListObj.print_llist()

#adding new element in between linked list
LinkedListObj.middle_insertion(2,5)

#again printing linked list to see the applied changes
print("New Linked List")
LinkedListObj.print_llist()

#deleting head of linked list
LinkedListObj.delete_head()

#again printing linked list to see the applied changes
print("New Linked List")
LinkedListObj.print_llist()

#deleting end of linked list
LinkedListObj.delete_end()

#again printing linked list to see the applied changes
print("New Linked List")
LinkedListObj.print_llist()

#deleting a element present in between linked list
LinkedListObj.delete_middle(2)

#again printing linked list to see the applied changes
print("New Linked List")
LinkedListObj.print_llist()

#printing length of linked list
print("Length Of Linked List = " ,end = ' ')
LinkedListObj.length_linkedlist()

#finding a element present in between linked list
LinkedListObj.find_element(2)

#displaying element at specific node in tge linked list.
LinkedListObj.element_at_node(2)

#Displaying element at specific index fom bottom of linked list.
LinkedListObj.element_from_last(2)

# displaying middle element of the linked list.
LinkedListObj.print_middle_element()