

TEXT = "Tpm owwl vmea ijwcb kwuxcbmza qa bpib bpmg lw epib gwc bmtt bpmu bw lw. Tpm jil vmea qa bpib bpmg lw epib gwc bmtt bpmu bw lw."

def palindrome_test(phrase):
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

def print_scalar(scalar, vector):
    #printVector(scalar float, vector []float) -> None
    #Prints the result of the scalar product to std output.
    newVec = []
    for x in vector:
        newVec.append(float(x)*float(scalar))
    print newVec
    return

def printAddVectors(vec1, vec2):
    # printAddVectors(vec1 []float, vec2 []float) -> None
    # Adds vectors vec1 and vec2 and prints result to std
    # output
    if len(vec1) != len(vec2):
        print "Vectors need to be the same size!"
        return
    newVec = []
    for i in range(len(vec1)):
        newVec[i] = vec1[i] + vec2[i]
    print newVec
    return

def caeser_encrypt(text, shift):
    # caeser_encrypt(text String, shift Int) -> String
    # Performs a caeser shift on text with the shift shift
    # and returns the encrypted text.
    encText = []
    text = text.lower() # makes things simpler
    for char in text:
        if char.isalpha():
            encText.append(chr((((ord(char)-97) + shift)%26) + 97))
        else:
            encText.append(char)
    return "".join(encText)
def caeser_decrypt(text, shift):
    # caeser_decrypt(text String, shift Int) -> String
    # decrypts text, given the shift it was encrypted
    # with
    decText = []
    text = text.lower()
    for char in text.lower():
        if char.isalpha():
            decText.append(chr((((ord(char)-97) - shift)%26)+97))
        else:
            decText.append(char)
    return "".join(decText)
def crack_text():
    # crack_text() -> None
    # cracks the text, using quite a hacky
    # method by storing it in a global var.
    # Prints cracked text.
    words = ["in","on","to","by","for","if","then","that","they","but",
             "open", "go", "and", "do"]
    results = []
    for shift in range(27):
        result = caeser_decrypt(TEXT,shift)
        print shift, result
        total_words = 0
        for word in words:
            idx = 0
            while result.find(word,idx) != -1:
                idx = result.find(word,idx) + 1
                total_words += 1
        results.append((total_words,shift))
    results.sort(key = lambda entry: entry[0])
    print results
        
    
