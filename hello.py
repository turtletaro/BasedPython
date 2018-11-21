Python 3.5.6 |Anaconda, Inc.| (default, Aug 26 2018, 16:30:03) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
In [2]: import itchat
   ...: itchat.auto_login()
   ...: itchat.send('Hello, filehelper', toUserName='filehelper')
Getting uuid of QR code.
Downloading QR code.
Please scan the QR code to log in.
Please press confirm on your phone.
Log in time out, reloading QR code.
Getting uuid of QR code.
Downloading QR code.
Please scan the QR code to log in.
---------------------------------------------------------------------------
BadStatusLine                             Traceback (most recent call last)
/anaconda3/envs/python354/lib/python3.5/site-packages/urllib3/connectionpool.py in urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
    599                                                   body=body, headers=headers,
--> 600                                                   chunked=chunked)
    601 

/anaconda3/envs/python354/lib/python3.5/site-packages/urllib3/connectionpool.py in _make_request(self, conn, method, url, timeout, chunked, **httplib_request_kw)
    383                     # otherwise it looks like a programming error was the cause.
--> 384                     six.raise_from(e, None)
    385         except (SocketTimeout, BaseSSLError, SocketError) as e:

/anaconda3/envs/python354/lib/python3.5/site-packages/urllib3/packages/six.py in raise_from(value, from_value)

/anaconda3/envs/python354/lib/python3.5/site-packages/urllib3/connectionpool.py in _make_request(self, conn, method, url, timeout, chunked, **httplib_request_kw)
    379                 try:
--> 380                     httplib_response = conn.getresponse()
    381                 except Exception as e:

/anaconda3/envs/python354/lib/python3.5/http/client.py in getresponse(self)
   1197             try:
-> 1198                 response.begin()
   1199             except ConnectionError:

/anaconda3/envs/python354/lib/python3.5/http/client.py in begin(self)
    296         while True:
--> 297             version, status, reason = self._read_status()
    298             if status != CONTINUE:

/anaconda3/envs/python354/lib/python3.5/http/client.py in _read_status(self)
    278             self._close_conn()
--> 279             raise BadStatusLine(line)
    280 

BadStatusLine:  200 OK


During handling of the above exception, another exception occurred:

ProtocolError                             Traceback (most recent call last)
/anaconda3/envs/python354/lib/python3.5/site-packages/requests/adapters.py in send(self, request, stream, timeout, verify, cert, proxies)
    448                     retries=self.max_retries,
--> 449                     timeout=timeout
    450                 )

/anaconda3/envs/python354/lib/python3.5/site-packages/urllib3/connectionpool.py in urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
    637             retries = retries.increment(method, url, error=e, _pool=self,
--> 638                                         _stacktrace=sys.exc_info()[2])
    639             retries.sleep()

/anaconda3/envs/python354/lib/python3.5/site-packages/urllib3/util/retry.py in increment(self, method, url, response, error, _pool, _stacktrace)
    366             if read is False or not self._is_method_retryable(method):
--> 367                 raise six.reraise(type(error), error, _stacktrace)
    368             elif read is not None:

/anaconda3/envs/python354/lib/python3.5/site-packages/urllib3/packages/six.py in reraise(tp, value, tb)
    684         if value.__traceback__ is not tb:
--> 685             raise value.with_traceback(tb)
    686         raise value

/anaconda3/envs/python354/lib/python3.5/site-packages/urllib3/connectionpool.py in urlopen(self, method, url, body, headers, retries, redirect, assert_same_host, timeout, pool_timeout, release_conn, chunked, body_pos, **response_kw)
    599                                                   body=body, headers=headers,
--> 600                                                   chunked=chunked)
    601 

/anaconda3/envs/python354/lib/python3.5/site-packages/urllib3/connectionpool.py in _make_request(self, conn, method, url, timeout, chunked, **httplib_request_kw)
    383                     # otherwise it looks like a programming error was the cause.
