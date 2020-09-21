#-- GEO1001.2020--hw01
#-- Özge Tufan
#-- 5263719

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats
from scipy.stats import gaussian_kde
import xlsxwriter

df_A = pd.read_excel("/Users/Asus/Desktop/hw01/HEAT - A_final.xls", header = 3, skiprows = range(4,5))
df_B = pd.read_excel("/Users/Asus/Desktop/hw01/HEAT - B_final.xls", header = 3, skiprows = range(4,5))
df_C = pd.read_excel("/Users/Asus/Desktop/hw01/HEAT - C_final.xls", header = 3, skiprows = range(4,5))
df_D = pd.read_excel("/Users/Asus/Desktop/hw01/HEAT - D_final.xls", header = 3, skiprows = range(4,5))
df_E = pd.read_excel("/Users/Asus/Desktop/hw01/HEAT - E_final.xls", header = 3, skiprows = range(4,5))

#Part 1
#Mean
print(df_A.mean())
print(df_B.mean())
print(df_C.mean())
print(df_D.mean())
print(df_E.mean())
#Variance
print(df_A.var())
print(df_B.var())
print(df_C.var())
print(df_D.var())
print(df_E.var())
#Standard Deviation
print(df_A.std())
print(df_B.std())
print(df_C.std())
print(df_D.std())
print(df_E.std())

workbook = xlsxwriter.Workbook('Mean_Statistics.xlsx')
worksheet = workbook.add_worksheet()
cell_format = workbook.add_format({'bold': True, 'font_color': 'black'})
worksheet.write('A1', 'Variables', cell_format)
worksheet.write('A2', 'Direction ‚ True')
worksheet.write('A3', 'Wind Speed')
worksheet.write('A4', 'Crosswind Speed')
worksheet.write('A5', 'Headwind Speed')
worksheet.write('A6', 'Temperature')
worksheet.write('A7', 'Globe Temperature')
worksheet.write('A8', 'Wind Chill')
worksheet.write('A9', 'Relative Humidity')
worksheet.write('A10', 'Heat Stress Index')
worksheet.write('A11', 'Dew Point')
worksheet.write('A12', 'Psychro Wet Bulb Temperature')
worksheet.write('A13', 'Station Pressure')
worksheet.write('A14', 'Barometric Pressure')
worksheet.write('A15', 'Altitude')
worksheet.write('A16', 'Density Altitude')
worksheet.write('A17', 'NA Wet Bulb Temperature')
worksheet.write('A18', 'WBGT')
worksheet.write('A19', 'TWL')
worksheet.write('A20', 'Direction ‚ Mag')
worksheet.write('B1', 'Mean - Sensor A', cell_format)
worksheet.write('B2', df_A.mean()[0])
worksheet.write('B3', df_A.mean()[1])
worksheet.write('B4', df_A.mean()[2])
worksheet.write('B5', df_A.mean()[3])
worksheet.write('B6', df_A.mean()[4])
worksheet.write('B7', df_A.mean()[5])
worksheet.write('B8', df_A.mean()[6])
worksheet.write('B9', df_A.mean()[7])
worksheet.write('B10', df_A.mean()[8])
worksheet.write('B11', df_A.mean()[9])
worksheet.write('B12', df_A.mean()[10])
worksheet.write('B13', df_A.mean()[11])
worksheet.write('B14', df_A.mean()[12])
worksheet.write('B15', df_A.mean()[13])
worksheet.write('B16', df_A.mean()[14])
worksheet.write('B17', df_A.mean()[15])
worksheet.write('B18', df_A.mean()[16])
worksheet.write('B19', df_A.mean()[17])
worksheet.write('B20', df_A.mean()[18])
worksheet.write('C1', 'Mean - Sensor B', cell_format)
worksheet.write('C2', df_B.mean()[0])
worksheet.write('C3', df_B.mean()[1])
worksheet.write('C4', df_B.mean()[2])
worksheet.write('C5', df_B.mean()[3])
worksheet.write('C6', df_B.mean()[4])
worksheet.write('C7', df_B.mean()[5])
worksheet.write('C8', df_B.mean()[6])
worksheet.write('C9', df_B.mean()[7])
worksheet.write('C10', df_B.mean()[8])
worksheet.write('C11', df_B.mean()[9])
worksheet.write('C12', df_B.mean()[10])
worksheet.write('C13', df_B.mean()[11])
worksheet.write('C14', df_B.mean()[12])
worksheet.write('C15', df_B.mean()[13])
worksheet.write('C16', df_B.mean()[14])
worksheet.write('C17', df_B.mean()[15])
worksheet.write('C18', df_B.mean()[16])
worksheet.write('C19', df_B.mean()[17])
worksheet.write('C20', df_B.mean()[18])
worksheet.write('D1', 'Mean - Sensor C', cell_format)
worksheet.write('D2', df_C.mean()[0])
worksheet.write('D3', df_C.mean()[1])
worksheet.write('D4', df_C.mean()[2])
worksheet.write('D5', df_C.mean()[3])
worksheet.write('D6', df_C.mean()[4])
worksheet.write('D7', df_C.mean()[5])
worksheet.write('D8', df_C.mean()[6])
worksheet.write('D9', df_C.mean()[7])
worksheet.write('D10', df_C.mean()[8])
worksheet.write('D11', df_C.mean()[9])
worksheet.write('D12', df_C.mean()[10])
worksheet.write('D13', df_C.mean()[11])
worksheet.write('D14', df_C.mean()[12])
worksheet.write('D15', df_C.mean()[13])
worksheet.write('D16', df_C.mean()[14])
worksheet.write('D17', df_C.mean()[15])
worksheet.write('D18', df_C.mean()[16])
worksheet.write('D19', df_C.mean()[17])
worksheet.write('D20', df_C.mean()[18])
worksheet.write('E1', 'Mean - Sensor D', cell_format)
worksheet.write('E2', df_D.mean()[0])
worksheet.write('E3', df_D.mean()[1])
worksheet.write('E4', df_D.mean()[2])
worksheet.write('E5', df_D.mean()[3])
worksheet.write('E6', df_D.mean()[4])
worksheet.write('E7', df_D.mean()[5])
worksheet.write('E8', df_D.mean()[6])
worksheet.write('E9', df_D.mean()[7])
worksheet.write('E10', df_D.mean()[8])
worksheet.write('E11', df_D.mean()[9])
worksheet.write('E12', df_D.mean()[10])
worksheet.write('E13', df_D.mean()[11])
worksheet.write('E14', df_D.mean()[12])
worksheet.write('E15', df_D.mean()[13])
worksheet.write('E16', df_D.mean()[14])
worksheet.write('E17', df_D.mean()[15])
worksheet.write('E18', df_D.mean()[16])
worksheet.write('E19', df_D.mean()[17])
worksheet.write('E20', df_D.mean()[18])
worksheet.write('F1', 'Mean - Sensor E', cell_format)
worksheet.write('F2', df_E.mean()[0])
worksheet.write('F3', df_E.mean()[1])
worksheet.write('F4', df_E.mean()[2])
worksheet.write('F5', df_E.mean()[3])
worksheet.write('F6', df_E.mean()[4])
worksheet.write('F7', df_E.mean()[5])
worksheet.write('F8', df_E.mean()[6])
worksheet.write('F9', df_E.mean()[7])
worksheet.write('F10', df_E.mean()[8])
worksheet.write('F11', df_E.mean()[9])
worksheet.write('F12', df_E.mean()[10])
worksheet.write('F13', df_E.mean()[11])
worksheet.write('F14', df_E.mean()[12])
worksheet.write('F15', df_E.mean()[13])
worksheet.write('F16', df_E.mean()[14])
worksheet.write('F17', df_E.mean()[15])
worksheet.write('F18', df_E.mean()[16])
worksheet.write('F19', df_E.mean()[17])
worksheet.write('F20', df_E.mean()[18])
worksheet.write('G1', 'Variance - Sensor A', cell_format)
worksheet.write('G2', df_A.var()[0])
worksheet.write('G3', df_A.var()[1])
worksheet.write('G4', df_A.var()[2])
worksheet.write('G5', df_A.var()[3])
worksheet.write('G6', df_A.var()[4])
worksheet.write('G7', df_A.var()[5])
worksheet.write('G8', df_A.var()[6])
worksheet.write('G9', df_A.var()[7])
worksheet.write('G10', df_A.var()[8])
worksheet.write('G11', df_A.var()[9])
worksheet.write('G12', df_A.var()[10])
worksheet.write('G13', df_A.var()[11])
worksheet.write('G14', df_A.var()[12])
worksheet.write('G15', df_A.var()[13])
worksheet.write('G16', df_A.var()[14])
worksheet.write('G17', df_A.var()[15])
worksheet.write('G18', df_A.var()[16])
worksheet.write('G19', df_A.var()[17])
worksheet.write('G20', df_A.var()[18])
worksheet.write('H1', 'Variance - Sensor B', cell_format)
worksheet.write('H2', df_B.var()[0])
worksheet.write('H3', df_B.var()[1])
worksheet.write('H4', df_B.var()[2])
worksheet.write('H5', df_B.var()[3])
worksheet.write('H6', df_B.var()[4])
worksheet.write('H7', df_B.var()[5])
worksheet.write('H8', df_B.var()[6])
worksheet.write('H9', df_B.var()[7])
worksheet.write('H10', df_B.var()[8])
worksheet.write('H11', df_B.var()[9])
worksheet.write('H12', df_B.var()[10])
worksheet.write('H13', df_B.var()[11])
worksheet.write('H14', df_B.var()[12])
worksheet.write('H15', df_B.var()[13])
worksheet.write('H16', df_B.var()[14])
worksheet.write('H17', df_B.var()[15])
worksheet.write('H18', df_B.var()[16])
worksheet.write('H19', df_B.var()[17])
worksheet.write('H20', df_B.var()[18])
worksheet.write('I1', 'Variance - Sensor C', cell_format)
worksheet.write('I2', df_C.var()[0])
worksheet.write('I3', df_C.var()[1])
worksheet.write('I4', df_C.var()[2])
worksheet.write('I5', df_C.var()[3])
worksheet.write('I6', df_C.var()[4])
worksheet.write('I7', df_C.var()[5])
worksheet.write('I8', df_C.var()[6])
worksheet.write('I9', df_C.var()[7])
worksheet.write('I10', df_C.var()[8])
worksheet.write('I11', df_C.var()[9])
worksheet.write('I12', df_C.var()[10])
worksheet.write('I13', df_C.var()[11])
worksheet.write('I14', df_C.var()[12])
worksheet.write('I15', df_C.var()[13])
worksheet.write('I16', df_C.var()[14])
worksheet.write('I17', df_C.var()[15])
worksheet.write('I18', df_C.var()[16])
worksheet.write('I19', df_C.var()[17])
worksheet.write('I20', df_C.var()[18])
worksheet.write('J1', 'Variance - Sensor D', cell_format)
worksheet.write('J2', df_D.var()[0])
worksheet.write('J3', df_D.var()[1])
worksheet.write('J4', df_D.var()[2])
worksheet.write('J5', df_D.var()[3])
worksheet.write('J6', df_D.var()[4])
worksheet.write('J7', df_D.var()[5])
worksheet.write('J8', df_D.var()[6])
worksheet.write('J9', df_D.var()[7])
worksheet.write('J10', df_D.var()[8])
worksheet.write('J11', df_D.var()[9])
worksheet.write('J12', df_D.var()[10])
worksheet.write('J13', df_D.var()[11])
worksheet.write('J14', df_D.var()[12])
worksheet.write('J15', df_D.var()[13])
worksheet.write('J16', df_D.var()[14])
worksheet.write('J17', df_D.var()[15])
worksheet.write('J18', df_D.var()[16])
worksheet.write('J19', df_D.var()[17])
worksheet.write('J20', df_D.var()[18])
worksheet.write('K1', 'Variance - Sensor E', cell_format)
worksheet.write('K2', df_E.var()[0])
worksheet.write('K3', df_E.var()[1])
worksheet.write('K4', df_E.var()[2])
worksheet.write('K5', df_E.var()[3])
worksheet.write('K6', df_E.var()[4])
worksheet.write('K7', df_E.var()[5])
worksheet.write('K8', df_E.var()[6])
worksheet.write('K9', df_E.var()[7])
worksheet.write('K10', df_E.var()[8])
worksheet.write('K11', df_E.var()[9])
worksheet.write('K12', df_E.var()[10])
worksheet.write('K13', df_E.var()[11])
worksheet.write('K14', df_E.var()[12])
worksheet.write('K15', df_E.var()[13])
worksheet.write('K16', df_E.var()[14])
worksheet.write('K17', df_E.var()[15])
worksheet.write('K18', df_E.var()[16])
worksheet.write('K19', df_E.var()[17])
worksheet.write('K20', df_E.var()[18])
worksheet.write('L1', 'Standard Deviation - Sensor A', cell_format)
worksheet.write('L2', df_A.std()[0])
worksheet.write('L3', df_A.std()[1])
worksheet.write('L4', df_A.std()[2])
worksheet.write('L5', df_A.std()[3])
worksheet.write('L6', df_A.std()[4])
worksheet.write('L7', df_A.std()[5])
worksheet.write('L8', df_A.std()[6])
worksheet.write('L9', df_A.std()[7])
worksheet.write('L10', df_A.std()[8])
worksheet.write('L11', df_A.std()[9])
worksheet.write('L12', df_A.std()[10])
worksheet.write('L13', df_A.std()[11])
worksheet.write('L14', df_A.std()[12])
worksheet.write('L15', df_A.std()[13])
worksheet.write('L16', df_A.std()[14])
worksheet.write('L17', df_A.std()[15])
worksheet.write('L18', df_A.std()[16])
worksheet.write('L19', df_A.std()[17])
worksheet.write('L20', df_A.std()[18])
worksheet.write('M1', 'Standard Deviation - Sensor B', cell_format)
worksheet.write('M2', df_B.std()[0])
worksheet.write('M3', df_B.std()[1])
worksheet.write('M4', df_B.std()[2])
worksheet.write('M5', df_B.std()[3])
worksheet.write('M6', df_B.std()[4])
worksheet.write('M7', df_B.std()[5])
worksheet.write('M8', df_B.std()[6])
worksheet.write('M9', df_B.std()[7])
worksheet.write('M10', df_B.std()[8])
worksheet.write('M11', df_B.std()[9])
worksheet.write('M12', df_B.std()[10])
worksheet.write('M13', df_B.std()[11])
worksheet.write('M14', df_B.std()[12])
worksheet.write('M15', df_B.std()[13])
worksheet.write('M16', df_B.std()[14])
worksheet.write('M17', df_B.std()[15])
worksheet.write('M18', df_B.std()[16])
worksheet.write('M19', df_B.std()[17])
worksheet.write('M20', df_B.std()[18])
worksheet.write('N1', 'Standard Deviation - Sensor C', cell_format)
worksheet.write('N2', df_C.std()[0])
worksheet.write('N3', df_C.std()[1])
worksheet.write('N4', df_C.std()[2])
worksheet.write('N5', df_C.std()[3])
worksheet.write('N6', df_C.std()[4])
worksheet.write('N7', df_C.std()[5])
worksheet.write('N8', df_C.std()[6])
worksheet.write('N9', df_C.std()[7])
worksheet.write('N10', df_C.std()[8])
worksheet.write('N11', df_C.std()[9])
worksheet.write('N12', df_C.std()[10])
worksheet.write('N13', df_C.std()[11])
worksheet.write('N14', df_C.std()[12])
worksheet.write('N15', df_C.std()[13])
worksheet.write('N16', df_C.std()[14])
worksheet.write('N17', df_C.std()[15])
worksheet.write('N18', df_C.std()[16])
worksheet.write('N19', df_C.std()[17])
worksheet.write('N20', df_C.std()[18])
worksheet.write('O1', 'Standard Deviation - Sensor D', cell_format)
worksheet.write('O2', df_D.std()[0])
worksheet.write('O3', df_D.std()[1])
worksheet.write('O4', df_D.std()[2])
worksheet.write('O5', df_D.std()[3])
worksheet.write('O6', df_D.std()[4])
worksheet.write('O7', df_D.std()[5])
worksheet.write('O8', df_D.std()[6])
worksheet.write('O9', df_D.std()[7])
worksheet.write('O10', df_D.std()[8])
worksheet.write('O11', df_D.std()[9])
worksheet.write('O12', df_D.std()[10])
worksheet.write('O13', df_D.std()[11])
worksheet.write('O14', df_D.std()[12])
worksheet.write('O15', df_D.std()[13])
worksheet.write('O16', df_D.std()[14])
worksheet.write('O17', df_D.std()[15])
worksheet.write('O18', df_D.std()[16])
worksheet.write('O19', df_D.std()[17])
worksheet.write('O20', df_D.std()[18])
worksheet.write('P1', 'Standard Deviation - Sensor E', cell_format)
worksheet.write('P2', df_E.std()[0])
worksheet.write('P3', df_E.std()[1])
worksheet.write('P4', df_E.std()[2])
worksheet.write('P5', df_E.std()[3])
worksheet.write('P6', df_E.std()[4])
worksheet.write('P7', df_E.std()[5])
worksheet.write('P8', df_E.std()[6])
worksheet.write('P9', df_E.std()[7])
worksheet.write('P10', df_E.std()[8])
worksheet.write('P11', df_E.std()[9])
worksheet.write('P12', df_E.std()[10])
worksheet.write('P13', df_E.std()[11])
worksheet.write('P14', df_E.std()[12])
worksheet.write('P15', df_E.std()[13])
worksheet.write('P16', df_E.std()[14])
worksheet.write('P17', df_E.std()[15])
worksheet.write('P18', df_E.std()[16])
worksheet.write('P19', df_E.std()[17])
worksheet.write('P20', df_E.std()[18])
workbook.close()

