#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Question1 

with open("example.txt", "r+") as a_file:
    for line in a_file:
        if 'placement' in line:
            line = line.replace('placement', 'screening')
print(line)


# In[10]:


#Abstraction 

from abc import ABC , abstractmethod

class Bank(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name
   
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @abstractmethod
    def get_returns(self):
        pass
    
class PremiumAccHondler(Bank):
    def __init__(self, first_name, last_name, Acc_bal, Tenure):
        super().__init__(first_name, last_name)
        self.Tenure = Tenure
        self.Acc_bal = Acc_bal 
        
    def get_returns(self):
        return self.Acc_bal * 0.05 * self.Tenure /100 + self.Acc_bal
    
class ZeroBalAccHolder(Bank):
    def __init__(self, first_name, last_name, Acc_bal):
        super().__init__(first_name, last_name)
        self.Acc_bal = Acc_bal
    
    def get_returns(self):
        return self.Acc_bal
    
class Calculation:
    
    def __init__(self):
        self.customer_list = []
        
    def add(self, customer):
        self.customer_list.append(customer)
        
    def print(self):
        for e in self.customer_list:
            print(f"{e.full_name} \t ${e.get_returns()}")

calculation = Calculation()

calculation.add(PremiumAccHondler("Jack", "Sparrow",5000,5))
calculation.add(ZeroBalAccHolder("William", "Jhon",5000))
calculation.add(PremiumAccHondler("Steve", "Strange",5000,5))
calculation.add(ZeroBalAccHolder("William", "Jack",5000))

calculation.print()


# In[12]:


#Multiple In heritance 

class Add:
    def __init__(self, a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    
    def add(self):
        return self.a+self.b+self.c
    
class Sub: 
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c = c
        
    def sub(self):
        return self.a-self.b-self.c
    
class Mul:
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    
        
    def mul(self):
        return self.a*self.b*self.c

class Div:
    def __init__(self, a,b,c):
        self.a = a 
        self.b = b
        self.c = c
    
    def div(self):
        return self.a/self.b
        
class Calculator(Add, Sub, Mul, Div):
    def __init__(self, *args):
        Add.__init__(self, *args)
        Sub.__init__(self, *args)
        Mul.__init__(self, *args)
        Div.__init__(self, *args)
        
n = Calculator(4,5,6)
print(n.add())
print(n.div())
print(n.sub())
print(n.mul())        


# In[21]:


def div(a,b):
    print(a/b)
    
def smart_div(func):
    
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    
    return inner
 
print("Out put which we dont want " + str(div(4,5)))

div1= smart_div(div)

print("Out put which we dont want " + str(div1(5,6)))


# In[ ]:




