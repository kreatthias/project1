from sklearn import tree
import numpy
from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(handle_unknown='ignore')
X = [['schere', 1], ['stein', 2], ['papier', 3]]
enc.fit(X)
print(X)

X = [[-1,-500,'s']]
Y = ['pr']

clf_tree = tree.DecisionTreeClassifier();
clf_tree = clf_tree.fit(X,Y);

test_data = [[1,1,'s']]

prediction_tree = clf_tree.predict(test_data);

print("Prediction: ", prediction_tree);
