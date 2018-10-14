import csv
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

def getMatrix(listX):
    '''
    input: listX:drug,disease,feature1,feature2,...,label
    output: feature1,feature2,...
    '''
    X = []
    for i in range(1, len(listX)):
        row = []
        for j in range(2, len(listX[0])-1):
            row.append(float(listX[i][j]))
        X.append(row)
    return X

    # # get columns not involving ADR
    # for i in range(1, len(listX)):
    #     row = []
    #     row.append(float(listX[i][2]))
    #     row.append(float(listX[i][3]))
    #     row.append(float(listX[i][4]))
    #     row.append(float(listX[i][6]))
    #     row.append(float(listX[i][7]))
    #     row.append(float(listX[i][9]))
    #     row.append(float(listX[i][10]))
    #     # row.append(float(listX[i][15]))
    #     # row.append(float(listX[i][16]))
    #     # row.append(float(listX[i][17]))
    #     # row.append(float(listX[i][19]))
    #     # row.append(float(listX[i][20]))
    #     # row.append(float(listX[i][22]))
    #     # row.append(float(listX[i][23]))
    #     X.append(row)
    # return X

    # # get columns involving ADR
    # for i in range(1, len(listX)):
    #     row = []
    #     row.append(float(listX[i][5]))
    #     row.append(float(listX[i][8]))
    #     row.append(float(listX[i][11]))
    #     row.append(float(listX[i][12]))
    #     row.append(float(listX[i][13]))
    #     row.append(float(listX[i][14]))
    #     row.append(float(listX[i][18]))
    #     row.append(float(listX[i][21]))
    #     row.append(float(listX[i][24]))
    #     row.append(float(listX[i][25]))
    #     row.append(float(listX[i][26]))
    #     row.append(float(listX[i][27]))
    #     X.append(row)
    # return X

def classification(trainFile, testFile):
    with open(trainFile,'rb') as f:
        rd = csv.reader(f)
        listX = list(rd)
    X = getMatrix(listX)

    data = pd.read_csv(trainFile)
    y = data['label'].values

    with open(testFile,'rb') as f:
        rd = csv.reader(f)
        listX_test = list(rd)
    X_test = getMatrix(listX_test)

    data = pd.read_csv(testFile)
    y_test = data['label'].values

    # clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(1, 2), random_state=1)
    # clf = svm.LinearSVC(penalty='l1',dual=False)
    # clf = svm.SVC()
    # clf = RandomForestClassifier(n_estimators=10, max_depth=None,min_samples_split=2, random_state=0)
    clf = GaussianNB()
    # clf = MultinomialNB()
    # clf = BernoulliNB()
    clf.fit(X,y)
    y_predicted = clf.predict(X_test)
    # print clf.score(X_test,y_test)

    tp,fp,fn,tn = 0,0,0,0
    pred_list = []
    for i in range(0, len(y_predicted)):
        # print y_test[i],y_predicted[i]
        line = []
        if y_test[i] == 1 and y_predicted[i] == 1:
            tp += 1
        elif y_test[i] == 1 and y_predicted[i] == 0:
            fn += 1
        elif y_test[i] == 0 and y_predicted[i] == 1:
            fp += 1
            line.append(listX_test[i][0]);line.append(listX_test[i][1]);line.append(y_test[i]);line.append(y_predicted[i])
            pred_list.append(line)
            # print listX_test[i][0],listX_test[i][1],y_test[i],y_predicted[i]
        else:
            tn += 1

    # print tp,tn,fp,fn
    try:
        precision = float(tp)/float(tp+fp)
    except ZeroDivisionError:
        precision = 0.0
    try:
        recall = float(tp)/float(tp+fn)
    except ZeroDivisionError:
        recall = 0.0
    try:
        f1 = 2*precision*recall/(precision+recall)
    except ZeroDivisionError:
        f1 = 0.0
    print precision, recall, f1

    # with open('./dataset/feature/predict_result1.csv', "wb") as f:
    #     writer = csv.writer(f)
    #     writer.writerows(pred_list)
    # print "Done"


if __name__ == "__main__":

    # trainFile = './dataset/feature/chunk0.csv'
    # testFile = './dataset/feature/all.csv'
    # classification(trainFile,testFile)

    # train on chunk i, test on chunk i+1
    for index in range(0, 10):
        trainFile = './dataset/feature_embedding/chunk'+str(index)+'.csv'
        test_index = index+1 if index != 9 else 0
        testFile = './dataset/feature_embedding/chunk'+str(test_index)+'.csv'
        classification(trainFile,testFile)


