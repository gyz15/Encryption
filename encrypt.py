def encrypt(words):
    output = ""
    for word in words:
        if word == "a":
            output += "s"
        elif word == "b":
            output += "n"
        elif word == "c":
            output += "v"
        elif word == "d":
            output += "f"
        elif word == "e":
            output += "r"
        elif word == "f":
            output += "g"
        elif word == "g":
            output += "h"
        elif word == "h":
            output += "j"
        elif word == "i":
            output += "o"
        elif word == "j":
            output += "k"
        elif word == "k":
            output += "l"
        elif word == "l":
            output += "a"
        elif word == "m":
            output += "z"
        elif word == "n":
            output += "m"
        elif word == "o":
            output += "p"
        elif word == "p":
            output += "q"
        elif word == "q":
            output += "w"
        elif word == "r":
            output += "t"
        elif word == "s":
            output += "d"
        elif word == "t":
            output += "y"
        elif word == "u":
            output += "i"
        elif word == "v":
            output += "b"
        elif word == "w":
            output += "e"
        elif word == "x":
            output += "c"
        elif word == "y":
            output += "u"
        elif word == "z":
            output += "x"
        elif word == "A":
            output += "S"
        elif word == "B":
            output += "N"
        elif word == "C":
            output += "V"
        elif word == "D":
            output += "F"
        elif word == "E":
            output += "R"
        elif word == "F":
            output += "G"
        elif word == "G":
            output += "H"
        elif word == "H":
            output += "J"
        elif word == "I":
            output += "O"
        elif word == "J":
            output += "K"
        elif word == "K":
            output += "L"
        elif word == "L":
            output += "A"
        elif word == "M":
            output += "Z"
        elif word == "N":
            output += "M"
        elif word == "O":
            output += "P"
        elif word == "P":
            output += "Q"
        elif word == "Q":
            output += "W"
        elif word == "R":
            output += "T"
        elif word == "S":
            output += "D"
        elif word == "T":
            output += "Y"
        elif word == "U":
            output += "I"
        elif word == "V":
            output += "B"
        elif word == "W":
            output += "E"
        elif word == "X":
            output += "C"
        elif word == "Y":
            output += "U"
        elif word == "Z":
            output += "X"
        else:
            output += word
    return output


a = encrypt("And the sleeping child you’re holding,\
Is the Great I Am!\
I Am!\
Mary, did you know\
Mary, did you know\
Mary, did you know\
")
print(a)
