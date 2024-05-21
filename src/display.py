###################################### Pllotting #################################### 
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

from src.piyavskishubert import estx as valx
 
def display(xstar, ystar, k, L, states, z): 
    # Define figure and axes
    fig, ax = plt.subplots()   
    fig.set_figwidth(12)
    fig.set_figheight(6) 
    ax.plot([], [])

    # x,f(x) valutati dall'algoritmo
    xp=[]
    yp=[]
    for x in sorted(z.keys()):
        xp.append(x)
        yp.append(z.get(x))
        
    plt.plot(xp, yp, 'b-')
    plt.plot(xstar, ystar, 'ro')
    plt.title('Piyavski-Shubert')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)

    # Build slider
    axk=fig.add_axes([0.05, 0.0, 0.9, 0.03])
    k_slider=Slider(
        ax=axk,
        label='k',
        valmin=0,
        valmax=k,
        valinit=0,
        valstep=1,
        orientation='horizontal'
    )

    # Define update algorithm state@k
    def update(val):
        k1=k_slider.val
        if k1<0:
            return
        ax.clear()
        ax.plot(xp, yp, 'b-')
        ax.plot(xstar, ystar, 'ro')
    
        if k1==k:
            # ultima iterazione
            pass
        else:
            # k-esima iterazione
            for node in states[k1]['nodes']:
                x=node.getLeft().getX()
                y=node.getRight().getX()
                estx=node.getX()
                estR=node.getR()
                if node.getX() is None:
                    # non e' minorante per la k esima iterazione
                    # calcola estimate x per nodo non minorante
                    estx=valx(L,x,y,z[x],z[y])

                # punti su funzione
                ax.scatter(x,z[x],color='black')
                ax.scatter(y,z[y],color='black')
                
                # minorante
                ax.plot([x, estx], [z[x], estR], color='grey')
                ax.plot([estx, y], [estR, z[y]], color='grey')

                if node.getK()>=0:
                    ax.scatter(estx,estR,color='green')
                    ax.text(estx, estR, f'x{node.getK()+1}', fontsize=10, ha='left', va='bottom')
        
                # zmin
                ax.plot(xp,[states[k1]['zmin']]*len(xp), color='black')

        ax.set_title('Piyavski-Shubert')
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.grid(True)

        fig.canvas.draw_idle()
        fig.canvas.flush_events()

    k_slider.on_changed(update)
    plt.show()