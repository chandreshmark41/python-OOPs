
# coding: utf-8

# # Object and Class

# Class is a blue print of all objects of same type.<br>
# An object will have variables and behavior(methods).<br>
# I have mentioned two basic definition of class and objects but if we go deeper in the discussion of class and object we will find that the object has exist in real world but class doesn't.<br>
# For example we have created a class of Student in which students of entire world are in the form of object.<br>
# It means you are also an object of this class.<br>
# But wait does the class name Student have any real existance.<br>
# The answer is no<br>
# Student is just a name not an object.<br>
# But if i say john and david which are the object of class Student have real existance as student.<br>
# So class is the just a blueprint and object is the real entity of this class.
# 

# # Code for understanding class and object

# In[3]:


class Computer:                          #defining class
    def config(self):                    #method
        print("i5,16gb,1tb")
com1 = Computer()                        #object creation
Computer.config(com1)                    #object as an argument
com1.config()                            #object itself calling method


# # __init__ method for creating variables

# In[17]:


class Computers:
    def __init__(self,cpu,ram,rom):
        self.cpu = cpu #self is used for the respective object and a,b,c are the variables
        self.ram = ram #self.variable=variable assign value for the variable respective to it's object
        self.rom = rom # you can make any number of variables for a object using __init__ method
    def show(self):#self argument is used for object 
        print(self.cpu,self.ram,self.rom)
com1 = Computers("i5","4GB","1TB")#giving values of cpu,ram,rom to the com1 computer
com2 = Computers("i5","8GB","1TB")#giving values of cpu,ram,rom to the com2 computer
com3 = Computers("i7","8GB","2TB")#giving values of cpu,ram,rom to the com3 computer
com4 = Computers("i7","12GB","4TB")#giving values of cpu,ram,rom to the com4 computer
com1.show()#calling show method using com1 object 
com2.show()
com3.show()
com4.show()


# # Objects are stored in Heap memory

# In[18]:


print(id(com1))
print(id(com2))
print(id(com3))
print(id(com4))


# # Size of an object

# the size of an object depends on the number of variables it has.<br>
# The larger number of variables the object has then the size will be get larger<br>

# # Self and other argument inside a function

# usually we use self argument inside a method which is used for the calling object to the method.<br>
# But we when use two argument inside a method then the second one will be called other.<br>
# The example is given below about this concept.<br>
# 

# In[3]:


class Person:
    def __init__(self,age):
        self.age=age
    def compare(self,other): #self is calling
        if self.age == other.age:
            print("Age is same")
        else:
            print("Age is different")
p1 = Person(18)
p2 = Person(18)
p1.compare(p2)                # c1 is calling at the place of self and c2 is at the place of other


# # *args And **kwargs

# *args used when we require to pass tuple as  argument inside a method.

# In[23]:


class A:
    def __init__(self,*args):
        self.args=args
        pass
a1 = A(10,20,30,40)
print(a1.args)


# **kwrgs used when we require to pass dictionary or key value pair as argument inside method

# In[25]:


class A:
    def __init__(self,**kwargs):
        self.kwargs=kwargs
        pass
b1 = A(name="chandresh",year="final")
print(b1.kwargs)


# # Types of variables in Python

# There are two types of variables <br>
# 1- Instance variable (object level)<br>
# 2- static variable (class level)<br>
# 
# *note- Namespace is an area where you create and store object/variables.<br>
# there are two type namespace class namespace and object namespace*<br>
# 
# If you we change class variable then it will be get changed for all instances of a class.<br>

# In[4]:


class car:
    wheels = 4 #class variable
    def __init__(self):
        self.name = "BMW" #object variable
        self.price = "1M" #object variable
car.wheels=6
car1 = car()
car1.wheels


# # Types of Methods in Python

# Basically there are 3 types of methods in python<br>
# 1- instance method # no use of decorator<br>
# 2- class method #use decorator @classmethod<br>
# 3- static method #use decorator @staticmethod<br>

# In[ ]:


#Instance method
#when object argument passed an argument
def get(self):#accessors
    return self.m1
