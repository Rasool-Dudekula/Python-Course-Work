'''
seat_type = input("Enter the seat type: ")
booking_days = int(input("Enter booking days: "))
festival = input("enter festival or not: ").lower() == "true"
age = int(input("enter your age: "))

price = 5000.0

if seat_type == "Business":
    price += price * 0.40
elif seat_type == "Premium Economy":
    price += price * 0.20

if booking_days > 30:
    price -= price * 0.10
elif booking_days < 7:
    price += price * 0.25

if festival:
    price += price * 0.20

if age >= 60:
    price -= price * 0.15

print(price)


#2nd prblm 
age = int(input("Enter the age: "))
health_score = int(input("Enter the score: "))
vehicle_type = input("enter the vehicle: ").lower()

premium = 10000.0

if age < 25:
    premium += premium * 0.20
elif age > 50:
    premium += premium * 0.15

if health_score >= 80:
    premium -= premium * 0.10
elif health_score < 60:
    premium += premium * 0.20

if vehicle_type == "sports":
    premium += premium * 0.30
elif vehicle_type == "suv":
    premium += premium * 0.15

print(premium)
'''