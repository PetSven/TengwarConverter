# Created by Imgur user PetSven
# 8/30/24

# Settings
SHOW_DEBUG = False

vowels = ["a", "e", "i", "o", "u"]
consonents = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
key = ["\u0043", "\u0077", "\u007a", "\u0032", "\u0046", "\u0065", "\u0078", "\u0039", "\u0042",
       "\u0073", "\u007a", "\u006a", "\u0074", "\u0035", "\u004e", "\u0071", "\u007a\u005B", "\u0036",
       "\u0038", "\u0031", "\u004a", "\u0072", "\u0079", "\u007a\u0069", "\u0068", "\u002c"]

vowel_key = [["", "", "", "", ""],
["\u0023", "\u0024", "\u0025", "\u005e", "\u0026"],
["\u0045", "\u0052", "\u0054", "\u0059", "\u004a"],
["\u0023", "\u0024", "\u0025", "\u005e", "\u0026"],
["", "", "", "", ""],
["\u0044", "\u0052", "\u0054", "\u0059", "\u0055"],
["\u0023", "\u0024", "\u0025", "\u005e", "\u0026"],
["\u0043", "\u0056", "\u0042", "\u004e", "\u004d"],
["", "", "", "", ""],
["\u0023", "\u0024", "\u0025", "\u005e", "\u0026"],
["\u0045", "\u0052", "\u0054", "\u0059", "\u0055"],
["\u0023", "\u0024", "\u0025", "\u005e", "\u0026"],
["\u0023", "\u0024", "\u0025", "\u005e", "\u0026"],
["\u0023", "\u0024", "\u0025", "\u005e", "\u0026"],
["", "", "", "", ""],
["\u0044", "\u0052", "\u0054", "\u0059", "\u0055"],
["", "", "", "", ""],
["\u0045", "\u0052", "\u0054", "\u0059", "\u0055"],
["\u0023", "\u0024", "\u0025", "\u005e", "\u0026"],
["\u0045", "\u0052", "\u0054", "\u0059", "\u0055"],
["", "", "", "", ""],
["\u0023", "\u0024", "\u0025", "\u005e", "\u0026"],
["\u0044", "\u0024", "\u0054", "\u005e", "\u0055"],
["", "", "", "", ""],
["\u0044", "\u0052", "\u0047", "\u0059", "\u0055"],
["\u0044", "\u0052", "\u0047", "\u0059", "\u0055"]]

trailing_e = ["", "\u0028", "\u004F", "\u0028",
"", "\u004F", "\u0028", "\u004F",
"", "\u0028", "\u004F", "\u004C", "\u0028", "\u0028",
"", "\u004F", "", "\u004F", "\u004F", "\u004F",
"", "\u0028", "\u004F",
"", "\u004F", "\u004F"]

double_letter = ["", "\u0022", "\u0027", "\u0022",
"", "\u0027", "\u0022", "\u0027",
"", "\u0022", "\u0027", "\u00B8", "\u0022", "\u0022",
"", "\u0027", "", "\u0027", "\u0027", "\u0027",
"", "\u0022", "\u0027",
"", "\u0027", "\u0027"]

# vowel_no_consonent = ["\u0043", "\u0046", "\u0042", "\u004e", "\u004a"]

numbers = ["\u00f0", "\u00f1", "\u00f2", "\u00f3", "\u00f4",
           "\u00f5", "\u00f6", "\u00f7", "\u00f8", "\u00f9"]


