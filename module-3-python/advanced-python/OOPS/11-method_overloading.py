# method_overloading is perfomed any opararions aor task using same fuction pass with diffrent argument that is calld method_overloading






class disply1:
    def info(self,a=None,b=None,c=None):
        if a is not None:
            print(a)
        if b is not None:
            print(b)
        if c is not None:
            print(c)        

class disply2(disply1):
    pass
obj=disply2()
obj.info(13,3,2006)        