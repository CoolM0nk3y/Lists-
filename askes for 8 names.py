#Oscar Stanley
#13/12/2014
#ask for a name then replaces it 
#askes for the name 
def get_data ():
    name1 = input("Please enter a name for the first person : ")
    name2 = input("Please enter a name for the second person: ")
    name3 = input("Please enter a name for the third person: ")
    name4 = input("Please enter a name for the fourth person: ")
    name5 = input("Please enter a name for the fith person: ")
    name6 = input("Please enter a name for the sixth person: ")
    name7 = input("Please enter a name for the seventh person: ")
    name8 = input("Please enter a name for the eight person: ")
    #puts into a list
    names = [name1,name2,name3,name4,name5,name6,name7,name8]
    return names
#prints it out
def display (names):
    #prints it out
    count = 0
    for each in names:
        count = count +1
        print("{0}.{1}".format(count,each))
    


#how to edit
def edit (names):
    num_edit = int(input("Please enter number of name you want to edit:"))
    num_edit = num_edit - 1
    (names[num_edit])= input("Please enter a new name:")
    
# new function
def end():
    ends = input(" Please enter  False to end and True to contue: ")
    if ends == False:
        return False
    else :
        return True

#main program
names = get_data ()

ends = False

while ends  ==  False:
    display(names)

    names = edit(names)
    ends = end()
    
