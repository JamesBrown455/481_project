#  fires.py
#
# 2018
# James Brown <brownj78@southernct.edu>
# and
# Dylan Gosselin <gosselind1@southernct.edu>
#

# Imports
from sklearn import svm
from sklearn import preprocessing


# Create Test and training files
def divide_data(data_list, label_list):
    train_list = []
    train_label = []
    test_list = []
    test_label = []

    i = 0
    counter = 0
    while i < label_list.lenght:

        if counter < 5:
            train_list.append(data_list[i])
            train_label.append(label_list[i])

        if counter == 5:
            test_list.append(data_list[i])
            test_label.append(label_list[i])

        counter += 1
        i += 1

    return train_list, train_label, test_list, test_label


# This method scales the data
def data_scale(train_list, test_list):
    train_scaled = preprocessing.scale(train_list)
    test_scaled = preprocessing.scale(test_list)
    return train_scaled, test_scaled


# This method trains and tests the SVM classifier
def run_svm(train, train_label, test):
    classifier = svm.SVC(C=1.0,
                         cache_size=200,
                         class_weight=None,
                         coef0=0.0,
                         decision_function_shape=None,
                         gamma='auto',
                         kernel='linear',
                         max_iter=-1,
                         probability=True,
                         random_state=None,
                         shrinking=False,
                         tol=0.0001,
                         verbose=False)

    classifier.fit(train, train_label)
    result = classifier.predict(test)

    return result


