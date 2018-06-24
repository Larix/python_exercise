# -*- coding: utf-8 -*-
l1=[1,5,7,9,10]
l2=[]

l2=[l*2 for l in l1]

#等同於
'''
for l in l1:
   l2.append(l*2)
'''
l2=[l for l in l1 if l%2==0]

#等同於
'''
for l in l1:
   if l%3==0:
      l2.append(l)
'''

a=[1,2,3]
b=[4,8,9]

z=[]

z=[(a_value, b_value) for a_value in a for b_value in b]

#等同於
'''
for a_value in a:
   for b_value in b:
      z.append((a_value, b_value))
'''

#list application in dictionary
n={}

m = [(1,3),(2,5),(3,6)]
n = {x:y for x,y in m}

#等同於
'''
for x,y in m:
   n.update({x:y})
'''