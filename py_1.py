import math
myNameIs="Siam"
myname=["Pyton","Javascript","C++"];
for i in myNameIs:
    print("You are",i);

myTuple=(1,2,3,4,5)


def my():
    print("I am a student")
my();

def myFullName(FitsrName,lastName):
    print("My fullname",FitsrName+" "+lastName);
    
myFullName("Hasibul Hasan","Siam")

finding_absolue_number=-20
print("finding absolute-Number",abs(finding_absolue_number));

triangle_height = float(input("Enter the triangle height: "))
triangle_base = float(input("Enter the triangle base: "))


triangle_area = 0.5 * triangle_height * triangle_base
print("The area of the triangle:", triangle_area)


#Object Oriented Programming in python
class Friends:
    def __init__(self,firstName,lastName,age):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        print("My FullName",self.firstName+" "+self.lastName);

#make a oject
myName_is=Friends("Hasibul-Hasan","Siam",20);
print("My firstName",myName_is.firstName);
print("My LastName ",myName_is.lastName);
print("My age is",myName_is.age);

#make Abstraction about your hobby
class MyHobby:
    def __init__(self,MyFirst_hobby,MySecondHobby,MyThirdHobby):
        self.MyFirst_hobby=MyFirst_hobby;
        self.MySecondHobby=MySecondHobby;
        self.MyThirdHobby=MyThirdHobby;
        # print("My firsthobby",self.MyFirst_hobby)
        # print("My Secondhobby",self.MySecondHobby)
        # print("My ThirdHobby", self.MyThirdHobby)
#Make a Object
MyHobby_list=MyHobby("Painted","Garderning","Reading");
print("My firsthobby",MyHobby_list.MyFirst_hobby);
print("My Secondhobby",MyHobby_list.MySecondHobby);
print("My ThridHobby",MyHobby_list.MyThirdHobby);


#Polymorphism
class Animal:
    def __init__(self,name):
        self.name=name;
        print(self.name+" "+"Was adopted");
    
    
    def run(self):
        print("She is  running");
    class Turtle:
        def run(self):
            print("Running slowly")
    
    tim=Turtle();
    tim.run();
    
    class Calculator1:
        def addition(self, a, b):
            return a + b
        def subtraction(self, a, b):
            return a - b
        def multiplication(self, a, b):
            return a * b
        def division(self, a, b):
            return a / b
    
    class Calculation2(Calculator1):
        def sum(self,a,b):
            return a+b;
    
    # make a object
    inheritance__object=Calculation2();
    print("Addition=",inheritance__object.addition(10,20));
    print("Subtraction",inheritance__object.subtraction(100,50))
    print("Multiplication",inheritance__object.multiplication(10,20));
    print("Division",inheritance__object.division(100,2));
    print("Sum=",inheritance__object.sum(100,200))
    
#Calculate trangle area programme using  function in Python

#Make  a function
def CalculationTrangleArea(height,base):
    return 0.5*height*base;
print("Trangle_area",CalculationTrangleArea(100,20));

    
    
     

        