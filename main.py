import random 
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

num_letters = int(input("How many letters do you want in your password? "))
num_nums = int(input("How many numbers do you want in your password? "))
num_symbols =int(input("How many symbols do you want in your password? "))

# random_letters = ''.join(random.choices(letters, k=num_letters))
# random_nums = ''.join(random.choices(nums, k=num_nums))
# random_symbols = ''.join(random.choices(symbols, k=num_symbols))
# password = random_letters + random_nums + random_symbols

password = ""
for i in range(1,num_letters+1):
    password += random.choice(letters)
    
for i in range(1,num_nums+1):
    password += random.choice(nums)

for i in range(1,num_symbols+1):
    password += random.choice(symbols )
    
print(f"Your password is: {password}")

password_list = list(password)
random.shuffle(password_list)

advance_password =  ""
for apd in password_list:
    advance_password += apd

print(f"Your advance_password is: {advance_password}")
print("Thank you")


