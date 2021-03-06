# Life Expectancy and Disease

-----------------------
Author: Djakim Latumalea

University: Hanze University of Applied Sciences

Institute: Life Science & Technology

Contact: d.d.latumalea@st.hanze.nl

------------------

**NOTE**
- Unfortunately the health organizations in The Netherlands do not keep track of all the numbers of non-communicable diseases.
They also do not provide data per year. The most data I could find about a specific manicupality were 2 data points in 10 year.
Based on the lack of data, I decided to compare data on a country-level.
- I chose not to extrapolate data of Canada as it contains many missing values. They did not report
their data to the WHO before 2000 and after 2005. It is outside the scope of this application to
extrapolate data based on data from other countries.

This dashboard tries to answer the following research question:
*Do non-communicable chronic diseases influence the life expectancy at birth?*

## Assumptions
At the moment, chronic diseases are responsible
for 71% of all deaths<sup>a</sup>. Thus, we assume chronic diseases have a very big impact on the life expectancy.

## Definitions
***Chronic disease***: a condition that, "tend to be of long duration and is the result of a
combination of genetic, physiological, environmental and behavioural factors<sup>a</sup>, for instance<sup>a,b,c</sup>:
<ul>
<li>Cardiovascular diseases</li>
<li>Cancer</li>
<li>Chronic respiratory diseases</li>
<li>Diabetes</li>
<li>Alzheimer's disease</li>
</ul>

***Life expectancy***: the number of years a person can expect to live. 
This can be calculated in several ways. Most studies use the 'period life expectancy'. It is an estimation of the average length of life
for a hypothetical cohort living through the age-specific mortality at one period in time. This means, the value can
deviate from the actual 'cohort life expectancy', which is the average life length of a particular cohort <sup>d</sup>.
The calculation can be based on the year of birth, death rates, current age, and demographic factors such as sex<sup>e</sup>.    

There are other definitions, but they will not be used in this project. If you'd like to know more, you can always contact me at d.d.latumalea@hst.hanze.nl

-----------------------------

## Reasoning

To answer this research question several datasets are analyzed. In total there are 9 datasets:
- A dataset with country codes.
- 3 datasets containng the life expectancy of respectfully, The Netherlands, Japan and Canada.
- 5 datasets containg the raw mortality rates of multiple countries that submitted their data to the World Health Organization.

A full analysis of the datasets can be found in the accompanying notebook *Data understanding.ipynb*.

The data is then further analyzed using graphs and statistical tests.

**Explaination visualisation techniques**:<br>
- Time series are visualized using line graphs, because it shows the change of a value through time.
- Line graphs make it easy to compare multiple variables.

**Explanation statistical tests**:<br>
- Correlation tests are used to find correlations between the variables.
- Granger test is used to see if one time series can be used to predict the other.

## Conclusion

**Main conclusion**:<br>
- Non-communicable diseases are predictive of the life expectancy, based on a p-value < 0.0 using Granger causality tests.
- It can be predictive in a negative causal way or positive causal way. This depends on the country.

## Discussion
**Discussion**:<br>
- Care should be taken in trusting the main conclusion, because one country may have a high negative correlation while the other has a high positive correlation.
- There may be other hidden factors that influence the life expectancy. Thus, it may not be 'true' causality.<br>
- Demographics play a very big role, and in this document they are not taken into account. Demographics could explain the reason why non-communicable diseases are rising in Japan and declining in The Netherlands.
- For future work, standardize the dataset by taking demographic factors such as age into account.