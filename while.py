x =1
while x<=10:
    print(x)
    x+=1
    #python program to find sum of n natural numbers
n = int(input("enter n value:"))
i = 1
sum1= 0
while i<=n:
    sum1+=i
    i+=1
print("sum of  ", n,"numbers= ",sum1)
#transfer statements
for j in range(10):
    if j ==7:
        print("break the loop")
        break
    print(j)
cart = [10,200,30,40,50,600]
for item in cart:
    if item>500:
        print("To place this order u should have membership")
        break
    print(item)
#write a python program whether the student passed or failed
subject_marks = list(map(int,input("enter marks:").split()))
flag = "1"
for marks in subject_marks:
      if marks<35:
            print("Failed")
            flag = "0"
            break
if flag!='0':
    print("Passed")
nums = [10,0,20,50,0]
for i in nums:
    if i==0:
        print("how can u divide with zero...U FOOL..!")
        continue
    print('100/{} = {}'.format(i,100/i))


    


















