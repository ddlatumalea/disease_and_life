# Life Expectancy and Disease
This notebook tries to answer the following research question:
*Do non-communicable chronic diseases influence the life expectancy at birth?*

To answer this research question several datasets are analyzed. In total there are 9 datasets:
- A dataset with country codes.
- 3 datasets containng the life expectancy of respectfully, The Netherlands, Japan and Canada.
- 5 datasets containg the raw mortality rates of multiple countries that submitted their data to the World Health Organization.

A full analysis of the datasets can be found in the accompanying notebook *Data understanding.ipynb*.

The data is then further analyzed using graphs and statistical tests.

*Main conclusion*:<br>
- Non-communicable diseases are predictive of the life expectancy, based on a p-value < 0.0 using Granger causality tests.

*Discussion*:<br>
- There may be other hidden factors that influence the life expectancy.
- Demographics play a very big role, and in this document they are not taken into account.