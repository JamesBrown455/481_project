# 2018
# James Brown <brownj78@southernct.edu>
# and
# Dylan Gosselin <gosselind1@southernct.edu>
import read_data
import results
import svm_test_train


def main():
    samples, true_values = read_data.readfile()
    train_list, train_label, test_list, test_label = svm_test_train.divide_data(samples, true_values)
    scaled_train_list, scaled_test_list = svm_test_train.data_scale(train_list, test_list)
    decisions = svm_test_train.run_svm(scaled_train_list, train_label, scaled_test_list)
    results.calc_results(decisions, test_label)
    # print(samples)
    # print(true_values)


if __name__ == "__main__":
    main()
