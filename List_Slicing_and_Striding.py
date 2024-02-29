
#List_Slicing_and_Striding

#Part 1: Creating a list from 0 to 50 without writing all numbers

List_numbers = list(range(51))

print(List_numbers)

#Part 2: Squaring the element of each list 

lis = [2, 3, 4]

def square(lis):   

    squared_list = [numbers ** 2 for numbers in lis]  #My previous code has squared_list = numbers ** 2, I got an error message that says unsupported operan.  I fixed it by making a one line for loop

    return squared_list

print(square(lis))

#Part 3: Printing out only the odd numbers from two lists 

List_A = list(range(1, 11))

List_B = list(range(20, 31))

def odd_integers():

    odd_numbers_list = []

    for number in List_A + List_B:

        if number % 2 != 0:

            odd_numbers_list.append(number)

    return odd_numbers_list
     
print(odd_integers()) #Got an error because I put 2 arguements in odd_integers when printing but not definging it in the function. This was the only error I got.  I rewrote the code but I kept getting the same number as the output, so I fixed this by putting a .append() so it would keep adding it to the list 