dataA = df_A["Temperature"]
dataB = df_B["Temperature"]
dataC = df_C["Temperature"]
dataD = df_D["Temperature"]
dataE = df_E["Temperature"]

dataAWS = df_A["Wind Speed"]
dataBWS = df_B["Wind Speed"]
dataCWS = df_C["Wind Speed"]
dataDWS = df_D["Wind Speed"]
dataEWS = df_E["Wind Speed"]

dataAWD = df_A["Direction ‚ True"]
dataBWD = df_B["Direction ‚ True"]
dataCWD = df_C["Direction ‚ True"]
dataDWD = df_D["Direction ‚ True"]
dataEWD = df_E["Direction ‚ True"]

#Histogram with 5 bins
fs=12
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=1, ncols=5, sharey="all", gridspec_kw=None, figsize=(10,6))
def hist1(data, x, title):
    sns.distplot(data['Temperature'], hist=True, kde=False, bins=5, color = 'blue', hist_kws={'edgecolor':'black'}, ax=x)
    x.set_title(title, fontsize=fs)
    x.set_xlabel('Temperature (°C)')
    
ax1.set_ylabel('Frequency')
hist1(df_A, ax1, 'Sensor A')
hist1(df_B, ax2, 'Sensor B') 
hist1(df_C, ax3, 'Sensor C')
hist1(df_D, ax4, 'Sensor D')
hist1(df_E, ax5, 'Sensor E')
plt.suptitle('Histograms with 5 Bins')
plt.tight_layout()
plt.show()


#Histogram with 50 bins
fs=12
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=1, ncols=5, sharey="all", gridspec_kw=None, figsize=(10,6))
def hist1(data, x, title):
    sns.distplot(data['Temperature'], hist=True, kde=False, bins=50, color = 'blue', hist_kws={'edgecolor':'black'}, ax=x)
    x.set_title(title, fontsize=fs)
    x.set_xlabel('Temperature (°C)')
    
ax1.set_ylabel('Frequency')
hist1(df_A, ax1, 'Sensor A')
hist1(df_B, ax2, 'Sensor B') 
hist1(df_C, ax3, 'Sensor C')
hist1(df_D, ax4, 'Sensor D')
hist1(df_E, ax5, 'Sensor E')
plt.suptitle('Histograms with 50 Bins')
plt.tight_layout()
plt.show()


#Frequency polygons
fig = plt.figure(figsize=(21,6))
fs = 14
ax1= fig.add_subplot(111)
[frequencyA,binsA]=np.histogram(dataA, bins=50)
[frequencyB,binsB]=np.histogram(dataB, bins=50)
[frequencyC,binsC]=np.histogram(dataC, bins=50)
[frequencyD,binsD]=np.histogram(dataD, bins=50)
[frequencyE,binsE]=np.histogram(dataE, bins=50)
ax1.plot(binsA[:-1],frequencyA)
ax1.plot(binsB[:-1],frequencyB)
ax1.plot(binsC[:-1],frequencyC)
ax1.plot(binsD[:-1],frequencyD)
ax1.plot(binsE[:-1],frequencyE)
ax1.set_ylabel('Frequency',fontsize=fs)
ax1.set_xlabel('Temperature (°C)',fontsize=fs)
ax1.tick_params(labelsize=fs)
ax1.legend(['Sensor A', 'Sensor B', 'Sensor C', 'Sensor D', 'Sensor E'])
plt.suptitle('Frequency Polygons')
plt.show()

#Boxplots
fig = plt.figure(figsize=(16, 6))
fs = 14
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)
WS = [dataAWS, dataBWS, dataCWS, dataDWS, dataEWS]
ax1.boxplot(WS, showmeans=True)
ax1.set_ylabel('Wind Speed [m/s] ',fontsize=fs)
ax1.set_xlabel('Sensors A - E', fontsize=fs)
ax1.tick_params(labelsize=fs)
WD = [dataAWD, dataBWD, dataCWD, dataDWD, dataEWD]
ax2.boxplot(WD, showmeans=True)
ax2.set_ylabel('Wind Direction [$^{\circ}$]', fontsize=fs)
ax2.set_xlabel('Sensors A - E', fontsize=fs)
ax2.tick_params(labelsize=fs)
T = [dataA, dataB, dataC, dataD, dataE]
ax3.boxplot(T, showmeans=True)
ax3.set_ylabel('Temperature (°C)',fontsize=fs)
ax3.set_xlabel('Sensors A - E', fontsize=fs)
ax3.tick_params(labelsize=fs)
plt.tight_layout()
plt.show()

#Part 2
# plot PMF
fs=12
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=1, ncols=5, sharey='all', gridspec_kw=None, figsize=(21,6))
def pmf(data, x, title, col):
    df_pmf = (data.value_counts())/len(data)
    x.bar((df_pmf.sort_index()).index, df_pmf.sort_index(), color=col)
    x.set_title(title, fontsize=fs)
    x.set_xlabel('Temperature (°C)', fontsize=fs)
    
pmf(dataA, ax1, 'Sensor A', 'b')
pmf(dataB, ax2, 'Sensor B', 'g')
pmf(dataC, ax3, 'Sensor C', 'c')
pmf(dataD, ax4, 'Sensor D', 'm')
pmf(dataE, ax5, 'Sensor E', 'r')
ax1.set_ylabel('Probability', fontsize=fs)
fig.suptitle('Probability Mass Functions')
plt.show()

