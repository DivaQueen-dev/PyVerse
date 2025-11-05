a = 10
print(type(a))
b = "rupa"

print(type(b))
c = 12.4
print(type(c))

d = 0B11+7.8j
print(d)
print(type(d))
d = 5.0+5.7j
print(d)
print(d.real)
print(d.imag)
e = True
print(e)
print(a<c)
c = a<c + c<=a
print(c)
print(True+True) #1+1 = 2
print(True-False)#1-0=1
print(True-True)#1-1=0
print(False - True)#0-1 = -1
print(False+False) #0+0=0
x =""" "rupa" """
print(x)
y = """ "hello  'rupa' how are you ?" """
x ="rupa"
y = "sree"
print(x)
print(y)
print(x,'\n',y)
a = input("enter name:")
#print(""" '' """,a)
#conditional statement
x = bool(input())
print(x)
if x>=18:
    print("Eligible for voting")
else:
    print("No not eligible for voting")






#d = 7+0B11j not possible

#binary ==> 0B or Ob
#octal form ==> 0o or 0O
#hexadecimal ==> 0x or 0X
#conversions ==> bin(),oct(),hex()
#floatinf point can only be decimal (oct,bin etc == not supported)
#a+bj ===> integer or floating point values(a and b)
#a = 0B11+5j correcr
#5+0B11j ==> incorrect(syntax error)
#var_name.real, var_name.imag ==> to extract real and imaginary
#true+true == 2
#true-false == 1
#3&&5 
#2||5
#string ==> to represent string in triple  quotes '''string''' , """string"""



