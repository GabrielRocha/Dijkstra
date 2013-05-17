#!/bin/python
# encoding: utf-8
"""
Dijkstra.py

Created by Gabriel Rocha on 2013-05-15.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""
import networkx as nx
import matplotlib.pyplot as plt
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
            weight, vertice = min([ (weight, vertice) 
                    for vertice, weight in self.graph.get(position).iteritems()
                    if self.S[vertice-1] == False])
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
        return self.Preds[vertice-1]

    def get_weight(self,cost):
        return self.weights[cost-1]

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
    
    def show_graph(self):
        graph=nx.Graph(self.graph)
        pos=nx.spectral_layout(graph)
        nx.draw_networkx_nodes(graph, pos, node_color='r', node_size=500, alpha=0.8)
        nx.draw_networkx_edges(graph,pos,width=1,alpha=0.5)
        nx.draw_networkx_edges(graph,pos, edge_labels={},edgelist=self.get_list_shortest_path(), width=8,alpha=0.5,edge_color='r')
        nx.draw_networkx_edge_labels(graph,pos, self.get_list_weights_edge(),label_pos=0.3)
        labels=self.set_labels()
        nx.draw_networkx_labels(graph,pos,labels,font_size=16)
        plt.title("Dijkstra")
        plt.text(0.5, 0.97, "Start: "+str(self.start)+" End: "+str(self.end),
                     horizontalalignment='center',
                     transform=plt.gca().transAxes)
        plt.text(0.5, 0.94, "Shortest Path: "+str(self.shortest_path),
                     horizontalalignment='center',
                     transform=plt.gca().transAxes)
        plt.text(0.5, 0.90, "Weights: "+str(self.weights),
                    horizontalalignment='center',
                    transform=plt.gca().transAxes)
        plt.text(0.5, 0.86, "Pred: "+str(self.Preds),
                    horizontalalignment='center',
                    transform=plt.gca().transAxes)
        plt.axis('off')
        self.get_list_weights_edge()
        plt.show()
    
    def set_labels(self):
        labels={}
        for position in self.graph.keys():
            labels[position]=position
        return labels
    
    def get_list_shortest_path(self):
        start =  self.start
        list_shortest_path = []
        for vertice in self.shortest_path:
            neighbor = (start,vertice)
            list_shortest_path.append(neighbor)
            start = vertice
        return list_shortest_path

    def get_list_weights_edge(self):
        list_weights_edge={}
        for position in self.graph.keys():
            for vertice, weight in self.graph.get(position).iteritems():
                if not(list_weights_edge.get((vertice,position))):                    
                    list_weights_edge[(position,vertice)] = weight
        return list_weights_edge

if __name__ == '__main__':
   print "Exemplo 1 - Graph"
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
   print "Preds   : %s" %(dijkstra.Preds)
   print "Weights : %s" %(dijkstra.weights)
   print "Shortest path : %s" %(dijkstra.shortest_path)
   dijkstra.show_graph()
    
   print "\n"
   print "Exemplo 2 - Graph"
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
   print "Preds   : %s" %(dijkstra.Preds)
   print "Weights : %s" %(dijkstra.weights)
   print "Shortest path : %s" %(dijkstra.shortest_path)
   dijkstra.show_graph()
 
   print "\n"
   print "Exemplo 3 - Graph"    
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
   print "Preds   : %s" %(dijkstra.Preds)
   print "Weights : %s" %(dijkstra.weights)
   print "Shortest path : %s" %(dijkstra.shortest_path)
   dijkstra.show_graph()