--> 384                     six.raise_from(e, None)
    385         except (SocketTimeout, BaseSSLError, SocketError) as e:

/anaconda3/envs/python354/lib/python3.5/site-packages/urllib3/packages/six.py in raise_from(value, from_value)

/anaconda3/envs/python354/lib/python3.5/site-packages/urllib3/connectionpool.py in _make_request(self, conn, method, url, timeout, chunked, **httplib_request_kw)
    379                 try:
--> 380                     httplib_response = conn.getresponse()
    381                 except Exception as e:

/anaconda3/envs/python354/lib/python3.5/http/client.py in getresponse(self)
   1197             try:
-> 1198                 response.begin()
   1199             except ConnectionError:

/anaconda3/envs/python354/lib/python3.5/http/client.py in begin(self)
    296         while True:
--> 297             version, status, reason = self._read_status()
    298             if status != CONTINUE:

/anaconda3/envs/python354/lib/python3.5/http/client.py in _read_status(self)
    278             self._close_conn()
--> 279             raise BadStatusLine(line)
    280 

ProtocolError: ('Connection aborted.', BadStatusLine(' 200 OK\r\n',))

During handling of the above exception, another exception occurred:

ConnectionError                           Traceback (most recent call last)
<ipython-input-2-eb7608dc768a> in <module>
----> 1 import codecs, os, ast;__pyfile = codecs.open('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/pyULmW6D''', encoding='''utf-8''');__code = __pyfile.read().encode('''utf-8''');__pyfile.close();os.remove('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/pyULmW6D''');__block = ast.parse(__code, '''/Users/wangqun/BasedPython/hello.py''', mode='exec');__last = __block.body[-1];__isexpr = isinstance(__last,ast.Expr);__block.body.pop() if __isexpr else None;exec(compile(__block, '''/Users/wangqun/BasedPython/hello.py''', mode='exec'));eval(compile(ast.Expression(__last.value), '''/Users/wangqun/BasedPython/hello.py''', mode='eval')) if __isexpr else None

~/BasedPython/hello.py in <module>
      1 print('hello world')
----> 2 print('hello')

/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/register.py in auto_login(self, hotReload, statusStorageDir, enableCmdQR, picDir, qrCallback, loginCallback, exitCallback)
     34     else:
     35         self.login(enableCmdQR=enableCmdQR, picDir=picDir, qrCallback=qrCallback,
---> 36             loginCallback=loginCallback, exitCallback=exitCallback)
     37 
     38 def configured_reply(self):

/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/login.py in login(self, enableCmdQR, picDir, qrCallback, loginCallback, exitCallback)
     51         isLoggedIn = False
     52         while not isLoggedIn:
---> 53             status = self.check_login()
     54             if hasattr(qrCallback, '__call__'):
     55                 qrCallback(uuid=self.uuid, status=status, qrcode=qrStorage.getvalue())

/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/login.py in check_login(self, uuid)
    131         uuid, int(-localTime / 1579), localTime)
    132     headers = { 'User-Agent' : config.USER_AGENT }
--> 133     r = self.s.get(url, params=params, headers=headers)
    134     regx = r'window.code=(\d+)'
    135     data = re.search(regx, r.text)

/anaconda3/envs/python354/lib/python3.5/site-packages/requests/sessions.py in get(self, url, **kwargs)
    544 
    545         kwargs.setdefault('allow_redirects', True)
--> 546         return self.request('GET', url, **kwargs)
    547 
    548     def options(self, url, **kwargs):

/anaconda3/envs/python354/lib/python3.5/site-packages/requests/sessions.py in request(self, method, url, params, data, headers, cookies, files, auth, timeout, allow_redirects, proxies, hooks, stream, verify, cert, json)
    531         }
    532         send_kwargs.update(settings)
--> 533         resp = self.send(prep, **send_kwargs)
    534 
    535         return resp

