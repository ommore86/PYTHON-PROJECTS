class Student():
    # Class variable / Static variable
    stream = "CO"
    roll = 0
    # Constructor
    def __init__(self, name, eng, sci, maths):
        # Instance variable
        self.name = name
        self.roll = Student.roll+1
        Student.roll+=1
        self.eng = eng
        self.sci = sci
        self.maths = maths
        self.percent = 0

    # Function
    def details(self, address, mobile):
        self.address = address
        self.mobile = mobile
        print(self.roll)
        print(self.stream)
        print(self.name)
        print(self.address)
        print(self.mobile)

    def percentage(self):
        total = self.sci + self.eng + self.maths
        self.percent = total/300*100

    def result(self):
        print("Name: ", self.name)
        print("Percentage: ", self.percent)     

obj = Student("Om", 90, 92, 95)
obj.details("Kalyan", 8591319006)
obj.percentage()
obj.result()
print("".center(30, "-"))

obj1 = Student("Ajinkya", 74, 66, 76)
obj1.details("Thane", 9835389293)
obj1.percentage()
obj1.result()
print("".center(30, "-"))

obj2 = Student("Shruti", 89, 91, 92)
obj2.stream = "MBA"
obj2.details("Nashik", 8591319007)
obj2.percentage()
obj2.result()
print("".center(30, "-"))