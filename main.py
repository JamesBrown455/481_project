# 2018
# James Brown <brownj78@southernct.edu>
# and
# Dylan Gosselin <gosselind1@southernct.edu>
import read_data


def main():
    samples, trueValues = read_data.readfile()
    print(samples)
    print(trueValues)


if __name__ == "__main__":
    main()
