#Intro to Data Analysis
##Project Instructions
The goal here was to apply data analysis techniques using the Python Pandas and Numpy library.

To showcase this, the wellknown **Titanic dataset** from Kaggle has been chosen. The main question that has been considered here was: **What factors made people more likely to survive**?

The correlation of the survival rate with each independent variable was studied, and visualizations were made to help the analyze. For a few unexpected results, additional Data manipulation was done to try to get some clues about possible explanations.

No machine learning algorythm has been used here. The point was not to recreate the Kaggle tutorial scripts, but to illustrate the first steps when confronted to a new (clean) dataset. 

##Background Dataset Information (from the Kaggle website)

The sinking of the RMS Titanic is one of the most infamous shipwrecks in history.  On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.

One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.

https://www.kaggle.com/c/titanic

##Analysis

Please look at the [Jupyter Notebook](Titanic.ipynb) to find my Analysis.

Packages versions:

- Python: v3.5.1
- Matplotlib: v1.5.1
- NumPy: v1.11.0
- Seaborn: 0.7.0


###Limitations
Only 891 from the 2344 Titanic passengers have been studied here. Chances are that they have been randomly selected and represent correctly the overall population, but, as with every sampling process, there are differences between the sample and the population characteristics.

All variables were not equally filled with Data. In particular, Age was missing 177 entries out of 891 passengers. I chose to replace the missing values by the variable mean, but as we saw, it has an impact on the sample standard deviation. Caution should be taken if a statistical test is done on this data.

Also, all the previous remarks on the possible correlation between the different variables were based on statistical calculation, but not on statistical testing. To validate these conclusion, additional testing should be pursued.

###Summary

Through this analysis, we were able to observe different correlations between survival rate and the other variables. In particular, being a woman seemed to be correlated with a higher survival rate (74%) than being a man (19%). Age seemed also to be an important factor, but only for kids (age < 10 years) who showed a survival rate higher than the mean (61% against 38%). Last but not least, passenger from higher class (1 and 2) showed also higher survival rate (resp. 63% and 47%).

But it is important to underline that these observations were not validated by statistical testing, which could be an opportunity to extend the analysis further on.

##Bibliography

Titanic dataset : https://www.kaggle.com/c/titanic/data

pyplot examples : http://matplotlib.org/api/pyplot_api.html

bining data : http://stackoverflow.com/questions/6163334/binning-data-in-python-with-scipy-numpy