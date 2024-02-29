
#Part 1: Printing a 5x5 Matrix 

five_by_five_matrix = [[0 for _ in range(5)] for _ in range(5)]

numbers = 1

for i in range(5):

    for j in range(5):

        five_by_five_matrix[i][j] = numbers 

        numbers += 1

for row in five_by_five_matrix:

    print(row)

#Part 2: Replacing all multiples of 3 with ?
    
for i in range(5):

    for j in range(5):

        if five_by_five_matrix[i][j] % 2 != 0:

            five_by_five_matrix[i][j] = '?'

for row in five_by_five_matrix:

    print(row)

        
    
