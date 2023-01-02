#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# DONT FORGET TO ADD COMMENTS


# In[65]:


#pat1 batch2
inp=int(input())
#initializing variables
AmstrongCount=0
NonAmstrongCount=0
#getting input till -1 encounter
while inp!=-1:
    sum=0
    num=inp
    #sum of (num to the power of no.of digits)
    while num>0:
        a=num%10
        sum+=a**len(str(inp))
        num=num//10
    #checking armstrong or not
    if inp==sum:
        AmstrongCount+=1
    else:
        NonAmstrongCount+=1
    inp=int(input())
print('AmstrongCount is',AmstrongCount)
print('NonAmstrongCount is',NonAmstrongCount)


# In[69]:


#pat1 batch1
inp=int(input())
PrimeCount=0
CompositeCount=0
while inp!=-1:
    #checking if the number is div by any num before it
    for i in range(2,inp):
        if inp%i==0:
            cc=1
            break
    if cc==1:
        CompositeCount+=1
    else:
        PrimeCount+=1
    inp=int(input())
print('primecount is',PrimeCount)
print('compositecount is',CompositeCount)


# In[75]:


#list ips batch1
lis=[]
for i in range(4):
    num=int(input())
    lis.append(num)
#removing first largest element
for i in range(lis.count(max(lis))):
    lis.remove(max(lis)) 
print(max(lis))


# In[76]:


#list ips2
num=int(input())
lis=[]
#iteration from 1 to input num
for i in range(1,num+1):
    n=i
    while True:
        s=0
        # sum of sq of nos
        while n>0:
            b=n%10
            n=n//10
            s+=b**2
        if s>10 or s==10:
            n=s
            continue
        else:
            break
    # if num is happy num then append
    if s==1:
        lis.append(i)
            
print(lis)


# In[11]:


#IPS for functions and default values
def bill(hour,mins):
    cost=0
    # if hours is in multiple of 5 cost is 200 per 5hr
    if hour%5==0:
        cost= 200*(hour//5)+mins
    # if not multiple of 5,reduce the num to multiple of 5 and add cost
    else:
        hr5=hour//5
        hr1=hour%5
        cost= 200*hr5 + 50*hr1 +mins
    return cost
hr=int(input())
mins=int(input())
print(bill(hr,mins))


# In[14]:


#IPS for functions
def first_last6(lis):
    if len(lis)>=1:
        # if first and last num is 6 means true
        if lis[0]==6 or lis[-1]==6:
            return True
        else:
            return False
list1=[]
# input num till blank space or non int
while True:
    try:
        inp=int(input())
        list1.append(inp)
    except:
        break
first_last6(list1)


# In[17]:


#IPS for Dictionary
n=int(input())
dict1={}
#getting every input as str and hence search for a value as str too
for i in range(n):
    key=input()
    value=input()
    dict1[key]=value
search=input()
srchcount=0
# checking if given key is present or not
for i in dict1:
    if search==i:
        print('Key existing')
        srchcount=1
if srchcount!=1:
    print('Key not existing')


# In[18]:


#PAT2-Class1
dict1={}
# getting 15 inputs
for i in range(15):
    key=input()
    value=int(input())
    dict1[key]=value
search=input()
# if search val is there, then find no.of states and states with similar district count
for i in dict1:
    if i==search:
        print(dict1[search])
        count=0
        lis=[]
        temp={}
        for j in dict1:
            if dict1[search]==dict1[j]:
                count+=1
                lis.append(j)
        temp[dict1[search]]=lis
print(count)
print(temp)


# In[77]:


#PAT2-Class2
list1=[]
# get input till non int
while True:
    try:
        inp=int(input())
        list1.append(inp)
    except:
        break
# if even num in even pos then replace num with word even and similarly for odd
for i in range(len(list1)):
    if (i+1)%2==0 and list1[i]%2==0:
        list1[i]='even'
    elif (i+1)%2!=0 and list1[i]%2!=0:
        list1[i]='odd'
print(list1)
print('odd=',list1.count('odd'))
oddpositionlist=[]
evenpositionlist=[]
# position of odd or even words
for i in range(len(list1)):
    if list1[i]=='odd':
        oddpositionlist.append(i)
    elif list1[i]=='even':
        evenpositionlist.append(i)
print('oddpositionlist=',oddpositionlist)
print('even=',list1.count('even'))
print('evenpositionlist=',evenpositionlist)


# In[23]:


#IPS for Strings
string=input()
print(len(string))
# if rev of string is same as input then its palindrome
if string[::-1]==string:
    print('palindrome')
else:
    print('not palindrome')


# In[33]:


#PAT3-Class2
'''print(ord('e'))
print(chr(101))'''
inp=input()
rot=int(input())
def rotate_word(word,rot):
    # making all letters to similar case
    temp=word.upper()
    newstr=''
    # rotating word wrt given number and subtract 26 if ascii value gets more than 90 (captial Z)
    for i in temp:
        asci=ord(i)+rot
        if asci>90:
            asci=asci-26
        newstr+=chr(asci)
    newstr=[i for i in newstr]
    word=[i for i in word]
    # changing case similar to input 
    for i in range(len(word)):
        if word[i].isupper():
            newstr[i]=newstr[i].upper()
        else:
            newstr[i]=newstr[i].lower()
    
    newstr=''.join(newstr)
    return newstr
output=rotate_word(inp,rot)
print(output)
vowel='AEIOUaeiou'
# if first and last chr is a vowel
if output[0] in vowel and output[-1] in vowel:
    print('Happy Cool String')
else:
    print('Happy Hot String')


# In[41]:


import re
# pattern condition for correct date format
pattern=re.compile('^[0-9]+\-+(JAN|FEB|MAR|APR|MAY|JUN|JLY|AUG|SEP|OCT|NOV|DEC)+\-+[0-9]{2}$')
date=input()
if re.search(pattern,date):
    print('Correct Format')
# if not in correct format
else:
    new=''
    dict1={1:'JAN',2:'FEB',3:'MAR',4:'APR',5:'MAY',6:'JUN',7:'JLY',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DEC'}
    #rearranging to crt format 
    new+=date[6:]+'-'+ dict1[int(date[3:5])]+'-'+date[0:2]
    print(new)
    print('Format Corrected')


# In[45]:


#IPS for Strings Regular Expression
import re
name=input()
# splitting if space occurs
name=re.split('\s',name)
newname=''
# replacing everyhting except last name to abbreviation
for i in range(len(name)-1):
        newname+=name[i][0]+'.'
newname+=name[-1]
print(newname)


# In[57]:


#IPS for String Regular Expression
import re
# if 2 cap or 2 lower case chrs are together condition
pattern=re.compile('([A-Z]{2}|[a-z]{2})')
str1=input()
str2=input()
str3=''
# mixmatching string1 and rev of string2 also considering if they differ in size
try:
    if len(str1)>len(str2):
        for i in range(len(str1)):str3+=str1[i]+str2[-i-1]
    else:
        for i in range(len(str2)):str3+=str1[i]+str2[-i-1]
except:
    if len(str1)>len(str2):
        str3+=str1[-1]
    else:
        str3+=str2[0]
if re.search(pattern,str3):
    print('Does Not Follow Any Pattern')
else:
    print('Follows Pattern')


# In[78]:


#Practice Question for PAT1
Four_Divisible_Count=0
Four_Not_Divisible_Count=0
#get input till -1 is encountered
while True:
    num=int(input())
    if num==-1:
        break
    else:
        #check if div by 4
        if num%4==0:
            Four_Divisible_Count+=1
        else:
            Four_Not_Divisible_Count+=1
print('Four_Divisible_Count is',Four_Divisible_Count)
print('Four_Not_Divisible_Count',Four_Not_Divisible_Count)

