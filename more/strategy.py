""" 
    Approccio Naive:
    Assumendo che l'heap sia stato ordinato in senso CRESC.
    Iterare seguendo la direzione specificata (left,right) dalla root verso la leaf 
    piu' a left (o right) dell' heap.
    Questa visita per livelli della struttura permette di verificare la condizione: 
        heap[i]>limit 
    e di tagliare da heap[i:] in modo da:
    1. rendere non validi i nodi che non soddisfano la condizione
    2. ridurre le dimensioni della struttura
    
    Per l'assunzione di heap ordinato in senso CRESC il taglio e' safe perche'
    significa che al livello h:
        1.  heap[i]<=heap[k] per ogni k di liv. h dell'heap
            quindi se limit<heap[i] => limit<heap[k] 
        2.  heap[i]>limit => heap[2*i+1]>limit and heap[2*i+2]>limit
            per le proprieta' dell'heap (che si mantengono anche se si ordina la struttura)
            ma cio' vale per ogni sotto-albero a partire dai nodi di liv. h 
            e quindi dal liv. h -> hmax 
    quindi e' possibile ridurre le dimensioni dell'heap senza perdere nodi utili nella ricerca
    dell'ottimo.  

    La direzione di default e' visitare per ogni liv. h dell'heap
    il nodo piu' a sinistra ('left'). 
    
    La direzione 'right' si basa sull'idea di visitare per ogni liv. h dell'heap
    il nodo piu' a destra, quindi il nodo con Rmax su liv. h.
    Se si soddisfa la proprieta' per heap[i] significa che per heap[i+1] che punta al 
    nodo piu' a sinistra di livello h+1 vale che:
        limit<heap[i]<heap[i+1]
    e quindi al caso 'left'.

    Complessita': 
        Ordinamento: O(n log n)
        Iterazione: O(log n)
"""

def naive(heap,limit,key=lambda x: x,direction='left'):  
    if direction!='left' or direction!='right':
        return
    
    length=len(heap)
    if length <= 3:
        return
    
    # [ root left right x x x x ... ]

    # Ordinamento - O(n log n)
    heap[1:]=sorted(heap[1:], reverse=False, key=key)
    
    # index 
    i=1
    incr=lambda x: 2*x+1
    if direction=='right':
        i=2
        incr=lambda x: 2*x+2

    # O(log n)
    while i<length:
        if key(heap[i])>limit:
            del heap[i:]
            break
        incr(i)

"""
    Approccio cutoff:
    Iterare e invalidare i nodi che non soddisfano la condizione:
        heap[i]<limit
    Invalidare un nodo heap[i] significa modificare il valore dello 
    stesso e dei suoi figli diretti.

    Ad esempio per heap : int[] => replace(heap[i], inf)
"""
#invalid=lambda x : (float('inf'),x[1])
def cutoff(heap,limit,key=lambda x: x,replace=lambda x: None):
    length=len(heap)
    if length <= 3:
        return

    # altezza
    h=0
    hmin=-1
    # [root left right x x x x x]
    pdx=2
    # O(log n)
    while pdx<length:
        i=pdx
        psx=pdx//2
        counter=0
        h+=1
        # O(2^h)
        while i>=psx:
            if key(heap[i])>limit:
                heap[i]=replace(heap[i])
                if 2*i+2<length:
                    heap[2*i+2]=replace(heap[2*i+2])
                    heap[2*i+1]=replace(heap[2*i+1])
                elif 2*i+1<length:
                    heap[2*i+1]=replace(heap[2*i+1])
                # update counter
                counter+=1
                # update hmin first occur
                # top level cutoff
                if hmin<0:
                    hmin=h
            i-=1

        if counter==pdx-psx+1:
            # tutti i nodi di livello h sono stati invalidati
            # allora per le proprieta' dell'heap tutti i discendenti 
            # dei nodi di livello h non soddisfano la proprieta'
            # posso eliminare tutti i livelli da h->hmax
            del heap[psx:]
            return 
        pdx=2*pdx+2
    
    length=len(heap)
    # considero ultimo psx; se l'heap e' completo psx punta al liv hmax+1
    # altrimeti psx punta al liv hmax
    psx=pdx//2
    i=pdx//2
    counter=0
    if i<length:
        h+=1
    # O(2^hmax)
    while i<length:
        if key(heap[i])>limit:
            heap[i]=replace(heap[i])
            if 2*i+2<length:
                heap[2*i+2]=replace(heap[2*i+2])
                heap[2*i+1]=replace(heap[2*i+1])
            elif 2*i+1<length:
                heap[2*i+1]=replace(heap[2*i+1])
            counter+=1
            if hmin<0:
                hmin=h
        i+=1

    if counter==length-psx+1:
        del heap[psx:]
        return
    
    # delete out limit node
    if hmin>10:
        # O(n log n)
        heap[1:]=sorted(heap[1:],reverse=False,key=key)
        i=len(heap)-1
        while i>=1:
            if key(heap[i])<limit:
                # significa che heap[i+1] era >limit
                del heap[i+1:]
                return
            i-=1


def confident(heap,hmax,limit,key=lambda x: x):
    """
    Dimensione dell'heap: 
        Data l'altezza h nell'heap sono contenuti 2^(h+1)-1 nodi

    IDEA:   mantenere l'heap di dimensione costante.
            Con l'ordinando della struttura si spera di avere nella 
            parte top (dal liv. 0 al livello hmax) i nodi che si
            di maggiore interesse.
    """
    length=len(heap)
    if length <= 3:
        return
    
    if hmax == 0:
        return
    
    # [ root left right x x x x ... ]

    # Ordinamento - O(n log n)
    heap[1:]=sorted(heap[1:], reverse=False, key=key)
    
    # O(log n)
    h=1
    i=1
    while i<length:
        if key(heap[i]) > limit or h==hmax:
            del heap[i:]
            return
        i=2*i+1
        h+=1

def recursive(heap,limit,key=lambda x: x,replace=lambda x: None):
    def rec(k):
        if k>=len(heap):
            return
        heap[k]=replace(heap[k]) 
        rec(2*k+1)
        rec(2*k+2)
    
    length=len(heap)
    if length <= 3:
        return

    # [root left right x x x x x]
    pdx=2
    # O(log n)
    while pdx<length:
        i=pdx
        psx=pdx//2
        # O(2^h)
        while i>=psx:
            if key(heap[i])>limit and key(heap[i])<float('inf'):
                rec(i)
            i-=1
        pdx=2*pdx+2
    
    # O(n log n)
    heap[1:]=sorted(heap[1:],reverse=False,key=key)
    i=len(heap)-1
    while i>=1:
        if key(heap[i])<limit:
            # significa che heap[i+1] era >limit
            del heap[i+1:]
            return
        i-=1