# #plot CDF
nb=50
fs=12
fig = plt.figure(figsize=(17,6))
ax1 = fig.add_subplot(151)
ax2 = fig.add_subplot(152)
ax3 = fig.add_subplot(153)
ax4 = fig.add_subplot(154)
ax5 = fig.add_subplot(155)
a1=ax1.hist(x=dataA.astype(float),bins=nb, cumulative=True, density=True, color='b',alpha=0.7, rwidth=0.85)
ax1.plot(a1[1][1:]-(a1[1][1:]-a1[1][:-1])/2,a1[0], color='k')
ax1.set_xlabel('Temperature (°C)', fontsize=fs)
ax1.set_ylabel('CDF', fontsize=fs)
ax1.set_title('Sensor A', fontsize=fs)
ax1.tick_params(labelsize=fs)
a2=ax2.hist(x=dataB.astype(float),bins=nb, cumulative=True, density=True, color='b',alpha=0.7, rwidth=0.85)
ax2.plot(a2[1][1:]-(a2[1][1:]-a2[1][:-1])/2,a2[0], color='k')
ax2.set_xlabel('Temperature (°C)', fontsize=fs)
ax2.set_title('Sensor B', fontsize=fs)
ax2.tick_params(labelsize=fs)
a3=ax3.hist(x=dataC.astype(float),bins=nb, cumulative=True, density=True, color='b',alpha=0.7, rwidth=0.85)
ax3.plot(a3[1][1:]-(a3[1][1:]-a3[1][:-1])/2,a3[0], color='k')
ax3.set_xlabel('Temperature (°C)', fontsize=fs)
ax3.set_title('Sensor C', fontsize=fs)
ax3.tick_params(labelsize=fs)
a4=ax4.hist(x=dataD.astype(float),bins=nb, cumulative=True, density=True, color='b',alpha=0.7, rwidth=0.85)
ax4.plot(a4[1][1:]-(a4[1][1:]-a4[1][:-1])/2,a4[0], color='k')
ax4.set_xlabel('Temperature (°C)', fontsize=fs)
ax4.set_title('Sensor D', fontsize=fs)
ax4.tick_params(labelsize=fs)
a5=ax5.hist(x=dataE.astype(float),bins=nb, cumulative=True, density=True, color='b',alpha=0.7, rwidth=0.85)
ax5.plot(a5[1][1:]-(a5[1][1:]-a5[1][:-1])/2,a5[0], color='k')
ax5.set_xlabel('Temperature (°C)', fontsize=fs)
ax5.set_title('Sensor E', fontsize=fs)
ax5.tick_params(labelsize=fs)
plt.suptitle('Cumulative Density Functions')
plt.tight_layout()
plt.show()

#plot PDF
fs=12
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=1, ncols=5, sharey='all', gridspec_kw=None, figsize=(21,6))
def pdf(data, x, title, col):
    x.hist(x=data.astype(float),bins=50, density=True, color=col,alpha=0.7, rwidth=0.85)
    sns.distplot(data.astype(float), color='k',ax=x)
    x.set_title(title, fontsize=fs)
    x.set_xlabel('Temperature (°C)', fontsize=fs)
    
pdf(dataA, ax1, 'Sensor A', 'b')
pdf(dataB, ax2, 'Sensor B', 'g')
pdf(dataC, ax3, 'Sensor C', 'c')
pdf(dataD, ax4, 'Sensor D', 'm')
pdf(dataE, ax5, 'Sensor E', 'r')
ax1.set_ylabel('Probability Density', fontsize=fs)
fig.suptitle('Probability Density Functions for Temperature Values')
plt.show()


#Wind Speed PDF
nb = 50
fs = 12 
fig = plt.figure(figsize=(17,6))
ax1 = fig.add_subplot(151)
ax2 = fig.add_subplot(152)
ax3 = fig.add_subplot(153)
ax4 = fig.add_subplot(154)
ax5 = fig.add_subplot(155)
a1=ax1.hist(x=dataAWS.astype(float),bins=nb, density=True, color='b',alpha=0.7, rwidth=0.85)
sns.distplot(dataAWS.astype(float), color='k',ax=ax1)
ax1.set_xlabel('Wind Speed [m/s]', fontsize=fs)
ax1.set_ylabel('Probability Density', fontsize=fs)
a2=ax2.hist(x=dataBWS.astype(float),bins=nb, density=True, color='b',alpha=0.7, rwidth=0.85)
sns.distplot(dataBWS.astype(float), color='k',ax=ax2)
ax2.set_xlabel('Wind Speed [m/s]', fontsize=fs)
a3=ax3.hist(x=dataCWS.astype(float),bins=nb, density=True, color='b',alpha=0.7, rwidth=0.85)
sns.distplot(dataCWS.astype(float), color='k',ax=ax3)
ax3.set_xlabel('Wind Speed [m/s]', fontsize=fs)
a4=ax4.hist(x=dataDWS.astype(float),bins=nb, density=True, color='b',alpha=0.7, rwidth=0.85)
sns.distplot(dataDWS.astype(float), color='k',ax=ax4)
ax4.set_xlabel('Wind Speed [m/s]', fontsize=fs)
a5=ax5.hist(x=dataEWS.astype(float),bins=nb, density=True, color='b',alpha=0.7, rwidth=0.85)
sns.distplot(dataEWS.astype(float), color='k',ax=ax5)
ax5.set_xlabel('Wind Speed [m/s]', fontsize=fs)
fig.suptitle('Probability Density Functions for Wind Speed Values')
plt.tight_layout()
plt.show()

#Kernel Density Estimation
fs=12
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=1, ncols=5, gridspec_kw=None, figsize=(10,6))
def kde(data, x, title):
    sns.distplot(data['Wind Speed'], hist=True, kde=True, bins=50, color='darkblue', ax=x)
    x.set_title(title, fontsize=fs)
    x.set_xlabel('Windspeed [m/s]')
    
kde(df_A, ax1,'Sensor A with PDF')
kde(df_B, ax2,'Sensor B with PDF')
kde(df_C, ax3,'Sensor C with PDF')
kde(df_D, ax4,'Sensor D with PDF')
kde(df_E, ax5,'Sensor E with PDF')
ax1.set_ylabel('Density') 
fig.suptitle('Kernel Density Estimation for Wind Speed Values')
plt.tight_layout()
plt.show()

#Part 3
#Correlation Temperature A - B 
#First remove nan values
dataA = dataA[~np.isnan(dataA)]
dataB = dataB[~np.isnan(dataB)]

#Find the length of datasets
# print(len(dataA))
# print(len(dataB))

#Compute coefficients
pearsAB = stats.pearsonr(dataA, dataB)[0]
spearAB = stats.spearmanr(dataA, dataB)[0]
print(pearsAB, spearAB)
print(np.cov(dataA, dataB))

#Correlation Temperature A - C
dataA = dataA[~np.isnan(dataA)]
dataC = dataC[~np.isnan(dataC)]

#Find the length of datasets
print(len(dataA))
print(len(dataC))

# Interpolate to equal size samples
dataA1 = np.interp(np.linspace(0,len(dataC),len(dataC)),np.linspace(0,len(dataA),len(dataA)),dataA)

#Compute coefficients
pearsAC = stats.pearsonr(dataA1, dataC)[0]
spearAC = stats.spearmanr(dataA1, dataC)[0]
print(pearsAC, spearAC)
print(np.cov(dataA1, dataC))

#Correlation Temperature A - D
dataA = dataA[~np.isnan(dataA)]
dataD = dataD[~np.isnan(dataD)]

#Find the length of datasets
print(len(dataA))
print(len(dataD))

# Interpolate to equal size samples
dataA1 = np.interp(np.linspace(0,len(dataD),len(dataD)),np.linspace(0,len(dataA),len(dataA)),dataA)

#Compute coefficients
pearsAD = stats.pearsonr(dataA1, dataD)[0]
spearAD = stats.spearmanr(dataA1, dataD)[0]
print(pearsAD, spearAD)
print(np.cov(dataA1, dataD))

#Correlation Temperature A - E
dataA = dataA[~np.isnan(dataA)]
dataE = dataE[~np.isnan(dataE)]

#Find the length of datasets
print(len(dataA))
print(len(dataE))

# Interpolate to equal size samples
dataA1 = np.interp(np.linspace(0,len(dataE),len(dataE)),np.linspace(0,len(dataA),len(dataA)),dataA)

#Compute coefficients
pearsAE = stats.pearsonr(dataA1, dataE)[0]
spearAE = stats.spearmanr(dataA1, dataE)[0]
print(pearsAE, spearAE)
print(np.cov(dataA1, dataE))

#Correlation Temperature B - C
dataB = dataB[~np.isnan(dataB)]
dataC = dataC[~np.isnan(dataC)]

#Find the length of datasets
print(len(dataB))
print(len(dataC))

# Interpolate to equal size samples
dataB1 = np.interp(np.linspace(0,len(dataC),len(dataC)),np.linspace(0,len(dataB),len(dataB)),dataB)

#Compute coefficients
pearsBC = stats.pearsonr(dataB1, dataC)[0]
spearBC = stats.spearmanr(dataB1, dataC)[0]
print(pearsBC, spearBC)
print(np.cov(dataB1, dataC))

