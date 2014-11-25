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
    """
    printMultipleBasePattern(row int, col int) -> None
    Prints a 3X3 cross pattern a (row * col) number of times
    such that the resulting grid of crosses has row number of
    rows and col number of columns.
    """
    for i in range(row*4):
        line = []
        for j in range(col):
            #Init current line with background char.
            text = list("-"*(4))

            #Given the index of this line change a
            #background char to an ink char.
            text[i%4] = text[3 - (i%4)] = 'X'

            #Put the correct text in the line proper.
            line[j*4:(j+1)*4] = text
        print "".join(line)

def encode(cypher, text):
    """
    encode(cypher {int:string}, text string) -> string
    Returns a string that has text encoded according to
    the cypher given by cypher for digits 0...9.
    """
    chars = list(text)
    ret = []
    for i in chars:
        ret.append(cypher[int(i)])
    return "".join(ret)

def advancedDecode(cypher, text):
    """
    advancedDecode(cypher {int:string}, text) -> string
    Returns the decoded text given the cypher that it was
    encoded with.
    """
    #Seperate text in to chunks of 4 to be decoded.
    chars = [text[4*i:(i*4)+4] for i in range(len(text)/4)]
    
    ret = []
    for char in chars:

        #Iterate over the map to try and find
        #matching for current chunk.
        for key, val in cypher.iteritems():
            if val == char:
                ret.append(str(key))
                break
    return "".join(ret)
