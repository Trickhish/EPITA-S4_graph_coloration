from algo_py import graph
from algo_py import stack
from algo_py import queue
import random

def __get_colors(G, cv, e):
    cll=[]
    for c in G.adjlists[e]:
        cll.append(cv[c])
    return(cll)

def greedy(G):
    M = [0]*G.order
    nbc = 0

    for e in range(G.order):
        ncls = __get_colors(G, M, e)
        
        for color in range(1, nbc + 2):
            if color not in ncls:
                M[e] = color
                break
        if M[e] > nbc:
            nbc = M[e]

    return nbc, M


def greedy_opti(G):
    cls = [0] * G.order
    nb_colors = 0
    s = stack.Stack()

    for e in range(G.order):
        s.push((-len(G.adjlists[e]), e))

    while not s.isempty():
        _, e = s.pop()
        vsc = __get_colors(G, cls, e)
        for color in range(1, nb_colors + 2):
            if color not in vsc:
                cls[e] = color
                break

        if cls[e] > nb_colors:
            nb_colors = cls[e]

    return nb_colors, cls

def dsatur(G):
    M = [0] * G.order
    nb_colors = 0
    dsatur_stack = stack.Stack()
    q = queue.Queue()

    for e in range(G.order):
        q.enqueue((-len(G.adjlists[e]), 0, e))
    cls = set()

    while not q.isempty():
        _, dsatur_value, e = q.dequeue()
        if e in cls:
            continue
        vsc = __get_colors(G, M, e)

        for color in range(1, nb_colors + 2):
            if color not in vsc:
                M[e] = color
                cls.add(e)
                break

        if M[e] > nb_colors:
            nb_colors = M[e]

        for n in G.adjlists[e]:
            if n not in cls:
                q.enqueue((-len(G.adjlists[n]), len(__get_colors(G, M, n)), n))

    return nb_colors, M

def largest_first(G):
    M = [0] * G.order
    nb_colors = 0
    dgs = stack.Stack()
    dgq = queue.Queue()
    pels = set()

    for e in range(G.order):
        if e not in pels:
            dgq.enqueue((-len(G.adjlists[e]), e))
            pels.add(e)

    while not dgq.isempty():
        _, e = dgq.dequeue()
        vsc = __get_colors(G, M, e)

        for color in range(1, nb_colors + 2):
            if color not in vsc:
                M[e] = color
                break
        if M[e] > nb_colors:
            nb_colors = M[e]
        dgs.push(e)

        for c in G.adjlists[e]:
            if c not in pels:
                dgq.enqueue((-len(G.adjlists[c]), c))
                pels.add(c)

    return nb_colors, M

def welsh_powell_coloring(G):
    M = [0] * G.order
    nb_colors = 0
    dgs = stack.Stack()
    dg = queue.Queue()

    for e in range(G.order):
        dg.enqueue((-len(G.adjlists[e]), e))

    while not dg.isempty():
        _, e = dg.dequeue()
        vsc = __get_colors(G, M, e)

        for color in range(1, nb_colors + 2):
            if color not in vsc:
                M[e] = color
                break

        if M[e] > nb_colors:
            nb_colors = M[e]

        dgs.push(e)

    return nb_colors, M

def degree_based(G):
    M = [0] * G.order
    nb_colors = 0
    dgs = stack.Stack()
    dg = queue.Queue()

    for e in range(G.order):
        dg.enqueue((-len(G.adjlists[e]), e))

    while not dg.isempty():
        _, e = dg.dequeue()
        vsc = __get_colors(G, M, e)

        for color in range(1, nb_colors + 2):
            if color not in vsc:
                M[e] = color
                break

        if M[e] > nb_colors:
            nb_colors = M[e]

        dgs.push(e)

    return nb_colors, M

def lubys(G):
    M = [0] * G.order
    nb_colors = 0
    sml = list(range(G.order))
    random.shuffle(sml)

    for e in sml:
        vcs = __get_colors(G, M, e)

        for color in range(1, nb_colors + 2):
            if color not in vcs:
                M[e] = color
                break
        
        if M[e] > nb_colors:
            nb_colors = M[e]

    return nb_colors, M