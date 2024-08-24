score=int(input("请输入一个分数："))
if score>100 or score<0:
    print("您输入的分数不合理")
else:
    if score<60:
        grade="不及格"
        print("您的分数不及格")
    elif score<70:
        grade="及格"
        print("您的分数为及格")
    elif score<80:
        grade="中等"
        print("您的分数为中等")
    elif score<90:
        grade="良好"
        print("您的分数为良好")
    else:
        grade="优秀"
        print("您的分数为优秀")
    print("您的分数为{0}，等级为{1}".format(score,grade))