#Correlation Temperature B - D
dataB = dataB[~np.isnan(dataB)]
dataD = dataD[~np.isnan(dataD)]

#Find the length of datasets
print(len(dataB))
print(len(dataD))

# Interpolate to equal size samples
dataB1 = np.interp(np.linspace(0,len(dataD),len(dataD)),np.linspace(0,len(dataB),len(dataB)),dataB)

#Compute coefficients
pearsBD = stats.pearsonr(dataB1, dataD)[0]
spearBD = stats.spearmanr(dataB1, dataD)[0]
print(pearsBD, spearBD)
print(np.cov(dataB1, dataD))

#Correlation Temperature B - E
dataB = dataB[~np.isnan(dataB)]
dataE = dataE[~np.isnan(dataE)]

#Find the length of datasets
print(len(dataB))
print(len(dataE))

# Interpolate to equal size samples
dataB1 = np.interp(np.linspace(0,len(dataE),len(dataE)),np.linspace(0,len(dataB),len(dataB)),dataB)

#Compute coefficients
pearsBE = stats.pearsonr(dataB1, dataE)[0]
spearBE = stats.spearmanr(dataB1, dataE)[0]
print(pearsBE, spearBE)
print(np.cov(dataB1, dataE))

#Correlation Temperature C - D
dataC = dataC[~np.isnan(dataC)]
dataD = dataD[~np.isnan(dataD)]

#Find the length of datasets
print(len(dataC))
print(len(dataD))

#Compute coefficients
pearsCD = stats.pearsonr(dataC, dataD)[0]
spearCD = stats.spearmanr(dataC, dataD)[0]
print(pearsCD, spearCD)
print(np.cov(dataC, dataD))


#Correlation Temperature C - E
dataC = dataC[~np.isnan(dataC)]
dataE = dataE[~np.isnan(dataE)]

#Find the length of datasets
print(len(dataC))
print(len(dataE))

# Interpolate to equal size samples
dataC1 = np.interp(np.linspace(0,len(dataE),len(dataE)),np.linspace(0,len(dataC),len(dataC)),dataC)

#Compute coefficients
pearsCE = stats.pearsonr(dataC1, dataE)[0]
spearCE = stats.spearmanr(dataC1, dataE)[0]
print(pearsCE, spearCE)
print(np.cov(dataC1, dataE))

#Correlation Temperature D - E
dataD = dataD[~np.isnan(dataD)]
dataE = dataE[~np.isnan(dataE)]

#Find the length of datasets
print(len(dataD))
print(len(dataE))

# Interpolate to equal size samples
dataD1 = np.interp(np.linspace(0,len(dataE),len(dataE)),np.linspace(0,len(dataD),len(dataD)),dataD)

#Compute coefficients
pearsDE = stats.pearsonr(dataD1, dataE)[0]
spearDE = stats.spearmanr(dataD1, dataE)[0]
print(pearsDE, spearDE)
print(np.cov(dataD1, dataE))

#Wet Bulb Globe Temperature Coefficients
dataAWBG = df_A["WBGT"]
dataBWBG = df_B["WBGT"]
dataCWBG = df_C["WBGT"]
dataDWBG = df_D["WBGT"]
dataEWBG = df_E["WBGT"]

#Correlation WBGT A - B 
#First remove nan values
dataAWBG = dataAWBG[~np.isnan(dataAWBG)]
dataBWBG = dataBWBG[~np.isnan(dataBWBG)]

#Find the length of datasets
# print(len(dataAWBG))
# print(len(dataBWBG))

# Compute coefficients
pearsABW = stats.pearsonr(dataAWBG, dataBWBG)[0]
spearABW = stats.spearmanr(dataAWBG, dataBWBG)[0]
print(pearsABW, spearABW)
print(np.cov(dataAWBG, dataBWBG))


#Correlation WBGT A - C
dataAWBG = dataAWBG[~np.isnan(dataAWBG)]
dataCWBG = dataCWBG[~np.isnan(dataCWBG)]

#Find the length of datasets
# print(len(dataAWBG))
# print(len(dataCWBG))

# Interpolate to equal size samples
dataAWBG1 = np.interp(np.linspace(0,len(dataCWBG),len(dataCWBG)),np.linspace(0,len(dataAWBG),len(dataAWBG)),dataAWBG)

#Compute coefficients
pearsACW = stats.pearsonr(dataAWBG1, dataCWBG)[0]
spearACW = stats.spearmanr(dataAWBG1, dataCWBG)[0]
print(pearsACW, spearACW)
print(np.cov(dataAWBG1, dataCWBG))


# Correlation WBGT A - D
dataAWBG = dataAWBG[~np.isnan(dataAWBG)]
dataDWBG = dataDWBG[~np.isnan(dataDWBG)]

# Find the length of datasets
# print(len(dataAWBG))
# print(len(dataDWBG))

# Interpolate to equal size samples
dataAWBG1 = np.interp(np.linspace(0,len(dataDWBG),len(dataDWBG)),np.linspace(0,len(dataAWBG),len(dataAWBG)),dataAWBG)

# Compute coefficients
pearsADW = stats.pearsonr(dataAWBG1, dataDWBG)[0]
spearADW = stats.spearmanr(dataAWBG1, dataDWBG)[0]
print(pearsADW, spearADW)
print(np.cov(dataAWBG1, dataDWBG))


#Correlation WBGT A - E
dataAWBG = dataAWBG[~np.isnan(dataAWBG)]
dataEWBG = dataEWBG[~np.isnan(dataEWBG)]

# Find the length of datasets
# print(len(dataAWBG))
# print(len(dataEWBG))

# Interpolate to equal size samples
dataAWBG1 = np.interp(np.linspace(0,len(dataEWBG),len(dataEWBG)),np.linspace(0,len(dataAWBG),len(dataAWBG)),dataAWBG)

#Compute coefficients
pearsAEW = stats.pearsonr(dataAWBG1, dataEWBG)[0]
spearAEW = stats.spearmanr(dataAWBG1, dataEWBG)[0]
print(pearsAEW, spearAEW)
print(np.cov(dataAWBG1, dataEWBG))


#Correlation WBGT B - C
dataBWBG = dataBWBG[~np.isnan(dataBWBG)]
dataCWBG = dataCWBG[~np.isnan(dataCWBG)]

#Find the length of datasets
# print(len(dataBWBG))
# print(len(dataCWBG))

# Interpolate to equal size samples
dataBWBG1 = np.interp(np.linspace(0,len(dataCWBG),len(dataCWBG)),np.linspace(0,len(dataBWBG),len(dataBWBG)),dataBWBG)

#Compute coefficients
pearsBCW = stats.pearsonr(dataBWBG1, dataCWBG)[0]
spearBCW = stats.spearmanr(dataBWBG1, dataCWBG)[0]
print(pearsBCW, spearBCW)
print(np.cov(dataBWBG1, dataCWBG))


#Correlation WBGT B - D
dataBWBG = dataBWBG[~np.isnan(dataBWBG)]
dataDWBG = dataDWBG[~np.isnan(dataDWBG)]

#Find the length of datasets
# print(len(dataBWBG))
# print(len(dataDWBG))

# Interpolate to equal size samples
dataBWBG1 = np.interp(np.linspace(0,len(dataDWBG),len(dataDWBG)),np.linspace(0,len(dataBWBG),len(dataBWBG)),dataBWBG)

#Compute coefficients
pearsBDW = stats.pearsonr(dataBWBG1, dataDWBG)[0]
spearBDW = stats.spearmanr(dataBWBG1, dataDWBG)[0]
print(pearsBDW, spearBDW)
print(np.cov(dataBWBG1, dataDWBG))


#Correlation WBGT B - E
dataBWBG = dataBWBG[~np.isnan(dataBWBG)]
dataEWBG = dataEWBG[~np.isnan(dataEWBG)]

#Find the length of datasets
# print(len(dataBWBG))
# print(len(dataEWBG))

# Interpolate to equal size samples
dataBWBG1 = np.interp(np.linspace(0,len(dataEWBG),len(dataEWBG)),np.linspace(0,len(dataBWBG),len(dataBWBG)),dataBWBG)

