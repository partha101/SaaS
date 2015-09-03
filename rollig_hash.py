#rolling hashes(it is the basic version)
class roll_hash:
    def __init__(self,base):
        self.a=base
        self.u=[]
        self.p=1151
        self.una=0
        self.hash=self.una%self.p
    def append(self,val):
        self.u.append(val)
        self.una=(self.una*self.a)+ord(val)
        self.hash=self.una%self.p
    def hashing(self):
        return (self.hash)
    def skip(self):
        self.una=((self.hash)-(ord(self.u[0])*(self.a**(len(self.u)-1)%self.p)))%self.p
        del(self.u[0])
        self.hash=self.una%self.p
        
        
        
        
