import os
result = []
def listdir(parentdir,filename=''):
    os.chdir(parentdir)
    dirlist=os.listdir()
    for i in dirlist:
        if i.endswith('.py'):
            flag=find_hello(i)
            if flag == True:
                result.append(os.path.abspath(i))
        else:
            listdir(i)
def find_hello(file):
    f=open(file,'rb')
    while True:
        i=f.readline()
        if not i:
            return False
            break
        i=i.decode()
        if 'hello' in i:
            return True
    f.close()
listdir(r'C:\Users\zsj\Desktop\test')
print(result)