# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:48:56 2020

@author: Eunjoo
"""

import gc

# remove unnecessary variables
def clean_up(vars_):
    for var in vars_:
        del var 
    print(gc.collect())
    

# scoring 
from sklearn.metrics import accuracy_score, cohen_kappa_score, classification_report, auc, roc_curve, precision_recall_curve
import pandas as pd
import matplotlib.pyplot as plt

def scoring(y_test, y_pred):
    acc = accuracy_score(y_test, y_pred)
    ck = cohen_kappa_score(y_test, y_pred)
    print ('accuracy score: ', round(acc, 4), 'cohens kappa: ', round(ck, 4)) 
    print(classification_report(y_test, y_pred, zero_division=0))

def get_pred(model, X_test):
    y_pred_p = model.predict_proba(X_test)
    y_pred = model.predict(X_test)
    return y_pred, y_pred_p
    
def evaluating(y_test, y_pred, y_pred_p):
    y_vals = pd.get_dummies(y_test, drop_first=False).values
    classes = ['negative', 'none', 'positive']

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize = (12, 6))
    ## Plot roc
    for i in range(3):
        FPR, TPR, thresh = roc_curve(y_vals[:,i], y_pred_p[:,i])

        ax[0].plot(FPR, TPR, label=f'{classes[i]} auc: {round(auc(FPR, TPR), 2)}')
        ax[0].plot([0,1], [0,1], linestyle='--')
        ax[0].set(xlim=[-0.05,1.0], ylim=[0.0,1.05], 
              xlabel="False Positive Rate", 
              ylabel="True Positive Rate", 
              title="ROC Curve")
        ax[0].legend()

        precision, recall, thresh = precision_recall_curve(y_vals[:,i], y_pred_p[:,i])
        ax[1].plot(recall, precision, label=f'{classes[i]} auc: {round(auc(recall, precision), 2)}')
        ax[1].set(xlim=[0.0,1.05], ylim=[0.0,1.05], xlabel='Recall', ylabel="Precision", 
                  title="Precision-Recall curve")
        ax[1].legend()
    plt.show()

    acc = accuracy_score(y_test, y_pred)
    ck = cohen_kappa_score(y_test, y_pred)
    print ('accuracy score: ', round(acc, 4), 'cohens kappa: ', round(ck, 4)) 
    print(classification_report(y_test, y_pred, zero_division=0))
