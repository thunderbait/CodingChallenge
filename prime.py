def prime(): # Function to identify whether a number is prime or not
	num = int(input("Enter a number: "))

	if num > 1:

		for i in range(2,num):
			if (num % i) ==0:
				print(num,"is not Prime!")
				print(i,"and",num//i,"are factors of ",num)
				break
		else:
			print("This in a prime number!")
	else:
		print("Not a prime number.")
		print("Prime numbers are greater than 1.")

prime()