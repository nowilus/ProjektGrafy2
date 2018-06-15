
from collections import defaultdict
import sys
import os
import os.path

listOfBridges = []
listOfAP = []

class createGraph:
  
    def __init__(init,vertices):
        init.V= vertices
        init.graph = defaultdict(list)
        init.Time = 0
  
    def createEdge(init,u,v):
        init.graph[u].append(v)
        init.graph[v].append(u)

    def articulationPoints(init):
  
        visitedPoint = [False] * (init.V)
        d = [float("Inf")] * (init.V)
        minimum = [float("Inf")] * (init.V)
        parent = [-1] * (init.V)
        aPoints = [False] * (init.V) 

        for i in range(init.V):
            if visitedPoint[i] == False:
                init.articulationPointsLoop(i,parent,d,minimum,aPoints,visitedPoint)
        
        apPoints = ""
        for index, value in enumerate (aPoints):
            if value == True:
                listOfAP.append(index+1)
                apPoints = apPoints + str(int(index)+1) + " "     
        print("                                   " + apPoints)     

    def findBridges(init):
  
        visitedPoint = [False] * (init.V)
        d = [float("Inf")] * (init.V)
        minimum = [float("Inf")] * (init.V)
        parent = [-1] * (init.V)
 
        for i in range(init.V):
            if visitedPoint[i] == False:
                init.findBridgesLopp(i, d, minimum, parent, visitedPoint)        
        
    def articulationPointsLoop(init,u,parent,d,minimum,aPoints,visitedPoint): 
 
        child =0

        visitedPoint[u]= True
 
        d[u] = init.Time
        minimum[u] = init.Time
        init.Time += 1

        for v in init.graph[u]:

            if visitedPoint[v] == False :
                parent[v] = u
                child += 1
                init.articulationPointsLoop(v,parent,d,minimum,aPoints,visitedPoint)

                minimum[u] = min(minimum[u], minimum[v])
 
                if parent[u] == -1 and child > 1:
                    aPoints[u] = True
 
                if parent[u] != -1 and minimum[v] >= d[u]:
                    aPoints[u] = True   
                     

            elif v != parent[u]: 
                minimum[u] = min(minimum[u], d[v])
           
    def findBridgesLopp(init, u , d, minimum, parent, visitedPoint): 
 
        child =0

        visitedPoint[u]= True
 
        d[u] = init.Time
        minimum[u] = init.Time
        init.Time += 1
        
        for v in init.graph[u]:
            if visitedPoint[v] == False :
                parent[v] = u
                child += 1
                init.findBridgesLopp(v, d, minimum, parent, visitedPoint)

                minimum[u] = min(minimum[u], minimum[v])
 
                if minimum[v] > d[u]:
                    listOfBridges.append([u+1,v+1])
                    print("                                   " + '%d %d'%(u+1,v+1))
                     
            elif v != parent[u]:
                minimum[u] = min(minimum[u], d[v])
 
def menu(modeOption):
    if modeOption == "1":
        while True:
            fileWithInputDataForMode1 = input("Podaj sciezke do pliku z zakodowanym grafem wejsciowym: ") 
            if os.path.exists(fileWithInputDataForMode1):   
                file_object  = open(fileWithInputDataForMode1, "r")
                print("\n# =====================================================")
                print("#            Wybrales plik: " +os.path.basename(fileWithInputDataForMode1))
                print("# =====================================================\n")
                break
            else:
                print ("Plik "+ os.path.basename(fileWithInputDataForMode1)+" nie istnieje, podaj inna sciezke!")
                continue
        
        numberOfEdges = 0
        edges = []
        for a, b in enumerate(file_object):
            if a == 0:
                numberOfEdges = int(b);
            else:
                c = b.split(" ")   
                for i in c:
                    if i != "\n":
                        edges.append([int(a)-1,int(i)-1])
     
        g1 = createGraph(numberOfEdges)
        
        for x in edges:
            g1.createEdge(x[0], x[1])
        print("\n# ================================================================================")
        print("#                       MOSTY W PODANYM GRAFIE TO: ")
        print("# ================================================================================\n")   
        g1.findBridges()        
        print("\n# ================================================================================\n")   
        
        fileWithOutputDataForMode1 = input("Podaj sciezke do pliku wyjsciowego: ")
        print("\n# =====================================================")
        print("#        Powstaly plik wyjsciowy to: " +os.path.basename(fileWithOutputDataForMode1))
        print("# =====================================================") 
        outputFileForMode1 = open(fileWithOutputDataForMode1, "w")
        firstLine = ""
        for x in listOfBridges:
            for a in x:
                firstLine = firstLine + str(a) + " "
            firstLine = firstLine + "\n"    
        lines = [firstLine]    
        outputFileForMode1.writelines(lines)
        outputFileForMode1.close()

        os.system(fileWithOutputDataForMode1) 
        
    elif modeOption == "2":

        while True:
            fileWithInputDataMode2 = input("Podaj sciezke do pliku wejsciowego: ") 
            if os.path.exists(fileWithInputDataMode2):   
                file_object  = open(fileWithInputDataMode2, "r")
                print("\n# =====================================================")
                print("#            Wybrales plik: " +os.path.basename(fileWithInputDataMode2))
                print("# =====================================================\n")
                break
            else:
                print ("Plik "+ os.path.basename(fileWithInputDataMode2)+" nie istnieje, podaj inna sciezke!")
                continue
                
        numberOfEdges = 0
        edges = []
        for a, b in enumerate(file_object):
            if a == 0:
                numberOfEdges = int(b);
            else:
                c = b.split(" ")   
                for i in c:
                    if i != "\n":
                        edges.append([int(a)-1,int(i)-1])               
        
        g1 = createGraph(numberOfEdges)
        
        for x in edges:
            g1.createEdge(x[0], x[1])

        print("\n# ================================================================================")
        print("#                PUNKTY ARTYKULACJI W PODANYM GRAFIE TO: ")
        print("# ================================================================================\n")   
        g1.articulationPoints()        
        print("\n# ================================================================================\n") 
  
        
        fileWithOutputDataForMode2 = input("Podaj sciezke do pliku wyjsciowego: ")
        print("\n# =====================================================")
        print("#        Powstaly plik wyjsciowy to: " +os.path.basename(fileWithOutputDataForMode2))
        print("# =====================================================\n") 
        outputFileForMode2 = open(fileWithOutputDataForMode2, "w")
        
        firstLine = ""
        
        for x in listOfAP:
            firstLine = firstLine + str(x) + " "
        lines = [firstLine]    
        
        outputFileForMode2.writelines(lines)
        outputFileForMode2.close()

        os.system(fileWithOutputDataForMode2) 

    elif modeOption == '3':
        os.system('cls')
        sys.exit()
        
    else:
        print("\n# =====================================================")
        print("#                        BLAD")
        print("#            PODAJ POPRAWNa WARTOSC Z MENU")
        print("# =====================================================\n")
        print("1. Znajdowanie mostow ")
        print("2. Znajdowanie punktow artykulacji")
        print("3. Zamknij program\n")
        print("# =====================================================\n")
        newVal = input(">> ")
        menu(newVal)
                
os.system('cls')    
print("\n# ================================================================================")
print("#           WITAJ W PROGRAMIE DO ZNAJDOWANIA MOSTOW I PUNKTOW ARTYKULACJI")
print("# ================================================================================\n")

print("1. Znajdowanie mostow ")
print("2. Znajdowanie punktow artykulacji")
print("3. Zamknij program\n")
print("# =====================================================\n")

modeOption = input(">> ")
    
menu(modeOption)
 