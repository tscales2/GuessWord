
import random
import os
import sys

def youActucallyWon():
    print('You managed to beat my game?!  You are a total unicorn')



def wordpicker(m):
    count = 0

    jack = random.choice(m)
    lenOfWord = len(jack)
    print('The word is '+ str(lenOfWord) + ' letters long.')
    n = input("Please guess the word starting with " + jack[0] + '\n')

    while n != jack:
        if n.isalpha():

            n = input("Not the word.")
            count += 1
            if count == 5:
                print('Sorry, the word was ', jack)
                break
            elif count == 4:
                if lenOfWord <= 5:
                    print('Sorry, the word was ', jack)
                    break
                else:
                    print('Try again. Here\'s a hint: The fifth letter is ' + jack[4])
            elif count == 3:
                if lenOfWord <= 4:
                    print('Sorry, the word was ', jack)
                    break
                else:
                    print('Try again. Here\'s a hint: The fourth letter is ' + jack[3])
            elif count == 2:
                if lenOfWord <= 3:
                    print('Sorry, the word was ', jack)
                    break
                else:
                    print('Try again. Here\'s a hint: The third letter is ' + jack[2])
            elif count == 1:
                print('Try again. Here\'s a hint: The second letter is ' + jack[1])
        else:
            n = input('Please enter a valid word')
    else:
        youActucallyWon()


def groupOfWords():
     myFile = open("web2.txt", "r")
     myFile.seek(0)
     words = (myFile.read())
     txt = words.splitlines()
     aTxt = [x for x in txt if x[0] == 'A']
     bTxt = [x for x in txt if x[0] == 'B']
     cTxt = [x for x in txt if x[0] == 'C']
     dTxt = [x for x in txt if x[0] == 'D']
     eTxt = [x for x in txt if x[0] == 'E']
     fTxt = [x for x in txt if x[0] == 'F']
     gTxt = [x for x in txt if x[0] == 'G']
     hTxt = [x for x in txt if x[0] == 'H']
     iTxt = [x for x in txt if x[0] == 'I']
     jTxt = [x for x in txt if x[0] == 'J']
     kTxt = [x for x in txt if x[0] == 'K']
     lTxt = [x for x in txt if x[0] == 'L']
     mTxt = [x for x in txt if x[0] == 'M']
     nTxt = [x for x in txt if x[0] == 'N']
     oTxt = [x for x in txt if x[0] == 'O']
     pTxt = [x for x in txt if x[0] == 'P']
     qTxt = [x for x in txt if x[0] == 'Q']
     rTxt = [x for x in txt if x[0] == 'R']
     sTxt = [x for x in txt if x[0] == 'S']
     tTxt = [x for x in txt if x[0] == 'T']
     uTxt = [x for x in txt if x[0] == 'U']
     vTxt = [x for x in txt if x[0] == 'V']
     wTxt = [x for x in txt if x[0] == 'W']
     xTxt = [x for x in txt if x[0] == 'X']
     yTxt = [x for x in txt if x[0] == 'Y']
     zTxt = [x for x in txt if x[0] == 'Z']

     myFile.close()

     wordstochoose = input('Enter either a letter all words starting with that letter\nor choose ALL for the entire list of words: \n')
     if wordstochoose == 'A':
         print('You chose the letter A')
         return aTxt
     elif wordstochoose == 'B':
         print('You chose the letter B')
         return bTxt
     elif wordstochoose == 'C':
         print('You chose the letter C')
         return cTxt
     elif wordstochoose == 'D':
         print('You chose the letter D')
         return dTxt
     elif wordstochoose == 'E':
         print('You chose the letter E')
         return eTxt
     elif wordstochoose == 'F':
         print('You chose the letter F')
         return fTxt
     elif wordstochoose == 'G':
         print('You chose the letter G')
         return gTxt
     elif wordstochoose == 'H':
         print('You chose the letter H')
         return hTxt
     elif wordstochoose == 'I':
         print('You chose the letter I')
         return iTxt
     elif wordstochoose == 'J':
         print('You chose the letter J')
         return jTxt
     elif wordstochoose == 'K':
         print('You chose the letter K')
         return kTxt
     elif wordstochoose == 'L':
         print('You chose the letter L')
         return lTxt
     elif wordstochoose == 'M':
         print('You chose the letter M')
         return mTxt
     elif wordstochoose == 'N':
         print('You chose the letter N')
         return nTxt
     elif wordstochoose == 'O':
         print('You chose the letter O')
         return oTxt
     elif wordstochoose == 'P':
         print('You chose the letter P')
         return pTxt
     elif wordstochoose == 'Q':
         print('You chose the letter Q')
         return qTxt
     elif wordstochoose == 'R':
         print('You chose the letter R')
         return rTxt
     elif wordstochoose == 'S':
         print('You chose the letter S')
         return sTxt
     elif wordstochoose == 'T':
         print('You chose the letter T')
         return tTxt
     elif wordstochoose == 'U':
         print('You chose the letter U')
         return uTxt
     elif wordstochoose == 'V':
         print('You chose the letter V')
         return vTxt
     elif wordstochoose == 'W':
         print('You chose the letter W')
         return wTxt
     elif wordstochoose == 'X':
         print('You chose the letter X')
         return xTxt
     elif wordstochoose == 'Y':
         print('You chose the letter Y')
         return yTxt
     elif wordstochoose == 'Z':
         print('You chose the letter Z')
         return  zTxt
     elif wordstochoose == 'ALL':
         print('You chose them all?  Good luck...')
         return txt


print('Hey, welcome to my guessing game! \nThis game is incredibly hard to win. \nHappy Playing!')

pickletter = groupOfWords()

wordpicker(pickletter)
input('Click any key to exit')


