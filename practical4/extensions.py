#!/usr/bin/python
# -*- coding: utf-8 -*-

import practical_4_part1 as tasks

def analayseText(text, n):
    text = text.lower()
    words = tasks.splitText(text)
    docLen = len(words)
    wordFreq = tasks.printWordsFrequency(text)
    total = 0.0
    for word in words:
        total += len(word)
    avgLen = total/float(len(words))
    totalWordsN = 0
    for el in wordFreq:
        if len(el[0]) == n:
            totalWordsN += el[1]
    print "Frequency of words:",wordFreq
    print "Total Number of words:", docLen
    print "Average word length:", avgLen
    print str(totalWordsN)+ " words of length "+str(n)+" in text"
#analayseText("Lloyds Banking Group has confirmed 9,000 job losses and the net closure of 150 branches over the next three years.The latest job losses - representing about 10 of its workforce - come on top of 43,000 cuts made since 2008.The bank said it would concentrate on urban branch closures first and has abandoned its pledge to keep open 'the last branch in town'.The group is also setting aside another £900m to cover possible payouts for the PPI mis-selling scandal.",4)

"""
Sparse matrix representation:
List of lists of numbers:
Each inner list represents a vector of the matrix.
But since most of the matrix is 0s, 0s are assumed in all spaces
0  0
1  0

The first column is encoded as:
[1,1,0]
Second Column:
[2]
[0,n,0,n,0]

Always starts with the number of 0s and ends with the number of 0s
even if 0.
"""
testmat = [[1,1,0],[0,1,1]] #Should be #(2,2)
testmat1 = [[4,23,0]] #Should be (1,5)
testmat2 = [[2],[1,4],[2],[1,6]] #Should be (4, 2)

def dimensions(sparseMatrix):
    x = len(sparseMatrix)
    col = sparseMatrix[0]
    length = 0
    for idx in range(len(col)):
        if idx % 2 == 0:
            length += col[idx]
        else:
            length += 1
    return (x, length)
print dimensions(testmat)

mat1 = [[1,1,0],[0,1,1]]
mat2 = [[2],[1,5,0]]
mat3 = [[0,1,1],[1,5,0]]

def sumMat(matrix1, matrix2):
    dim1 = dimensions(matrix1)
    dim2 = dimensions(matrix2)
    if dim1 != dim2:
        print "Error!"
        return 0
    retMatrix = [[0 for a in range(dim1[1])] for b in range(dim1[0])]

    for col in range(dim1[0]):
        head1 = 0
        head2 = 0
        for idx in range(len(matrix1[col])):
            if idx % 2 == 0:
                head1 += matrix1[col][idx]
            else:
                retMatrix[col][head1] += matrix1[col][idx]
                head1 += 1
        for idx in range(len(matrix2[col])):
            if idx % 2 == 0:
                head2 += matrix2[col][idx]
            else:
                retMatrix[col][head2] += matrix2[col][idx]
                head2 += 1
    
    return retMatrix
print sumMat(mat1,mat2)
print sumMat(mat2, mat1)
print sumMat(mat2, mat3)

def transpose(matrix):
    def decodeVec(sparseVec):
        head = 0
        vec = [0 for i in range(length)]
        for idx in range(len(sparseVec)):
            if idx % 2 == 0:
                head += sparseVec[idx]
            else:
                vec[head] = sparseVec[idx]
                head += 1
        return vec
    def encodeVec(vec):
        sparseVec = []
        count = 0
        for i in range vec:
            
