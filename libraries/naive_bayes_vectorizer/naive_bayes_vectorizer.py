from sklearn.naive_bayes import ComplementNB

__all__ = ['ComplementNB']

def transform(self, X, y=None):
    return self.predict_log_proba(X)

def fit_transform(self, X, y, sample_weight=None):
    return self.fit(X, y, sample_weight=None).transform(X, y)

setattr(ComplementNB, 'transform', transform)
setattr(ComplementNB, 'fit_transform', fit_transform)

class ComplementNB(ComplementNB):
    def __init__(self, *, alpha=1.0, fit_prior=True, class_prior=None,
                 norm=False):
        self.alpha = alpha
        self.fit_prior = fit_prior
        self.class_prior = class_prior
        self.norm = norm