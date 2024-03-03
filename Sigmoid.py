import numpy as np
import pylab
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# csfont = {'fontname':'Times New Roman'}
csfont = {'fontname':'Arial'}

def hill(x, Emax,h,IC):
     y = Emax*(x**h) / (x**h + (IC)**h);
     return y
###
def hill2(x2, Emax2,h2,IC2):
     y2 = Emax2*(x2**h2) / (x2**h2 + (IC2)**h2);
     return y2
###
def hill2(x5, Emax5,h5,IC2):
     y5 = Emax5*(x5**h5) / (x5**h5 + (IC2)**h5);
     return y5
#*********************************************Sotrovimab
# #Delta
xdata5 = np.array([0.017264505764316,0.05145913131625103,0.14789737787631366,0.4655691443990876,1.3876901004571855,4.061585988377001,12.554928080507748,
36.746619407367064,107.552510791864,326.4630187025598,990.9401630487145,3005.8825180431177,8488.945687061083])
ydata5 = np.array([0.18416206261508705,3.49907918968691,0.18416206261508705,2.762430939226533,1.8416206261510126,0.18416206261508705,3.1307550644567357,16.20626151012891,
28.54511970534068,55.432780847145466,71.27071823204417,79.18968692449353,82.68876611418044])
# #Omicron
# xdata4 = np.array([0.05145913131625103,0.15338071254240038,0.4741211488363367,1.3626595108583772,4.136192954523138,12.328467394420722,37.42161528285903,
# 113.58891949635583,326.46301870256116,990.9401630487145,8644.878489001881,8800,100000 ])
# ydata4 = np.array([0.18416206261511547,1.289134438305723,4.604051565377546,9.208103130755092,11.049723756906076,11.233885819521191,7.182320441988907,14.91712707182316,
# 25.23020257826886,48.80294659300182,75, 75, 75])
# ##
# xdata4s = np.array([0.05145913131625103,0.15338071254240038,0.4741211488363367,1.3626595108583772,4.136192954523138,12.328467394420722,37.42161528285903,
# 113.58891949635583,326.46301870256116,990.9401630487145,8644.878489001881])
# ydata4s = np.array([0.18416206261511547,1.289134438305723,4.604051565377546,9.208103130755092,11.049723756906076,11.233885819521191,7.182320441988907,14.91712707182316,
# 25.23020257826886,48.80294659300182,75])
####
#Whuhan
xdata3 = np.array([10**1.0550262514739006,10**1.225715830754423,10**1.690233261138792,10**1.9636053946326737,10**2.279738461858957,10**2.6275447491877153,10**3.1277466037751642,10**3.642509483813358])
ydata3 = np.array([0.19649538370433106,0.17765336060941195,0.13727759683453655,1.104052829443816,20.193713942199864,43.43893838658448,62.776237517159686,92.55821736516737])
#Omicron
xdata4 = np.array([10**1.0823914110770427,10**1.6833640565801784,10**2.2740433336729873,10**2.86275508786231,10**3.490172575102127,10**4.6935073596843075])
ydata4 = np.array([0.002834566894861723,0.023510231304371132,3.6717645642085017,19.546006132298302,35.83176011782906,83.1894435541393])
#Omicron
xdata4s = np.array([10**1.0823914110770427,10**1.6833640565801784,10**2.2740433336729873,10**2.86275508786231,10**3.490172575102127,10**4.073348586885033,10**4.6935073596843075,10**5.254607097533185])
ydata4s = np.array([0.002834566894861723,0.023510231304371132,3.6717645642085017,19.546006132298302,35.83176011782906,70.97224718164387,83.1894435541393,93.98206626958027])
# #
# popt, pcov = curve_fit(hill, xdata3, ydata3)
# popt5, pcov5 = curve_fit(hill, xdata5, ydata5)
# popt2, pcov2 = curve_fit(hill2, xdata4, ydata4)
#
# # x = np.linspace(-1, 12, 150)
# x = np.linspace(0, 10000000,10000000)#Delta
# y = hill(x, *popt)
# ###
# x2 = np.linspace(0, 10000000,10000000)#Omicron
# y2 = hill2(x2, *popt2)
# ###
# x5 = np.linspace(0, 10000000,10000000)#Omicron
# y5 = hill2(x5, *popt5)
#*********
try:
    # Fitting for xdata5
    popt5, pcov5 = curve_fit(hill, xdata3, ydata3)
    if pcov5 is not None:
        perr5 = np.sqrt(np.diag(pcov5))
        confidence_interval5 = 1.96 * perr5
        print("Confidence intervals for parameters from fit to xdata5:", confidence_interval5)
    else:
        print("Covariance matrix not returned for xdata3.")

    # Fitting for xdata4
    popt2, pcov2 = curve_fit(hill2, xdata4, ydata4)
    if pcov2 is not None:
        perr2 = np.sqrt(np.diag(pcov2))
        confidence_interval2 = 1.96 * perr2
        print("Confidence intervals for parameters from fit to xdata4:", confidence_interval2)
    else:
        print("Covariance matrix not returned for xdata4.")

