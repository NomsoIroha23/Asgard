#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=1


# In[2]:


b=2


# In[3]:


c = a + b


# In[5]:


print (c)


# In[6]:


type(c) 


# In[7]:


name = "francis"


# In[8]:


type (name)


# In[9]:


fname = 1
sname = "okoye"


# In[10]:


a = "2"
b = 3


# In[12]:


int (a) + b


# In[13]:


a = 1
b = 2
c = 3
total = a + b + c
print (total)


# In[14]:


a = 1/2


# In[15]:


type (a)


# In[18]:


z = (2+3) + (5+10)


# In[19]:


z


# In[20]:


name = "francis" 
planet = "earth"


# In[21]:


print ("my name is {} and i live on {}". format(name,planet) #the variables of name and planet can always be changed that is francis and eath)


# In[22]:


planet ="mars"
diameter = 1000000


# In[23]:


print ("the diameter of {} is {} kilometer".format (planet,diameter))


# In[24]:


1, 2, 3, 4, 5, 6, 7, 8, 9, 10


# In[25]:


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[26]:


type (number)


# In[27]:


a = [1,2,3,"francis","hello",[1,2,3,4,5]]


# In[28]:


a.append("ayobami")


# In[29]:


a


# In[30]:


a[-1]


# In[33]:


numbers = a[-1]
numbers


# In[35]:


a.insert(2,"ayobami")


# In[36]:


a


# In[37]:


a


# In[39]:


hello = a[5]
print(hello)


# In[40]:


a[0]


# In[42]:


len(a) #len means number of items in the data set


# In[43]:


a[5][0]


# In[44]:


a


# In[45]:


a[:]


# In[46]:


# a and [:] are the same, they run the data in the list


# In[47]:


a[:4]


# In[48]:


a[2:]


# In[50]:


a[2:-2]


# In[53]:


strings =a[2:-1]
print(strings)


# In[64]:


members = {"francis":"anambra","ayobami":"osun",jabar:"kano"}


# In[65]:


members = {'francis':'anambra','ayobami':'osun','jakbar':'kano'}


# In[66]:


members


# In[67]:


members = {'emp001':['francis','anambra',50,'wild life'],'emp002':['ayobami','osun',16,]}


# In[80]:


type(members)


# In[71]:


a = []list
b = {key:value}
c = {} set
d = ()tuple


# In[72]:


tup = (1,2,3,4,5,1,2,3,4,5,5)


# In[73]:


tup[-1]


# In[74]:


tup[-1] = 10


# In[75]:


print()


# In[76]:


b = {1,2,3,4,4,5,1,1,1,1,1,1,1,1,1,}


# In[77]:


b


# In[78]:


#a set doesnt permit repeating values hence only 1,2,3,4,5


# In[81]:


1>2


# In[82]:


1<2


# In[83]:


#these are buleans true or false


# In[84]:


a=1


# In[85]:


a==1


# In[86]:


a==2


# In[87]:


#one equals to is an assignment and 2 equals too is a comparison


# In[88]:


(1>2) and (2<3) #and means two conditions must be satisfied 


# In[89]:


#answer is false because the conditions of 1>2 is false


# In[90]:


(1>2) or (2<3)


# In[91]:


#for and both conditions must be met, while or just one condition must be mean, so therefore only 2<3 IS correct hence true


# In[92]:


(1==2) or (3==4) or (5==5)


# In[93]:


#for or only one condition needs to be correct


# In[96]:


if 10<20:
    print("how?")


# In[98]:


if 100<20:
    print("how?")
else:
    print("are you normal?")


# In[102]:


if 1==10:
    print("a")
elif 30==30:
    print("b")
else:
    print("c")


# In[114]:


numbers =list(range(1,11))


# In[115]:


numbers


# In[118]:


for i in numbers:
    print (2**2)


# In[122]:


for i in range(5)
    print(i)


# In[126]:


pages = list(range(1,11))


# In[127]:


pages


# In[129]:


result = []
for page in pages:
    result.append(page*2)
print(result)


# In[130]:


#append is used to add something to a list


# In[131]:


name = "francis"


# In[137]:


name = input("enter your name:")


# In[133]:


fr


# In[ ]:


price = input()


# In[138]:


price = input("enterprice of the item: ")
print("the price of the item is", price, "naira")


# In[139]:


tax = input("enter tax rate: ")
print("your tax rate is:", tax,"%")


# In[143]:


tax = int(tax)


# In[140]:


(100*0.05)+ 100


# In[141]:


total_price = (price * tax)+ price


# In[144]:


price = float(input


# In[150]:


def my_function(fname):
    print (fname + "" + "okoye")
    


# In[151]:


my_function("francis")


# In[152]:


def interest(p,r,t):
    interest = p*r*t
    return interest


# In[153]:


interest(100,0.05,5)


# In[ ]:




