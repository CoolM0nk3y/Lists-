#Oscar Stanley
#13/12/2014
#ask for a name then replaces it 
#askes for the name

def get_names():
    names=[]
    count=0
    
    while count!=8:
        name=input("Please enter a name for person {0}: ".format(count+1))
        names.append(name)
        count+=1
        
    return names

#prints it out
def display(names):
    #prints it out
    count = 0
    print()
    
    for each in names:
        count = count +1
        print("{0}.{1}".format(count,each))
        
    print()
    
#how to edit
def edit (names):
    ends=False
    valid=False
    
    while not valid:
        try:
            value=(int(input("Please enter number of name you want to edit(0 to end the program): ")))-1
            valid=True
            if value>len(names):
                ValueError
            
        except ValueError:
            print("Not valid")
            
    if value==-1:
        ends=True
    else:
        names[value]= input("Please enter a new name: ")
        
    return ends,names
    

#main program
def main():
    names=get_names()
    ends = False
    
    while not ends:
        display(names)
        ends,names = edit(names)

        
if __name__=="__main__":
    main()
    
