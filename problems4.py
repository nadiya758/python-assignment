Hight=float(input("Enter my Hight in meters:"))
Weight=float(input("Enter my Weight in kg:"))
bmi=Weight/Hight**2
print("my bmi is") 

if bmi<18.5:
    print("under Weight")

elif bmi<=24.9:
    print("Normal")

elif bmi<=29.9:
    print("over wight")
else:
    print("obese")

