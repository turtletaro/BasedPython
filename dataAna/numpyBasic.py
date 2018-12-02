import numpy as np
np.random.rand(4,2)
np.random.randn(4,2)
np.random.randint(2, size=10)
np.random.randint(1, size=5)
np.random.randint(9, size=(4,5))
np.random.random((3,5))
np.random.choice(8,3)
a = [3,5,6,8,2,6,8]
np.random.choice(a,1)
np.random.choice(a,1)
np.random.choice(a,3)
np.random.choice(a,4)
arr = np.arange(9)
np.random.shuffle(arr)
str1 = '1+4'
str2 = '[1,2,3,4,5,6,7]'
str3 = '[[1,],[2],[3,]]'

type(eval(str1))

type(eval(str2))
type(eval(str3))

hash = {'name':'hoho','age':18}

