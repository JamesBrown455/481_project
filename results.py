#  fires.py
#
# 2018
# James Brown <brownj78@southernct.edu>
# and
# Dylan Gosselin <gosselind1@southernct.edu>
#

# Imports
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


# Calculate the Results
def calc_results(results_list, true_list):
    results_matrix = confusion_matrix(results_list, true_list)
    accuracy = accuracy_score(results_list, true_list)
    
    print("Confusion Matrix")
    print(results_matrix)
    print()
    print("Accuracy: " + str(accuracy))
