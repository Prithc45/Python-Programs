#types: 1.Explicit  2.Implicit
# 1.Explicit
a="20"
b="10"
print("a is a:",type(a))
print("b is a:",type(b))
c=(int(a)+int(b))
print("c is a:",type(c))
print(a,"+",b,"=",c)

#implicit
a=9.5
b=10
print(a+b)#here b convreted to 10.0