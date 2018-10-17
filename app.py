from sklearn import tree
import numpy

X = [[1,5,15],[76,-4,-14],[-1,-500,1989]]
Y = ['pr','pr','mr']

clf_tree = tree.DecisionTreeClassifier();
clf_tree = clf_tree.fit(X,Y);

test_data = numpy.array([2,4,4]).reshape(1,-1)

prediction_tree = clf_tree.predict(test_data);

print("Prediction: ", prediction_tree);
