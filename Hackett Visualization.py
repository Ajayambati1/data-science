#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
Hackett=pd.read_excel("C:\\Users\\91912\\Documents\\Ajay\\Projects\\FN_Key_Issues_Test data.xlsx",'Rd_text',header=0)
H=Hackett.iloc[1:,:]
H=H.astype('category')
H['Q6#1_33']=H['Q6#1_33'].cat.rename_categories([4,3,1,2])
H['Q6#1_33']=H['Q6#1_33'].astype('int64')
from matplotlib import style
import matplotlib.pyplot as plt
style.use('ggplot')
H['Q6#1_33'].plot.hist()
plt.title('Support Enterprise Digital Transformation strategy,objectives and initiatives',color='red')
plt.suptitle('FINANCE',fontweight='bold')


# In[390]:


H['Q9_4'].value_counts().plot.pie(autopct='%1.1f%%',explode=(0.1,0.1,0,0,0),figsize=(10,5),colors=['red','grey','cyan','yellow','orange'])
plt.title('Global Service Organisation')


# In[392]:


colors=['red','green','yellow','orange','cyan']
H['Q9_5'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.1,0,0))
plt.xlabel('Corporate Finance /HQ')


# In[33]:


sizes=[]
for j in ['Q6#1_33','Q6#1_34','Q6#1_35','Q6#1_36','Q6#1_37','Q6#1_39']:
    for i in range(1,5):
        a=H.loc[H[j]==i,j].count()
        sizes.append(a)
sizes


# In[3]:


plt.pie(sizes[:4],autopct='%1.1f%%',explode=(0,0,0,0.1),colors=['red','green','yellow','pink'],labels=['Low','Moderate','High','Critical'])
plt.axis('equal')


# In[14]:


plt.pie(sizes[4:8],autopct='%1.1f%%',explode=(0,0,0,0.1),colors=['red','green','yellow','pink'],labels=['Low','Moderate','High','Critical'])


# In[15]:


plt.pie(sizes[8:12],autopct='%1.1f%%',explode=(0,0,0,0.1),colors=['red','green','yellow','pink'],labels=['Low','Moderate','High','Critical'])


# In[16]:


plt.pie(sizes[12:16],autopct='%1.1f%%',explode=(0,0,0,0.3),colors=['red','green','yellow','pink'],labels=['Low','Moderate','High','Critical'],
       shadow=True,startangle=125)
plt.axis('equal')


# In[17]:


plt.pie(sizes[16:20],autopct='%1.1f%%',explode=(0,0,0,0.1),colors=['red','green','yellow','pink'],labels=['Low','Moderate','High','Critical'])
plt.axis('equal')


# In[34]:


plt.pie(sizes[20:24],autopct='%1.1f%%',explode=(0,0,0,0.1),colors=['red','green','yellow','pink'],labels=['Low','Moderate','High','Critical'])
plt.axis('equal')


# In[55]:





# In[105]:


data=[]
for i in ['Q6#1_38','Q6#1_39','Q6#1_40','Q6#1_41','Q6#1_42','Q6#1_43','Q6#1_44','Q6#1_45','Q6#1_46']:
    a=H.loc[H[i]=='Critical',i].count()
    b=H.loc[H[i]=='High',i].count()
    c=H.loc[H[i]=='Moderate',i].count()
    d=H.loc[H[i]=='Low',i].count()
    data.append(a)
    data.append(b)
    data.append(c)
    data.append(d)
data


# In[113]:


