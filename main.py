import random
import string

while True:
    length = str(input("Input password length: "))
    if length.isdigit():
        l = int(length)
        break


digits_count = 0
u_letters_count = 0
l_letters_count = 0
punct_count = 0
while True: # at least one symbol of each set(Uppercase letters, lowercase letters, numbers and punctuation)
    password=[]
    for i in range(l):
        password.append(random.choice(string.ascii_letters+string.digits+string.punctuation))
        if password[i] in string.ascii_lowercase:
            l_letters_count+=1
        elif password[i] in string.ascii_uppercase:
            u_letters_count+=1
        elif password[i] in string.digits:
            digits_count+=1
        elif password[i] in string.punctuation:
            punct_count+=1
    if (digits_count!=0) and (u_letters_count!=0) and (l_letters_count!=0) and (punct_count!=0):
        break

print('Your password is: '+''.join(password))