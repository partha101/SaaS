
class llnode(object):
    def __init__(self,k):
        self.key=k
        self.left=None
        self.right=None
    def insert(self,node):
        if self.right is not None:
            self.right.insert(node)
        else :
            self.right=node
            node.left=self
            node.right=None
    def delete(self,k):
        current=self
        while self.right is not None:
            if k==self.key:
                self.left.right=self.right
                self.right.left=self.left
                return self
            else :
                self.right.delete(k)
class linked_list(object):
    def __init__(self):
        self.root=None
    def insert(self,k):
        node=llnode(k)
        if self.root is None:
            self.root=node
        else :
            self.root.insert(node)
    def print_list(self):
        if self.root is None:
            return
        else:
            current=self.root
            while current is not None:
                print current.key
                current=current.right
    def delete(self,val):
	    if self.root.key==val:
		    current=self.root
		    current.right.left=None
		    self.root==current.right
	    else:
			current=self.root
			while current.right is not None:
				if current.right.key==val:
					current.right=current.right.right
					current.right.right.left=current
					break
				current=current.right



