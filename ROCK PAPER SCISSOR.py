#!/usr/bin/env python
# coding: utf-8

# In[20]:


import random
def gamewin(comp,win):
    if comp==a:
        return None
    elif comp=='r':
        if a=='p':
            return False
        if a=='s':
            return False
    elif comp=='p':
        if a=='r':
            return False
        if a=='s':
            return True
    elif comp=='s':
        if a=='r':
            return True
        if a=='p':
            return False
print("comp turn:rock(r),paper(p),scissor(s)?")
randomnum=random.randint(1,3)
if randomnum==1:
    comp='r'
elif randomnum==2:
        comp='p'
elif randomnum==3:
    comp='s'
print(randomnum)
a=input("your_turn:rock(r),paper(p),scissor(s)?")
print(f"computer chose {comp}")
print(f"you chose {a}")
result=gamewin(comp,a)
if result==None:
    print("game is a tie!")
elif result:
        print("you win!")
else:
        print("you lost!")


# In[22]:





# In[ ]:





# In[ ]:




