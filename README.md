# Analysis of Chronic Disease and Life Expectancy

**Research question**: Do chronic diseases influence the life expectancy?

**H<sub>0</sub>**: Chronic diseases do not significantly influence the life expectancy.

**H<sub>1</sub>**: Chronic diseases do significantly influence the life expectancy.

-------
When plotting the data in a graph, diseases should so a negative correlation with life expectancy:
https://bigcitieshealthdata.org/city/new-york-city-ny/?metrics=02-03-04%2C02-04-08%2C02-05-11%2C05-02-04&years=%2C%2C%2C&groups=%2C%2C%2C
-------

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

## SOLID
### Single Responsibility Principle
- A class should have, and only one reason to change.
- A class can have multiple methods as long as they correspond to the same logic.

### Open Close Principle
- Be able to extend a classes behaviour, without modifying it.

### Liskov Substitution Principle
- Derived classes must be substitutable for their base classes.

### Interface Segregation Principle
- Make fine grained interfaces that are client specific.

### Dependency Inversion Principle
- Depend on abstractions, not on concretions.

# Running the files
1) Run `preprocessing.py` to clean the files.

## Resources
<sup>a</sup>https://www.who.int/news-room/fact-sheets/detail/noncommunicable-diseases

<sup>b</sup>https://www.cdc.gov/chronicdisease/about/index.htm

<sup>c</sup>https://www.government.nl/topics/quality-of-healthcare/quality-of-care-for-patients-with-chronic-disease

<sup>d</sup>https://ourworldindata.org/life-expectancy-how-is-it-calculated-and-how-should-it-be-interpreted

<sup>e</sup>https://en.wikipedia.org/wiki/Life_expectancy

https://www.who.int/data/maternal-newborn-child-adolescent-ageing/indicator-explorer-new/mca/life-expectancy-at-birth

https://www.who.int/data/gho/data/themes/mortality-and-global-health-estimates/ghe-leading-causes-of-death

https://www.rivm.nl/media/profielen/profile_3_Appingedam_gezonddet.html

https://opendata.cbs.nl/statline/#/CBS/nl/dataset/81628NED/table?ts=1642168757218

https://opendata.cbs.nl/#/CBS/nl/dataset/37852/table

