class Node:
    def __init__(self, value): #Initiate all the properties of the node on creation of an object
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self): #nice repr method to explain the objects of this calsss
        return f"<Node {self.value}>"