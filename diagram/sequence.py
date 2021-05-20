from .models import Possesion
from .Node import Node
import math

class Sequence ():

    def __init__(self):
        self.sequenceList = Possesion.objects.all()
        self.peak = 'Лицо'
        self.seqList = ['Лицо']
        self.seqListTotal = []

    def getChild (self, mother):

        # for object in self.sequenceList:
        #
        #     if object.mother == mother:
        return 1

    def getGraphDisct (self):

        graph = {}
        for obj in self.sequenceList:
            graph[obj.mother] = 0

        for k in graph:
            l = []
            for obj in self.sequenceList:
                if k == obj.mother:
                    l.append(obj.child)
            graph[k] = l
        return graph


    def find_all_paths(self,graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]: #[A,B] A not in path
            if node not in path:
                newpaths = self.find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def shareCalculations (self, path):

        share = []
        for index,object in enumerate(path):
            for obj in self.sequenceList:
                if object == obj.mother and path[index+1] == obj.child:
                    share.append(obj.share)

        shareMultiplication = math.prod(share)
        shareInpercentage = "{:.2%}".format(shareMultiplication)

        return shareInpercentage




