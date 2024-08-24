import numpy as np
from scipy.integrate import odeint
from matplotlib.pyplot import figure
import matplotlib.pyplot as plot
import matplotlib.pyplot as plt
from colorspacious import cspace_converter
# import seaborn as sns
# sns.set()
#Flu
csfont = {'fontname':'Arial'}
#############################################################Antibody:
Data1 = np.loadtxt("/Users/suzan/Desktop/VW.txt")
Data2 = np.loadtxt("/Users/suzan/Desktop/VO.txt")

xdata1 = np.array([0.021098333,2.91018878,17.15370475,20.05633128,21.09605439,23.06551994,24.98129005,26.1613119,26.95041028,29.00561586,30.07503548])
ydata1 = np.array([5.255981602,3.830362723,2.753954067,1.49398991,1.990539705,2.15545892,1.492177042,2.121190531,1.767525832,1.512781584,1.512387933])
###
xdata2 = np.array([0.113244905,6.148943516,22.16358977,21.09390571,22.10575841,25.1686639,26.09847449])
ydata2 = np.array([8.775134041,6.123546728,2.543628912,1.510604049,1.511329392,1.513525023,1.514191554])
###
xdata3 = np.array([0.055345334,5.970597385,8.972935416,11.89007675,16.05580492,19.06650003,22.07836578,23.0081804,27.05580384,])
ydata3 = np.array([7.618203911,6.049329537,2.514606464,3.998999535,2.52842979,2.118549141,1.516039416,1.515044371,1.47860815])
###
xdata4 = np.array([0,7.917414722,11.04129264,14.00359066,15,16.02333932,19.03949731,22.89048474,24.04847397])
ydata4 = np.array([7.696113074,2.872791519,2.713780919,1.48409894,1.48409894,1.992932862,1.696113074,1.494699647,1.48409894])
###
xdata5 = np.array([0.049658667,3.140826729,6.042943911,8.975369057,12.06552991])
ydata5 = np.array([6.381062356,5.923787529,4.094688222,3.585450346,2.7852194])
###
xdata6 = np.array([0,7.145359019,10.06129597,13.02977233,16.07705779,19.01926445,22.01401051,])
ydata6 = np.array([7.20412844,7.20412844,6.306192661,2.951834862,3.767201835,2.693807339,3.344036697])
###

x1 = Data1[:, 0];x2 = Data2[:, 0];
y1 = Data1[:, 1];y2 = Data2[:, 1];

fig, ax = plot.subplots(figsize=(8,6))
#################################################
ax.scatter(xdata1, ydata1, color="Orange", s=200, alpha=1)
ax.scatter(xdata2, ydata2, color="red", s=200, alpha=1)
ax.scatter(xdata3, ydata3, color="black", s=200, alpha=1)
ax.scatter(xdata4, ydata4, color="brown", s=200, alpha=1)
ax.scatter(xdata5, ydata5, color="blue", s=200, alpha=1)
ax.scatter(xdata6, ydata6, color="green", s=200, alpha=1)
# # ax.plot(xdata1,ydata1,linewidth="4",color="#3C486B",alpha=1,label="Delta", linestyle="-")
# # ax.scatter(xdata2,10**ydata2, color="blue",s=200)
ax.plot(x1,y1,linewidth="4",label='Wuhan', color="#090580")
ax.plot(x2,y2,linewidth="4",label='Omicron', color="#F45050")
# ax.plot(x4,y4,linewidth="4",label="",color="#F45050",alpha=1)
# ax.plot(x6,y6,linewidth="4",label="900",color="brown",alpha=1)
####
ax.set_xlim(-1,30)
ax.set_ylabel('Viral load ($log_{10}(copies/ml)$)',**csfont,size=23)
# # ax.set_ylabel('Antibody (ng/ml)',**csfont,size=20)
ax.set_xlabel('Time (days)',**csfont,size=20)
ax.axhline(y=1.6, linewidth=3, color='gray',linestyle="--")
# ax.legend(shadow=True,fontsize=15,loc="upper right")
# ax.legend(fontsize=15,loc="upper right")
# # axs[1, 2].set_xlim(0, 60)
ax.tick_params(direction="in")
ax.tick_params(axis='both',labelsize=20)
# plot.grid()
# plt.savefig('/Users/suzan/Desktop/Primary.pdf')
plot.savefig('/Users/suzan/Desktop/Primary.pdf',bbox_inches='tight')
plot.show()