#Compute coefficients
pearsBEW = stats.pearsonr(dataBWBG1, dataEWBG)[0]
spearBEW = stats.spearmanr(dataBWBG1, dataEWBG)[0]
print(pearsBEW, spearBEW)
print(np.cov(dataBWBG1, dataEWBG))


#Correlation WBGT C - D
dataCWBG = dataCWBG[~np.isnan(dataCWBG)]
dataDWBG = dataDWBG[~np.isnan(dataDWBG)]

#Find the length of datasets
# print(len(dataCWBG))
# print(len(dataDWBG))

#Compute coefficients
pearsCDW = stats.pearsonr(dataCWBG, dataDWBG)[0]
spearCDW = stats.spearmanr(dataCWBG, dataDWBG)[0]
print(pearsCDW, spearCDW)
print(np.cov(dataCWBG, dataDWBG))


#Correlation WBGT C - E
dataCWBG = dataCWBG[~np.isnan(dataCWBG)]
dataEWBG = dataEWBG[~np.isnan(dataEWBG)]

#Find the length of datasets
# print(len(dataCWBG))
# print(len(dataEWBG))

# Interpolate to equal size samples
dataCWBG1 = np.interp(np.linspace(0,len(dataEWBG),len(dataEWBG)),np.linspace(0,len(dataCWBG),len(dataCWBG)),dataCWBG)

#Compute coefficients
pearsCEW = stats.pearsonr(dataCWBG1, dataEWBG)[0]
spearCEW = stats.spearmanr(dataCWBG1, dataEWBG)[0]
print(pearsCEW, spearCEW)
print(np.cov(dataCWBG1, dataEWBG))


#Correlation WBGT D - E
dataDWBG = dataDWBG[~np.isnan(dataDWBG)]
dataEWBG = dataEWBG[~np.isnan(dataEWBG)]

#Find the length of datasets
# print(len(dataDWBG))
# print(len(dataEWBG))

# Interpolate to equal size samples
dataDWBG1 = np.interp(np.linspace(0,len(dataEWBG),len(dataEWBG)),np.linspace(0,len(dataDWBG),len(dataDWBG)),dataDWBG)

#Compute coefficients
pearsDEW = stats.pearsonr(dataDWBG1, dataEWBG)[0]
spearDEW = stats.spearmanr(dataDWBG1, dataEWBG)[0]
print(pearsDEW, spearDEW)
print(np.cov(dataDWBG1, dataEWBG))


#Crosswind Speed Coefficients
dataACS = df_A["Crosswind Speed"]
dataBCS = df_B["Crosswind Speed"]
dataCCS = df_C["Crosswind Speed"]
dataDCS = df_D["Crosswind Speed"]
dataECS = df_E["Crosswind Speed"]


#Correlation CS A - B 
#First remove nan values
dataACS = dataACS[~np.isnan(dataACS)]
dataBCS = dataBCS[~np.isnan(dataBCS)]

#Find the length of datasets
# print(len(dataA))
# print(len(dataB))

#Compute coefficients
pearsABC = stats.pearsonr(dataACS, dataBCS)[0]
spearABC = stats.spearmanr(dataACS, dataBCS)[0]
print(pearsABC, spearABC)
print(np.cov(dataACS, dataBCS))


#Correlation CS A - C
dataACS = dataACS[~np.isnan(dataACS)]
dataCCS = dataCCS[~np.isnan(dataCCS)]

#Find the length of datasets
# print(len(dataACS))
# print(len(dataCCS))

# Interpolate to equal size samples
dataACS1 = np.interp(np.linspace(0,len(dataCCS),len(dataCCS)),np.linspace(0,len(dataACS),len(dataACS)),dataACS)

#Compute coefficients
pearsACC = stats.pearsonr(dataACS1, dataCCS)[0]
spearACC = stats.spearmanr(dataACS1, dataCCS)[0]
print(pearsACC, spearACC)
print(np.cov(dataACS1, dataCCS))


#Correlation CS A - D
dataACS = dataACS[~np.isnan(dataACS)]
dataDCS = dataDCS[~np.isnan(dataDCS)]

#Find the length of datasets
# print(len(dataACS))
# print(len(dataDCS))

# Interpolate to equal size samples
dataACS1 = np.interp(np.linspace(0,len(dataDCS),len(dataDCS)),np.linspace(0,len(dataACS),len(dataACS)),dataACS)

#Compute coefficients
pearsADC = stats.pearsonr(dataACS1, dataDCS)[0]
spearADC = stats.spearmanr(dataACS1, dataDCS)[0]
print(pearsADC, spearADC)
print(np.cov(dataACS1, dataDCS))


#Correlation CS A - E
dataACS = dataACS[~np.isnan(dataACS)]
dataECS = dataECS[~np.isnan(dataECS)]

#Find the length of datasets
# print(len(dataACS))
# print(len(dataECS))

# Interpolate to equal size samples
dataACS1 = np.interp(np.linspace(0,len(dataECS),len(dataECS)),np.linspace(0,len(dataACS),len(dataACS)),dataACS)

#Compute coefficients
pearsAEC = stats.pearsonr(dataACS1, dataECS)[0]
spearAEC = stats.spearmanr(dataACS1, dataECS)[0]
print(pearsAEC, spearAEC)
print(np.cov(dataACS1, dataECS))


#Correlation CS B - C
dataBCS = dataBCS[~np.isnan(dataBCS)]
dataCCS = dataCCS[~np.isnan(dataCCS)]

#Find the length of datasets
# print(len(dataBCS))
# print(len(dataCCS))

# Interpolate to equal size samples
dataBCS1 = np.interp(np.linspace(0,len(dataCCS),len(dataCCS)),np.linspace(0,len(dataBCS),len(dataBCS)),dataBCS)

#Compute coefficients
pearsBCC = stats.pearsonr(dataBCS1, dataCCS)[0]
spearBCC = stats.spearmanr(dataBCS1, dataCCS)[0]
print(pearsBCC, spearBCC)
print(np.cov(dataBCS1, dataCCS))


#Correlation CS B - D
dataBCS = dataBCS[~np.isnan(dataBCS)]
dataDCS = dataDCS[~np.isnan(dataDCS)]

#Find the length of datasets
# print(len(dataBCS))
# print(len(dataDCS))

# Interpolate to equal size samples
dataBCS1 = np.interp(np.linspace(0,len(dataDCS),len(dataDCS)),np.linspace(0,len(dataBCS),len(dataBCS)),dataBCS)

#Compute coefficients
pearsBDC = stats.pearsonr(dataBCS1, dataDCS)[0]
spearBDC = stats.spearmanr(dataBCS1, dataDCS)[0]
print(pearsBDC, spearBDC)
print(np.cov(dataBCS1, dataDCS))


#Correlation CS B - E
dataBCS = dataBCS[~np.isnan(dataBCS)]
dataECS = dataECS[~np.isnan(dataECS)]

#Find the length of datasets
# print(len(dataBCS))
# print(len(dataECS))

# Interpolate to equal size samples
dataBCS1 = np.interp(np.linspace(0,len(dataECS),len(dataECS)),np.linspace(0,len(dataBCS),len(dataBCS)),dataBCS)

#Compute coefficients
pearsBEC = stats.pearsonr(dataBCS1, dataECS)[0]
spearBEC = stats.spearmanr(dataBCS1, dataECS)[0]
print(pearsBEC, spearBEC)
print(np.cov(dataBCS1, dataECS))


#Correlation CS C - D
dataCCS = dataCCS[~np.isnan(dataCCS)]
dataDCS = dataDCS[~np.isnan(dataDCS)]

#Find the length of datasets
# print(len(dataCCS))
# print(len(dataDCS))

#Compute coefficients
pearsCDC = stats.pearsonr(dataCCS, dataDCS)[0]
spearCDC = stats.spearmanr(dataCCS, dataDCS)[0]
print(pearsCDC, spearCDC)
print(np.cov(dataCCS, dataDCS))


#Correlation CS C - E
dataCCS = dataCCS[~np.isnan(dataCCS)]
dataECS = dataECS[~np.isnan(dataECS)]

#Find the length of datasets
# print(len(dataCCS))
# print(len(dataECS))

