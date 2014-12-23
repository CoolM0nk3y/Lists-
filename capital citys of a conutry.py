#get the random number
def random ():
    import random 
    random_num = random.randint(0,10)
    return random_num
#lists
def list1():
    column1 = ["England","Australia","Germany","France","Lithuania","China","United States of America","Jamaica","Mexico","Thailand"]
    return column1
def list2 ():
    column2 = ["London","Canberra","Berlin","Paris","Vilnius","Beijing","Washington","Kingston","Mexico City","Bangkok"]
    return column2

#cut the list
def cut_list1 (column1,random_num):
    country = column1[random_num]
    return country
#cut the list to get the capital
def cut_list2 (column2,random_num):
    capital = column2[random_num]
    return capital
def ask_user (country,capital):


    answer = input("What is the caital {0}: ".format(country))
    if answer == capital:
        print("That is correct")
    else:
        print("That is wrong")





#main program
count = 0
while count != 5:
    count = count + 1

    random_num = random()
    column1 = list1()
    column2 = list2()
    country = cut_list1 (column1,random_num)
    capital = cut_list2 (column2,random_num)
    ask_user (country,capital)

