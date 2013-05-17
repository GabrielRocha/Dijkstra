#!/bin/python
# encoding: utf-8
"""
Dijkstra.py

Created by Gabriel Rocha on 2013-05-15.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""
class Dijkstra():
    def __init__(self,graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.weights = self.init_weights()
        self.Preds = self.init_Preds()
        self.S = self.init_S()
        self.shortest_path = []
        self.calculate_shortest_path()

    def calculate_shortest_path(self):
        position = self.start
        while self.S[self.end-1] == False:
            weight, vertice = min([ (weight, vertice) for vertice, weight in self.graph.get(position).iteritems() if self.S[vertice-1] == False])
            if self.S[position-1] == False:
                self.Preds[vertice-1] = position
                self.S[position-1] = True
                self.shortest_path.append(position)                
                self.calculate_weight(position)
            if vertice == self.end:
                self.S[vertice-1] = True
                self.Preds[vertice-1] = position
                self.shortest_path.append(vertice)
                self.calculate_weight(vertice)
            position = vertice

    def calculate_weight(self,position):
        for vertice , weight in self.graph.get(position).iteritems():
            if (weight + self.weights[position-1] < self.weights[vertice-1]):
                self.weights[vertice-1] = weight + self.weights[position-1]

    def get_Pred(self, vertice):
        print "Pred : %s" %(self.Preds[vertice-1])

    def get_weight(self,cost):
        print "Weight : %s" %(self.weights[cost-1])

    def init_weights(self):
        weights = []
        for position in range(len(self.graph)):
            weights.append(float("inf"))
        weights[self.start-1] = 0
        return weights

    def init_Preds(self):
        Preds = []
        for position in range(len(self.graph)):
            Preds.append(None)
        Preds[self.start-1] = -1
        return Preds

    def init_S(self):
        S = []
        for position in range(len(self.graph)):
            S.append(False)
        return S

if __name__ == '__main__':
    print "Graph"
    graph = { 
            1: { 2: 3, 4: 3 },
            2: { 1: 3, 4: 1, 3: 1 },
            3: { 2: 1, 5: 5, 6: 5 },
            4: { 1: 3, 2: 1, 5: 1 },
            5: { 4: 1, 3: 5, 6: 1 },
            6: { 3: 5, 5: 1 },
        }

    for value in range(1,len(graph)+1):
        print value, graph.get(value)

    print "\n"
    print "Start: %s \nEnd: %s" %(3,6)
    dijkstra = Dijkstra(graph,3,6)
    print "Pred   : %s" %(dijkstra.Preds)
    print "Weights : %s" %(dijkstra.weights)
    print "Shortest path : %s" %(dijkstra.shortest_path)

    print "\n"
    print "Graph"
    graph = { 
        1: { 2: 1, 4: 3 },
        2: { 1: 1, 4: 1, 3: 5 },
        3: { 2: 5, 5: 3, 6: 3 },
        4: { 1: 3, 2: 1, 5: 1 },
        5: { 4: 1, 3: 3, 6: 7 },
        6: { 3: 3, 5: 7 },
    }

    for value in range(1,len(graph)+1):
        print value ,graph.get(value)

    print "\n"
    print "Start: %s \nEnd: %s" %(1,6)
    dijkstra = Dijkstra(graph,1,6)
    print "Pred   : %s" %(dijkstra.Preds)
    print "Weights : %s" %(dijkstra.weights)
    print "Shortest path : %s" %(dijkstra.shortest_path)

    print "\n"
    print "Graph"    
    graph = { 
        1: { 2: 7 , 3: 9 , 6: 14 },
        2: { 1: 7 , 3: 10, 4: 15 },
        3: { 1: 9 , 2: 10, 4: 11, 6: 2  },
        4: { 2: 15, 3: 11, 5: 6  },
        5: { 4: 6 , 6: 9  },
        6: { 1: 14, 3: 2 , 5: 9 },
    }

    for value in range(1,len(graph)+1):
        print value, graph.get(value)

    print "\n"
    print "Start: %s \nEnd: %s" %(1,5)
    dijkstra = Dijkstra(graph,1,5)
    print "Pred   : %s" %(dijkstra.Preds)
    print "Weights : %s" %(dijkstra.weights)
    print "Shortest path : %s" %(dijkstra.shortest_path)