# 1900968
from sklearn.svm import SVC
import numpy as np

__all__ = ['SVC']

def separateInClasses(self):
  """
  Separates support vectors by classes

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
  accuracy_score : shape(n_samples)
  """
  c = 0
  class_sv = []

  for e in self.n_support_:
    z = 0
    c += 1
    print("class: ", c, " vectors: ", e)
    class_sv.append(self.support_vectors_[z:e])
    z = e
  self.class_sv = class_sv

def avgDistSV(self, X, distFunc):
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
  self.separateInClasses()
  SV = self.class_sv
  dist = np.zeros((len(X), len(SV)))
  for i, x in enumerate(X): # each sample in X
    for j, c in enumerate(SV): # each class in SV
      for sv in c: # each support vector in class
        dist[i][j] += distFunc(x, sv)
      dist[i][j] /=  len(c)

  return dist


def getDistSV(self, X, distFunc):
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
  self.separateInClasses()
  SV = self.class_sv
  dist = [] #np.zeros((len(X), len(SV)))
  for i, x in enumerate(X): # each sample in X
    arr = []
    for j, c in enumerate(SV): # each class in SV
      t = []
      for sv in c: # each support vector in class
        t.append(distFunc(x, sv))
      arr.append(t)
    dist.append(arr)
      #dist[i][j] /=  len(c)

  return dist

setattr(SVC, 'separateInClasses', separateInClasses)
setattr(SVC, 'avgDistSV', avgDistSV)
setattr(SVC, 'getDistSV', getDistSV)

"""class SVC(SVC):
    def __init__(self, *, C=1.0, kernel='rbf', degree=3, gamma='scale',
                 coef0=0.0, shrinking=True, probability=False,
                 tol=1e-3, cache_size=200, class_weight=None,
                 verbose=False, max_iter=-1, decision_function_shape='ovr',
                 break_ties=False,
                 random_state=None):
        class_sv = []
        super().__init__(
            kernel=kernel, degree=degree, gamma=gamma,
            coef0=coef0, tol=tol, C=C, nu=0., shrinking=shrinking,
            probability=probability, cache_size=cache_size,
            class_weight=class_weight, verbose=verbose, max_iter=max_iter,
            decision_function_shape=decision_function_shape,
            break_ties=break_ties,
            random_state=random_state)"""