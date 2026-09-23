from abc import ABC,abstractmethod

class payment(ABC):
    def source(self):
        print("Scanner/upiid/mobile number")
    def amount(self):
        print("Enter the amount")
    def bank(self):
        print("Enter the Bank")
    def pin(slf):
        print("Enter the pin")

    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("payment Success/fail")

class HDFC(payment):
    def paymentprocess(self):
        print("payment is process through HDFC Bank")
class ICIC(payment):
    def paymentprocess(self):
        print("payment is process through ICIC Bank")
class UNION(payment):
    def paymentprocess(self):
        print("payment is process through UNION Bank")
class AXIS(payment):
    def paymentprocess(self):
        print("payment is process through AXIS Bank")

Ranjith = HDFC()
Ranjith.source()
Ranjith.amount()
Ranjith.bank()
Ranjith.pin()
Ranjith.paymentprocess()
Ranjith.paymentstatus()

Rasool = ICIC()
Rasool.source()
Rasool.amount()
Rasool.bank()
Rasool.pin()
Rasool.paymentprocess()
Rasool.paymentstatus()

Dinesh = UNION()
Dinesh.source()
Dinesh.amount()
Dinesh.bank()
Dinesh.pin()
Dinesh.paymentprocess()
Dinesh.paymentstatus()

Dipak = AXIS()
Dipak.source()
Dipak.amount()
Dipak.bank()
Dipak.pin()
Dipak.paymentprocess()
Dipak.paymentstatus()