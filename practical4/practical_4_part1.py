def splitText(text):
    """
    splitText(text String) -> [String]
    Takes a string of text in and splits it up in to
    words which are assumed to be delimited by non
    alphabumeric characters. Then returns a list of
    these words.
    """
    wordStart= 0
    wordEnd = 0
    results = []
    
    while wordStart < len(text):
        wordEnd += 1 #Start new word
        while wordEnd < len(text) and text[wordEnd].isalnum():
            wordEnd += 1
            
        if text[wordStart:wordEnd].isalnum():
            results.append(text[wordStart:wordEnd])
            
        wordStart = wordEnd +1 #Due to start being inclusive.
    return results
def getWordsStartingWith(text,letter):
    """
    getWordsStartingWith(text string, letter string) -> [String]
    returns a list of unique words that begin with the letter from
    the string text.
    """
    letter = letter.lower()
    text = text.lower()
    words = splitText(text)
    words =  [word for word in words if word[0] == letter]
    toDel = []
    for idx in range(len(words)):
        if words[idx] in words[:idx]:
            toDel.append(idx)
    words = [words[idx] for idx in range(len(words)) if idx not in toDel]
    return words
#print getWordsStartingWith("A cow that has so much fun is great beef!","t")
#print getWordsStartingWith(" a a a a a a ","a")
def printWordsFrequency(text):
    """
    printWordsFrequency(text string) -> {string:int}
    calculates the frequency of each word in the string text.
    Returns a dictionary which shows how many times each word
    appears
    """
    text = text.lower()
    words = splitText(text)
    wordFreq = {}
    for word in words:
        if wordFreq.has_key(word):
            wordFreq[word] += 1
        else:
            wordFreq[word] = 1
    wordFreq = [(word, wordFreq[word]) for word in wordFreq]
    return sorted(wordFreq, key=lambda el:el[1], reverse=True)
#print printWordsFrequency("A sausage comes to tea, tea, alpha a, to yay")


    
