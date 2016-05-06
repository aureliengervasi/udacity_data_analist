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

The first part of my work is focused on getting some first clues about data quality of the OSM file. The idea was to find out which treatment has to be done to the data before importing it to the database. 

But as the file size is very big, it was not very handy to do all the auditing via the OSM file. This is why, after having imported the data into MongoDB, I started with some further auditing in order to check the data quality level. 

Once satisfied with the MongoDB database, I used some queries to analyze the OSM data further and tried to find out interesting numbers or trends with the Paris Metroline data.


##Jupyter Notebook
As for the previous projects, I displayed my code and analysis via a Jupyter Notebook. I was not able to upload the OSM data on the GitHub platform (file size limited to 100 MB), and, as I needed an active MongoDB database, the hosted notebook does not run correctly.

But I put an html version in the "html" folder which should display the correct results. Thank you to open [this page](html/notebook.html) if you wish to consult my work.
