a=(1,2,3,4,5)
c=(1,2,3,4,5,6)
b=a
print(a is b)
print(a is c)
print(a is not b)
print(a is not c)
#task2
a="haseem"
b="hello world"
if a in b:
    print("true")
if a not in b:
    print ("false")
 #task3
eng=int(input())
math=int(input())
sci=int(input())
total=(eng+math+sci)
average=(total/3)
print(average)
if average >= 91 and average <=100:
    print("your grade is a+")
elif average >=70 and average <= 90:
    print("your grade is b")
elif average >= 50 and average <=69:
    print("your grade is c")
elif average >=0 and average <= 49:
    print("your grade is d")
else:
    print("invalid input")