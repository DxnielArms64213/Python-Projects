
#simple greeting function that takes in a name and prints a greeting message

name=input("please enter your name: ")
def greeting(name):
    print("hello there",name,)
greeting(name)



#asks user to input two numbers and an operator/function to perform the calculation, 
# tries/excepts to perform validation 

def calculation():
    valid=False
    operator_valid=False
    while not valid:
        try:
            number1 = float(input("please enter the first number: ").strip())
            number2 = float(input("please enter the second number: ").strip())
            valid=True
        except ValueError:
            print("invalid number")
    while not operator_valid:
            operator = input("enter the operation you want to do: ").lower().strip()
            if operator in ["+", "-", "*", "/", "%", "**"]:
                operator_valid=True
                break
            else: 
                print("invalid operator")
    if operator == "+":
        result = number1+number2
    elif operator == "-":
        result = number1-number2
    elif operator == "/":
        try:
            result = number1/number2 
        except ZeroDivisionError:
            print("cannot divide by 0")
            return 
    elif operator == "*":
        result = number1*number2
    elif operator =="**":
        result = number1**number2
    elif operator == "%":
        result= number1%number2
    return result


#function to define repeat question code

def repeat_question():
    repeat=input("do you want to do another calculation? yes/no ").lower()
    while repeat != "yes" and repeat !="no":
        repeat=input("do you want to do another calculation? yes/no ").lower()
    return repeat


#while loop to continue calculations
#indented while loop to ask again if the user puts an invalid answer

repeat = repeat_question()
while repeat=="yes":
    answer=calculation()
    if answer is not None:
        print(answer)
    repeat=repeat_question()

print("thank you for using the calculator")








  
    































