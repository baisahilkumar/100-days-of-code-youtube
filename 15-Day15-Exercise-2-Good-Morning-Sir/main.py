import time
Time = int(time.strftime("%H"))
print("Time:", Time, type(Time))

if ( Time < 12):
    print("Good Morning")
elif ( Time < 16):
    print("Good Afternoon")
elif ( Time < 20):    
    print("Good Evening")   
else:
    print("Good Night")
# https://docs.python.org/3/library/time.html#time.strftime
