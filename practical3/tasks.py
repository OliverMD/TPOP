def palindromeTest(phrase):
    #palindromeTest(phrase String) -> Bool
    #Returns True if the phrase entered is a
    #palindrome, otherwise returns False.
    
    chars = []
    for char in phrase.lower():
        if char.isalpha():#Allow only letters
            chars.append(char)
    revChars = list(chars)
    revChars.reverse()

    #Reorganise the lists of strings to contain only
    #half the string each. Unless length is odd in which
    #case the middle letter is ignored. Because it'll be
    #the same.
    if len(chars) % 2 == 0:
        chars = chars[:len(chars)/2]
        revChars = revChars[:len(revChars)/2]
    else:
        chars = chars[:(len(chars)-1)/2]
        revChars = revChars[:(len(revChars)-1)/2]

    #Check whether the front and back portions are equal
    if chars == revChars:
        return True
    else:
        return False

def printScalar(scalar, vector):
    #printVector(scalar float, vector []float) -> None
    #Prints the result of the scalar product to std output.
    newVec = []
    for x in vector:
        newVec.append(float(x)*float(scalar))
    print newVec
    return

def printAddVectors(vec1, vec2):
    #printAddVectors(vec1 []float, vec2 []float) -> None
    if len(vec1) != len(vec2):
        print "Vectors need to be the same size!"
        return
    newVec = []
    for i in range(len(vec1)):
        newVec[i] = vec1[i] + vec2[i]
    print newVec
    return

def caeser_encrypt(text, shift):
    #caeser_encrypt(text String, shift Int) -> String
    #Performs a caeser shift on text with the shift shift
    #and returns the encrypted text.
    encText = []
    text = text.lower() # makes things simpler
    for char in text:
        if char.isalpha():
            encText.append(chr((((ord(char)-97) + shift)%26) + 97))
        else:
            encText.append(char)
    return "".join(encText)
def caeser_decrypt(text, shift):
    #caeser_decrypt(text String, shift Int) -> String
    decText = []
    text = text.lower()
    for char in text:
        if char.isalpha():
            decText.append(chr((((ord(char)-97) - shift)%26)+97))
        else:
            decText.append(char)
    return "".join(decText)
