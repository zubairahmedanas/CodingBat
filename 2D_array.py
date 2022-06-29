# arr = [x for x in range(0,2)]
# print(arr)


row = int(input("pls enter how many rows will be there : "))
column = int(input("pls enter how many column will be there : "))
matrix = []
for i in range(0, row):
	matrix.append([])
# print("the result is", matrix)
	for j in range(0,column):
		user_input = input("pls input the value of matrix : ")
		matrix[i].append(user_input)

print("the result is", matrix)


