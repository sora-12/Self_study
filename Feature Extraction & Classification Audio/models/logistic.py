import numpy as np 
import sklearn
from sklearn.linear_model import LogisticRegression
import feat_extract

feat_extract.main()

X_train =  np.load('feat.npy')
y_train =  np.load('label.npy').ravel()

X_test=np.load('predict_feat.npy')
y_test=np.load('predict_label.npy').ravel()

log_clf = LogisticRegression()
log_clf.fit(X_train,y_train)
log_clf.score(X_test, y_test)

