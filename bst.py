class BSTNode(object):
	def __init__(self,parent,k):
		self.key=k
		self.parent=parent
		self.left=None
		self.right=None
	def find(sekf,k):
		if k==selfkey:
			return self
		elif k<self.key:
			if self.left is None:
				return None
			else :
				return self.left.find(k)
		else:
			if self.right is None:
				return None
			else :
				return self.right.find(k)
	def find_min(self):
		current=self
		while currentleft is not None:
			current=current.left
		return current
	def next_larger(self):
		if self.roght is not None:
			return self.right.find_min()
		current=self
		while current.parent is not None and current is current.parent.right:
			current=current.parent
		return current.parent
	def insert(self,node):
		if node is None:
			return 
		if node.key<self.key:
			if self.left is None:
				node.parent=self
				self.left=node
			else:
				self.left.insert(node)
		else :
			if self.right is None:
				node.parent=self
				self.right=node
			else:
				self.right.insert(node)





class BST(object):
	def __init__(self):
		self.root=None
	def find(self,k):
		return self.root and self.root.find(k)
	def find_min(self):
		return self.root and self.root.find_min()
	def insert(self,k):
		node=BSTNode(None,k)
		if self.root is None:
			self.root=node
		else :
			self.root.insert(node)
	def inorder_traverse(self):
		current=self.root
		if current is not None:
			current.left.inorder_traverse()
			print current.key
			current.right.inorder_traverse()
		

bst1=BST()
n=input("enter the numbe of terms to be stored\n")
for i in range(n):
	x=input()
	bst1.insert(x)
	

dis=raw_input("press y or n whether you want to print the list in ascending oder or not\n")
if dis=="y":	
	bst1.inorder_traverse()
elif dis=="n":
	pass
else:
	"invalid input"

	
			
		
<<<<<<< HEAD

=======
>>>>>>> c0d003c01e93ca2b4a25a7b6b6036b1552a6f7f9
