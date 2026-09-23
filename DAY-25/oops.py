'''
class flipkart:
    pass

virat = flipkart()
rohit = flipkart()
bumrah = flipkart()

class flipkart:
    discount = 30
    def info(self,name,phoneno,address):
        self.name = name
        self.phoneno = phoneno
        self.address = address 
        print(f'Welcome to the Flipkart',self.name)

virat = flipkart()
virat.info('virat',292342349,'hyd')
rohit = flipkart()
rohit.info('rohit',292342399,'hyd')
bumrah = flipkart()
bumrah.info('bumrah',292342949,'hyd')

class flipkart:
    discount = 30

    @classmethod
    def updatediscount(cls):
        cls.discount = 40
        print("updated discount:",cls.discount)

    def info(self,name,phoneno,address):
        self.name = name
        self.phoneno = phoneno
        self.address = address
        print(f'welcome to the flipkart',self.name)

    @staticmethod
    def banner():
        print(f"{flipkart.discount}% discount is going , grab the product...")

virat = flipkart()
virat.info('virat',423424290,'hyd')
virat.updatediscount()
virat.banner()

rohit = flipkart()
rohit.info('rohit',423424299,'hyd')
rohit.updatediscount()
rohit.banner()

bumrah = flipkart()
bumrah.info('bumrah',423424298,'hyd')
bumrah.updatediscount()
bumrah.banner()
'''