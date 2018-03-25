import os
side='='*48
print(side)
print('学生成绩管理系统'.center(len(side)-5))
print(side)
print('输入1：添加学生信息')
print('输入2：查找学生信息')
print('输入3：删除学生信息')
print('输入4：修改学生信息')
print('输入5：显示所有学生信息')
print('输入6：按成绩排序')
print('输入7：退出')
print(side)

totalstudeninfo=[]
def readfile():
    with open('stuinfo.txt') as f:
        while True:
            content=f.readline()  
            if content == '':
                break
            print(content)
            list1=content.split('-')
            print(list1)
            stu={}
            stu['name']=list1[1]
            stu['age']=list1[3]
            stu['score']=list1[5]
            totalstudeninfo.append(stu)
def addstu():
    stu={}
    name=input('请输入要增加的学生名字:')
    age=int(input('请输入学生年龄:'))
    score=int(input('请输入学生成绩:'))
    stu['name']=name
    stu['age']=age
    stu['score']=score
    print(stu)
    totalstudeninfo.append(stu)
      
def writefile(content):
    f=open("stuinfo.txt",'w')
    for i in content:
        #print(type(i['name']))
        f.write('姓名:-%s-\t年龄:-%s-\t成绩:-%s-\t\n'%(i['name'],i['age'],i['score']))
    f.close()
def findstu():
    name=input('请输入要查找的学生名字:')
    count=len(totalstudeninfo)
    for student in totalstudeninfo:
        if name in student.values():
            print(student)
            break
        count-=1
        if count == 0:
            print('查无此人') 
def delstu():
    name=input('请输入要删除的学生名字:')
    count=len(totalstudeninfo)
    for student in totalstudeninfo:
        if name in student.values():
            totalstudeninfo.remove(student)
            break
        count-=1
        if count == 0:
            print('查无此人') 
def changestu():
    name=input('请输入要修改的学生名字:')
    count=len(totalstudeninfo)
    for student in totalstudeninfo:
        if name in student.values():
            name=input('请输入要增加的学生名字:')
            age=input('请输入学生年龄:')
            score=input('请输入学生成绩:')
            student['name']=name
            student['age']=age
            student['score']=score
            break
        count-=1
        if count == 0:
            print('查无此人')
readfile()
while True:
    key=input('请输入操作代码:')
    if key == '1':
        addstu()
    elif key == '2':
        findstu()      
    elif key == '3':
        delstu()
    elif key == '4':
        changestu()
    elif key == '5':
        for i in totalstudeninfo:
            print(i)
    elif key == '6':
        foo=lambda s:s['score'] 
        sortstu=sorted(totalstudeninfo,key=foo,reverse=True)
        print(sortstu)
    elif key == '7':
        break
    writefile(totalstudeninfo)