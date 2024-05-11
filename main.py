from datetime import datetime
import inspect 

from src.display import display
from src.piyavskishubert import algorithm

from functions import f2 as f
from functions import t2 as params

##################################### Run ####################################   
(a,b,L)=params

toview=False
n=1000000000
eps=0.00001
h=10

if toview:
    n=10000
    eps=0.00001
    h=10

t=datetime.now()
(xstar, ystar, k, pruned, states, z) = algorithm(f, a, b, L, h, n, eps, display=toview)
t=datetime.now()-t

print("-------------------------------------------------------------------")
print()
print(f"Piyavski Schubert per {inspect.getsourcelines(f)[0][0].split('=')[0]} in [{a},{b}] con L={L}")
print(f"con eps={eps} e n={n}")
print(f"con hmax={h} e {pruned} nodi potati")
print()
print(f"(xstar,ystar): ({xstar},{ystar})")
print()
print(f"k: {k}")
print(f"time: {t}")
print(f"mode: {toview}")
print()
print("-------------------------------------------------------------------")

if toview:
    display(xstar, ystar, k, L, states, z)
