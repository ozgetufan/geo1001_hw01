## Files

### geo1001_hw01.py
The main file "geo1001_hw01.py" contains and executes the code.

### Excel files 
The excel files of the datasets for the 5 sensors are imported to Python and named as df_A to df_E. The path of the files should be changed according to the location of the files in the computer. 

## Variables
- dataA, dataB, dataC, dataD, dataE: contain the "Temperature" column of df_A, df_B, df_C, df_D, df_E respectively.
- dataAWS, dataBWS, dataCWS, dataDWS, dataEWS: contain the "Wind Speed" column of df_A, df_B, df_C, df_D, df_E respectively.
- dataAWD, dataBWD, dataCWD, dataDWD, dataEWD: contain the "Direction, True" column of df_A, df_B, df_C, df_D, df_E respectively.
- dataAWBG, dataBWBG, dataCWBG, dataDWBG, dataAEWBG: contain the "WBGT" column of df_A, df_B, df_C, df_D, df_E respectively.
- dataACS, dataBCS, dataCCS, dataDCS, dataECS: contain the "Crosswind Speed" column of df_A, df_B, df_C, df_D, df_E respectively.

## Part 1
- Mean statistics (mean, variance and standard deviation) are computed and added in an Excel file "Mean_Statistics.xlsx".
- Histograms with 5 and 50 bins for temperature values are plotted by defining a function called "hist1(data, x, title)".
- Frequency polygons for temperature values are plotted for 5 sensors. 
- Boxplots are plotted for 5 sensors and for Wind Speed, Wind Direction and Temperature.

## Part 2
- Probability Mass Functions (PMF) for temperature values are plotted for 5 sensors in subplots with a function called "pmf(data, x, title, col)". 
- Cumulative Density Functions (CDF) for temperature values are plotted for 5 sensors in subplots. 
- Probability Density Functions (PDF) for temperature values are plotted for 5 sensors in subplots with a function called "pdf(data, x, title, col)". 
- Probability Density Functions (PDF) for wind speed values are plotted for 5 sensors in subplots.
- Kernel Density Estimation (KDE) for wind speed values is plotted for 5 sensors in subplots with a function called "kde(data, x, title)". 

## Part 3
- Correlations and covariances between all the sensors for the variables Temperature, Wet Bulb Globe Temperature (WBGT), Crosswind Speed are computed.
- Pearson's and Spearman's coefficients are plotted in strip plots for the three variables by first creating data frames with all the coefficients and sensor pair names. Then, these data frames are used to generate strip plots. 

## Part 4
- Cumulative Density Functions (CDF) for wind speed and temperature values are plotted for 5 sensors in subplots.
- The 95% confidence intervals are computed for variables Temperature and Wind Speed for all the sensors and saved in a .txt file called "Confidence_Intervals.txt". 
- The hypothesis is tested for sensor pairs by computing the p-values with a function called "test(data1, data2, sensors)". 

## Bonus question
- The hottest and coldest days recorded by the 5 sensors are computed with a function called "aver_temp(data, sensor)". In this function, a data frame called "df1" is created with the mean temperature of each day and the corresponding dates. Then, the maximum and minimum values are extracted. 