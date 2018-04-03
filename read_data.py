# 2018
# James Brown <brownj78@southernct.edu>
# and
# Dylan Gosselin <gosselind1@southernct.edu>


def readfile():
    LINESTOIGNORE = 1  # First line is data headers
    FILEPATH = "./forestfires.csv"
    sampleList = []
    trueValueList = []

    with open(FILEPATH) as dataFile:
        dataFile.readlines(LINESTOIGNORE)
        for dataLine in dataFile.readlines():
            dataList = dataLine.strip("\n").split(",")
            sample, trueValue = processData(dataList)
            sampleList.append(sample)
            trueValueList.append(trueValue)

    return sampleList, trueValueList


def processData(data):
    TRUECLASSINDEX = 12
    # 12 is the area burned
    INDICIESTOIGNORE = [0, 1, 2, 3]
    # 0 and 1 are positional coordinates
    # 2 and 3 are month and day of the week (ex: mon) respectively

    trueValue = classifyTrueValue(float(data[TRUECLASSINDEX]))
    for index in sorted(INDICIESTOIGNORE, reverse=True):
        del(data[index])
    sample = list(map(float, data))

    return sample, trueValue

def classifyTrueValue(trueInput):
    NODAMAGE = 0
    LIGHTDAMAGE = 1
    MEDIUMDAMAGE = 2
    LARGEDAMAGE = 3
    SEVEREDAMAGE = 4

    trueValue = None

    if trueInput == 0:
        trueValue = NODAMAGE
    elif trueInput < 25:
        trueValue = LIGHTDAMAGE
    elif trueInput < 75:
        trueValue = MEDIUMDAMAGE
    elif trueInput < 150:
        trueValue = LARGEDAMAGE
    else:
        trueValue = SEVEREDAMAGE

    return trueValue


def tester():
    samples, trueValues = readfile()

    print(samples)
    print(trueValues)


if __name__ == "__main__":
    tester()