/anaconda3/envs/python354/lib/python3.5/site-packages/requests/sessions.py in send(self, request, **kwargs)
    644 
    645         # Send the request
--> 646         r = adapter.send(request, **kwargs)
    647 
    648         # Total elapsed time of the request (approximately)

/anaconda3/envs/python354/lib/python3.5/site-packages/requests/adapters.py in send(self, request, stream, timeout, verify, cert, proxies)
    496 
    497         except (ProtocolError, socket.error) as err:
--> 498             raise ConnectionError(err, request=request)
    499 
    500         except MaxRetryError as e:

ConnectionError: ('Connection aborted.', BadStatusLine(' 200 OK\r\n',))

In [3]: import itchat
   ...: @itchat.msg_register(itchat.content.TEXT)
   ...: def text_reply(msg):
   ...:     return msg.text
   ...: 
   ...: itchat.auto_login()
   ...: itchat.run()
itchat has already logged in.
Start auto replying.

In [4]: xx
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-4-ce3af7760f12> in <module>
----> 1 xx

NameError: name 'xx' is not defined

In [5]: import itchat
   ...: @itchat.msg_register(itchat.content.TEXT)
   ...: def text_reply(msg):
   ...:     return msg.text
   ...: 
   ...: itchat.auto_login()
   ...: itchat.run()
itchat has already logged in.
Start auto replying.

In [6]: import itchat
   ...: @itchat.msg_register(itchat.content.TEXT)
   ...: def text_reply(msg):
   ...:     return msg.text
   ...: 
   ...: itchat.auto_login()
   ...: itchat.run()
   ...: 
   ...: @itchat.msg_register(TEXT)
   ...: def _(msg):
   ...:     # equals to print(msg['FromUserName'])
   ...:     print(msg.fromUserName)
itchat has already logged in.
Start auto replying.
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-6-2f732e2fdcf9> in <module>
----> 1 import codecs, os, ast;__pyfile = codecs.open('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/pyKIOIUu''', encoding='''utf-8''');__code = __pyfile.read().encode('''utf-8''');__pyfile.close();os.remove('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/pyKIOIUu''');__block = ast.parse(__code, '''/Users/wangqun/BasedPython/hello.py''', mode='exec');__last = __block.body[-1];__isexpr = isinstance(__last,ast.Expr);__block.body.pop() if __isexpr else None;exec(compile(__block, '''/Users/wangqun/BasedPython/hello.py''', mode='exec'));eval(compile(ast.Expression(__last.value), '''/Users/wangqun/BasedPython/hello.py''', mode='eval')) if __isexpr else None

~/BasedPython/hello.py in <module>

NameError: name 'TEXT' is not defined

In [7]: import itchat
   ...: @itchat.msg_register(itchat.content.TEXT)
   ...: def text_reply(msg):
   ...:     return msg.text
   ...: 
   ...: itchat.auto_login()
   ...: itchat.run()
   ...: itchat.auto_login(enableCmdQR=True)
itchat has already logged in.
Start auto replying.
itchat has already logged in.

In [8]: import itchat
   ...: itchat.search_friends()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-8-7c0ebb348b10> in <module>
----> 1 import codecs, os, ast;__pyfile = codecs.open('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/py9R9q54''', encoding='''utf-8''');__code = __pyfile.read().encode('''utf-8''');__pyfile.close();os.remove('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/py9R9q54''');__block = ast.parse(__code, '''/Users/wangqun/BasedPython/hello.py''', mode='exec');__last = __block.body[-1];__isexpr = isinstance(__last,ast.Expr);__block.body.pop() if __isexpr else None;exec(compile(__block, '''/Users/wangqun/BasedPython/hello.py''', mode='exec'));eval(compile(ast.Expression(__last.value), '''/Users/wangqun/BasedPython/hello.py''', mode='eval')) if __isexpr else None

~/BasedPython/hello.py in <module>
      1 print('hello world')
----> 2 print('hello')

