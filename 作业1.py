str = input("Please input a string:")

i = str.rfind(":")                 
new_string = str[i+1:]

f = float(new_string)             

print(f)