def set(self,value):         #mutators
    self.m1=value
    
#Class method
@classmethod                  #decorator must be used before declaring class method
    def info(cls):            #pass cls as argument for a method
        return cls.school
    print(Student.info())
    
#static method
@staticmethod                       # decorator must be used before declaring static method
    def info():                     # the argument field is emply
        print("This is static method")


# # Inner class in python

# Inner class method used in python when a class take place inside a outer class.<br>
# This is useful when a object of outer class obtain attributes of inner class.<br>
# This is concept is little tricky but as practice it became easy to understand the working of inner class concept.<br>
# 

# In[22]:


class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()                   #creating object lap insdie the outer class
    
        
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()                         #calling show method for lap with respect to student
        
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'I5'
            self.ram = '8GB'

        def show(self):
            print(self.brand, self.cpu, self.ram)
        
s1 = Student('Navin',2)
s2 = Student('Jenny',3)
s1.show()


# # Inheritance

# In real life everything is based on inheritance.Because every human inherit something from its parent or ancestors.<br>
# For example you have inherited DNA,blood group etc from your parents,Our civilization inherited vast knowledge from our ancestors.<br>
# So basically when a class use the features or methods of another class in programming world it's called inheritance.<br>
# We will see the types of inheritance in the following code:-<br>

# In[27]:


#basic example of inheritance

class A:
    def feature1(self):
        print("This is feature 1")
class B:
    def feature2(self):
        print("This is feature 2")
c1=B()
c1.feature1                   #c1 object cannot access method feature 1 it will show error


# In[26]:


#basic example of inheritance

class A:
    def feature1(self):
        print("This is feature 1")
class B(A):                        #This is the way of inheriting a class into another class
    def feature2(self):
        print("This is feature 2")
c1=B()                             # c1 object created of class B
c1.feature1()                      #Now c1 can access the method of class A


# # Multi level inheritance

# In[28]:


# example of multilevel Inheritance
class A:
    def feature1(self):
        print("This is feature 1")
class B(A):        #This is the way of inheriting a class into another class
    def feature2(self):
        print("This is feature 2")
class C(B):       # when parent child relationship goes upto grandparent then it will be multi level inheritance
    def feature3(self):
        print("This is feature 3")
        
c1 = C()            #c1 object created of class C
c1.feature2()
c1.feature1()
                     #This can access the methods of both class B and class A
    


# # Multiple Inheritance

# In[29]:


#code for multiple inheritance
class A:
    def feature1(self):
        print("This is feature 1")
class B:
    def feature2(self):
        print("This is feature 2")
class C(A,B):# It will inherit both class A and B
    def feature3(self):
        print("This is feature 3")
        
c1 = C()                #c1 object created of class C
c1.feature2()
c1.feature1()
                       #This can access the methods of both class B and class A


# Note:- There are many types of inheritance based on type inheriting features.

# # Constructor in Inheritance

# Every class can have it own init method(Constructor) but a class will prefer to its own init method if it has.<br>
# Otherwise it will prefer to have it's parent class init method in the method resolution order(MRO).We will discuss later about MRO.<br>
# Note:- If both parent and child classes have it's own init method and we also want to access the init method of parent class then user "super()" for accessing init method of parent class<br>
# Understand this concept in the following code:-<br>
# 

# In[30]:


class A:
    def __init__(self):
        print("init method of class A")
class B(A):
    pass
a1 = B()# at the time of object creation init method will be automatically called


# In the above example class B don't have it's own init method then it's calling init method of it's parent class A

# In[31]:


class A:
    def __init__(self):
        print("init method of class A")
class B(A):
    def __init__(self):
        print("init method of class B")
a1 = B()                 # at the time of object creation init method will called automatically


# In the above example class B and class A both have init method but it's calling its own.

# # Super()

# When we want to access init method of both parent and child then for accessing init method of parent super() is used

# In[33]:


class A:
    def __init__(self):
        print("init method of class A")
class B(A):
    def __init__(self):
        super().__init__()
        print("init method of class B")
