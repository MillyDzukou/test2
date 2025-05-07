"""
This is a simple program to 
print 'Hello World'
"""

for i in range(10):
    print("Hello world for the {} th time".format(i))

a=0
while(a<10):
    print("This is the {} th term".format(a**2))
    a = a+1
print("End of the while loop")

""" This is a comment to show you that I this file is updated by Mai 06, 2025"""

file = "idiot.txt"
stream = open(file, 'w')
stream.write("This man is crazy")
stream.flush()
stream.close()

print("End of the program")