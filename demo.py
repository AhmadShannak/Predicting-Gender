# dep
# we need to create our decision tree so we import this :
# wondering whatss a decision tree?? here is alink :
# https://upload.wikimedia.org/wikipedia/commons/f/f3/CART_tree_titanic_survivors.png
from sklearn import tree

# [ height,weight,shoe size]
BodyDetails = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
                [190, 90, 47], [175, 64, 39],[177, 70, 40], [159, 55, 37], [171, 75, 42],
                [181, 85, 43]]
# male or female (those are labels for the above list for ex : [181, 80, 44] which is the first
# element is a male while the third element  [160, 60, 38] is a female)
LabelsForTHeBodyDetailsList = ['male', 'male', 'female', 'female', 'male', 'male', 'female',
                               'female', 'female', 'male', 'male']

# Now lets intilize our tree
clf = tree.DecisionTreeClassifier()
# lets put some data in it
clf = clf.fit(BodyDetails, LabelsForTHeBodyDetailsList)

# lets test it
# step one : asking the user to enter his height and his weight and shoe size
print ('Please Enter Your Height And Your Weight And Your Shoe Size ', 'Eg:190 70 43')
# step two : storing them
list = map(int, raw_input().split())
# step three : lets try to predict it
pred = clf.predict([list])

# print our predict
print pred




