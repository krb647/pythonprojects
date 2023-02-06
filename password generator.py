import random
print("Welcome to the PyPassword Genarator!")
letters=int(input("How many letters would you like in your password? "))
symbols=int(input("How many symbols would you like in your password? "))
numbers=int(input("How many numbers would you like in your password? "))
total_letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
total_symbols=["!","@","#","$","%","^","&","*","(",")","_"]
total_numbers=["0","1","2","3","4","5","6","7","8","9"]
p1=[]
p2=[]
p3=[]
for i in range(0,letters):
    p1.append(random.choice(total_letters))
for i in range(0,symbols):
    p2.append(random.choice(total_symbols))
for i in range(0,numbers):
    p3.append(random.choice(total_numbers))
password=p1+p2+p3
random.shuffle(password)
final_password=""
for i in password:
    final_password+=i
print(f"Your final password is {final_password}")



    
