# Created Spring 2019
# Here is one example experiement.
# For you, if you want to make a different experiment then I recommend
# creating another class with the name of the experiment you are making
# and running it from experiment controller. That way you can keep old
# experiments, run them again in the future, and quickly run different ones.

import PlatesAndOlivesTools as p_o
import GeoEquivClassesTools as geo
import jsonPrintingTools as json

def experiment1():
    # Create Sequences of Geometric Equivilance Classes for T = 2 -> T = 4
    fileLoc = "/home/james/FiorniWork/GeoGraphs"
    json.writeToJsonWPath(fileLoc, "T2Graphs", geo.genGeoGraphs(["A1","A2"]))
    json.writeToJsonWPath(fileLoc, "T3Graphs", geo.genGeoGraphs(["A1","A2","A3"]))
    json.writeToJsonWPath(fileLoc, "T4Graphs", geo.genGeoGraphs(["A1","A2","A3","A4"]))

    # Create Sequences of Geo Equiv Classes in Immediate Neighborhood for T = 2 -> T = 4
    json.writeToJsonWPath(fileLoc, "T2Graphs_ImmediateNeighborhood",
        geo.genGeoGraphsInImmediateNeighborhood(geo.genGeoGraphs(["A1","A2"]), 2))
    json.writeToJsonWPath(fileLoc, "T3Graphs_ImmediateNeighborhood",
        geo.genGeoGraphsInImmediateNeighborhood(geo.genGeoGraphs(["A1","A2","A3"]), 3))
    json.writeToJsonWPath(fileLoc, "T4Graphs_ImmediateNeighborhood",
        geo.genGeoGraphsInImmediateNeighborhood(geo.genGeoGraphs(["A1","A2","A3","A4"]), 4))

    # Test to make sure the Geometric Equivilance Classes are generated correctly
    # geo.testGeoGen()

    # Create Plates and Olives Sequences from the Geometric Sequences for T = 2 -> T = 4
    p_o_FileLoc = "/home/james/FiorniWork/PlatesAndOlivesSequences"
    for i in range(2, 5):
        T = i
        geoGraphs = json.getJsonFile("GeoGraphs/T"+str(T)+"Graphs.json")
        # Make P and O Sequences
        json.writeToJsonWPath(p_o_FileLoc, "P_O_T"+str(T)+"Graphs", p_o.genP_O_SeqInDict(geoGraphs, T))

        # Make P and O Sequences with Maxs and Mins (a.k.a. Crit Points) included
        json.writeToJsonWPath(p_o_FileLoc,
            "P_O_T"+str(T)+"Graphs_wCritPnts", p_o.genP_O_SeqAndCritPntsTupleInDict(geoGraphs, T))

        # Make P and O Sequences in Immediate Neighborhood
        graphsInImmNeighborhood = json.getJsonFile("GeoGraphs/T"+str(T)+"Graphs_ImmediateNeighborhood.json")
        json.writeToJsonWPath(p_o_FileLoc,
            "P_O_T"+str(T)+"Graphs_ImmediateNeighborhood", p_o.genP_O_SeqInDict(graphsInImmNeighborhood, T))

    # Some examples of getting sequences and printing them
    T = 2
    # Get and print sequences of geometric equivilance classes
    geoGraphs = json.getJsonFile("GeoGraphs/T"+str(T)+"Graphs.json")
    print(geoGraphs, "\n")

    # Get and print plates and olives sequences
    p_o_seq = p_o.genPlatesAndOlivesSequences(geoGraphs, T)
    print(p_o_seq, "\n")

    # Get and print plates and olives sequences in dictionary format
    # Tends to be more readable
    p_o_Dict = p_o.genP_O_SeqInDict(geoGraphs,T)
    printDictReadable(p_o_Dict)
    print("Length: ", len(p_o_Dict))

    # Get and print plates and olives sequences with Maxs and Mins (CritPnts) included
    p_o_CritTupleDict = p_o.genP_O_SeqAndCritPntsTupleInDict(geoGraphs,T)
    printDictReadable(p_o_CritTupleDict)
    print("Length: ", len(p_o_CritTupleDict))

### Useful Tools ###

def printDictReadable(dict):
    for key, value in sorted(dict.items(), key=lambda x: x[0], reverse=True):
        print("{} : {}".format(key, value))
