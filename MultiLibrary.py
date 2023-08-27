class MultipleFunctions():
   
    def OddEven():
        num1=int(input("Enter the number: "))
        if(num1%2==1):
            print(num1," is odd number")
        else:
            print(num1," is Even number")
    def eligible():
        gen=input("Enter the Gender: ")
        age=int(input("Enter the Age: "))
        if((gen=="Male") and (age>=21)):
            print("Eligible")
        elif((gen=="Female") and (age>=18)):
            print("Eligible")
        else:
            print("Not eligible")
    def Subfields():
        print("Subfields in AI are: ")
        print("Machine learning")
        print("Neural networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural language processing")
    def percentage():
        Subject1=98
        Subject2=87
        Subject3=95
        Subject4=95
        Subject5=93
        print("Subject1= ",Subject1)
        print("Subject2= ",Subject2)
        print("Subject3= ",Subject3)
        print("Subject4= ",Subject4)
        print("Subject5= ",Subject5)
        Total= Subject1 +  Subject2 +  Subject3 +  Subject4 +  Subject5
        print("Total= ",Total)
        Percentage= Total / 5
        print("Percentage= ",Percentage)
    def Triangle():
        base=34
        height=32
        print("Height: ",height)
        print("Base: ",base)
        Area=1/2 * base * height
        print("Area of Triangle: ",Area)
        height1=2
        height2=4
        base1=4
        Peri=height1 + height2 + base1
        print("Perimeter of Triangle: ",Peri)    
    def Agecategory():
        age=int(input("Enter the age: "))
        if(age<18):
            print("children")   
        elif(age<35):
            print("Adult")            
        elif(age<50):
            print("Citizen")            
        else:
            print("Senior Citizen")
    def BMI():
        bmi=int(input("Enter the BMI index:"))
        if(bmi<18):
            print("Under Weight")
        elif(bmi<25):
            print("Normal Weight")
        elif(bmi<=30):
            print("Over Weight")
        else:
            print("Very Overweight")
    
        
       