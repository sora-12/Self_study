import numpy as np 
import sklearn
from sklearn.linear_model import LogisticRegression
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import feat_extract

feat_extract.main(setting_first=False)

X_train =  np.load('feat_big.npy')
y_train =  np.load('label_big.npy').ravel()

X_test=np.load('predict_feat_big.npy')
y_test=np.load('predict_label_big.npy').ravel()

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)

log_clf = LogisticRegression()
log_clf.fit(X_train,y_train)
log_clf.score(X_test, y_test)

