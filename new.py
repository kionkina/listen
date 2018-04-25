'''
Karina Ionkina
SoftDev2 pd07
K #15 -- Do You Even List?
2018-04-25
'''

UC_LETTERS = "QWERTYUIOPASDFGHJKLZXCVBNM"
LC_LETTERS = UC_LETTERS.lower()
NUMBERS = "1234567890"
CHARS = ".?!&#,;:-_*"    

def min_thres(pswd):
    '''
    Returns whether a password meets minimum threshold:
    It contains a mixture of upper- and lowercase letters, and at least one number
    '''
    U= [1 if x in UC_LETTERS else 0 for x in pswd]
    L= [1 if x in LC_LETTERS else 0 for x in pswd]
    N = [1 if x in NUMBERS else 0 for x in pswd]
    upper = 1 in U
    lower = 1 in L
    num = 1 in N
    return upper and lower and num

print min_thres("boopBoop123")
    

def rating(pswd):
    '''
    Returns a password's strength rating based on a 1-10 scale
    Criteria:
    Mixture of upper- and lower-case
    Inclusion of numerals
    Inclusion of non-alphabetic chars
    Length of the password
    '''
    U= [1 if x in UC_LETTERS else 0 for x in pswd]
    L= [1 if x in LC_LETTERS else 0 for x in pswd]
    N = [1 if x in NUMBERS else 0 for x in pswd]
    C = [1 if x in CHARS else 0 for x in pswd]
    upper = 1 in U
    lower = 1 in L
    num = 1 in N
    char = 1 in C
    length = len(pswd) > 10
    strength = [upper, lower, num, char, length]
    score = 0
    for i in strength:
        if i == True:
            score += 2.0
    return score


print rating("UNicn123!")
    


    
