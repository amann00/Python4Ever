import random   # To open 'random' module....Press and Hold 'ctrl' and click over 'random'

# 1.  Random Integer using randint() function
random_num = random.randint(1,10)  # random integer from 1 to 10 is taken
print(random_num)   # 7 is given here


# 2.  Random decimal random() function
rand_num = round(random.random(),5)  # round function for rounding off the decimals upto 5
# random() function takes no arguments
# no values could be written inside parenthesis ( ) in random() function
print(rand_num)   # 0.31059 is given here


# 3.
classics = ['Kuch Toh Log Kahenge','Aankhon Mein humne Apke','Aaj Mausam Bada Beimaan hai','Pal Pal Dil Ke Pas']

choice = random.choice(classics)
print(choice)   # 'Kuch Toh Log Kahenge' is given here


# 4.
tupl = ('happy','robin','billu','bablu')

var1 = random.choice(tupl)
print(var1)   # bablu




# 5 (IMPORTING PYTHON MODULES) >
import sklearn as sk
print(sk.__version__)   # To know the version of installed module, here it's > 0.23.2
import sys
print(sys.path)   # ['E:\\Python4Ever', 'E:\\Python4Ever', 'C:\\Python3.8.1\\python38.zip',
# 'C:\\Python3.8.1\\DLLs', 'C:\\Python3.8.1\\lib',
# 'C:\\Python3.8.1', 'C:\\Python3.8.1\\lib\\site-packages']


from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier)    # this is used to shorten the path specified by sys.path

import file1  # Importing any any function or anything from existing python file in your project
print(file1.k)
file1.joke("never mind")

"""<class 'sklearn.ensemble._forest.RandomForestClassifier'>
1
"""





