from node import Node

#Create a class that builds out binary tree
class BinaryTree:
    def __init__(self, head): #BinaryTree() takes an argument of a Node object 
        self.head = head    #The node object is now the root or head of the binary tree

    def add(self, new_node: Node):  #A method to add a node to the tree which takes the node you want to add as argument
        current_node = self.head    #this starts the traversal at the root/head of the tree
        while current_node:         #This sets the lloop off at the top of the tree, each time we traverse the tree it sets the landing node to the head until there are no more nodes
            if new_node.value == current_node: #Checks if the node is a duplicate 
                raise ValueError("this value already exists!")
            elif new_node.value < current_node.value: #checks if the new node is less than the head, if it is less enter the next flow control
                if current_node.left: #checks if there is a node to the left of the head or not
                    current_node = current_node.left #if there is a node to the left, this node is not the root of the next traversal and the loop starts again
                else:
                    current_node.left = new_node #If there was no node to the left, place the new node there and break the loop
                    break
            elif new_node.value > current_node.value:   # check if the new node is greater than the root/head
                if current_node.right: #checks if there is anything to the right
                    current_node = current_node.right #if there is a node to the right, replace the current node and start the lop with the node from the right as the root/head
                else:
                    current_node.right = new_node #If there was nothing in the right value, place the new node there as this is its rightful place
                    break

    def inorder(self): #create a recursive function t print the tree
        self._inorder_recursive(self.head) #The inorder function calls a function passing the head/root variable to it. The function starts with _ to signify that it is private. 
    
    def _inorder_recursive(self, current_node): #the head/root node is passed to the function as the first current_node
        if not current_node: #if thee current node is not Truthy, aka 0 or None then return to the function that called it
            return #if the current node has a value then move on with the code
        self._inorder_recursive(current_node.left)# recursively call the function. This finds the furthest left node. oce that node is found the if statement is run but there will be no value so it will return to the loop that called it and move tothe next line of code
        print(current_node)#at this stage the inorder traversal has gone left, now it checks and prints the current node before moving right
        self._inorder_recursive(current_node.right) # This now sets the recursion off down the right side of the node but uses the same logic of if there is no value, go back to the calling function and its values. in other words work the way back up the tree

    def find(self, value):
        current_node = self.head
        while current_node: #Keep the loop going as long as current node is Truthy
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise LookupError(f"A node with the value {value} was not found")

    def find_parent(self, value):
        if self.head and self.head.value == value: #check if the number we are looking for is the head first otherwise we wont find the value using the following algorithm
            return self.head
        current_node = self.head #set the current node to the tof of the tree
        while current_node: #while there is a value in the current node it is Truthy
            if (current_node.left and current_node.left.value == value) or\
                    (current_node.right and current_node.right.value == value):#if there is a left node and the value of the left node matches that of the value or the same but on the right side, then this must be the correct parent
                return current_node #return the partent to the programme
            elif value > current_node.value:
                current_node = current_node.right  #This code block moves the node in question depending on its value
            elif value < current_node.value:
                current_node = current_node.left
            

    def find_rightmost(self, node):
        current_node = node #assigns the value given to the nnode variable (proprty)
        while current_node.right: #checks if there is a current node, if so make that node the current node until there is no more nodes to the right 
            current_node = current_node.right
        return current_node #return the rightmost node to the programme

    def delete(self, value):
        to_delete = self.find(value) #uses the find function to store the found value in the property to_delete
        to_delete_parent = self.find_parent(value) #uses the find_parent function to grab the parent of the provided value

        if to_delete.left and to_delete.right: #This will find if the node has 2 children by checking if left and right have truthy values
            rightmost = self.find_rightmost(to_delete.left)
            rightmost_parent = self.find_parent(rightmost.value)
            if to_delete.left == to_delete_parent.left: 
                if rightmost_parent != to_delete:
                    rightmost_parent.right = rightmost.left
                    rightmost.left = to_delete.left
                rightmost.right = to_delete.right
                to_delete_parent.left = rightmost
            elif to_delete.right == to_delete_parent.right:
                if rightmost_parent != to_delete:
                    rightmost_parent.right = rightmost.left
                    rightmost.left = to_delete.leftrightmost_parent.right = rightmost.left
                rightmost.left = to_delete.left
                rightmost.right = to_delete.right
                to_delete_parent.right = rightmost
            else:
                if rightmost_parent != to_delete:
                    rightmost_parent.right = rightmost.left
                    rightmost.left = to_delete.left
                rightmost.right = to_delete.right
                self.head = rightmost
        elif to_delete.left or to_delete.right: #this will find if the node has 1 child by using the or operator to check if one value is truthy
            if to_delete == to_delete_parent.left: #check if the node you want to delete is the left child of the parent, if so point the parent's left side to the child of the node you want to delete thus severing the connection but not orphaning the children
                to_delete_parent.left = to_delete.right or to_delete.left #assign the child of the deleted node to the parent
            elif to_delete == to_delete_parent.right: #chjeck the same for the right side
                to_delete_parent.right = to_delete.right or to_delete.left
            else: #if there is no parent then the parent must be the root/head that you wnat to delete so set the parent of to delee to be the head
                self.head = to_delete.right or to_delete.left
            
        else:  #This will know if the node has no children
            if to_delete == to_delete_parent.left:#checks if it is the left child of the parent and severs connection
                to_delete_parent.left = None
            elif to_delete == to_delete_parent.right:# checks if it is the right child of the parent and severs the connection
                to_delete_parent.right = None
            else: #checks if there is no parent to the value meaning it must be root. if it is root/head, make the property None
                self.head = None

