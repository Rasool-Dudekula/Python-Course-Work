'''
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")

rasool = whatsappv1()
rasool.message()

class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv3(whatsappv2):
    def groups(self):
        print("You can create a group and talk to multiple people at a same time")

class

Rasool = whatsappv1()
Rasool.message()

Virat = whatsappv2()
Virat.message()
Virat.status()

Rohit = whatsappv3()
Rohit.message()
Rohit.status()
Rohit.groups()
'''
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status for 24hrs")

class whatsappv3:
    def groups(self):
        print("You can create a group and talk to multiple people at a same time")

class whatsappv4:
    def community(self):
        print("You can multiple groups")

class whatsappv5(whatsappv4,whatsappv3,whatsappv2):
    def channels(self):
        print("You can post regularly with huge crowd")

rasool = whatsappv5()
rasool.message()
rasool.status()
rasool.groups()
rasool.community()
rasool.channels()

