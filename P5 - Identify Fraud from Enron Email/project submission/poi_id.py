#!/usr/bin/python

import sys
import pickle
from sklearn.linear_model import LogisticRegression
from tester import dump_classifier_and_data, test_classifier

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

# Task 1: Select what features you'll use.
# features_list is a list of strings, each of which is a feature name.
# The first feature must be "poi".
features_list = ['poi', 'salary', 'total_payments', "total_stock_value",
                 "to_messages", "shared_receipt_with_poi",
                 "from_this_person_to_poi", "from_poi_to_this_person",
                 "from_messages"]

# Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

# Task 2: Remove outliers
data_dict.pop("TOTAL")  # remove the TOTAL entry, as it appears clearcly as a general outlier.

# Task 3: Create new feature(s)
# Adding the ratio of messages received, shared and sent to POIs
for name in data_dict.keys():
    try:
        data_dict[name]["to_messages_poi_ratio"] = \
            1.0*data_dict[name]["from_this_person_to_poi"]/data_dict[name]["from_messages"]
        data_dict[name]["from_messages_poi_ratio"] = \
            1.0*data_dict[name]["from_poi_to_this_person"]/data_dict[name]["to_messages"]
        data_dict[name]["shared_messages_poi_ratio"] = \
            1.0*data_dict[name]["shared_receipt_with_poi"]/data_dict[name]["to_messages"]
    except TypeError:
        data_dict[name]["to_messages_poi_ratio"] = "NaN"
        data_dict[name]["from_messages_poi_ratio"] = "NaN"
        data_dict[name]["shared_messages_poi_ratio"] = "NaN"

features_list.append("to_messages_poi_ratio")
features_list.append("from_messages_poi_ratio")
features_list.append("shared_messages_poi_ratio")

# Store to my_dataset for easy export below.
my_dataset = data_dict

# Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys=True)
labels, features = targetFeatureSplit(data)

# Task 4: Try a varity of classifiers
# Please name your classifier clf for easy export below.
# Note that if you want to do PCA or other multi-stage operations,
# you'll need to use Pipelines. For more info:
# http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.


# Task 5: Tune your classifier to achieve better than .3 precision and recall
# using our testing script. Check the tester.py script in the final project
# folder for details on the evaluation method, especially the test_classifier
# function. Because of the small size of the dataset, the script uses
# stratified shuffle split cross validation. For more info:
# http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

clf = LogisticRegression(C=10, penalty="l1", class_weight="balanced", random_state=42)
test_classifier(clf, my_dataset, features_list, folds=1000)

# Task 6: Dump your classifier, dataset, and features_list so anyone can
# check your results. You do not need to change anything below, but make sure
# that the version of poi_id.py that you submit can be run on its own and
# generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