# Interpolate to equal size samples
dataCCS1 = np.interp(np.linspace(0,len(dataECS),len(dataECS)),np.linspace(0,len(dataCCS),len(dataCCS)),dataCCS)

#Compute coefficients
pearsCEC = stats.pearsonr(dataCCS1, dataECS)[0]
spearCEC = stats.spearmanr(dataCCS1, dataECS)[0]
print(pearsCEC, spearCEC)
print(np.cov(dataCCS1, dataECS))


#Correlation CS D - E
dataDCS = dataDCS[~np.isnan(dataDCS)]
dataECS = dataECS[~np.isnan(dataECS)]

#Find the length of datasets
# print(len(dataDCS))
# print(len(dataECS))

# Interpolate to equal size samples
dataDCS1 = np.interp(np.linspace(0,len(dataECS),len(dataECS)),np.linspace(0,len(dataDCS),len(dataDCS)),dataDCS)

#Compute coefficients
pearsDEC = stats.pearsonr(dataDCS1, dataECS)[0]
spearDEC = stats.spearmanr(dataDCS1, dataECS)[0]
print(pearsDEC, spearDEC)
print(np.cov(dataDCS1, dataECS))


#Strip Plot
pears = [pearsAB, pearsAC, pearsAD, pearsAE, pearsBC, pearsBD, pearsBE, pearsCD, pearsCE, pearsDE]
spear = [spearAB, spearAC, spearAD, spearAE, spearBC, spearBD, spearBE, spearCD, spearCE, spearDE]
list1 = ['AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD', 'CE', 'DE']
list2 = ['AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD', 'CE', 'DE']
dict1 = {'Sensor Pairs':list1, 'Pearson':pears}
dict2 = {'Sensor Pairs':list2, 'Spearman':spear}
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

#Strip plot
fig=plt.figure()

ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)

sns.stripplot(x='Sensor Pairs', y='Pearson', data=df1, ax=ax1)
sns.stripplot(x='Sensor Pairs', y='Spearman', data=df2, ax=ax2)

ax1.set_ylabel('Pearson Correlation')
ax1.set_xlabel('Sensor Pairs')
ax2.set_ylabel('Spearman Correlation')
ax2.set_xlabel('Sensor Pairs')
plt.suptitle('Temperature Coefficients')

plt.show()


#WBGT Strip Plot
pears = [pearsABW, pearsACW, pearsADW, pearsAEW, pearsBCW, pearsBDW, pearsBEW, pearsCDW, pearsCEW, pearsDEW]
spear = [spearABW, spearACW, spearADW, spearAEW, spearBCW, spearBDW, spearBEW, spearCDW, spearCEW, spearDEW]
list1 = ['AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD', 'CE', 'DE']
list2 = ['AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD', 'CE', 'DE']
dict1 = {'Sensor Pairs':list1, 'Pearson':pears}
dict2 = {'Sensor Pairs':list2, 'Spearman':spear}
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

#Strip plot
fig=plt.figure()

ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)

sns.stripplot(x='Sensor Pairs', y='Pearson', data=df1, ax=ax1)
sns.stripplot(x='Sensor Pairs', y='Spearman', data=df2, ax=ax2)

ax1.set_ylabel('Pearson Correlation')
ax1.set_xlabel('Sensor Pairs')
ax2.set_ylabel('Spearman Correlation')
ax2.set_xlabel('Sensor Pairs')
plt.suptitle('Wet Bulb Globe Temperature Coefficients')

plt.show()


#Crosswind Strip Plot
pears = [pearsABC, pearsACC, pearsADC, pearsAEC, pearsBCC, pearsBDC, pearsBEC, pearsCDC, pearsCEC, pearsDEC]
spear = [spearABC, spearACC, spearADC, spearAEC, spearBCC, spearBDC, spearBEC, spearCDC, spearCEC, spearDEC]
list1 = ['AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD', 'CE', 'DE']
list2 = ['AB', 'AC', 'AD', 'AE', 'BC', 'BD', 'BE', 'CD', 'CE', 'DE']
dict1 = {'Sensor Pairs':list1, 'Pearson':pears}
dict2 = {'Sensor Pairs':list2, 'Spearman':spear}
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

fig=plt.figure()

ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)

sns.stripplot(x='Sensor Pairs', y='Pearson', data=df1, ax=ax1)
sns.stripplot(x='Sensor Pairs', y='Spearman', data=df2, ax=ax2)

ax1.set_ylabel('Pearson Correlation')
ax1.set_xlabel('Sensor Pairs')
ax2.set_ylabel('Spearman Correlation')
ax2.set_xlabel('Sensor Pairs')
plt.suptitle('Crosswind Speed Coefficients')

plt.show()

#Part 4
#plot CDF -Temperature
nb=50
fs=12
fig = plt.figure(figsize=(17,6))
ax1 = fig.add_subplot(151)
ax2 = fig.add_subplot(152)
ax3 = fig.add_subplot(153)
ax4 = fig.add_subplot(154)
ax5 = fig.add_subplot(155)
a1=ax1.hist(x=dataA.astype(float),bins=nb, cumulative=True, color='b',alpha=0.7, rwidth=0.85)
ax1.plot(a1[1][1:]-(a1[1][1:]-a1[1][:-1])/2,a1[0], color='k')
ax1.set_xlabel('Temperature (°C)', fontsize=fs)
ax1.set_ylabel('CDF', fontsize=fs)
ax1.set_title('Sensor A', fontsize=fs)
ax1.tick_params(labelsize=fs)
a2=ax2.hist(x=dataB.astype(float),bins=nb, cumulative=True, color='b',alpha=0.7, rwidth=0.85)
ax2.plot(a2[1][1:]-(a2[1][1:]-a2[1][:-1])/2,a2[0], color='k')
ax2.set_xlabel('Temperature (°C)', fontsize=fs)
ax2.set_title('Sensor B', fontsize=fs)
ax2.tick_params(labelsize=fs)
a3=ax3.hist(x=dataC.astype(float),bins=nb, cumulative=True, color='b',alpha=0.7, rwidth=0.85)
ax3.plot(a3[1][1:]-(a3[1][1:]-a3[1][:-1])/2,a3[0], color='k')
ax3.set_xlabel('Temperature (°C)', fontsize=fs)
ax3.set_title('Sensor C', fontsize=fs)
ax3.tick_params(labelsize=fs)
a4=ax4.hist(x=dataD.astype(float),bins=nb, cumulative=True, color='b',alpha=0.7, rwidth=0.85)
ax4.plot(a4[1][1:]-(a4[1][1:]-a4[1][:-1])/2,a4[0], color='k')
ax4.set_xlabel('Temperature (°C)', fontsize=fs)
ax4.set_title('Sensor D', fontsize=fs)
ax4.tick_params(labelsize=fs)
a5=ax5.hist(x=dataE.astype(float),bins=nb, cumulative=True, color='b',alpha=0.7, rwidth=0.85)
ax5.plot(a5[1][1:]-(a5[1][1:]-a5[1][:-1])/2,a5[0], color='k')
ax5.set_xlabel('Temperature (°C)', fontsize=fs)
ax5.set_title('Sensor E', fontsize=fs)
ax5.tick_params(labelsize=fs)
fig.suptitle('Cumulative Density Functions for Temperature Values')
plt.tight_layout()
plt.show()

