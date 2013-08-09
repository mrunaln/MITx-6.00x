# 6.00x Problem Set 10
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            print node.getName()
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]



class WeightedEdge(Edge):
    wEdge = {}
    def __init__(self, src, dest, total , outdoor):
        super(WeightedEdge, self).__init__(src, dest)
        #if (src,dest) in self.wEdge.keys():
        #    print "Already here src = !! " + str(src) + " dest = " + str(dest) + " tot = " + str(total) + " out = " + str(outdoor)
            #self.wEdge[(src, dest)].append((total, outdoor))
        self.wEdge[(src, dest)] = (total , outdoor)

    
    def getTotalDistance(self):
        s = self.getSource()
        d = self.getDestination()
        return (self.wEdge[(s, d)][0])
        

    def getOutdoorDistance(self):
        s = self.getSource()
        d = self.getDestination()
        return (self.wEdge [(s, d)][1])

    def __str__(self):
        s = self.getSource()
        d = self.getDestination()
        return str(s) + '->' + str(d) + " " + str(self.wEdge[(s,d)])

class WeightedDigraph(Digraph):
    myedges = {}

    def __init__(self):
        super(WeightedDigraph, self).__init__()
        self.myedges = dict()
        
        
    def addNode(self, node):
        super(WeightedDigraph, self).addNode(node)
        
    #def has_key(self, start):
        
    def addEdge(self, edge):
        super(WeightedDigraph, self).addEdge(edge)
        
        for k in self.edges:
            children = self.childrenOf(k)
            self.myedges[k] = []
            for c in children:
                if  self.hasNode(c):
                    self.myedges[k].append([ c,(edge.wEdge[(k,c)]) ])
                    
    def __str__(self):
        
        res = ""
        for k in self.myedges:
            for d in self.myedges[k]:
              res = '{0}{1} -> {2} ({3}, {4})\n'.format(res, k, d[0], float(d[1][0]), float(d[1][1]) )
        
        return res[:-1]




"""
nj = Node('j')
nk = Node('k')
nm = Node('m')
ng = Node('g')
g = WeightedDigraph()
g.addNode(nj)
g.addNode(nk)
g.addNode(nm)
g.addNode(ng)
randomEdge = WeightedEdge(nj, ng, 31, 24)
print " adding edge j - > g "
g.addEdge(randomEdge)
randomEdge = WeightedEdge(ng, nk, 45, 8)
print " adding edge g - > k "
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nm, nj, 77, 44)
print " adding edge m - > k "
g.addEdge(randomEdge)
randomEdge = WeightedEdge(ng, nm, 55, 13)

g.addEdge(randomEdge)
randomEdge = WeightedEdge(nm, ng, 73, 27)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nm, ng, 13, 12)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(ng, nj, 16, 16)
g.addEdge(randomEdge)
randomEdge = WeightedEdge(nm, nk, 39, 38)
g.addEdge(randomEdge)
print g
"""
