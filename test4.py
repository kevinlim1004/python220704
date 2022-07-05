#교집합 함수
from re import L
import struct
from turtle import pos


def intersect(pre,post):
    result = []
    for x in pre:
        if x in post and x not in result:
            result.append(x)
    return result

print(intersect("banana","nanaba"))

print("ㅡㅡㅡㅡㅡㅡㅡㅡ")
x = 1
print(id(x))
def func1(a):
    return a+x
    
def func2(a):
    print(id(x))
    y = x
    print(id(y))
    y=3
    print("y=",y)
    print("x=",x)
    return a+x

print(id(x))
print(func1(5))
print(func2(5))
print(x)

print(id(x))
print("ㅡㅡㅡㅡㅡㅡㅡㅡ")
a=1
b=a
print(id(a))
print(id(b))

def times(a=10,b=20):
    return a*b

print(times(2))
print(times())
print(times(b=3,a=7))
a=[1]
b=[2]

def puts(*ar):
    for x in ar:
        for x in ar:
            print(x)

puts("sdf","Fsd","xwwace")


def user(server,port,**user):
    strURL = "https://"+server+":"+port+"/?"
    for key in user.keys():
        strURL += key+"="+user[key]+"&"
    return strURL

print(user("caca.com","80",id="kim",passwd="1234"))
print(user("caca.com","80",id="kim",passwd="1234"
,name="kev"))

g = lambda x,y:x*y
print(g(3,4))
print((lambda x:x*x)(4))
print(globals())