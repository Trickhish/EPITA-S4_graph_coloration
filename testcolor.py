# -*- coding: utf-8 -*-
"""
S4 - Coloration function tests for students
@author: Nathalie
"""

from algo_py import graph
import os
import statistics
import time

def __graphlist(dirpath):
    """builds a list of graphs from a given directory
    Args: 
        dirpath (str): path to the graph directory (".gra" format)
    Returns:
        Graph list
    """
    
    files = os.listdir(dirpath)
    files.sort()
    L = []
    for f in files:
        if ".gra" in f:
            L.append(graph.load(dirpath + "/" + f))
    return L
    
# for suscribers of "list comprehensions"

def __graphlist2(dirpath):
    files = os.listdir(dirpath)
    files.sort()
    return [graph.load(dirpath + "/" + f) for f in files if ".gra" in f]
    

#without verification!
def run_coloration(f, dirpath):
    """test coloration function on a list of graphs (without verification)
    Args: 
        f (function): the coloration function (returns (nbcol, color list)) 
            color vector: contains integers in [1, nbcol]
        dirpath (str): path to the graph directory (".gra" format)
    Returns:
        list of color numbers
    """
    return [f(G)[0] for G in __graphlist(dirpath)]

# with color verification
def __testcolors(G, colors):
    """
    Args:
        G: simple graph
        colors: supposed color vector for G
    Returns:
        Does the vector "colors" represent a correct coloration for G?
    """
    for s in range(G.order):
        if not colors[s]:
            return False
        for adj in G.adjlists[s]:
            if colors[s] == colors[adj]:
                return False
    return True

def run_verif_coloration(f, dirpath):
    """test the coloration function f on a list of graphs:
        - check that each coloration (the color vector) is correct
        - build the list of resulted chromatic numbers, and information (when coloration is wrong)
    Args: 
        f (function): the coloration function (returns (nbcol, color vector)) 
            color vector: contains integers in [1, nbcol]
        dirpath (str): path to the graph directory (".gra" format)
    Returns:
        the result list: for each graph in dirpath, 
            - the color number if result is correct, 
            - otherwise a pair (color number or None, info) ...
    """
    graphs_tested = __graphlist(dirpath)
    #print(graphs_tested)
    results = []
    lts=[]
    for G in graphs_tested:
        t=time.time()
        (nb, colors) = f(G)
        et = time.time()-t
        et = round((et)*1000000, 5)
        lts.append(et)
        #print(f"{f.__name__} Took {et}μs for {}")
        if not __testcolors(G, colors):
            results.append((None, "wrong coloration"))
        elif nb != max(colors):
            results.append((nb, "wrong chromatic number"))
        else:
            results.append((nb, ""))
    #print(f"{f.__name__} Took {sum(lts)/len(lts)}μs in average")
    return(sum(lts)/len(lts), statistics.median(lts), results)
