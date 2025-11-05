name = input("Enter name:")
if name=="rupa":
    print("Hello rupa!good morning")
else:
    print("Hello guest! good morning")
print("How are u?") 
#write  a program to find the biggest among three numbers

a,b,c = map(int,input("enter 3 numbers:").split())
if a>b and a>c:
    print(a," is biggest")
elif b>a and b>c:
    print(b," is biggest")
elif c>a and c>b:
    print(c," is biggest")
else:
    print("All are equal")

#write a program to find the english word for given digit
a = int(input("enter number:"))
if a==0:
    print("ZER0")
elif a==1:
    print("ONE")
elif a==2:
    print("TWO")
elif a==3:
    print("THREE")
elif a==4:
    print("FOUR")
elif a==5:
    print("FIVE")
elif a==6:
    print("SIX")
elif a==7:
    print("SEVEN")
elif a==8:
    print("EIGHT")
elif a==9:
    print("NINE")
elif a==10:
    print("TEN")
else:
    print("NOT A SINGLE DIGIT")



