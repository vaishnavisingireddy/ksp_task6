# To print a statement or number 
number1 = 5
name = "Renu"
char = 'v'
f = 90.65
k = True
print(number1)
print(name)
print(char)
print(f)
print(k)

""" We use three double quotes for
 multi line comments """
# Hash is used for single comments

#To find the datatype
print(type(number1))
print(type(name))
print(type(char))
print(type(f))
print(type(k))

#Type Casting
print(int(f))
print(str(number1))
print(float(number1))

#strings
name1 = "Srinivasa Ramanujan"
print(name1)
print(name1[:10])
print(name1[0:])
print(name1[12:])
print(name1[3:9])
print("Srinivasa" in name1)
print(len(name1))
print("Srinivasa" not in name1)

# Arithmetic operators
number2 = 45
number3 = 34;
print(number2+number3)
print(number2-number3)
print(number2*number3)
print(number2/number3)
print(number2%number3)

 # Comparision operators
number4 = 48
number5 = 27
print(number4==number5)
print(number4>number5)
print(number4<number5)
print(number4>=number5)
print(number4<=number5)
print(number4!=number5)

#Identify Operators
ex1 = ["books", "pen"]
ex2 = ["books", "bag"]
ex3 = ["books", "pen"]
print(ex1 is ex2)
print(ex1 is not ex2)
print(ex2 is ex3)
print(ex2 is not ex3)
print(ex1 is ex3)
print(ex1 is not ex3)

#Loops
#while loop
number6 = 10
while number6 < 20:
    print(number6)
    number6+=1

#for loop
for i in range(1,10):
    print(i)


# if else
number7 = int(input("Enter a number")) #To read a number fro user
if number7 < 10:
    print("less than 10")
elif number7>10:
    print("greater than 10")
elif number7>20:
    print("greater than 20")
else:
    print("The number is not in range")
















