

a={"cc":"red","cc":"blue"}
b = a
print(a)
print(a["cc"])
print(a["cc"])
print(a["cc"])
del a["cc"]
print(a)
print(b)
# 튜플은 한방에 리턴하는 용도
# 파이썬은 값복사x 참조복사O

a=3
b=a
a=4
print(a)
print(b)
a=["f"]
b=a
a=["g"]
print(a)
print(b)
a={"cc":"red"}
b=a
a={"ff":"blue"}
print(a)
print(b)
a={"cc":"red"}
b=a
a["ff"]="blue"
print(a)
print(b)