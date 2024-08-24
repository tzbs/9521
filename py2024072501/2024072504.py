#for循环
for x in (20,30,40,50):
    print("x={0}".format(x))
for x in "abcdefg":
    print("{0}".format(x))
d={"姓名":"唐昭","年龄":24,"身份":"学生"}
for x in d.items():
    print(x)
for x in range(10,34,5):
    print(x)
print("############################")

for x in range(1,10):
    for y in range(1,x+1):
        print("{0}*{1}={2}".format(y,x,x*y),end="\t")
    print()
for x in range(1,10001):
    for y in range(1,x+1):
        if(x%y==0 and y!=1 and y!=x):
            break
        else:
            y+=1
    if(y==x+1):
        print(x)

