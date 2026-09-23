class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    @property
    def accesspost(self):
        return self._post

rasool = Instagram('rasool','12345')

print(rasool.username)
print(rasool.getpassword())
print(rasool.accesspost)