/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/core.py in search_friends(self, name, userName, remarkName, nickName, wechatAccount)
    453             wechatAccount=None):
    454         return self.storageClass.search_friends(name, userName, remarkName,
--> 455             nickName, wechatAccount)
    456     def search_chatrooms(self, name=None, userName=None):
    457         return self.storageClass.search_chatrooms(name, userName)

/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/storage/__init__.py in search_friends(self, name, userName, remarkName, nickName, wechatAccount)
     64         with self.updateLock:
     65             if (name or userName or remarkName or nickName or wechatAccount) is None:
---> 66                 return copy.deepcopy(self.memberList[0]) # my own account
     67             elif userName: # return the only userName match
     68                 for m in self.memberList:

IndexError: list index out of range

In [9]: import itchat
   ...: tchat.login() 
   ...: #爬取自己好友相关信息， 返回一个json文件 
   ...: friends = itchat.get_friends(update=True)[0:]
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-9-dd9f787a3cb6> in <module>
----> 1 import codecs, os, ast;__pyfile = codecs.open('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/py67Qlqw''', encoding='''utf-8''');__code = __pyfile.read().encode('''utf-8''');__pyfile.close();os.remove('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/py67Qlqw''');__block = ast.parse(__code, '''/Users/wangqun/BasedPython/hello.py''', mode='exec');__last = __block.body[-1];__isexpr = isinstance(__last,ast.Expr);__block.body.pop() if __isexpr else None;exec(compile(__block, '''/Users/wangqun/BasedPython/hello.py''', mode='exec'));eval(compile(ast.Expression(__last.value), '''/Users/wangqun/BasedPython/hello.py''', mode='eval')) if __isexpr else None

~/BasedPython/hello.py in <module>
      1 print('hello world')
----> 2 print('hello')

NameError: name 'tchat' is not defined

In [10]: import itchat
    ...: itchat.login() 
    ...: #爬取自己好友相关信息， 返回一个json文件 
    ...: friends = itchat.get_friends(update=True)[0:]
itchat has already logged in.
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-10-5640c323e0df> in <module>
----> 1 import codecs, os, ast;__pyfile = codecs.open('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/py9rsXSp''', encoding='''utf-8''');__code = __pyfile.read().encode('''utf-8''');__pyfile.close();os.remove('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/py9rsXSp''');__block = ast.parse(__code, '''/Users/wangqun/BasedPython/hello.py''', mode='exec');__last = __block.body[-1];__isexpr = isinstance(__last,ast.Expr);__block.body.pop() if __isexpr else None;exec(compile(__block, '''/Users/wangqun/BasedPython/hello.py''', mode='exec'));eval(compile(ast.Expression(__last.value), '''/Users/wangqun/BasedPython/hello.py''', mode='eval')) if __isexpr else None

~/BasedPython/hello.py in <module>
      2 print('hello')

/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/contact.py in get_friends(self, update)
    304 def get_friends(self, update=False):
    305     if update:
--> 306         self.get_contact(update=True)
    307     return utils.contact_deep_copy(self, self.memberList)
    308 

/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/contact.py in get_contact(self, update)
    283     seq, memberList = 0, []
    284     while 1:
--> 285         seq, batchMemberList = _get_contact(seq)
    286         memberList.extend(batchMemberList)
    287         if seq == 0:

/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/contact.py in _get_contact(seq)
    267         return utils.contact_deep_copy(self, self.chatroomList)
    268     def _get_contact(seq=0):
