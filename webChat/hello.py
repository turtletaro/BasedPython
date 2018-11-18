import itchat
import sys
import codecs
import re
from pandas import DataFrame
# soure from https://github.com/youfou/wxpy python 2-3
# soure from https://github.com/liuwons/wxBot python 2
# soure from https://itchat.readthedocs.io/zh/latest/

#print(sys.stdout.encoding)
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
###print(sys.stdout.encoding)
#itchat.auto_login() 
itchat.send('hello webChat',toUserName='filehelper')
user = itchat.get_friends()

#get the first user for yourself
i = str(user[:1])
print(i)

info = i[8:-2]
print(info)

name = str(re.findall(r"'NickName': '(.+?)'", info))[2:-2]
sign = str(re.findall(r"'Signature': '(.+?)'", info))[2:-2]
sex = str(re.findall(r"'Sex': (.+?),", info))[2:-2]
uin = str(re.findall(r"'Uin': (.+?),", info))[2:-2]
print(name)
print(sign)
print(sex)
print(uin)

friends = itchat.get_friends(update=True)[0:]
male = female = other = 0 
#friends[0]是自己的信息，所以要从friends[1]开始 
for i in friends[1:]: 
    sex = i["Sex"] 
    if sex == 1: 
        male += 1 
    elif sex == 2: 
        female += 1 
    else: 
        other +=1 
#计算朋友总数 
total = len(friends[1:]) 
#打印出自己的好友性别比例 
print("男性好友： %.2f%%" % (float(male)/total*100) + "\n" + 
"女性好友： %.2f%%" % (float(female) / total * 100) + "\n" + 
"不明性别好友： %.2f%%" % (float(other) / total * 100))

#定义一个函数，用来爬取各个变量 
def get_var(var): 
    variable = [] 
    for i in friends: 
        value = i[var] 
        variable.append(value) 
    return variable 
#调用函数得到各变量，并把数据存到csv文件中，保存到桌面 
NickName = get_var("NickName") 
Sex = get_var('Sex') 
Province = get_var('Province') 
City = get_var('City') 
Signature = get_var('Signature') 

data = {'NickName': NickName, 'Sex': Sex, 'Province': Province, 
        'City': City, 'Signature': Signature} 
frame = DataFrame(data) 
frame.to_csv('data.csv', index=True) 
