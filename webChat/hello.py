import itchat
import sys
import codecs

#print(sys.stdout.encoding)
#sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
###print(sys.stdout.encoding)
#itchat.auto_login() 
itchat.send('hello webChat',toUserName='filehelper')
user = itchat.get_friends()

#get the first user for yourself
i = str(user[:1])
print(i)
