from time import time 
t = time() 
lista = [1,2,3,4,5,6,7,8,9,10] 
listb =[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.01] 
len1=len(lista) 
len2=len(listb) 
for i in xrange (1000000): 
    x = [a+b for a in lista for b in listb]
print "total run time:"
print time()-t