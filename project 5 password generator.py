import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9']
symbols= ['!','@','$''%','^','&','*','(',')','_','+']


#input functions         
n_letters=int(input("Enter the number of letters you need"))
n_numbers=int(input("enter the count of numbers you need"))
n_symbols=int(input("enter the number of symbols you need"))


#EASY LEVEL PASSWORD generating with fixed password length using inputs

#password=""
#for char in range(1,n_letters+1):
  #random_char = random.choice(letters)
  #password += random_char
  
#for n in range(1,n_numbers+1):
 # random_n = random.choice(numbers)
 # password += random_n
 
#for s in range(1,n_symbols+1):
 # random_s=random.choice(symbols)
 # password += random_s
#print(password)



'''#hard level generating password with random length without inputs so make input function lines as comments

#password=''
#for char in range(1,len(letters)):
 # password += random.choice(letters) 

#for char in range(1,len(numbers)):
  #password += random.choice(numbers) 

#for char in range(1,len(symbols)):
 # password += random.choice(symbols) 
#print(password)'''  you can use this best code for password generating that i mentioned between triple quotes..you can remove hash at everyline in order to run the code and dont use input funtion at beginning.





#Other method to do it using inputs with unorder .....first method and this both are same except here in this method  we took list and it is unordered

password_list=[]
random.shuffle(password_list)

for char in range(1,n_letters+1):
  password_list+=(random.choice(letters))

for char in range(1,n_numbers+1):
  password_list+=(random.choice(numbers))

for char in range(1,n_symbols+1):
  password_list+=(random.choice(symbols))

print(password_list)
