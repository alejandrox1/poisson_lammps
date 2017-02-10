import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

n3="P8_3_D3.txt"
n7="P8_7_D3.txt"
n15="P8_15_D3.txt"

p3 = np.genfromtxt(n3)
p7 = np.genfromtxt(n7)
p15 = np.genfromtxt(n15)

markers = ['s', 'o', 'v', 's', '+', '>']
harmonics = ['P8-3-D3', 'P8-7-D3', 'P8-15-D3']


fig = plt.figure()#figsize=(16,26))
#ax = fig.add_subplot(111)
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)


#ax1 = plt.subplot(221)
#ax1.plot(p3[:,0], p3[:,1], marker=markers[0], color="black", ls='--', label="P8-3")
ax1.bar(p3[:,0], p3[:,1], width=0.5 , color="black", align='center')
ax1.set_title('P8-3')
ax1.set_xticks(p3[:,0])
ax1.set_yticks(np.arange(min(p3[:,1])-0.1, max(p3[:,1])+0.25, 0.15))
ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax1.legend(loc='best')

ax2.bar(p7[:,0], p7[:,1], width=0.5 , color="black", align='center')
ax2.set_title('P8-7')
ax2.set_xticks(p7[:,0])
ax2.set_yticks(np.arange(min(p7[:,1])-0, max(p7[:,1])+0.25, 0.2))
ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax2.legend(loc='best')

ax3.bar(p15[:,0], p15[:,1], width=0.5 , color="black", align='center')
ax3.set_title('P8-15')
ax3.set_xticks(p15[:,0])
ax3.set_yticks(np.arange(min(p15[:,1]), max(p15[:,1]), 0.1))
ax3.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax3.legend(loc='best')


ax3.legend(loc='best')

ax1.axhline(y=0.00,xmin=0,xmax=3,c="black",linewidth=1.5,zorder=0)
ax2.axhline(y=0.00,xmin=0,xmax=3,c="black",linewidth=1.5,zorder=0)
ax3.axhline(y=0.00,xmin=0,xmax=3,c="black",linewidth=1.5,zorder=0)


fig.text(0.04, 0.5, "Poisson's Ratio", ha='center', va='center', rotation='vertical', fontsize=18)
plt.xlabel("Number of STW Defects", fontsize=18)


plt.savefig("poisson.png", dpi=300)
#plt.show()
