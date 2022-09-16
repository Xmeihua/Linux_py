total=0
average=0
count=0
max_num=0
min_num=0
input_num=[]
while True:
	num = input("please input a number:")
	if num == 'done':
		break
	else:
		try:
			num = float(num)
			input_num.append(num)
		except:
			print("Invalid input")

for i in input_num:
	total=total+input_num[i]
	count = count +1
average = total/count
max_num=max(input_num)
min_num=min(input_num)
print(max_num,min_num,average)