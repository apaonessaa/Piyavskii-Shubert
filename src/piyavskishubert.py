import heapq
import copy 

from src.tree import BinaryTree as Node

def estR(L,x,y,zx,zy): return (zx+zy)/2 - L*(y-x)/2

def estx(L,x,y,zx,zy): return (x+y)/2 - (zy-zx)/(L*2)
 
# hmax=15 ====> 0<=len(heap)<=65535  
def algorithm(f, a, b, L, hmax=15, n=1000000, eps=0.0000001, display=False):
    # Display mode
    states={}

    # define and init z
    z = {}
    z[a]=f(a)
    z[b]=f(b)

    # leaves of Binary Tree
    frontier=[] 
    heapq.heapify(frontier)
    push=lambda k, v : heapq.heappush(frontier, (k,v))
    pop=lambda : heapq.heappop(frontier)
    key=lambda x : x[0]
    pruned=0
            
    # Crea tree con node root, a e b
    A=Node().setR(float('inf')).setX(a)
    B=Node().setR(float('inf')).setX(b)
    root=Node().setLeft(A).setRight(B)
    
    (left,right)=(root,None)

    zmin=float('inf')
    k=1
    while k<=n:
        # Calcolo del minorante
        if left is not None:
            xs=left.getLeft().getX()
            xe=left.getRight().getX()
            R=estR(L,xs,xe,z[xs],z[xe])
            left.setR(R)

            if R<=zmin:
                push(R,left)
            else:
                pruned+=1

        if right is not None:
            xs=right.getLeft().getX()
            xe=right.getRight().getX()
            R=estR(L,xs,xe,z[xs],z[xe])
            right.setR(R)
            
            if R<=zmin:
                push(R,right)
            else:
                pruned+=1

        # Aggiunge i due nodi alle liste delle frontier
        # che si possono espandere e prendo la leaf
        # con minorante piu' piccolo
        (_,left)=pop()

        # criterio di arresto
        xs=left.getLeft().getX()
        xe=left.getRight().getX()
        if xe-xs<=eps:
            break
        
        # calcola xt e set k
        xt=estx(L,xs,xe,z[xs],z[xe])
        left.setX(xt).setK(k)
        z[xt]=f(xt)

        # branch&bound
        if z[xt]<zmin:
            zmin=z[xt]
            pruned+=strategy(frontier,hmax,zmin,key=key)

        # alloca frontier iterazione corrente 
        # colleziona zmin all'iterazione k
        if display:
            states[k]={}
            states[k]['nodes']=[copy.copy(leaf) for R,leaf in frontier]
            states[k]['nodes'].append(copy.copy(left))
            states[k]['zmin']=zmin

        # espansione del nodo 
        (left,right)=left.expand()

        # prossima iterazione
        k+=1
    
    # aggiungi nodo ottimo
    if display:
        states[k]={}
        states[k]['nodes']=[copy.copy(left)]

    xe=left.getRight().getX()
    return (xe, z[xe], k, pruned, states, z)

"""
Dimensione dell'heap: 
    Data l'altezza h nell'heap sono contenuti 2^(h+1)-1 nodi

IDEA:   eliminare i nodi che non soddisfano il limite e mantenere l'heap di dimensione costante.
        Con l'ordinando della struttura si spera di avere nella parte top (dal liv. 0 al livello hmax) 
        i nodi che sono di interesse.
"""
def strategy(heap,hmax,limit,key=lambda x: x):
    """
        h=0                    root
        h=1           n1                    n2       
        h=2    n3           n4       n5            n6
        ...  
        @h<hmax (ni>limit) .... 
        @h==hmax ni .....   
    """
    length=len(heap)
    if length <= 3: return 0

    # Ordinamento - O(n log n)
    heap[1:]=sorted(heap[1:], reverse=False, key=key)
    
    i=1
    h=1
    # O(log n)
    while i<length:
        if key(heap[i])>limit or h==hmax:
            del heap[i:]
            return length-i
        i=2*i+1
        h+=1
    return 0

    