except RuntimeError as e:
    print("An error occurred during curve fitting:", e)

# Use the correct variable names for plotting
x = np.linspace(0, 10000000, 10000000)  # Data range
y = hill(x, *popt5)  # Use popt5 here for xdata5 fitting

x2 = np.linspace(0, 10000000, 10000000)  # Data range
y2 = hill2(x2, *popt2)  # Use popt2 here for xdata4 fitting


# Data3 = np.loadtxt("/Users/suzan/Desktop/Viral/NAPd.txt")
# # Data4 = np.loadtxt("/Users/suzan/Desktop/Viral/NAPo.txt")
# x3 = Data3[:, 0];
# # x4 = Data4[:, 0];
# y3 = Data3[:, 1];
# y4 = Data4[:, 1];

pylab.plot(xdata3, ydata3,'o', label='Wuhan-Hu-1', color="#090580",markersize="10")
# pylab.plot(x,y, linewidth="3",color="black",label=r'fit: $E_{max}$=%5.3f, $h$=%5.3f, $IC_{50}=%5.3f$' % tuple(popt5))
pylab.plot(x,y, linewidth="3",color="#090580",label="")
###
# pylab.plot(xdata5, ydata5,'o', label='Wuhan', color="black",markersize="10")
# # pylab.plot(x,y, linewidth="3",color="black",label=r'fit: $E_{max}$=%5.3f, $h$=%5.3f, $IC_{50}=%5.3f$' % tuple(popt))
# pylab.plot(x5,y5, linewidth="3",color="black",label="")
###
pylab.plot(xdata4s, ydata4s,'o', label='B1.1.529(Omicron)', color="#F45050",markersize="10")
# pylab.plot(x2,y2, linewidth="3",color="blue",label=r'fit: $E_{max}$=%5.3f, $h$=%5.3f, $IC_{50}=%5.3f$' % tuple(popt2))
pylab.plot(x2,y2, linewidth="3",color="#F45050",label='')#Omicron
plt.xlabel(r'Antibody (ng/ml)',**csfont,size=20)
plt.ylabel('Neutralization (%)',**csfont,size=20)
plt.axhline(y=100, color='gray', linestyle='--')
# plt.xlabel(r'$Log_{10}(Antibody)$',**csfont,size=25)
# plt.xlabel('Antibody (ng/ml)',**csfont,size=20)
plt.xscale('log')
# plt.axhline(y = 100, color = 'gray', linestyle = '--')
plt.xticks(size = 20)
plt.yticks(size = 20)
plt.tick_params(which='both',direction="in")
pylab.legend(loc='best',fontsize=13)
##############
# plt.ylabel('Transmission rate', **csfont,fontsize=30);
plt.tick_params(direction="in")
# plt.grid()
plt.savefig('/Users/suzan/Desktop/Fit.pdf',bbox_inches='tight')
pylab.show()
