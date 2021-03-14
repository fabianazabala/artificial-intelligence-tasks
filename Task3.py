from sklearn import datasets

iris = datasets.load_iris()


def predictRow(sl, sw, pl, pw):
    if sl >= 4.9 and sw >= 3.0 and pl == 1.4 and pw == 0.2:
        return "setosa"
    elif sl >= 6.4 and sw == 3.2 and pl >= 4.5 and pw >= 1.4:
        return "virginica"
    else:
        return "versicolor"


def main():
    print(predictRow(6.9, 3.2, 4.6, 1.5))


if __name__ == "__main__":
    main()