a1 = B()                # at the time of object creation init method will called automatically


# I hope you will be able to understand the concept.it's very simple actually<br>
# 1-if you have own init then use it <br>
# 2- otherwise use init method of your parent<br>
# 3- If both have its own init method then it will also use init method of itself but if you want to access init method of parent class then use "super()".<br>
# 
# Problem:- If a class have two parent class. It means it's a multiple inheritance scenario.Of which class init method will be called if child class don't its own.<br>
# Answer:- You are good question(It's a Dialogue of pappi from tanu wends manu return for making you laugh during studying about oops concepts hope you will get refreshed)<br>
# So basically the answer is MRO (Method Resolution Order)<br>
# let's see what it is.<br>

# # Method Resolution Order Same as Method Overriding

# If a class have two parent and want to access a method and both class have the same method then child class will prefer the parent which is left side in order.<br>
# for example there are 3 classes A B and C
# And C is child class and A and B both are parent class of C <br>
# C(A,B) # C inheriting A and B the A is in the left position then C will prefer to access method of A if the same method exist in both parent class.<br>
# I can understand it's little tricky.<br>
# let's understand it with help of code<br>

# In[37]:


class A:
    def show(self):
        print("Show method of class A")
class B:
    def show(self):
        print("Show method of class B")
class C(A,B):
    pass
c1 = C()
c1.show()


# I think you got it.In the above example both classes A and B have the same method show but when we call show method with object c1 of class C(class don't have method show) then it will call show method of A instead of B because A is in the left most position and MRO says that the order will be left to right of calling methods from the parent class.

# In[38]:


class A:
    def show(self):
        print("Show method of class A")
class B:
    def show(self):
        print("Show method of class B")
class C(A,B):
    def show(self):
        print("Show method of class C")
c1 = C()
c1.show()


# Now in the above line Class C has it's own show method then it will call its own
# 

# In[41]:


class A:
    def show(self):
        print("Show method of class A")
class B:
    def show(self):
        print("Show method of class B")
class C(A,B):
    def show(self):
        super().show()
        print("Show method of class C")
c1 = C()
c1.show()


# now we have used super() then it will show method of parent but this time also the left one.<br>
# I think it's enough to make you understand how the MRO concept work.<br>
# If we replace show() method with any kind method then also the concept remain same.<br>
# for example if replace show() with init method then complete order will be same.<br>
# first priority self and look for parents. If there are more than one parent then the order will be left to right.<br>
# Real life example:- Assume you are class and you don't have money so have to go to your parents for money.And both are offernig same amoung of money for you then which from which parent you will like to get money.<br>
# The logical answer is you check which one of parent is near to you.If your daddy is outside home and mother is at home then you will go to your mother.If both are outside home and there is not online payment transfer mode available then you will figure out which one of your parent is near to you.<br>
# Same concept is MRO. Both class A and B offering same service in form of show() method then the child class C will figure out which one is closer to it.<br>
# According the MRO rule left parent is closer to child that's why it will go for class A.<br>
# I think i have explained more than enough to make it clear.<br>

# # Polymorphism

# poly means many<br>
# morph means forms<br>
# when a single thing can have more than one form then they will be called polymorphic and this concept is called polymorphism.<br>
# Basically polymorphism can be explained in 4 parts<br>
# 1-Duck typing<br>
# 2-Operator overloading<br>
# 3-Method overloading<br>
# 4-Method overriding<br>

# # Duck Typing

# Let us write some piece of code and we will understand it with the help of code

# In[42]:


class Pycharm:
    def execute(self):
        print("compile the code")
class Myeditor:
    def execute(self):
        print("spell check")
        print("compile the code")
class Laptop:
    def code(self,ide):
        ide.execute()
lap1 = Laptop()
ide = Myeditor()                #object ide is created in class Myeditor
lap1.code(ide)                  #it will execute Myeditor execute() method


# The concept of duck typing a little confusing when you are seeing it at the first time.<br>
# But don't worry we will understand it with an easy real life example.<br>
# let see another code realted to duck typing concept<br>

# In[43]:


