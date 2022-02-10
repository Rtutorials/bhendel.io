import sklearn.metrics
from flask import Flask
import pandas as pd
import random
from flask import request
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pickle

def Examine_the_pickle():
    X_test = pd.read_csv("X_test.csv")
    Y_pred_original = np.loadtxt("preds.csv", delimiter=",", dtype = int)
    Y_pred = nb2.predict(X_test)
    assert np.array_equal(Y_pred, Y_pred_original)


app = Flask(__name__)
@app.route('/predict_churn')
def predict_churn():
    argslist = []
    for col in cnames:
        argslist.append(request.args.get(col))
    in_row = pd.DataFrame(np.array(argslist).reshape(1, -1))
    in_row.columns = X_test.columns
    print(str(nb2.predict(in_row)))
    return str(nb2.predict(in_row))



if __name__ == '__main__':
    infile = open('churn_model.pkl', 'rb')
    nb2 = pickle.load(infile)
    infile.close()
    Examine_the_pickle()
    X_test = pd.read_csv("X_test.csv")
    cnames = X_test.columns
    app.run(host='0.0.0.0')



