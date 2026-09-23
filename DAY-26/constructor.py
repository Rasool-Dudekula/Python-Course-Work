'''
class Instagram:

    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f"Welcome to Instagram, {self.username}")

rasool = Instagram('rasool','12345')

class Instagram:
    def __init__(self,username,password):
        self.__password = password
        self._post = [] 

def getpassword(self):
    return self.__password 

def setpassword(self,newpassword):
    self.__password = newpassword 

@property
rasool = Instagram('rasool','12345')

print(rasool.username)
print(rasool.getpassword())
print(rasool.accesspost)

rasool.username = 'rasool_124'
print(rasool.username)

rasool.setpassword('rasool@@123')
print(rasool.getpassword())

rasool.accesspost = 'python intro'
rasool.accesspost = 'strings'
rasool.accesspost = 'project'
print(rasool.accesspost)
'''