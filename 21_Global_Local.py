g = 10

def function1(n):
    l1 = 40
    l2 = 25
    print(l1, l2)
    # print(g)  # We cannot change Global Var prior to 'Global' declaration...Error line
    global g  # We cannot simply change global variable.So this keyword 'global'
    # is used to make changes to global variable 'g'.
    g = g * 5
    print(g)
    print(n, "How are you ? ")

function1("I am Ok...")
# print(l1)   # Local var cannot be used in Global Scope...Error line

"""Output >
40 25
50
I am Ok... How are you ?
"""


def tom():  # main function
    x = 5

    def jerry():  # Nested function jerry() inside tom()
        global x   # Declaration of Global Keyword
        x = 500

    print("Before calling jerry", x)
    jerry()
    print("After calling jerry", x)

tom()  #
print(x)  # 500 printed, as jerry() function created a global var 500 outside the main function

"""Output >
Before calling jerry 5
After calling jerry 5
500
"""


