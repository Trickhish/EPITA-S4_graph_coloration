# -*- coding: utf-8 -*-
"""Graph module.

Provide an implementation of graphs with adjacency matrix.
This can also be called static implementation.

In a graph, vertices are considered numbered from 0 to the order of the graph
minus one. 

"""


class GraphMat:
    """ Simple class for static graph.

    Attributes:
        order (int): Number of vertices.
        directed (bool): True if the graph is directed. False otherwise.
        adj (List[List[int]]): Adjacency matrix
    """

    def __init__(self, order, directed):
        """
        Args:
            order (int): Number of nodes.
            directed (bool): True if the graph is directed. False otherwise.
        """
        
        self.order = order
        self.directed = directed
        self.adj = [[0 for j in range(order)] for i in range(order)]


    def addedge(self, src, dst):
        """Add egde to graph.
    
        Args:
            src (int): Source vertex.
            dst (int): Destination vertex.
    
        Raises:
            IndexError: If any vertex index is invalid.
    
        """

        if src >= self.order or src < 0:
            raise IndexError("Invalid src index")
        if dst >= self.order or dst < 0:
            raise IndexError("Invalid dst index")
        
        self.adj[src][dst] += 1
        if not self.directed and dst != src:
            self.adj[dst][src] += 1



def dot(G):
    """Dot format of graph.

    Args:
        GraphMat

    Returns:
        str: String storing dot format of graph.

    """

    if G.directed:
        s = "digraph {\n"
        link = " -> "
        for x in range(G.order):
            for y in range(G.order):
                s += (str(x) + link + str(y) + '\n') * G.adj[x][y]
    else:
        s = "graph {\n"
        link = " -- "
        for x in range(G.order):
            for y in range(x+1):
                s += (str(x) + link + str(y) + '\n') * G.adj[x][y]
    return s + '}'



def display(G, eng=None):
    """
    *Warning:* Made for use within IPython/Jupyter only.
    eng: graphivz.Source "engine" optional argument (try "neato", "fdp", "sfdp", "circo")
    
    """
    
    try:
        from graphviz import Source
        from IPython.display import display
    except:
        raise Exception("Missing module: graphviz and/or IPython.")
    display(Source(dot(G), engine = eng))
    

# load / save gra format    (do not manage labels and other infos) 

def load(filename,):
    """Build a new graph from a GRA file.

    Args:
        filename (str): File to load.

    Returns:
        Graph: New graph.

    Raises:
        FileNotFoundError: If file does not exist.

    """

    f = open(filename)
    directed = bool(int(f.readline()))
    order = int(f.readline())
    g = GraphMat(order, directed)
    for line in f.readlines():
        edge = line.strip().split(' ')
        (src, dst) = (int(edge[0]), int(edge[1]))
        g.addedge(src, dst)
    f.close()
    return g

def save(G, fileOut):
    gra = str(int(G.directed)) + '\n'
    gra += str(G.order) + '\n'
    for x in range(G.order):
        if G.directed:
            n = G.order
        else:
            n = x + 1
        for y in range(n):    
            for i in range(G.adj[x][y]):
                gra += str(x) + " " + str(y) + '\n'
    fout = open(fileOut, mode='w')
    fout.write(gra)
    fout.close()
