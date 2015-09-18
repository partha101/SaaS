class llnode(object):
	def __init__(self,key):
		self.key=key
		self.next=None
	def insert(self,node):
		if self.next is None:
			self.next=node
		else:
			self.next.insert(node)
	def insert_mid(self,key):
		node=llnode(key)
		current=self.next
		self.next=node
		node.next=current
	def print_reverse(self):
		if self.next is None:
			print self.key
			return
		self.next.print_reverse()
		print self.key
class link_list(object):
	def __init__(self):
		self.root=None
	def insert(self,key):
		node=llnode(key)
		if self.root is None:
			self.root=node
		else:
			self.root.insert(node)
	def print_list(self):
		current=self.root
		while current is not None:
			print current.key
			current=current.next
	def delete(self,val):
		if self.root.key==val:
			self.root=self.root.next
		else:
			current=self.root
			while current.next is not None:
				if current.next.key==val:
					current.next=current.next.next
					break
				current=current.next
	def insert_middle(self,val,key):
		current=self.root
		while current.next is not None:
				if current.key==val:
					current.insert_mid(key)
					break
				current=current.next
	def insert_first(self,key):
		node=llnode(key)
		if self.root is None:
			self.root=node
		else:
			temp=self.root
			self.root=node
			self.root.next=temp
	def rev_print(self):
                self.root.print_reverse()
