from sklearn import tree

X = [[1],[5],[15],[76],[-4],[-14],[-1],[-500],[1989],[2],[42]]
Y = ['p','p','p','p','m','m','m','m','p','p,','p']

clf_tree = tree.DecisionTreeClassifier();
clf_tree = clf_tree.fit(X,Y);

test_data = [[2],[6],[-3]];

prediction_tree = clf_tree.predict(test_data);

print("Prediction: ", prediction_tree);