plt.pie(data[:4],labels=['Critical','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2))
plt.axis('equal')


# In[114]:


plt.pie(data[4:8],labels=['Critical','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2))
plt.axis('equal')


# In[115]:


plt.pie(data[8:12],labels=['Critical','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2))
plt.axis('equal')


# In[116]:


plt.pie(data[12:16],labels=['Critical','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2))
plt.axis('equal')


# In[117]:


plt.pie(data[16:20],labels=['Critical','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2))
plt.axis('equal')


# In[118]:


plt.pie(data[20:24],labels=['Critical','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2))
plt.axis('equal')


# In[119]:


plt.pie(data[24:28],labels=['Critical','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2))
plt.axis('equal')


# In[120]:


plt.pie(data[28:32],labels=['Critical','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2))
plt.axis('equal')


# In[129]:


plt.pie(data[32:36],labels=['Critical','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2),frame=True,counterclock=True)
plt.axis('equal')


# In[131]:


Ability=[]
for i in ['Q6#2_33','Q6#2_34','Q6#2_35','Q6#2_36','Q6#2_37','Q6#2_38','Q6#2_39','Q6#2_40','Q6#2_41','Q6#2_42','Q6#2_43','Q6#2_44',
         'Q6#2_45','Q6#2_46']:
    v=H.loc[H[i]=='Very High',i].count()
    h=H.loc[H[i]=='High',i].count()
    m=H.loc[H[i]=='Moderate',i].count()
    l=H.loc[H[i]=='Low',i].count()
    Ability.append(v)
    Ability.append(h)
    Ability.append(m)
    Ability.append(l)
Ability


# In[132]:


plt.pie(Ability[:4],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2),counterclock=True)
plt.axis('equal')


# In[134]:


plt.pie(Ability[4:8],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2),counterclock=True)
plt.axis('equal')


# In[135]:


plt.pie(Ability[8:12],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2),frame=True,counterclock=True)
plt.axis('equal')


# In[136]:


plt.pie(Ability[12:16],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2),counterclock=True)
plt.axis('equal')


# In[137]:


plt.pie(Ability[16:20],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2),counterclock=True)
plt.axis('equal')


# In[151]:


plt.pie(Ability[20:24],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0.1,0,0.5),counterclock=True)
plt.axis('equal')


# In[139]:


plt.pie(Ability[24:28],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2),counterclock=True)
plt.axis('equal')


# In[140]:


plt.pie(Ability[28:32],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2),counterclock=True)
plt.axis('equal')


# In[141]:


plt.pie(Ability[32:36],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.2),counterclock=True)
plt.axis('equal')


# In[152]:


plt.pie(Ability[36:40],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.5),counterclock=True)
plt.axis('equal')
plt.show()


# In[145]:


plt.pie(Ability[40:44],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.5),counterclock=True)
plt.axis('equal')


# In[146]:


plt.pie(Ability[44:48],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.5),counterclock=True)
plt.axis('equal')


# In[147]:


plt.pie(Ability[48:52],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.5),counterclock=True)
plt.axis('equal')


# In[148]:


plt.pie(Ability[52:56],labels=['VeryHigh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0,0,0,0.5),counterclock=True)
plt.axis('equal')


# In[169]:


Importance=[]
for i in ['Q7#1_19','Q7#1_20','Q7#1_21','Q7#1_22','Q7#1_23','Q7#1_24',
         'Q7#1_25','Q7#1_26','Q7#1_27','Q7#1_28','Q7#1_29','Q7#1_30',
         'Q7#1_31','Q7#1_32','Q7#1_33','Q7#1_34','Q7#1_35','Q7#1_36']:
    H[i]=H[i].str.strip()
    ff=H.loc[H[i]=='Critical',i].count()
    fg=H.loc[H[i]=='Major',i].count()
    fh=H.loc[H[i]=='Moderate',i].count()
    fl=H.loc[H[i]=='Low',i].count()
    Importance.append(ff)
    Importance.append(fg)
    Importance.append(fh)
    Importance.append(fl)
Importance


# In[198]:


AS=[]
for i in ['Q7#2_19','Q7#2_20','Q7#2_21','Q7#2_22','Q7#2_23','Q7#2_24',
         'Q7#2_25','Q7#2_26','Q7#2_27','Q7#2_28','Q7#2_29','Q7#2_30',
         'Q7#2_31','Q7#2_32','Q7#2_33','Q7#2_34','Q7#2_35','Q7#2_36']:
    H[i]=H[i].str.strip()
    f=H.loc[H[i]=='Very High',i].count()
    g=H.loc[H[i]=='High',i].count()
    h=H.loc[H[i]=='Moderate',i].count()
    l=H.loc[H[i]=='Low',i].count()
    AS.append(f)
    AS.append(g)
    AS.append(h)
    AS.append(l)
AS


# In[176]:


plt.pie(Importance[0:4],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Reduce Finance Operating Cost',color='orange',fontsize=12.5,fontweight='bold')
plt.show()


# In[201]:


plt.pie(AS[0:4],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Reduce Finance Operating Cost',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of Objective/Issue')
plt.show()


# In[177]:


plt.pie(Importance[4:8],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Measure and manage finance performanc eand Business value',color='orange',fontsize=12.5,fontweight='bold')
plt.show()


# In[202]:


plt.pie(AS[4:8],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Measure and manage finance performance and Business value',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of objective/Issue')
plt.show()


# In[179]:


plt.pie(Importance[8:12],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.1),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Optimize deployment of financial resources across the organization',color='orange',fontsize=12.5,fontweight='bold')
plt.show()


# In[205]:


plt.pie(AS[8:12],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.5),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Optimize deployment of financial resources across the organization',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of Objective/Issue')
plt.show()


# In[180]:


plt.pie(Importance[12:16],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Align financial skills and talent with changing business needs',color='orange',fontsize=12.5,fontweight='bold')
plt.show()


# In[206]:


plt.pie(AS[12:16],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Align financial skills and talent with changing business needs',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of objective/Issue')
plt.show()


# In[181]:


plt.pie(Importance[16:20],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Ensure security of finance data and systems',color='orange',fontsize=12.5,fontweight='bold')
plt.show()


# In[207]:


plt.pie(AS[16:20],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Ensure security of finance data and systems',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of Objective/Issue')
plt.show()


# In[182]:


plt.pie(Importance[20:24],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improve finance agility',color='orange',fontsize=12.5,fontweight='bold')
plt.show()


# In[208]:


plt.pie(AS[20:24],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improve finance agility',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of Objective/Issue')
plt.show()


# In[183]:


plt.pie(Importance[24:28],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Modernize finance application platforms',color='orange',fontsize=12.5,fontweight='bold')
plt.show()


# In[209]:


plt.pie(AS[24:28],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Modernize finance application platforms',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of objective/Issue')
plt.show()


# In[184]:


plt.pie(Importance[28:32],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improve finance analytical,modeling and reporting capabilities',color='orange',fontsize=12.5,fontweight='bold')
plt.show()


# In[210]:


plt.pie(AS[28:32],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improve finance analytical,modeling and reporting capabilities',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of Objective/Issue')
plt.show()


# In[185]:


plt.pie(Importance[32:36],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Increase Finance customer centricity',color='orange',fontsize=12.5,fontweight='bold')
plt.show()


# In[213]:


plt.pie(AS[32:36],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.5),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Increase Finance customer centricity',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of Objective/issue')
plt.show()


# In[187]:


plt.pie(Importance[36:40],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Redeploy Capacity created through operational efficiency',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Importance of issue/objective')
plt.show()


# In[215]:


plt.pie(AS[36:40],labels=['Very HIgh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.5),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Redeploy Capacity created through operational efficiency',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of issue/objective')
plt.show()


# In[188]:


plt.pie(Importance[40:44],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Develop better business partnerships with BU and functions',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Importance of issue/objective')
plt.show()


# In[216]:


plt.pie(AS[40:44],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Develop better business partnerships with BU and functions',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of issue/objective')
plt.show()


# In[189]:


plt.pie(Importance[44:48],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improve finance risk management capabilities',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Importance of issue/objective')
plt.show()


# In[218]:


plt.pie(AS[44:48],labels=['Very High','HIgh','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.5),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improve finance risk management capabilities',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of issue/objective')
plt.show()


# In[190]:


plt.pie(Importance[48:52],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Take advantage of new finance and technology',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Importance of issue/objective')
plt.show()


# In[219]:


plt.pie(AS[48:52],labels=['Very HIgh','HIgh','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.5),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Take advantage of new finance and technology',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of issue/objective')
plt.show()


# In[191]:


plt.pie(Importance[52:56],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improve integration of planning processes',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Importance of issue/objective')
plt.show()


# In[220]:


plt.pie(AS[52:56],labels=['Very HIgh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.5),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improve integration of planning processes',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of issue/objective')
plt.show()


# In[192]:


plt.pie(Importance[56:60],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improve compliance/internal controls',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Importance of issue/objective')
plt.show()


# In[221]:


plt.pie(AS[56:60],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.5),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improve compliance/internal controls',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of issue/objective')
plt.show()


# In[193]:


plt.pie(Importance[60:64],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Optimize tax structure',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Importance of issue/objective')
plt.show()


# In[222]:


plt.pie(AS[60:64],labels=['Very HIgh','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.5),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Optimize tax structure',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of issue/objective')
plt.show()


# In[194]:


plt.pie(Importance[64:68],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improving Work capital management',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Importance of issue/objective')
plt.show()


# In[223]:


plt.pie(AS[64:68],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.5),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Improving Work capital management',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of issue/objective')
plt.show()


# In[195]:


plt.pie(Importance[68:72],labels=['Critical','Major','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.2),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Evaluate opportunities to improve capital Allocation process',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Importance of issue/objective')
plt.show()


# In[224]:


plt.pie(AS[68:72],labels=['Very High','High','Moderate','Low'],autopct='%1.1f%%',explode=(0.1,0,0,0.5),colors=['red','green','orange','yellow'])
plt.axis('equal')
plt.title('Evaluate opportunities to improve capital Allocation process',color='orange',fontsize=12.5,fontweight='bold')
plt.xlabel('Ability of issue/objective')
plt.show()


# In[249]:


apply=[]
for i in ['Q7#3_19_1','Q7#3_20_1','Q7#3_21_1','Q7#3_22_1','Q7#3_23_1','Q7#3_24_1',
         'Q7#3_25_1','Q7#3_26_1','Q7#3_27_1','Q7#3_28_1','Q7#3_29_1','Q7#3_30_1',
         'Q7#3_31_1','Q7#3_32_1','Q7#3_33_1','Q7#3_34_1','Q7#3_35_1','Q7#3_36_1']:
    jj=H[i].str.count("Check all that apply")
    apply.append(jj.count())
apply


# In[272]:


S=pd.Series(apply)
S1=pd.Series((S/37)*100)
Check=pd.DataFrame([S,S1])
p=Check.T
from pylab import *
fig=plt.figure(figsize=(15,8))
subplot(1,2,1)
p[1].plot.bar()
plt.title('Percentage of Check that all Apply')
subplot(1,2,2)
p[0].plot.bar()
plt.title('Count of Check that all Apply')


# In[293]:


com=[]
com1=[]
com2=[]
com3=[]
for i in ['Decline more than 20%','Decline 16 to 20%','Decline 11 to 15%','Decline 7 to 10%',
          'Decline 4 to 6%','Decline 1 to 3%','No change','Increase 1 to 3%','Increase 4 to 6%',
          'Increase 7 to 10%','Increase 11 to 15%','Increase 16 to 20%','Increase more than 20%']:
    H['Q8#1_4']=H['Q8#1_4'].str.strip()
    H['Q8#1_5']=H['Q8#1_5'].str.strip()
    H['Q8#2_4']=H['Q8#2_4'].str.strip()
    H['Q8#2_5']=H['Q8#2_5'].str.strip()
    com.append(H.loc[H['Q8#1_4']==i,'Q8#1_4'].count())
    com1.append(H.loc[H['Q8#1_5']==i,'Q8#1_5'].count())
    com2.append(H.loc[H['Q8#2_4']==i,'Q8#2_4'].count())
    com3.append(H.loc[H['Q8#2_5']==i,'Q8#2_5'].count())
print(com,com1,com2,com3)


# In[304]:



plt.figure(figsize=(15,15))
plt.pie(com2,labels=['Decline more than 20%','Decline 16 to 20%','Decline 11 to 15%','Decline 7 to 10%',
          'Decline 4 to 6%','Decline 1 to 3%','No change','Increase 1 to 3%','Increase 4 to 6%',
          'Increase 7 to 10%','Increase 11 to 15%','Increase 16 to 20%','Increase more than 20%'],
       autopct='%1.1f%%')
plt.show()


# In[394]:


H['Q9_6'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('BUSINESS UNIT')


# In[395]:


H['Q9_7'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Centers of Excellence')

    


# 

# In[396]:


H['Q9_8'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Outsourced')


# In[398]:


H['Q9_9'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('OFFSHORED')
plt.show()


# In[399]:


H['Q9_10'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('SELF SERVICE')
plt.show()


# In[405]:


from pylab import *
fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Modernized Core Platform')
H['Q10#1_19'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_19'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[406]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Cloud Based Business Applications',color='green',fontsize=20)
H['Q10#1_20'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_20'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[408]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Robotic Process Automation',color='green',fontsize=20)
H['Q10#1_21'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_21'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[409]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Advanced Analytics',color='green',fontsize=20)
H['Q10#1_22'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_22'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[410]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Data Visualization Tools',color='green',fontsize=20)
H['Q10#1_23'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_23'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[411]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Master data Management Technologies',color='green',fontsize=20)
H['Q10#1_24'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_24'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[412]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Advanced data Architecture Technologies',color='green',fontsize=20)
H['Q10#1_25'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_25'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[413]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Mobile Computing',color='green',fontsize=20)
H['Q10#1_26'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_26'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[414]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Social Media/Collaboration',color='green',fontsize=20)
H['Q10#1_27'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_27'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[415]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Cognitive Computing / Artificial Intelligence',color='green',fontsize=20)
H['Q10#1_28'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_28'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[416]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Virtual assistants/chatbots',color='green',fontsize=20)
H['Q10#1_29'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_29'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[417]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Block Chain',color='green',fontsize=20)
H['Q10#1_30'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_30'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[421]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Internet of Things',color='green',fontsize=20)
H['Q10#1_31'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q10#2_31'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[427]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Performance Dashboards',color='green',fontsize=20)
H['Q11#1_118'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_118'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[428]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Self-service analytics and reporting',color='green',fontsize=20)
H['Q11#1_119'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_119'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[429]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Business Process management',color='green',fontsize=20)
H['Q11#1_120'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_120'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[430]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Automated Reconciliation Tools',color='green',fontsize=20)
H['Q11#1_121'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_121'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[431]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Financial Close Management',color='green',fontsize=20)
H['Q11#1_122'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_122'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[432]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Financial Compliance Management Automation',color='green',fontsize=20)
H['Q11#1_123'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_123'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[433]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('XBRL tagging Technology',color='green',fontsize=20)
H['Q11#1_124'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_124'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[434]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Automated Filing',color='green',fontsize=20)
H['Q11#1_125'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_125'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[435]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Electronic bill payment and presentment',color='green',fontsize=20)
H['Q11#1_126'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_126'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[436]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Supplier Self Service Portal',color='green',fontsize=20)
H['Q11#1_127'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_127'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[437]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Cash and liquidity management applications',color='green',fontsize=20)
H['Q11#1_128'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_128'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[443]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Tax Compliance',color='green',fontsize=20)
H['Q11#1_129'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_129'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[444]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Automated Audit',color='green',fontsize=20)
H['Q11#1_130'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Currently')
subplot(1,2,2)
H['Q11#2_130'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title(' 1-2 Years')
plt.show()


# In[447]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Attainment of Enterprise Objectives',color='green',fontsize=20)
H['Q12#1_62'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Impact')
subplot(1,2,2)
H['Q12#2_62'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected next 2-3 years')
plt.show()


# In[448]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('How finance services are delivered to Business',color='green',fontsize=20)
H['Q12#1_63'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Impact')
subplot(1,2,2)
H['Q12#2_63'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected next 2-3 years')
plt.show()


# In[449]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Finance Service Delivery Performance',color='green',fontsize=20)
H['Q12#1_63'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Impact')
subplot(1,2,2)
H['Q12#2_63'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected next 2-3 years')
plt.show()


# In[450]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Roles,Skills,Profiles and Needs of finance function',color='green',fontsize=20)
H['Q12#1_64'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Impact')
subplot(1,2,2)
H['Q12#2_64'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected next 2-3 years')
plt.show()


# In[452]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Our finance function has in place and executing a formal digital transformation Strategy',color='green',fontsize=20)
H['Q13#1_82'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Situation')
subplot(1,2,2)
H['Q13#2_82'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected next 2-3 years')
plt.show()


# In[453]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Our finance digital transformation Strategy is aligned with Enterprise DT strategy',color='green',fontsize=15)
H['Q13#1_83'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Situation')
subplot(1,2,2)
H['Q13#2_83'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected next 2-3 years')
plt.show()


# In[454]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Our finance function has resources and competencies in place to execute DT strategy',color='green',fontsize=20)
H['Q13#1_84'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Situation')
subplot(1,2,2)
H['Q13#2_84'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected next 2-3 years')
plt.show()


# In[455]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
plt.suptitle('Our IT organization supports finance digital transformation Strategy',color='green',fontsize=20)
H['Q13#1_85'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Situation')
subplot(1,2,2)
H['Q13#2_85'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected next 2-3 years')
plt.show()


# In[459]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q14_4'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,labels=['NA','Process','Finance','Analytics','Enterprise'])
plt.title('Setting of Finance data and analytics')
subplot(1,2,2)
H['Q14_5'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,labels=['NA','Process','Finance','Analytics','Enterprise'])
plt.title('Data Governance')
plt.show()


# In[460]:





# In[461]:


H['Q14_8'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,labels=['NA','Process','Finance','Analytics','Enterprise'])
plt.title('Development of advance analytics')
plt.show()


# In[464]:


H['Q15_9'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Expand end to end process ownership')
plt.show()


# In[465]:


H['Q15_10'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Develop and expand business Partnering roles')
plt.show()


# In[466]:


H['Q15_11'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Improve specialist skills in finance')
plt.show()


# In[467]:


H['Q15_12'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Improve finance business acumen')
plt.show()


# In[468]:


H['Q15_13'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Develop Finance Technology Roadmap')
plt.show()


# In[469]:


H['Q15_14'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Develop and implement finance KPI')
plt.show()


# In[470]:


H['Q15_15'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Improve finance data stewardship')
plt.show()


# In[471]:


H['Q15_16'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Extend Core finance application')
plt.show()


# In[472]:


H['Q15_17'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Re-engineer')
plt.show()


# In[473]:


H['Q15_18'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Transform the forecasting, budgeting and planning processes')
plt.show()


# In[477]:


H['Q16'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Planning to repatriate offshore cash')
plt.show()


# In[485]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q17#1_14'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
subplot(1,2,2)
H['Q17#2_14'].value_counts().plot.bar()
plt.show()


# In[486]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q17#1_15'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
subplot(1,2,2)
H['Q17#2_15'].value_counts().plot.bar()
plt.show()


# In[490]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q17#1_16'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.show()


# In[491]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q17#1_17'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
subplot(1,2,2)
H['Q17#2_17'].value_counts().plot.bar()
plt.show()


# In[492]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q17#1_18'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
subplot(1,2,2)
H['Q17#2_18'].value_counts().plot.bar()
plt.show()


# In[494]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q17#1_19'].value_counts().plot.bar()
subplot(1,2,2)
H['Q17#2_19'].value_counts().plot.bar()
plt.show()


# In[495]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q17#1_20'].value_counts().plot.bar()
subplot(1,2,2)
H['Q17#2_20'].value_counts().plot.bar()
plt.show()


# In[496]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q17#1_21'].value_counts().plot.bar()
subplot(1,2,2)
H['Q17#2_21'].value_counts().plot.bar()
plt.show()


# In[501]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q18'].value_counts().plot.bar()
subplot(1,2,2)
H['Q19_4'].value_counts().plot.pie(autopct='%1.1f%%')
plt.show()


# In[504]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q19_5'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0))
subplot(1,2,2)
H['Q19_6'].value_counts().plot.pie(autopct='%1.1f%%',explode=(0.1,0.05,0))
plt.show()


# In[508]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q20_12'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
subplot(1,2,2)
H['Q20_13'].value_counts().plot.pie(autopct='%1.1f%%')
plt.show()


# In[509]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q20_14'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
subplot(1,2,2)
H['Q20_15'].value_counts().plot.pie(autopct='%1.1f%%')
plt.show()


# In[510]:


H['Q20_16'].value_counts().plot.pie(autopct='%1.1f%%')
plt.show()


# In[514]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q21_4'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
subplot(1,2,2)
H['Q21_5'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
plt.show()


# In[515]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q21_6'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
subplot(1,2,2)
H['Q21_7'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
plt.show()


# In[516]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q21_8'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
subplot(1,2,2)
H['Q21_9'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
plt.show()


# In[517]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q21_10'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
subplot(1,2,2)
H['Q21_11'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
plt.show()


# In[518]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q21_12'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
subplot(1,2,2)
H['Q21_13'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
plt.show()


# In[520]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q21_14'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))


# In[524]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q22#1_86'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
subplot(1,2,2)
H['Q22#2_86'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.show()


# In[526]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q22#1_87'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
subplot(1,2,2)
H['Q22#2_87'].value_counts().plot.pie(autopct='%1.1f%%',colors=['yellow','blue','green'])
plt.show()


# In[528]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q22#1_88'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
subplot(1,2,2)
H['Q22#2_88'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.show()


# In[531]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q23#1_89'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
subplot(1,2,2)
H['Q23#2_89'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.show()


# In[532]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q23#1_90'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
subplot(1,2,2)
H['Q23#2_90'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.show()


# In[533]:


fig=plt.figure(figsize=(10,6))
subplot(1,2,1)
H['Q23#1_91'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,explode=(0.1,0.05,0,0))
subplot(1,2,2)
H['Q23#2_91'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.show()


# In[23]:


from pylab import *
fig=plt.figure(figsize=(10,6))
colors=['red','green','yellow','matt','orange']
subplot(1,2,1)
plt.suptitle('Supply Chain Risk',color='green',fontsize=20)
H['Q24#1_13'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_13'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[24]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Financial Crisis',color='green',fontsize=20)
H['Q24#1_14'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_14'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[25]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Regulatory Risk',color='green',fontsize=20)
H['Q24#1_15'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_15'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[26]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Geopolitical Risk',color='green',fontsize=20)
H['Q24#1_16'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_16'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[27]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Intensified Competition',color='green',fontsize=20)
H['Q24#1_17'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_17'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[28]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Disruptive Innovation',color='green',fontsize=20)
H['Q24#1_18'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_18'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[29]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Access to Critical Talent',color='green',fontsize=20)
H['Q24#1_19'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_19'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[30]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Regional Deman Weakness',color='green',fontsize=20)
H['Q24#1_20'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_20'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[31]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('IP Theft / Industrial Espoinage',color='green',fontsize=20)
H['Q24#1_21'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_21'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[32]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Cyber/Information Security',color='green',fontsize=20)
H['Q24#1_22'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_22'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[33]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Exchange rate Volatility',color='green',fontsize=20)
H['Q24#1_23'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_23'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[34]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Reputational Risk',color='green',fontsize=20)
H['Q24#1_24'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_24'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[35]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Global Trade Barriers',color='green',fontsize=20)
H['Q24#1_25'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Current Level of Risk')
subplot(1,2,2)
H['Q24#2_25'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change in risk over next 2 years')
plt.show()


# In[38]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange','red','grey','violet']
subplot(1,2,1)
plt.suptitle('Budgeted and Projected Revenue Growth',color='green',fontsize=20)
H['Q25_7'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Budgeted - 2019')
subplot(1,2,2)
H['Q25_9'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected -2019')
plt.show()


# In[39]:


fig=plt.figure(figsize=(10,6))
colors=['green','yellow','orange']
subplot(1,2,1)
plt.suptitle('Number of FTE',color='green',fontsize=20)
H['Q25_10'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Budgeted - 2018')
subplot(1,2,2)
H['Q25_11'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected change - 2018')
plt.show()


# In[40]:


H['Q25_8'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Projected Revenue Growth - 2018')
plt.show()


# In[69]:


H.iloc[:,269]


# In[42]:


H['Q27'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors)
plt.title('Levels in your Company')
plt.show()


# In[45]:


H['Q28'].value_counts().plot.pie(autopct='%1.1f%%',colors=colors,startangle=90)
plt.title('GBS/Shared Services')
plt.show()


# In[57]:


country=[]
for i in ['Q29_1','Q29_2','Q29_3','Q29_4','Q29_5','Q29_6','Q29_7']:
    ca=H[i].count()
    country.append(ca)
plt.pie(country,autopct='%1.1f%%',labels=['USA','NA','SA','Europe','East','Africa','Asia'])
plt.show()


# In[64]:


S=pd.Series(country,index=['USA','NA','SA','Europe','East','Africa','Asia'])
S.plot.barh()


# In[70]:


df


# In[ ]:




