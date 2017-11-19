"""
Checks year for Leap or Not. Command line arguments is the year
"""


import sys

def main():
    print ("Hello World!")
    if (len(sys.argv)) == 1:
        y = input("Enter year in yyyy format : ")
        ChkLeap(y)
    else:
        for i in range(1, len(sys.argv)):
            ChkLeap(sys.argv[i])

    return



def ChkLeap(args):
    year = int(args)
    if (year%4 == 0) :
        if (year%100 == 0):
            if (year%400 == 0):
                print("{0} is a leap year".format(year))
            else:
                print("{0} is NOT a leap year". format(year))
        else:
            print("{0} is a Leap year".format(year))
    else:
        print("{0} is a NOT Leap year".format(year))


if __name__ == '__main__':
    main()
   