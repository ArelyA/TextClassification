from sklearn.naive_bayes import GaussianNB

__all__ = ['GaussianNB']

def transform(self, X, y=None):
    return self.predict_proba(X)

def fit_transform(self, X, y, sample_weight=None):
    return self.fit(X, y, sample_weight=None).transform(X, y)

setattr(GaussianNB, 'transform', transform)
setattr(GaussianNB, 'fit_transform', fit_transform)

class GaussianNB(GaussianNB):
    def __init__(self, *, priors=None, var_smoothing=1e-9):
        self.priors = priors
        self.var_smoothing = var_smoothing