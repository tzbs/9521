names=("张三","李四","王五","赵六")
ages=(12,34,23,13)
jobs=("总统","总理","首相","主席")
for name,age,job in zip(names,ages,jobs):
    print("{0}__{1}__{2}".format(name,age,job))

print([x for x in range(1,9)])
print([x*x for x in range(1,9)])
print([x for x in range(1,30) if x%4==0])

print([a for a in "abcdefg"])
print([(x,y) for x in range(1,10) for y in range(1,20)])