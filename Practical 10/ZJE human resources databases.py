class staff (object):      # create a class
    def __init__(self,x,y,z):     # create a function with the specific viriable "self"
    # define the viarables
        self.x = x               
        self.y = y
        self.z = z


# give an example
a = staff('Chen Yanhui', 'International Campus', 'administration')  # call the class
print(a.x)
## Chen Yanhui
print(a.y)
## International Campus
print(a.z)
## administration
