

def multiply(n1,n2):
  return n1*n2

def add(n1,n2):
  return n1+n2

def div(n1,n2):
  return n1/n2

def sub(n1,n2):
  return  n1-n2

operations = {
  "+": add,
  "/": div,
  "*": multiply,
  "-": sub,
}

flag = False

for operator in operations:
  print(operator)
  
first_number = int(input("Tell me the first number"))
operator = input("What operation you want from the list?")
second_number = int(input("Tell me the second number"))
operation_functon = operations[operator]
final_number = operation_functon(first_number,second_number)
print (f"first number {first_number} and second number{second_number} and final output is {final_number}")

while not flag:
  user_choice = input("Do you want further calculations on the previous O/p yes or No?").lower()
  if user_choice == "yes":
    operator = input("What operation you want from the list?")
    number3 = int(input("Tell me the second number"))
    operation_function = operations[operator]
    final_number = operation_function(final_number,number3)
    print(final_number)
  
  else:
    flag = True
  
  

