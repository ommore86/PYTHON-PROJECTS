name, std, div = input("Enter Name, Std, Div: ").split(',')
eng = int(input("Enter marks for English: "))
sci = int(input("Enter marks for Science: "))
maths = int(input("Enter marks for Maths: "))

print("Result".center(40,'-'))
print("Name: {}\tStd: {}\tDiv: {}".format(name,std,div))
print("-"*40)

print("English: ",eng)
print("Science: ",sci)
print("Maths: ",maths)
print("-"*40)

total = eng+sci+maths
per = total/300*100
print("Total: ",total,end="\t")
print("Percentage: ",round(per,2),"%")