def convertToTengwar(line):

    # Convert to lowercase
    lower = line.lower()

    # Add spacing so that " the " and " of " can be detected
    lower = " " + lower + " "

    # Convert one character at a time
    result = ""
    modifyingVowel = ""
    i = 0
    while i < len(lower):
        remaining = len(lower) - i

        test1 = False
        if remaining >= 5:
            if lower[i:i+5] == " the " or lower[i:i+5] == " the\n":
                test1 = True

        test2 = False
        if remaining >= 4:
            if lower[i:i+4] == " of " or lower[i:i+5] == " of\n":
                test2 = True

        if test1:  # "The" is replaced by a single character
            # print("Test1")
            result = result + "\u0020\u0040"
            i = i + 4
        elif test2:  # "Of" is replaced by a single character
            # print("Test2")
            result = result + "\u0020\u0057"
            i = i + 3
        elif ord(lower[i]) >= 48 and ord(lower[i]) <= 57:
            result = result + numbers[ord(lower[i])-48]
            i = i + 1
        elif lower[i] in vowels:  # Vowels need to be placed above letters
            # print("Test3")
            value = ord(lower[i])
            test3 = False
            test4 = False
            nextLetter = ""
            if remaining >= 1:  # If the vowel is followed by a consonent.
                # print("Test4")
                nextLetter = lower[i+1]
                if nextLetter in consonents:
                    # print("Test5")
                    test3 = True

            if lower[i] == "e":  # If e is the last letter
                if remaining >= 1:
                    # print("Test6")
                    nextLetter = lower[i+1]
                    # previousLetter = ord(lower[i-1])
                    previousLetter = lower[i-1]
                    if nextLetter == " " or nextLetter == "\n":
                        if previousLetter in consonents:
                            test4 = True
            if test3:
                # print("Test7")
                x = ord(nextLetter)-97
                y = vowels.index(lower[i])
                # try:
                modifyingVowel = vowel_key[x][y]
                # except IndexError:
                #     print(nextLetter)
                #     print(lower[i])
                #     print(x)
                #     print(y)
            elif test4:
                # print("Test8")
                x = ord(lower[i-1])-97
                # try:
                result = result + trailing_e[x]
                # except IndexError:
                #     print(x)
                #     print(lower[i-2])
                #     print(lower[i-1])
                #     print(lower[i])
            else:  # Print the vowel above a line
                # print("Test7")
                result = result + "\u0060" + key[value-97]
            i = i + 1
        else:
            # print("Test8")
            char = lower[i]
            value = ord(char)
            if value >= 97 and value <= 122:  # If the character is a letter
                # print("Test9")
                if remaining >= 1:  # If there is another letter
                    # print("Test10")
                    char2 = lower[i+1]
                    value2 = ord(char2)
                    # print(nextLetter+lower[i+2])
                    if value == value2:  # If the is a double consonent
                        # print("Test11")
                        # if value == "l":
                        #     # print("Test12")
                        #     mark = "\u00B8"
                        # else:
                        #     # print("Test13")
                        #     mark = "\u003A"
                        x = value-97
                        result = result + key[value-97] + double_letter[x]
                        i = i + 2
                    elif char+char2 == "ch":
                        # print("Test14")
                        result = result + "\u0061"
                        i = i + 2
                    elif char+char2 == "th":
                        # print("Test15")
                        result = result + "\u0033"
                        i = i + 2
                    elif char+char2 == "sh":
                        # print("Test16")
                        result = result + "\u0064"
                        i = i + 2
                    elif char+char2 == "ng":
                        # print("Test17")
                        result = result + "\u0062"
                        i = i + 2
                    elif char+char2 == "wh":
                        # print("Test18")
                        result = result + "\u006F"
                        i = i + 2
                    elif char+char2 == "ph":
                        # print("Test19")
                        result = result + "\u0051"
                        i = i + 2
                    elif char+char2 == "nd":
                        # print("Test19")
                        result = result + "\u0032\u0050"
                        i = i + 2
                    elif char+char2 == "mb":
                        # print("Test19")
                        result = result + "\u0077\u0050"
                        i = i + 2
                    else:
                        # print("Test32")
                        result = result + key[value-97]
                        i = i + 1
                else:
                    # print("Test20")
                    result = result + key[value-97]
                    i = i + 1
                if modifyingVowel != "":
                    # print("Test21")
                    result = result + modifyingVowel
                    modifyingVowel = ""
            elif char == ".":
                # print("Test22")
                result = result + "\u002D"
                i = i + 1
            elif char == ",":
                # print("Test23")
                result = result + "\u003D"
                i = i + 1
            elif char == "\"":
                # print("Test24")
                result = result + "\u203A"
                i = i + 1
            elif char == "?":
                # print("Test25")
                result = result + "\u00c0"
                i = i + 1
            elif char == "-":
                # print("Test26")
                result = result + "\u00c2"
                i = i + 1
            elif char == " ":
                # print("Test27")
                result = result + "\u0020"
                if remaining > 1:
                    # print("Test28")
                    char2 = lower[i+1]
                    if char2 == "r":
                        # print("Test29")
                        result = result + "\u0037"
                        i = i + 1
                    elif char2 == "y":
                        # print("Test30")
                        result = result + "\u006C"
                        i = i + 1
                i = i + 1

            else:
                # print("Test31")
                if SHOW_DEBUG:
                    print(ord(lower[i]))
                i = i + 1
    result = result + "\n"
    return result


# res = convertToTengwar("tree see sea too moo")
# print(res)
# for char in res:
#     print(ord(char))