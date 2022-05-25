class staff (object):      # create a class
    def __init__(self,x,y,z):     # create a function with the specific viriable "self"
    # define the viarables
        self.x = x               
        self.y = y
        self.z = z
       # print out the information
        print("Name:",self.x,"Location:",self.y,"Role:",self.z)

# give an example
a = staff('Chen Yanhui', 'International Campus', 'administration')  # call the class
## Name: Chen Yanhui Location: International Campus Role: administration
