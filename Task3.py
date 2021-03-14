from sklearn import datasets

iris = datasets.load_iris()


def predictRow(sl, sw, pl, pw):
    if (4.3 <= sl <= 5.8) and (2.3 <= sw <= 4.4) and (1.0 <= pl <= 1.9) and (0.1 <= pw <= 0.6):
        return 'setosa'
    elif (4.9 <= sl <= 7.0) and (2.0 <= sw <= 3.4) and (3.0 <= pl <= 5.1) and (1.0 <= pw <= 1.8):
        return 'versicolor'
    else:
        return 'virginica'


def main():
    print("___________________________________________________________________")
    points = 0
    dataset_length = len(iris['data'])
    for i in range(dataset_length):
        if iris['target_names'][iris['target'][i]] == predictRow(
                iris['data'][i][0], iris['data'][i][1], iris['data'][i][2], iris['data'][i][3]):
            points = points + 1
    accuracy = (points / dataset_length) * 100

    print("Accuracy is {}%".format(accuracy))


def calculate_min_max():
    min_sl = iris['data'][50:100, 0].min()
    max_sl = iris['data'][50:100, 0].max()
    min_sw = iris['data'][50:100, 1].min()
    max_sw = iris['data'][50:100, 1].max()
    min_pl = iris['data'][50:100, 2].min()
    max_pl = iris['data'][50:100, 2].max()
    min_pw = iris['data'][50:100, 3].min()
    max_pw = iris['data'][50:100, 3].max()

    print("min_sl {}, max_sl {}, min_sw {}, max_sw {}, min_pl {}, max_pl {}, min_pw {}, max_pw {}"
          .format(min_sl, max_sl, min_sw, max_sw, min_pl, max_pl, min_pw, max_pw))


if __name__ == "__main__":
    main()