#plot CDF - Wind Speed
nb=50
fs=12
fig = plt.figure(figsize=(17,6))
ax1 = fig.add_subplot(151)
ax2 = fig.add_subplot(152)
ax3 = fig.add_subplot(153)
ax4 = fig.add_subplot(154)
ax5 = fig.add_subplot(155)
a1=ax1.hist(x=dataAWS.astype(float),bins=nb, cumulative=True, density=True, color='b',alpha=0.7, rwidth=0.85)
ax1.plot(a1[1][1:]-(a1[1][1:]-a1[1][:-1])/2,a1[0], color='k')
ax1.set_xlabel('Wind Speed [m/s]', fontsize=fs)
ax1.set_ylabel('CDF', fontsize=fs)
ax1.set_title('Sensor A', fontsize=fs)
ax1.tick_params(labelsize=fs)
a2=ax2.hist(x=dataBWS.astype(float),bins=nb, cumulative=True, density=True, color='b',alpha=0.7, rwidth=0.85)
ax2.plot(a2[1][1:]-(a2[1][1:]-a2[1][:-1])/2,a2[0], color='k')
ax2.set_xlabel('Wind Speed [m/s]', fontsize=fs)
ax2.set_title('Sensor B', fontsize=fs)
ax2.tick_params(labelsize=fs)
a3=ax3.hist(x=dataCWS.astype(float),bins=nb, cumulative=True, density=True, color='b',alpha=0.7, rwidth=0.85)
ax3.plot(a3[1][1:]-(a3[1][1:]-a3[1][:-1])/2,a3[0], color='k')
ax3.set_xlabel('Wind Speed [m/s]', fontsize=fs)
ax3.set_title('Sensor C', fontsize=fs)
ax3.tick_params(labelsize=fs)
a4=ax4.hist(x=dataDWS.astype(float),bins=nb, cumulative=True, density=True, color='b',alpha=0.7, rwidth=0.85)
ax4.plot(a4[1][1:]-(a4[1][1:]-a4[1][:-1])/2,a4[0], color='k')
ax4.set_xlabel('Wind Speed [m/s]', fontsize=fs)
ax4.set_title('Sensor D', fontsize=fs)
ax4.tick_params(labelsize=fs)
a5=ax5.hist(x=dataEWS.astype(float),bins=nb, cumulative=True, density=True, color='b',alpha=0.7, rwidth=0.85)
ax5.plot(a5[1][1:]-(a5[1][1:]-a5[1][:-1])/2,a5[0], color='k')
ax5.set_xlabel('Wind Speed [m/s]', fontsize=fs)
ax5.set_title('Sensor E', fontsize=fs)
ax5.tick_params(labelsize=fs)
fig.suptitle('Cumulative Density Functions for Wind Speed Values')
plt.tight_layout()
plt.show()

#Confidence Intervals

#TempA 
conf_level = 0.95
deg_freedomA = dataA.size - 1
meanA = dataA.mean()
errorA = stats.sem(dataA)
conf_intA = stats.t.interval(conf_level, deg_freedomA, meanA, errorA)
print(conf_intA)

#TempB
conf_level = 0.95
deg_freedomB = dataB.size - 1
meanB = dataB.mean()
errorB = stats.sem(dataB)
conf_intB = stats.t.interval(conf_level, deg_freedomB, meanB, errorB)
print(conf_intB)

#TempC
conf_level = 0.95
deg_freedomC = dataC.size - 1
meanC = dataC.mean()
errorC = stats.sem(dataC)
conf_intC = stats.t.interval(conf_level, deg_freedomC, meanC, errorC)
print(conf_intC)

#TempD
conf_level = 0.95
deg_freedomD = dataD.size - 1
meanD = dataD.mean()
errorD = stats.sem(dataD)
conf_intD = stats.t.interval(conf_level, deg_freedomD, meanD, errorD)
print(conf_intD)

#TempE
conf_level = 0.95
deg_freedomE = dataE.size - 1
meanE = dataE.mean()
errorE = stats.sem(dataE)
conf_intE = stats.t.interval(conf_level, deg_freedomE, meanE, errorE)
print(conf_intE)

#WindA
conf_level = 0.95
deg_freedomA = dataAWS.size - 1
meanA = dataAWS.mean()
errorA = stats.sem(dataAWS)
conf_intAW = stats.t.interval(conf_level, deg_freedomA, meanA, errorA)
print(conf_intAW)

#WindB
conf_level = 0.95
deg_freedomB = dataBWS.size - 1
meanB = dataBWS.mean()
errorB = stats.sem(dataBWS)
conf_intBW = stats.t.interval(conf_level, deg_freedomB, meanB, errorB)
print(conf_intBW)

#WindC
conf_level = 0.95
deg_freedomC = dataCWS.size - 1
meanC = dataCWS.mean()
errorC = stats.sem(dataCWS)
conf_intCW = stats.t.interval(conf_level, deg_freedomC, meanC, errorC)
print(conf_intCW)

#WindD
conf_level = 0.95
deg_freedomD = dataDWS.size - 1
meanD = dataDWS.mean()
errorD = stats.sem(dataDWS)
conf_intDW = stats.t.interval(conf_level, deg_freedomD, meanD, errorD)
print(conf_intDW)

#WindE
conf_level = 0.95
deg_freedomE = dataEWS.size - 1
meanE = dataEWS.mean()
errorE = stats.sem(dataEWS)
conf_intEW = stats.t.interval(conf_level, deg_freedomE, meanE, errorE)
print(conf_intEW)

sensors = ['A', 'B', 'C', 'D', 'E']
temp = [conf_intA, conf_intB, conf_intC, conf_intD, conf_intE]
winds = [conf_intAW, conf_intBW, conf_intCW, conf_intDW, conf_intEW]
dict1 = {'Sensors':sensors, 'Temperature Confidence Intervals':temp, 'Wind Speed Confidence Intervals':winds}
df1 = pd.DataFrame(dict1)

file = open('Confidence_Intervals.txt', 'a')
file.write(str(df1))
file.close()

#Hypothesis Testing
#Temperature
def test(data1, data2, sensors):
    data = data1.values, data2.values
    t, p = stats.ttest_ind(data[0],data[1])
    print(sensors)
    print("t = " + str(t))
    print("p = " + str(p))

print('Temperature')
test(dataE, dataD, 'Sensors E - D')
test(dataD, dataC, 'Sensors D - C')
test(dataC, dataB, 'Sensors C - B')
test(dataB, dataA, 'Sensors B - A')

#Wind Speed
def test(data1, data2, sensors):
    data = data1.values, data2.values
    t, p = stats.ttest_ind(data[0],data[1])
    print(sensors)
    print("t = " + str(t))
    print("p = " + str(p))

print('Wind Speed')
test(dataEWS, dataDWS, 'Sensors E - D')
test(dataDWS, dataCWS, 'Sensors D - C')
test(dataCWS, dataBWS, 'Sensors C - B')
test(dataBWS, dataAWS, 'Sensors B - A')

#Bonus question
def aver_temp(data, sensor):
    means=[data[0:72].mean(), data[72:144].mean(), data[144:216].mean(), data[216:288].mean(), data[288:360].mean(), data[360:432].mean(), data[432:504].mean(), data[504:576].mean(), data[576:648].mean(),
    data[648:720].mean(), data[720:792].mean(), data[792:864].mean(), data[864:936].mean(), data[936:1008].mean(), data[1008:1080].mean(), data[1080:1152].mean(), data[1152:1224].mean(), data[1224:1296].mean(),
    data[1296:1368].mean(), data[1368:1440].mean(), data[1440:1512].mean(), data[1512:1584].mean(), data[1584:1656].mean(), data[1656:1728].mean(), data[1728:1800].mean(), data[1800:1872].mean(), data[1872:1944].mean(),
    data[1944:2016].mean(), data[2016:2088].mean(), data[2088:2160].mean(), data[2160:2232].mean(), data[2232:2304].mean(), data[2304:2376].mean(), data[2376:2448].mean()]
    days=['June10', 'June11', 'June12', 'June13', 'June14', 'June15', 'June16', 'June17', 'June18', 'June19', 'June20', 'June21', 'June22', 'June23', 'June24', 'June25', 'June26', 'June27', 'June28', 'June29', 'June30',
    'July1', 'July2', 'July3', 'July4', 'July5', 'July6', 'July7', 'July8', 'July9', 'July10', 'July11', 'July12', 'July13']
    dict1={'Average Temperature':means, 'Date':days}
    df1=pd.DataFrame(dict1)
    #Hottest Day
    print('Hottest day according to', sensor + ':\n', df1.loc[df1['Average Temperature'] == max(df1['Average Temperature'])])
    #Coldest Day
    print('Coldest day according to', sensor + ':\n',df1.loc[df1['Average Temperature'] == min(df1['Average Temperature'])])
aver_temp(dataA, 'sensor A')
aver_temp(dataB, 'sensor B')
aver_temp(dataC, 'sensor C')
aver_temp(dataD, 'sensor D')
aver_temp(dataE, 'sensor E')