class Pycharm:
    def execute(self):
        print("compile the code")
class Myeditor:
    def execute(self):
        print("spell check")
        print("compile the code")
class Laptop:
    def code(self,ide):
        ide.execute()
lap1 = Laptop()           #object created of laptop class
ide = Pycharm()           # object ide is created in class Pycharm
lap1.code(ide)            #it will execute Pycharm execute() method


# So you have seen both the code and must have seen the difference between the output of the code.<br>
# Let me explain it:-<br>
# we have three classes Pycharm,Myeditor and Laptop.<br>
# Pycharm has an execute method which print "compile the code" and take one argument self(used for class object).<br>
# Myeditor has an exucute method which print "spell check" and "compile the code" and take one argument self(used for class object).<br>
# Laptop has a code method which take two argument self and ide.<br>
# self for object and ide to pass in the method.<br>
# lap1 object created of class Laptop.<br>
# ide object created two different time first in class Myeditor and second in class Pycharm.<br>
# Here the Tricky part starts<br><br>
# case1:- when ide created in class Myeditor<br>
# def code(self,ide)<br>
#     ide.execute()<br>
# the execute method of class Myeditor is called because ide is object of Myeditor class.<br>
# <br>
# case2:- When ide created in class Pycharm<br>
# def code(self,ide)<br>
#     ide.execute()<br>
# the execute method of class Pycharm is called because ide is object of Pycharm class.<br>
# This is duck typing concept here ide has different forms according to the situation.<br>
# 
# 
# 
# 
# 

# # Operator Overloading

# Operators are symbols Like(+,-,*,/,%,etc) which have predefined methods to perform a operation between operands.<br>
# for example a + b here a and b are operands and + symbol is operator.<br>
# I know this very basic thing and you thought just now why this man is starting from the basic.<br>
# So the reason is this i want tell you the behind the scene what happens when we use operator and operands.<br>
# In python everything is object.<br>
# for example x=5 is object an class int<br>
# and x = 'a' is an object of class str<br>
# lets confirm it from python.<br>

# In[45]:


x = 5 
print(type(x))


# In[46]:


x = 'a'
print(type(x))


# So we use + operator with objects of int class it just add two number<br>
# but we use + operator with objects of str class it just concatinate two strings<br> 

# In[47]:


5 + 7


# In[48]:


'Jai' + 'Hind'


# How this is all is happing,there are predefined methods who are doing this for us.<br>
# lets talk about the predefined methods<br>

# In[50]:


a=5
b=7
print(a+b)
print(int.__add__(a,b))


# you are seeing that both output are same.<br>
# it means when we are using + operator it is calling int.__add__(a,b)<br>
# because for int class __add__(a,b) is predefined<br>
# similarly for str class __add__(a,b) is predefined<br>

# # Need of operator overloading

# I think you understood why + operator can perform addition for int and concatination for str.<br>
# The answer is because methods for these operators are predefined.<br>
# But lets assume you created a class Student and objects s1,s2 of class Student.<br>
# Question:- Can you use + operator between s1 and s2 <br>
# Answer:- No,because there is no predefined method of + operator for class Student.<br>
# But we want to use the + operator then how can we use it for objects of Student class.<br>
# So here we will define method for + operator and then we will be able use + operator for class Student.<br>

# In[12]:


class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        return self.m1+self.m2+other.m1+other.m2
        
s1 = Student(10,20)
s2 = Student(10,20)
s3 = s1 + s2     #Student.__add__(s1,s2)
print(s3)


# in the following we have created a __add__() method for Student class objects.<br>
# s3 = s1 + s2 is similar as Student.__add__(s1,s2) <br>
# which we have seen in int.__add__(a,b) or int.__add__(self,other)<br>
# Now lets take a little complex example<br>

# In[68]:


