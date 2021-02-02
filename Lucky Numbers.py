number = input("Number is: ")
reverse_number = number[::-1]

sum_of_even_digits = 0
sum_of_odd_digits = 0

i = 0
while i < len(reverse_number):
	if i % 2 == 0 :
		sum_of_even_digits += int(reverse_number[i])
	else : 
		sum_of_odd_digits += int(reverse_number[i])
	i += 1

# checking number is lucky or not
if sum_of_odd_digits == sum_of_even_digits : print("Number is Lucky !!!")
else : print("Number is not Lucky !!!")