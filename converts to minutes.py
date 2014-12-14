#get total of hours
def hour():
    hours = int(input("Please enter the amount of hours: "))
    return hours
#get total of hours 
def minute():
    mins = int(input("Please enter the amount of minutes: "))
    return mins
#get total of seconds
def sec():
    seconds = int(input("Please enter the amount of seconds: "))
    return seconds
#calculate total seconds
def calculate (hours, mins,seconds):
    total = (3600 / hours) + (60 / mins) + seconds
    return total 


#main program

hours = hour()
mins = minute()
seconds = sec()
total = calculate (hours, mins ,seconds)
print (total)



