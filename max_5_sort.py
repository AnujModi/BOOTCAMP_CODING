num = []
num1 = int(input("How many number do you want to write (range is 1-20)?"))
if num1 < 1 or num1 > 20:
    print("I SAID RANGE IS 1-20... Run again now...")
else:
    for i in range(num1):
        temp = input("Enter Number " + str(i + 1) + ": ")
        num.append(temp)
flag = 0
num2 = num[:] 
num2.sort()
if (num == num2): 
    flag = 1
if (flag):
    print("List is sorted")
else:
    print("List is not sorted")
num2.sort(reverse=True)
top5 = []
for i in range(min(5, len(num2))):
    top5.append(num2[i])
print(top5)