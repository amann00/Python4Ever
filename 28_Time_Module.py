import time

initial1 = time.time()

# Using While Loop >
k = 1
while k < 100000:
    print("Johny Baba Zindabad")
    k += 1
print("While loop ran in", time.time() - initial1, "seconds")

# Using For Loop >
initial2 = time.time()
for i in range(100000):
    print("Johny Baba Zindabad")
print("For loop ran in", time.time() - initial2, "seconds")


"""
While loop ran in 1.509160041809082 seconds
For loop ran in 1.4805357456207275 seconds
Aproximately same
"""


# Displaying Local-Time of your country
localtime = time.asctime(time.localtime(time.time()))
print(localtime)   # The current time will be printed
"""Tue Sep  1 14:40:19 2020"""

# Sleep  function in Time module
initial3 = time.time()
for i in range(5):
    print("Johny Baba now want some fun")
    time.sleep(2)   # time.sleep() function prints one statement after every 2 seconds
print("For loop ran in", time.time() - initial3, "seconds")
