#  fires.py
#
# 2018
# James Brown <brownj78@southernct.edu>
# and
# Dylan Gosselin <>
#

# Imports
from sklearn import svm
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# Calculate the Results
def calc_results(results_list, true_list):
    results_matrix = confusion_matrix(results_list, true_list)
    
    print("Results")