--> 269         url = '%s/webwxgetcontact?r=%s&seq=%s&skey=%s' % (self.loginInfo['url'],
    270             int(time.time()), seq, self.loginInfo['skey'])
    271         headers = {

KeyError: 'url'

In [11]: import itchat
    ...: itchat.login() 
    ...: #爬取自己好友相关信息， 返回一个json文件 
    ...: friends = itchat.get_friends(update=True)[0:]
itchat has already logged in.
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-11-2025108c326c> in <module>
----> 1 import codecs, os, ast;__pyfile = codecs.open('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/pyXZMSg0''', encoding='''utf-8''');__code = __pyfile.read().encode('''utf-8''');__pyfile.close();os.remove('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/pyXZMSg0''');__block = ast.parse(__code, '''/Users/wangqun/BasedPython/hello.py''', mode='exec');__last = __block.body[-1];__isexpr = isinstance(__last,ast.Expr);__block.body.pop() if __isexpr else None;exec(compile(__block, '''/Users/wangqun/BasedPython/hello.py''', mode='exec'));eval(compile(ast.Expression(__last.value), '''/Users/wangqun/BasedPython/hello.py''', mode='eval')) if __isexpr else None

~/BasedPython/hello.py in <module>
      2 print('hello')

/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/contact.py in get_friends(self, update)
    304 def get_friends(self, update=False):
    305     if update:
--> 306         self.get_contact(update=True)
    307     return utils.contact_deep_copy(self, self.memberList)
    308 

/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/contact.py in get_contact(self, update)
    283     seq, memberList = 0, []
    284     while 1:
--> 285         seq, batchMemberList = _get_contact(seq)
    286         memberList.extend(batchMemberList)
    287         if seq == 0:

/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/contact.py in _get_contact(seq)
    267         return utils.contact_deep_copy(self, self.chatroomList)
    268     def _get_contact(seq=0):
--> 269         url = '%s/webwxgetcontact?r=%s&seq=%s&skey=%s' % (self.loginInfo['url'],
    270             int(time.time()), seq, self.loginInfo['skey'])
    271         headers = {

KeyError: 'url'

In [12]: import itchat
    ...: itchat.login() 
    ...: #爬取自己好友相关信息， 返回一个json文件 
    ...: friends = itchat.get_friends(update=True)[0:]
itchat has already logged in.
Traceback (most recent call last):
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 3267, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-12-520b97bc1b97>", line 1, in <module>
    import codecs, os, ast;__pyfile = codecs.open('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/pyK9tf8P''', encoding='''utf-8''');__code = __pyfile.read().encode('''utf-8''');__pyfile.close();os.remove('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/pyK9tf8P''');__block = ast.parse(__code, '''/Users/wangqun/BasedPython/hello.py''', mode='exec');__last = __block.body[-1];__isexpr = isinstance(__last,ast.Expr);__block.body.pop() if __isexpr else None;exec(compile(__block, '''/Users/wangqun/BasedPython/hello.py''', mode='exec'));eval(compile(ast.Expression(__last.value), '''/Users/wangqun/BasedPython/hello.py''', mode='eval')) if __isexpr else None
  File "/Users/wangqun/BasedPython/hello.py", line 4, in <module>
    friends = itchat.get_friends(update=True)[0:]
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/contact.py", line 306, in get_friends
    self.get_contact(update=True)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/contact.py", line 285, in get_contact
    seq, batchMemberList = _get_contact(seq)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/itchat/components/contact.py", line 269, in _get_contact
    url = '%s/webwxgetcontact?r=%s&seq=%s&skey=%s' % (self.loginInfo['url'],
KeyError: 'url'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 3185, in run_ast_nodes
    if (yield from self.run_code(code, result)):
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 3284, in run_code
    self.showtraceback(running_compiled_code=True)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2023, in showtraceback
    self._showtraceback(etype, value, stb)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2041, in _showtraceback
    print(self.InteractiveTB.stb2text(stb))
UnicodeEncodeError: 'ascii' codec can't encode characters in position 2459-2469: ordinal not in range(128)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2845, in _run_cell
    return runner(coro)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/async_helpers.py", line 67, in _pseudo_sync_runner
    coro.send(None)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 3020, in run_cell_async
    interactivity=interactivity, compiler=compiler, result=result)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 3210, in run_ast_nodes
    self.showtraceback()
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2023, in showtraceback
    self._showtraceback(etype, value, stb)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2041, in _showtraceback
    print(self.InteractiveTB.stb2text(stb))
UnicodeEncodeError: 'ascii' codec can't encode characters in position 2902-2912: ordinal not in range(128)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/anaconda3/envs/python354/bin/ipython3", line 11, in <module>
    sys.exit(start_ipython())
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/__init__.py", line 125, in start_ipython
    return launch_new_instance(argv=argv, **kwargs)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/traitlets/config/application.py", line 658, in launch_instance
    app.start()
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/terminal/ipapp.py", line 356, in start
    self.shell.mainloop()
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/terminal/interactiveshell.py", line 490, in mainloop
    self.interact()
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/terminal/interactiveshell.py", line 481, in interact
    self.run_cell(code, store_history=True)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2819, in run_cell
    raw_cell, store_history, silent, shell_futures)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2850, in _run_cell
    self.showtraceback(running_compiled_code=True)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2023, in showtraceback
    self._showtraceback(etype, value, stb)
  File "/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/interactiveshell.py", line 2041, in _showtraceback
    print(self.InteractiveTB.stb2text(stb))
UnicodeEncodeError: 'ascii' codec can't encode characters in position 2902-2912: ordinal not in range(128)

If you suspect this is an IPython bug, please report it at:
    https://github.com/ipython/ipython/issues
or send an email to the mailing list at ipython-dev@python.org

You can print a more detailed traceback right now with "%tb", or use "%debug"
to interactively debug it.

Extra-detailed tracebacks for bug-reporting purposes can be enabled via:
    %config Application.verbose_crash=True


Process Python exited abnormally with code 1
Python 3.5.6 |Anaconda, Inc.| (default, Aug 26 2018, 16:30:03) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
In [2]: import itchat
   ...: itchat.auto_login()
   ...: itchat.send('Hello, filehelper', toUserName='filehelper')
Getting uuid of QR code.
Downloading QR code.
Please scan the QR code to log in.
Please press confirm on your phone.
Loading the contact, this may take a little while.
Login successfully as \u5c0f\u5c0f\u5c11\u5e74\U0001f31f
Out[2]: ---------------------------------------------------------------------------
UnicodeEncodeError                        Traceback (most recent call last)
<ipython-input-2-0bd9de7b64e6> in <module>
----> 1 import codecs, os, ast;__pyfile = codecs.open('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/pyo7sxxu''', encoding='''utf-8''');__code = __pyfile.read().encode('''utf-8''');__pyfile.close();os.remove('''/var/folders/4b/vnybf_3j2pg8344598dv96qw0000gn/T/pyo7sxxu''');__block = ast.parse(__code, '''/Users/wangqun/BasedPython/hello.py''', mode='exec');__last = __block.body[-1];__isexpr = isinstance(__last,ast.Expr);__block.body.pop() if __isexpr else None;exec(compile(__block, '''/Users/wangqun/BasedPython/hello.py''', mode='exec'));eval(compile(ast.Expression(__last.value), '''/Users/wangqun/BasedPython/hello.py''', mode='eval')) if __isexpr else None

/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/displayhook.py in __call__(self, result)
    259             self.fill_exec_result(result)
    260             if format_dict:
--> 261                 self.write_format_data(format_dict, md_dict)
    262                 self.log_output(format_dict)
    263             self.finish_displayhook()

/anaconda3/envs/python354/lib/python3.5/site-packages/IPython/core/displayhook.py in write_format_data(self, format_dict, md_dict)
    188                 result_repr = '\n' + result_repr
    189 
--> 190         print(result_repr)
    191 
    192     def update_user_ns(self, result):

UnicodeEncodeError: 'ascii' codec can't encode characters in position 59-62: ordinal not in range(128)

In [3]: UnicodeEncodeError: 'ascii' codec can't encode characters in position 59-62: ordinal not in range(128)

In [3]:   C-c C-c
KeyboardInterrupt escaped interact()


In [3]: LOG OUT!
