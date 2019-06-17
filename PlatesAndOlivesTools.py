# Created Spring 2019
# Tools for generating plates and olives sequences from sequences of graphs

import jsonPrintingTools as json

def genPlatesAndOlivesSequences(graphs, T):
    critPntGraphs = genMaxMinSaddleListForGraphs(graphs, T)
    platesAndOlivesSequences = __genPlatesAndOlivesLabelsForGraphs(critPntGraphs, T)
    return platesAndOlivesSequences

def genMaxMinSaddleListForGraphs(graphs,T):
    critPntGraphs = []
    for g in graphs:
        critPntGraphs.append(__genMaxMinSaddleList(g,T))
    return critPntGraphs

def genP_O_SeqInDict(graphs, T):
    graphSeqTuple = zip(graphs,genPlatesAndOlivesSequences(graphs, T))
    seqDict = {}
    for g, seq in graphSeqTuple:
        seqKey = str(seq)
        if seqKey not in seqDict:
            seqDict[seqKey] = []
            seqDict[seqKey].append(str(g))
        else:
            seqDict[seqKey].append(str(g))
    return seqDict

def genP_O_SeqAndCritPntsTupleInDict(graphs, T):
    poSequences = genPlatesAndOlivesSequences(graphs, T)
    critPntGraphs = genMaxMinSaddleListForGraphs(graphs, T)
    SeqCritTuple = zip(poSequences, critPntGraphs)
    graphSeqTuple = zip(graphs, SeqCritTuple)
    seqDict = {}
    for g, seq in graphSeqTuple:
        seqKey = str(seq)
        if seqKey not in seqDict:
            seqDict[seqKey] = []
            seqDict[seqKey].append(str(g))
        else:
            seqDict[seqKey].append(str(g))
    return seqDict

def __genPlatesAndOlivesLabelsForGraphs(graphs, T):
    platesAndOlivesList = []
    for g in graphs:
        platesAndOlivesList.append(__genPlatesAndOlivesLabels(g, T))
    return platesAndOlivesList

def __genPlatesAndOlivesLabels(critPntGraph, T):
    platesAndOlivesList = [None] * (2*T + 2)
    platesAndOlivesList[0] = "P-"
    platesAndOlivesList[2*T + 1] = "P+"
    for i in range(1, 2*T+1):
        if critPntGraph[i] == "m": platesAndOlivesList[i] = "P+"
        if critPntGraph[i] == "M": platesAndOlivesList[i] = "O-"
        if critPntGraph[i] == "S": platesAndOlivesList[i] = "P-,O+"
    return platesAndOlivesList

def __genMaxMinSaddleList(graph, T):
    maxMinSaddleList = [None] * (2*T + 2)
    maxMinSaddleList[graph.index("a1_h")] = "M"
    maxMinSaddleList[graph.index("a"+str(T)+"_t")] = "m"
    for i in range(1,T+1):
        saddle = graph.index("A"+str(i))
        leaf = graph.index("a"+str(i))
        maxMinSaddleList[saddle] = "S"
        if leaf > saddle:
            maxMinSaddleList[leaf] = "m"
        if leaf < saddle:
            maxMinSaddleList[leaf] = "M"
    return maxMinSaddleList
