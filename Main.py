KEY_16 =   ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
KEY_8 = ["000", "001", "010", "011", "100", "101", "110", "111"]

def twoToEight(number):
    return

def twoToSixteen(number):
    return

def twoToTen(number):
    return

def eightToTwo(number):
    return

def eightToTen(number):
    return

def eightToSixteen(number):
    return

def tenToTwo(number):
    number = int(number)
    result = ""

    if number % 2 == 1:
        result += "1"
    else:
        result += "0"
        
    return

def tenToEight(number):
    return

def tenToSixteen(number):
    return

def sixteenToTwo(number):
    return

def sixteenToEight(number):
    return

def sixteenToTen(number):
    return

if __name__ == "__main__":
    base = input("Please choose a base (2, 8, 10, 16): ")
    number = str(input("Please enter your number:" ))

    newBase = input("Which base would you like to convert to?")
    if base == newBase:
        print("Already in base " + str(base))
    elif base == 2:
        if newBase == 8:
            print(twoToEight(number))
        elif newBase == 10:
            print(twoToTen(number))
        elif newBase == 16:
            print(twoToSixteen(number))
    elif base == 8:
        if newBase == 2:
            print(eightToTwo(number))
        elif newBase == 10:
            print(eightToTen(number))
        elif newBase == 16:
            print(eightToSixteen(number))
    elif base == 16:
        if newBase == 8:
            print(sixteenToEight(number))
        elif newBase == 10:
            print(sixteenToTen(number))
        elif newBase == 2:
            print(sixteenToTwo(number))
    elif base == 10:
        if newBase == 8:
            print(tenToEight(number))
        elif newBase == 2:
            print(tenToTwo(number))
        elif newBase == 16:
            print(tenToSixteen(number))
    else:
        print("Invalid base selected")