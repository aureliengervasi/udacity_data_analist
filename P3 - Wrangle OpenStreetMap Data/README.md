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



##Code
As for the previous projects, I displayed my code and analysis via a [Jupyter Notebook](P3%20-%20Wrangle%20OSM%20Data%20with%20MongoDB.ipynb). 

*NB: I was not able to upload the OSM data on the GitHub platform (file size limited to 100 MB), but the data is freely available under the link specified at the begining of this page.*

Packages versions:

- Python: v2.7.11
- et_xmlfile: v1.0.1
- pymongo: 3.0.3
- numpy: v1.10.4
- matplotlib: v1.5.1

##Conclusions

###Process
Throughout this work I was able to use OSM data from the Paris Metroline to learn how to assess data quality, clean data if need be, and store it in a MongoDB database.

The first part of my work enabled me to see what the OSM data structure looked like and what were the main data quality issues to be dealt with before importing it in the MongoDB database. It was also the occasion to select the most frequent and useful fields from the entire OSM dataset.

The second part was focused on parsing the OSM file and restructuring it into a JSON file before importing it to the MongoDB database. Due to the large file size, import in the database had to be done in chunks in order to avoid memory overload.

Once the data was stored into MongoDB, it was very easy to access. Pymongo makes the interface between Python and MongoDB very easy. The first queries were used to check the data quality of the main entry types, especially for the fields cleaned by the python scripts.

Several funny facts could be discovered from the OSM data:
- who are the main contributors and how much did they contribute to the dataset?
- What are the main amenities?
- What are the main cuisine types?
- What are the biggest cities in population in the dataset?
- What are the main tree genuses?

###Data Quality

I spent some time auditing the street names. At first, it could appear that the entries are uniformly filled and that the data quality is high, but when looking on the entire dataset, some issues were spotted. I focused my work on assuring that the main street qualifiers were uniformly spelled, and looked at the consistency problem when several qualifiers were given for the same name. I also had a look at the specific case of hyphens and how they can create uniformity issues. Accuracy was difficult to assess, as there was no data available to easily compare the database entries.

The main challenge in the dataset is the completeness issue. Most of the entries (street name, postcode, etc.) are not available for each amenity, as they are linked via relation elements (members and node). Though this structure keeps the overall dataset weight fairly low, it complicates our work for now. A next step could be to build an index listing the different elements related to the same postcode and street name. To improve the data quality for amenities, it could be possible to add address entries based on the relationship elements (members and node) that are linked to this amenity.

If all the amenities had their address entries correctly filled, it would be possible to do a more detailed analysis by cities, or by arrondissement. For instance, it could be possible to check which arrondissements are the most touristy by looking at the number of restaurants they have compared to their area, or population. The main challenge to achieve this improvement is to find a way to transit the address information (postcodes, street names) from high level relation element (cities, arrondissements, ways, etc.) to all the relevant amenities in the related area.


##Bibliography

OSM Metroline database: https://mapzen.com/data/metro-extracts/

OSM XML schema: http://wiki.openstreetmap.org/wiki/OSM_XML

Pprint class that prints unicode: http://stackoverflow.com/questions/10883399/unable-to-encode-decode-pprint-output

rotate x labels with pyplot: http://stackoverflow.com/questions/10998621/rotate-axis-text-in-python-matplotlib