class Student:
    def __init__(self,m1,m2,m3,m4,m5):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
    def __add__(self,other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        m3 = self.m3+other.m3
        m4 = self.m4+other.m4
        m5 = self.m5+other.m5
        s3 = Student(m1,m2,m3,m4,m5)# marks of s3 of each subject will be addition of self and other marks,
                                    #which are operands of + operator
        
        return s3
s1 = Student(60,70,80,70,70)
s2 = Student(80,70,60,70,70)
s3 = s1+s2
print(s3.m1)
print(s3.m2)
print(s3.m3)
print(s3.m4)
print(s3.m5)


# In the the above example the concept is same but we have 5 variable m1 to m5 and student s3 have addition of both s1 and s2 in each subject.<br>
# so when print s3.m1 then it is addition of m1 of s1 and m1 of s2.<br>
# We can change many methods like __sub__(),__mul__(),__gt__() etc<br>

# # Method Overloading

# it's trap guys.Technically Python doesn't have method overloading feature but wait when we don't have proper infrastructure or resources, In india we use "jugad".I hope you have heard about this word.
# But let's talk method overloading concept.
# If we declare any method which takes n number of argument and at the time of calling that method we pass less than the number of argument we have declared for the method is called method overloading.
# Lets see code to get idea about it

# In[2]:


class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a,b,c):
        s=a+b+c
        return s
s1=Student(70,80)
print(s1.sum(10,20,30))


# In the above example you can see method sum() has four arguments self,a,b and c .self is used for object so basically there are 3 argument to pass.And we have passed three arguments when we are calling sum(10,20,30).<br>
# The answer is 60.<br>
# No error found because we have passed 3 argument which was declared in the method definition.<br>
# Lets see another piece of code when we pass less than three argument.<br>

# In[3]:


class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a,b,c):
        s=a+b+c
        return s
s1=Student(70,80)            #only two arguments passed instead of 3.
print(s1.sum(10,20))        #calling sum method.


# So i think you got it.I was talking about this error from the begining of this topic method topic.<br>
# In the above lines of code we have passed only 2 arguments and in the method definition we have declared 3 argument to pass.<br>
# Then how we can achieve the functionality of method overloading in python,what is the "Jugad".<br>
# So let me explain about it in the following code.<br>

# In[11]:


class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        elif a!=None:
            s=a
        else:
            s=0
        return s
s1=Student(70,80)            #only two arguments passed instead of 3.
print(s1.sum(10,20))        #calling sum method.


# So you have seen that we passed two arguments and it's returning the value of s without any problem or error.<br>
# So this is the trick to achieve method overloading feature in python.<br>

# Note:- We have discussed method overriding in the method resolution order.Method overriding is simple concept nothing fancy 
# just see MRO part.

# # Composition

# When a class outsource some task for another class then it's called compostion.<br>
# You will get clear idea with the help  of code.<br>
# so see the follwing code:-<br>

# In[36]:


class Fee:
    def __init__(self,tution,mess):
        self.tution=tution
        self.mess=mess
    def totalfee(self):
        return self.tution+self.mess
class Student:
    def __init__(self,name,year,branch,tution,mess): #you have to pass all arguments
        self.name=name
        self.year=year
        self.branch=branch
        self.feeobject=Fee(tution,mess) #here self.feeobject is a object of Fee class
    def annualfee(self):
        return self.feeobject.totalfee()
s1 = Student("chandresh",4,"it",65000,25000)
s1.annualfee()
    


# In the above line of code we have seen that class Student contain Fee class, So the class Student is container here.<br>
# And we have create self.feeobject inside the Student class because if we delete instance of Student then instance of Fee class will be automatically deleted.<br>
# So here you can see class Student using class Fee for a particular task this is called composition.

# # Aggregation

# In[38]:


class Fee:
    def __init__(self,tution,mess):
        self.tution=tution
        self.mess=mess
    def totalfee(self):
        return self.tution+self.mess
class Student:
    def __init__(self,name,year,branch,fee): #you have to pass all arguments
        self.name=name
        self.year=year
        self.branch=branch
        self.fee=fee#here self.feeobject is a object of Fee class 
    def annualfee(self):
        return self.fee.totalfee()
fee=Fee(65000,25000)
s1 = Student("chandresh",4,"it",fee)
s1.annualfee()
    

