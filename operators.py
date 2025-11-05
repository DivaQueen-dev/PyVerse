#&,|,^,~,<<.>>
print(6&5)
print(6|5)
#print(10.5 &6.7) Type error: unsupported operand type(s) for &'.float' and 'float'
print(True & True)
print(True | False)
print(False |False)
print(True & False)
print(False & False)
print(4^5)#both should be different
print(~9)
print(~True) #1+1 ==>-2
print(~False)#0+1 ==>-1
print(True ^ False)
print(True ^True)
print(False ^ True)
print(False ^ False)
#>>==> right shift operator
print(10>>2)
print(True <<2) #==> 4
print(True >>2)  #==> 0
print(False<<2)
print(False>>2)
#asignnment
x = 10
x+=10
print(x)
age =18
x ="eligible for voting" if age>=18 else "not eligible"
print(x)
a,b = 10,20
print(a,b)
#min of two numbers
'''a = int(input("enter 1st num:"))
b = int(input("enter 2nd num:"))
c = int(input("enter 3 rd num;"))
min = a if a<b and a<c ''' 



#identity operators ==>address comparison==> is,is not 
a = 20
b = 10
print(a is b)
print(a is not b)
#membership operator whether given object present in collection or not  ==> in,not in
a = [1,2,3,4]
print(9 in a)
x = "hello not a good morning...!";
print( 'x'in x)
a = ['sunny', ' bunny', 'chinny']
print('sunny' in a)




  
