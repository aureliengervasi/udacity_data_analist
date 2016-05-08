#P3 Wrangle OSM Data with MongoDB - Paris Metroline

**Map area : Paris Metroline, France**

Source : https://mapzen.com/data/metro-extracts/

##Motivation

To the outside world, working as a Data Scientist is often associated with Machine Learning, cool visualization and statistics. But an important part of the Data Scientist job is also to prepare data (i.e. gathering it, cleaning it, and storing it in a convenient format) before applying all the analytical tools available. 

The goal of this work is to use data from the Open Street Map community to learn how to assess data quality, clean data if need be, and store it in a MongoDB database. The major skill I wanted to hone and apply here are:
- Assessing the quality of the data for validity, accuracy, completeness, consistency and uniformity
- Parsing and gathering data from popular file formats such as .json and .xml
- Process data from very large files that can not be cleaned with spreadsheet programs
- Learn how to store, query, and aggregate data using MongoDB

The first part of my work is focused on getting some first clues about data quality of the OSM file. The idea is to find out which treatment has to be done to the data in order to improve its quality before importing it to the database. The main focus is on postcodes, streetnames, and population.

As the file size is very big, it is not very handy to do all the auditing via the OSM file. This is why, after having imported the data into MongoDB, I start with some further auditing in order to check the data quality level. 

When satisfied with the MongoDB database, I use some queries to analyze the OSM data further and try to find out interesting numbers or trends with the Paris Metroline data.



##Jupyter Notebook
As for the previous projects, I displayed my code and analysis via a Jupyter Notebook. I was not able to upload the OSM data on the GitHub platform (file size limited to 100 MB), but the data is freely available under the link specified at the begining of this page. 
You can find the notebook [here](P3%20-%20Wrangle%20OSM%20Data%20with%20MongoDB.ipynb)