
# coding: utf-8

# In[9]:

#Assignment 11.1
#Consider a DataFrame df where there is an integer column 'X':
#df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
#For each value, count the difference back to the previous zero (or the start of the Series, whichever is closer).
#These values should therefore be [1, 2, 0, 1, 2, 3, 4, 0, 1, 2]. Make this a new column 'Y'.

#"Approach 1"
ctr=0
lstdisp=[]
lst=[7,2,0,3,4,2,5,0,3,4]

#for i in range(len(lst)):       
    #print lst[i]

for j in lst:       
    if j==0:
        ctr=0
    else:    
        ctr+=1
    lstdisp.append(ctr) 
    
print("Result Approach 1:")
print(lstdisp) 

#Approach 2 using Pandas
import pandas as pd
s = pd.Series([7, 2, 0, 3, 4, 2, 5, 0, 3, 4])
#print(s)
# coding: utf-8

# In[32]:

import numpy as np
import pandas as pd
lst = [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]
#Output - [1, 2, 0, 1, 2, 3, 4, 0, 1, 2].
print(lst)
ctr=1
numlst=[]
for index in lst:
    #print(lst[index])
    if(lst[index]==0):
        ctr=0
    else:
        ctr=ctr+1       
    numlst.append(ctr)
print(numlst)        
df = pd.DataFrame({'x':[7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
df


# In[ ]:




lst1 = (s.groupby(s.eq(0).cumsum().mask(s.eq(0))).cumcount() + 1).mask(s.eq(0), 0).tolist()
print("Result Approach 2: ")
print(lst1)   


# In[ ]:




# In[ ]:



