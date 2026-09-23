'''
var = lambda arg: exp

wish = lambda name: f"Welcome to the course {name}"
print(wish("virat"))
print(wish("rohit"))

gst = lambda price: price+price*0.18
print(gst(1000))
print(gst(2000))

avg = lambda a,b,c: (a+b+c)/3
print(avg(3,4,5))
print(avg(8,10,15))

iseven = lambda a: "Even" if a%2==0 else "Odd"
print(iseven(10))
print(iseven(11))

largest = lambda a,b,c: a if a>b and a>c else (b if b>c else c)
print(largest(23,34,45))
print(largest(30,40,50))

isvowel = lambda a: "vowel" if a in "aeiouAEIOU" else "cons"
print(isvowel("e"))
print(isvowel("k"))

l = [1,2,3,4,5,6]
update = list(map(lambda i: i+10,l))
print(update)

t=(132,234,34,890,234,890890)
discount = list(map(lambda i: i-i*0.3,t))
print(discount)

l = [1,2,3,4,5,6]
update = list(filter(lambda i: i%2!=0,l))
print(update)

t=(132,234,34,890,234,890890)
discount = list(filter(lambda i: i>1000,t))
print(discount)

l = ["rasool@gmail.com", "rasool@codegnan.com", "rasool@yahoo.com", "rasool@outlook.com"]
domains = list(map(lambda i: i.split("@")[1].split(".")[0], l))
print(domains)

from functools import reduce
l = [2,3,4,232,12,3,4,23232]
res = reduce(lambda sum,i:sum+i,l)
print(res)

res1 = reduce(lambda pro,i: pro*i,l)
print(res1)

's1': True,ava = list(filter(lambda i:seats[i]!=True,seats))
print(ava)

products ={'egg':80,'sugar':100,'salt':20,'butter':40,'milk':50}
res = list(filter(lambda i: products[i]>50,products))
print(res)
'''
