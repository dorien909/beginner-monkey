#function practice
#def function1():
#    print("ahhhh")
#    print("ahhhh 2")
#print("this is outside of the function")
#function1()
#function1()

#def function2(x):
#    return 2*x
#a = function2(3)
#print (a)


#def function3(x, y):
#    return x + y

#e = function3(1, 2)

#print(e)

name1 = "David"
height_m1 = 2
weight_kg1 = 90

name2 = "Scarlet"
height_m2 = .75
weight_kg2 = 12

name3 = "Dorian"
height_m3 = .50
weight_kg3 = 5


def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print ("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)
