mystr  = "Happy is a bad boy"
print(mystr)
print(len(mystr))  #length of string
print(mystr[4])
print(mystr[5])
print(mystr[7])
print(mystr[0:4])  #range (chars before 4th index printed)
print(mystr[3:58])  #when range enterred more than length of string
print(mystr[0:5:2])  #skip one char from 0 to 5 (0,2,4)
print(mystr[0:10:3])  #print chars 0,3,6,9 skipping two chars in b/n
print(mystr[0:])   #full string printed
print(mystr[11:])  #string ahead to 11th char printed
print(mystr[:5])   #string before 5th char printed. #By default 0 is taken before':'
print(mystr[::])   #by-default values taken=(0:18:1)  # 1-denotes gap in b/w
print(mystr[0:18:1])  #full string printed
print(mystr[:])    #by-default values taken=(0:18)
print(mystr[::1])  #full string printed
print(mystr[::2])  #one char skipped in string
print(mystr[:10:2])  #one char skipped from 0 to 10
print(mystr[::1000])  #only 1st char printed

#Negative String Slicing >
print(mystr[::-1])  #-ve string slicicng.Reverse of the string'll be printed
# Start counting from back & initialize from -1,-2,-3,-4,-5,-6,-7,-8.......
print(mystr[-3:-10:-1])  #Reverse string having a range -3 to -10 OR
print(mystr[8:15])   #same as range -3 to -10

#Some string functions >
print(mystr.isalnum()) #False is returned. #check if the string is alpha numeric.As the given string is not Alpha Numeric due to the spaces b/w words.
# If the string has no Spaces in b/w,then it is Alpha Num
print(mystr.isalpha()) #False is returned. #As the string is not Alpha due to spaces.

print(mystr.endswith("boy"))  #True is returned, as String is ending with "boy"
print(mystr.endswith("is"))  #False is returned
print(mystr.startswith("Happy"))
print(mystr.startswith("bad"))

print(mystr.count("Happy"))  #Counts no. of "Happy" in string
print(mystr.count("p"))  #Counts no. of "p" in string

print(mystr.capitalize())  #Capitalize the 1st letter of String if it's not.
print(mystr.lower())  #Lowers the letters of full string
print(mystr.upper())  #Uppers the letters of full string

print(mystr.find("is"))  #6 is returned, as "is" starts from 6th index
print(mystr.replace("boy","girl"))  #Replaces the word "boy" with "girl"


"""
OUTPUT >
2.  Happy is a bad boy
3.  18
4.  y
5.   
6.  s
7.  Happ
8.  py is a bad boy
9.  Hpy
10.  Hpia
11. Happy is a bad boy
12. bad boy
13. Happy
14. Happy is a bad boy
15. Happy is a bad boy
16. Happy is a bad boy
17. Happy is a bad boy
18. Hpyi  a o
19. Hpyi 
20. H
23. yob dab a si yppaH
25. b dab a
26.  a bad 
29. False
31. False
33. True
34. False
35. True
36. False
38. 1
39  2
41. Happy is a bad boy
42. happy is a bad boy
43. HAPPY IS A BAD BOY
45. 6
46  Happy is a bad girl
"""

