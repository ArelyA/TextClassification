from statistics import median, mean
from scipy.stats import zscore
from sklearn.metrics import accuracy_score
import numpy as np
from joblib import dump, load

def split(dataset):
  dataset = dataset[:len(dataset) - 1]

  X = []
  y = []

  for id, doc in enumerate(dataset):
    dataset[id] = doc.split('	')
    
    y.append(dataset[id][0])
    X.append(dataset[id][1])

  print("(", len(X),len(X[0]), ")")

  return X, y


def medDistSV(X, SV, distFunc):
  """
  Average distance between points and support vectors

  Parameters
  ----------------
  X : shape(n_samples, n_features)
    array of points
  SV : shape(n_classes, n_support_vectors)
    array of support vectors divided by classes
  distFunc : function
    distance function received for calculations

  Attributes
  ----------------
  dist : shape(n_samples, n_classes)
  """
  dist = np.zeros((len(X), len(SV)))
  for i, x in enumerate(X): # each sample in X
    for j, c in enumerate(SV): # each class in SV

      arr = []
      for sv in c: # each support vector in class
        arr.append(distFunc(x, sv))
      dist[i][j] =  median(arr)

  return dist

def avgDistSV(X, SV, distFunc):
  """
  Average distance between points and support vectors

  Parameters
  ----------------
  X : shape(n_samples, n_features)
    array of points
  SV : shape(n_classes, n_support_vectors)
    array of support vectors
  distFunc : function
    distance function received for calculations

  Attributes
  ----------------
  dist : shape(n_samples, n_classes)
    array of distances of each point in the sample to each of the classes
  """
  dist = np.zeros((len(X), len(SV)))
  for i, x in enumerate(X): # each sample in X
    for j, c in enumerate(SV): # each class in SV
      for sv in c: # each support vector in class
        dist[i][j] += distFunc(x, sv)
      dist[i][j] /=  len(c)

  return dist

def evaluate(distances, classes, y):
  """
  Calculates the class with the smallest distance per sample

  Parameters
  ----------------
  distances : shape(n_samples, n_classes)
    array of distances of each point in the sample to each of the classes
  classes : shape(n_classes)
    array of class labels
  y : shape(n_samples)
    array of actual labels per sample

  Attributes
  ----------------
  accuracy: shape(n_samples)
  """
  y_pred = []
  for i, e in enumerate(distances): # each element in distances
    y_pred.append(classes[e.argmin()])
  #print(y_pred, y, sep="\n")
  accuracy = accuracy_score(y, y_pred)
  return accuracy

def svm_serializer(X, y, c, kernel, currentFolder, vect, SVC):
  arr =[]
  for k in kernel:
    temp = []
    for i in c:
      clf_SVC = SVC(C=i, kernel=k)
      clf_SVC.fit(X, y)
      filename = currentFolder + vect + '-' + k + "-" + str(i) + ".joblib"
      dump(clf_SVC, open(filename, 'wb'))
      print("saved ", filename, end="\t")
      temp.append(clf_SVC)
    arr.append(temp)
  return arr
  
def save_distances(X, c, kernel, distanceFunc, distFunc, vect, currentFolder):
    for k in kernel:
        for i in c:
            filename = currentFolder + "models/" + vect + '-' + k + "-" + str(i)
            clf = load(filename + '.joblib')
            distances = clf.getDistSV(X, distanceFunc)
            filename = currentFolder + "distances/" + distFunc + "-" + vect + '-' + k + "-" + str(i)
            np.save(filename + ".npy", distances)

def getClassDist(y, classes, c, kernel, func, distFunc, vect, currentFolder, remOut="None"):
  for k in kernel:
    print(k, end="\t")
    for i in c:
      filename = currentFolder + "distances/" + distFunc + "-" + vect + '-' + k + "-" + str(i)
      distances = np.load(filename + ".npy", allow_pickle=True)
      dist = np.zeros((len(distances), len(distances[0])))
      for z, sample in enumerate(distances):
        for j, cl in enumerate(sample):
          if(np.nanstd(cl) == 0.0):
              dist[z][j] = cl[0]
          else:
            if remOut == "IQR":
              #IQR
              Q1 = np.nanquantile(cl,0.25)
              Q3 = np.nanquantile(cl, 0.75)
              IQR = Q3 - Q1
              lower = Q1 - 1.5 * IQR
              upper = Q3 + 1.5 * IQR
              arr = []
              for d in cl:
                if (d >= lower) and (d <= upper):
                  arr.append(d)
              if(len(arr) == 0):
                dist[z][j] = func(cl)
              else:
                dist[z][j] = func(arr)
            elif remOut == "Z":
              #Z-score
              arr = []
              zs = zscore(cl, nan_policy='omit')
              for e, d in enumerate(zs):
                if (abs(d) <= 3):
                  arr.append(cl[e])
              dist[z][j] = func(arr)
            else:
              dist[z][j] = func(cl)
      print(evaluate(dist, classes, y), end="\t")

def evaluateSVM(X, y, c, kernel, vect, currentFolder):
  for k in kernel:
    print(k, end="\t")
    for i in c:
      filename = currentFolder + "models/" + vect + '-' + k + "-" + str(i)
      clf = load(filename + '.joblib')
      print(clf.score(X, y), end="\t")
  print("\n")

