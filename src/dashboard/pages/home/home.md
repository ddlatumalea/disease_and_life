# Life Expectancy and Disease

-----------------------
Author: Djakim Latumalea

University: Hanze University of Applied Sciences

Institute: Life Science & Technology

Contact: d.d.latumalea@st.hanze.nl

------------------

**NOTE**
- I chose not to extrapolate data of Canada as it contains many missing values. They did not report
their data to the WHO before 2000 and after 2005. It is outside the scope of this application to
extrapolate data based on data from other countries.

This dashboard tries to answer the following research question:
*Do non-communicable chronic diseases influence the life expectancy at birth?*

To answer this research question several datasets are analyzed. In total there are 9 datasets:
- A dataset with country codes.
- 3 datasets containng the life expectancy of respectfully, The Netherlands, Japan and Canada.
- 5 datasets containg the raw mortality rates of multiple countries that submitted their data to the World Health Organization.

A full analysis of the datasets can be found in the accompanying notebook *Data understanding.ipynb*.

The data is then further analyzed using graphs and statistical tests.

**Main conclusion**:<br>
- Non-communicable diseases are predictive of the life expectancy, based on a p-value < 0.0 using Granger causality tests.

**Discussion**:<br>
- Care should be taken in trusting the main conclusion, because one country may have a high negative correlation while the other has a high positive correlation.
- There may be other hidden factors that influence the life expectancy. Thus, it may not be 'true' causality.<br>
- Demographics play a very big role, and in this document they are not taken into account. Demographics could explain the reason why non-communicable diseases are rising in Japan and declining in The Netherlands.
- For future work, standardize the dataset by taking demographic factors such as age into account.