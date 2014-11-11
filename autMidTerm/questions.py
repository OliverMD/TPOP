def printExtendedBasePattern(size, ink, canvas):
    """
    printBasePattern(size int, ink char, canvas char) -> void
    Prints a cross pattern to the output, of the form:
    x...x
    .x.x.
    ..x..
    .x.x.
    x...x

    Where x is the ink char that is used
    and . is the canvas char used
    """
    if size < 3:
        raise ValueError("Size must be 3 or greater!")

    for line in range(size):
        #iterate through each line number and print each row.
        text = list(canvas*size)

        
        #With len(canvas) * position we get a better result if the canvas is a
        #multi character string.
        text[len(canvas) * line] = text[len(canvas) * (size-line -1)] = ink
        
        print "".join(text)
def printMultipleBasePattern(row,col):
    for i in range(row*4):
        line = []
        for j in range(col):
            text = list("-"*(4))
            text[i%4] = text[3 - (i%4)] = 'X'
            line[j*4:(j+1)*4] = text
        print "".join(line)
#printMultipleBasePattern(2,2)

decypherbook = {'0000':8, '0001':1, '0010':0, '0011':9,
 '0100':5, '0101':3, '0110':7, '0111':2,
 '1110':4, '1111':6}
cypherbook = {8:'0000', 1:'0001', 0:'0010', 9:'0011',
 5:'0100', 3:'0101', 7:'0110', 2:'0111',
 4:'1110', 6:'1111'}
def encode(cypher, text):
    chars = list(text)
    ret = []
    for i in chars:
        ret.append(cypher[int(i)])
    return "".join(ret)
print encode(cypherbook, "12")
def advancedDecode(cypher, text):
    chars = [text[4*i:(i*4)+4] for i in range(len(text)/4)]
    ret = []
    for char in chars:
        for key, val in cypher.iteritems():
            if val == char:
                ret.append(str(key))
    print "".join(ret)

advancedDecode(cypherbook, encode(cypherbook,"12"))
