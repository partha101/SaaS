class llnode(object):
	def __init__(self,key):
		self.key=key
		self.next=None
	def insert(self,node):
		if self.next is None:
			self.next=node
		else:
			self.next.insert(node)
class link_list(object):
	def __init__(self):
		self.root=None
	def insert(self,key):
		node=llnode(key)
		if self.root is None:
			self.root=node
		else:
			self.root.insert(key)
