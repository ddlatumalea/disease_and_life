# Statistics

See the accompanying notebook *statistics.ipynb* for a full overview of the statistical procedures and the graphs.

This page summarized the main takeaways:

## 1) Life Expectancy and Deaths
In general the life expectancy rise through the years.
Especially the life expectancy of Japan has risen the last decades.

The rise in life expectancy of The Netherlands looks to slow down.
This indicates a change in demographic composition or the difficulties of preventing non-communicable diseases.

In general, deaths by non-communicable chronic diseases seem to decline, except in Japan where they rise. 
This could also be due to demographic factors.

## 2) Pearson Correlation
Pearson correlation was chosen as a first method, because of the ease of use. It provides insight in the correlation between time series.

*The Netherlands*
<ul>
<li> There is a very high negative correlation between life expectancy [age] and non-communicable chronic disease [deaths].</li>
<li> Overall, there seems to be a moderate to high negative correlation between diseases and life expectancy.</li>
</ul>

*Japan*

<ul>
<li> There is a very high correlation between diseases in general and life expectancy.</li>
</ul>

We see The Netherlands show a very high negative correlation, while Japan shows a very high positive correlation between diseases and life expectancy. This can be due to demographic factors. In japan, 25-30% of people are 65+ years old. This is in contrast with the netherlands, where only around 20% are more than 65 years old.

<strong>Conclusion</strong>: There seems to be a high (positive/negative) correlation between non-communicable chronic diseases and life expectancy.

## 3) Cross validation
Cross validation was chosen as second method, as it also provides insight in correlation, but cross validates the result. 
This is more valid for time series. 

*The Netherlands*:
<ul>
<il>There is a moderate to high negative correlation after 1-4 lags</il>
</ul>

*Japan*:
<ul>
<il>There is a moderate to high positive correlation after 1-4 lags.</il>
</ul>

## 4) Granger
The Granger test is mostly used to test if one series is predictive for the other.
The test is chosen, because it is useful to know if the amount of non-communicable deaths can forecast the life expectancy.

H0: lagged x-values do not explain the variation in y.<br>
H1: lagged x-values do explain the variation in y.

Normally this test should use stationary time series data. Due to difficulties making
this time series stationary, I used the standardized data as it is.

*Netherlands*

<ul>
<il>Lag 1: non-communicable chronic disease Granger-cause the life expectancy. **Thus there is a 'causality' between non-communicable chronic disease and the life expectancy with a p-value of 0**.</il>
</ul>


*Japan*

<ul>
<il>Lag 2: non-communicable chronic disease Granger-cause the life expectancy. **Thus, there is a 'causality' between non-communicable chronic disease and the life expectancy with a p-value of 0**.</il>
</ul>

**Conclusion**:

<ul>
<il>Life expectancy is influences by non-communicable chronic disease. The expectation is that we can increase life expectancy by decreasing non-communicable chronic diseases. </il>
</ul>
