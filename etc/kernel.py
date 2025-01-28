import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import *

def k(r):
    r2=r**2
    if 0.6>r2:
        return 8*(0.6-r2)**4
    return 0

fig=plt.figure(figsize=(4,4),layout="constrained") # inch
ax=fig.add_subplot()
#ax.set_ylabel("y")
ax.set_xlabel("r")

r=np.linspace(0,1,100)
y=[k(r) for r in r]
ax.plot(r,y)

ax.text(0.3,0.8,r"$k(r)$",fontsize=20)

ax.grid("on")
ax.set(ylim=(0,1.2))
ax.set(xlim=(0,1))
#ax.xaxis.set_major_locator(MultipleLocator(base=1.0))
#ax.yaxis.set_major_locator(MultipleLocator(base=1.0))
plt.savefig("kernel.svg")
plt.show()

