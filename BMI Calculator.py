print("BMI CALCULATOR")
height=1.65
weight=80

BMI=weight/height ** 2

print(BMI)

print (int(BMI))

print(round(BMI))

print(round(BMI, 1))

if BMI > 25:
    print("overweight")
else:
    print("normal")