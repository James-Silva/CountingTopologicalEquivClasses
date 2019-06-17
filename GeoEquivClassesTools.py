# Created Spring 2019 by James Silva
# Tools for generating geomentric equivilance classes

import jsonPrintingTools as json
import copy

def genGeoGraphs(achain):
    T = len(achain) # T is the number of critical points
    achain.insert(0,"a1_h")
    achain.append("a"+str(T)+"_t")
    ## Case 1
    case1Graphs = []
    case1Graphs.append(achain)
    # Insert a1 avoiding A1,...,AT,aT
    case1Graphs = __createNewGraphsWithInsert("a1", 1, T+1, case1Graphs)
    # Insert aT avoiding A1,...,AT,a1,aT
    case1Graphs = __createNewGraphsWithInsert("a"+str(T),0, T+2, case1Graphs)

    ## Case 2
    case2Graphs = []
    case2Graphs.append(achain)
    case2Graphs[0].append("a1")
    #Insert aT avoiding A1,...,AT,a1
    case2Graphs = __createNewGraphsWithInsert("a"+str(T),0, T+1, case2Graphs)

    ## Add middle leaves
    graphsList = case1Graphs + case2Graphs
    for i in range(2,(T-1)+1):
        graphsList = __createNewGraphsWithInsert("a"+str(i),0, len(graphsList), graphsList)

    return graphsList

def genGeoGraphsInImmediateNeighborhood(geoGraphs, T):
    output = []
    for g in geoGraphs:
        saddleIndicies = [None]*(T+1) #saddleIndicies[0] = None for clarity later
        maxMinIndicies = [None]*(T+1)
        for i in range(1,T+1):
            saddleIndicies[i] = g.index("A"+str(i))
            maxMinIndicies[i] = g.index("a"+str(i))
        if maxMinIndicies[1] < saddleIndicies[2]:
            if maxMinIndicies[T] > saddleIndicies[T-1]:
                isTrue = True
                for j in range(2,T): #Loop to check if middle is not correct
                    if maxMinIndicies[j] > saddleIndicies[j+1] or maxMinIndicies[j] < saddleIndicies[j-1]:
                        isTrue = False
                if isTrue == True:
                    output.append(g)
    return(output)

def __createNewGraphsWithInsert(insertValue, min, max, graphsList):
    """Internal. Creates graphs with inserted value at each possible position"""
    newGraphsList = []
    for i in range(min,max+1):
        for g in graphsList:
            gcopy = copy.deepcopy(g)
            gcopy.insert(i, insertValue)
            if gcopy not in newGraphsList: # Check for Dubplicates
                newGraphsList.append(gcopy)
    return newGraphsList

def testGeoGen():
    """Values taken from V.I. Arnold's 'Experimental Mathematics'"""

    print("Check A1, A2")
    print("Program Number: ",len(genGeoGraphs(["A1","A2"])))
    print("Expected Number: ", 19)

    print("\nCheck A1, A2, A3")
    print("Program Number: ", len(genGeoGraphs(["A1","A2","A3"])))
    print("Expected Number: ", 232)

    print("\nCheck A1, A2, A3, A4")
    print("Program Number: ",len(genGeoGraphs(["A1","A2","A3","A4"])))
    print("Expected Number: ", 3690)
