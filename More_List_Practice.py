
#Function that gives out a copy of the list with no duplicates

Initial_list = [1, 1, 2, 3, 4, 4]

def Remove_Duplicates(Initial_List):

    unique = set(Initial_List)

    result_list = list(unique) #Got an error that said 'list' is not callable to fix this I had to change the name of my original list to not match the list that changes the set back into the list 

    return result_list

print(Remove_Duplicates(Initial_list)) #Again I put in an arguement in the print statement and not the function 