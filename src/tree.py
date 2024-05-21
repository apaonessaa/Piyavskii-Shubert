class BinaryTree:  
    def __init__(self):
        """
            Ogni nodo x dell'albero binario oltre agli attributi parent, sx e dx
            contiene informazioni quali:
                - left, right: riferimenti ai nodi che delimitano x => [left, x, right]
                - R : minorante 
                - x : stima di xt
                - k : iterazione di espansione del nodo 

            Il concetto di espansione si basa sull'idea di dato x compreso nell'intervallo [y x z]
            generare due nodi v e w che saranno figli di x (e quindi generati da x) e che rispettivamente
            ricadranno nell'intervallo [x.left v x] e [x w x.right] => [y v x] e [x w z].
            
            Di conseguenza, sara' necessario anche modificare lo stato del nodo x espanso che sara' contenuto
            nell'intervallo [v x w].
            
            Questa strategia permette di avere un albero binario tale per cui:
                1) i nodi foglia sono nodi che potrebbero essere espansi
                2) i nodi non foglia sono nodi gia' espansi alla nodo.getK() iterazione
        """
        self.parent : BinaryTree=None
        self.sx : BinaryTree=None
        self.dx : BinaryTree=None

        self.left : BinaryTree=None
        self.right : BinaryTree=None
        self.R : float=None
        self.x : float=None
        self.k : int=-1

    def setSx(self, child):
        if child is None:
            return
        if not isinstance(child, type(self)):
            return
        child.parent=self
        self.sx=child
        return self

    def setDx(self, child):
        if child is None:
            return
        if not isinstance(child, type(self)):
            return
        child.parent=self
        self.dx=child
        return self
        
    def getSx(self):
        return self.sx
    
    def getDx(self):
        return self.dx
    
    def getParent(self):
        return self.parent

    def setLeft(self, left):
        self.left=left
        return self

    def setRight(self, right):
        self.right=right
        return self
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def setR(self, R):
        self.R=R
        return self
    
    def setX(self,x):
        self.x=x
        return self
    
    def setK(self,k):
        self.k=k
        return self
    
    def getR(self):
        return self.R
    
    def getX(self):
        return self.x
    
    def getK(self):
        return self.k
    
    def expand(self):
        """
            Espansione del nodo x:
                                    parent(x)
                        [x]                         x   
                left        right           x               x
    
                            parent(x)
                    x                           [x]   
                x       x               left           right

            Oltre a modificare lo stato del nodo x e' necessario, se esiste
            aggiornare anche lo stato del nodo parent(x).

            Nello specifico, sara' necessario aggiornare l'estremo di definzione
            dell'intervallo in cui e' compreso parent(x) a seconda del caso:

                1.  se x e' figlio sinistro di parent(x) allora cambia parent(x).left con right
                    cioe' [x parent(x) ?] => [right parent(x) ?]

                2.  se x e' figlio destro di parent(x) allora cambia parent(x).right con left 
                    cioe' [x parent(x) ?] => [right parent(x) ?]
        """
        left=BinaryTree().setLeft(self.left).setRight(self)
        right=BinaryTree().setLeft(self).setRight(self.right)
        
        # aggiorna figli e intervallo di x 
        self.setSx(left).setDx(right)
        self.setLeft(left).setRight(right)

        # aggiorna intervallo di parent(x)
        parent=self.getParent()
        if parent is not None:
            if parent.getSx() == self:
                parent.setLeft(right)
            else:
                parent.setRight(left)
        return (left, right)
    
    def expansionOrder(self, kmax):
        """
            Visita per livelli dell'albero in ordine di espansione.
            Si considerano solo i nodi con k!=None fino a kmax iterazioni.
        """
        ret=[None]*kmax
        queue=[self]
        while len(queue)!=0:
            curr=queue.pop(0)
            if curr.getK()>=0 and curr.getK()<kmax:
                ret[curr.getK()]=curr
                if curr.getSx() is not None:
                    queue.append(curr.getSx())
                if curr.getDx() is not None:
                    queue.append(curr.getDx())
        return ret

    def __str__(self):
        left=self.getLeft().getX() if self.getLeft() is not None else ""
        right=self.getRight().getX() if self.getRight() is not None else ""
        return f"<left={left}, right={right}> [R={self.getR()},x={self.getX()}]"
    
    def __cmp__(self, other):
        """ 
            confronto per valore di R 
            e per valore di X se gli R sono coincidenti.
        """
        if self.getR() > other.getR():
            return 1
        if self.getR() < other.getR():
            return -1
        if self.getRight().getX() < other.getRight().getX():
            return -1
        if self.getRight().getX() > other.getRight().getX():
            return 1
        return 0     
    
    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, BinaryTree):
            return False
        if self is other:
            return True
        if self.getRight().getX() is not None and other.getRight().getX() is not None:
            return self.__cmp__(other)==0
        return False
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __le__(self, other):
        if other is None:
            return False
        if not isinstance(other, BinaryTree):
            return False
        if self.getRight().getX() is not None and other.getRight().getX() is not None:
            return self.__cmp__(other)<=0
        return self.getR()<=other.getR()

    def __lt__(self, other):
        if other is None:
            return False
        if not isinstance(other, BinaryTree):
            return False
        if self.getRight().getX() is not None and other.getRight().getX() is not None:
            return self.__cmp__(other)<0
        return self.getR()<=other.getR()

    def __ge__(self, other):
        if other is None:
            return False
        if not isinstance(other, BinaryTree):
            return False
        if self.getRight().getX() is not None and other.getRight().getX() is not None:
            return self.__cmp__(other)>=0
        return self.getR()>=other.getR()
    
    def __gt__(self, other):
        if other is None:
            return False
        if not isinstance(other, BinaryTree):
            return False
        if self.getRight().getX() is not None and other.getRight().getX() is not None:
            return self.__cmp__(other)>0
        return self.getR()>other.getR()
    

        
    


    
        

        

        