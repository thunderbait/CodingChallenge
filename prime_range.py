def prime_range(): # Function to define prime nums in range of values

	print("Define a range of numbers!")
	min_num = int(input("Enter the minimum number:"))
	max_num = int(input("Enter the maxumum number:"))

	print("Calculating prime numbers between",min_num,"and","max_num")
	print("Prime numbers in this range are:")

	for x in range(min_num,max_num):
		if x > 1:
			for i in range(2,x):
				if (x % i) == 0:
					break
			else:
				print(x)

prime_range()