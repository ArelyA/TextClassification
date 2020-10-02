# TextClassification
# 1900968
[Click me for pretrained models](https://drive.google.com/drive/folders/1cePGZH7ZBIFJY6ovKi1uaTbKEKwmKbvd?usp=sharing)

[Click me for precalculated distances](https://drive.google.com/drive/folders/1lE3CcYC0wcI3x6nUqgKryyMKaEo3UyB0?usp=sharing)

[Click me for datasets](https://drive.google.com/drive/folders/1p3-IeJ1MMAdtjBEtOj3RMIvuYtaGkjpi)
## Pipeline:
Vectorizer &#8594; SVM &#8594; Distance &#8594; OutlierRemoval

### Vectorizers:
* TFIDF
* Gaussian Naive Bayes
* Complement Naive Bayes

### SVM Kernels:
* linear
* polynomial
* rbf
* sigmoid
 
### Similarity Distance Measures:
* Euclidian
* BrayCurtis
* Canberra
* Manhattan

### Outlier Removal
* Interquantile Range
* Z-Score

## WebKB

* [Train set](https://drive.google.com/file/d/1gGMMNFANv59ENBzw2e0SyvG_Ycx04xXX/view?usp=sharing)
* [Test set](https://drive.google.com/file/d/1gGMMNFANv59ENBzw2e0SyvG_Ycx04xXX/view?usp=sharing)

### [Train SVMs](https://github.com/ArelyA/TextClassification/blob/main/webkb_train_SVM.ipynb)

### [Calculate Distances](https://github.com/ArelyA/TextClassification/blob/main/webkb_distances.ipynb)

### [Evaluate SVM](https://github.com/ArelyA/TextClassification/blob/main/webkb_evaluate_SVM.ipynb)

### [Evaluate Distances](https://github.com/ArelyA/TextClassification/blob/main/webkb_evaluate_distances.ipynb)

### Evaluate Distances with Outlier Removal
#### [IQR](https://github.com/ArelyA/TextClassification/blob/main/webkb_evaluate_distances_IQR.ipynb)
#### [Z-Score](https://github.com/ArelyA/TextClassification/blob/main/webkb_evaluate_distances_Z.ipynb)

## R8
* [Train set](https://drive.google.com/file/d/1kXCjpY0YD_e7dCwNU3ZdYambgf0RYErm/view?usp=sharing)
* [Test set](https://drive.google.com/file/d/1sRj3CyoJ9KfCF3mPFQHY5_oVPRekmjHH/view?usp=sharing)

### [Train SVMs](https://github.com/ArelyA/TextClassification/blob/main/r8_train_SVM.ipynb)

### [Calculate Distances](https://github.com/ArelyA/TextClassification/blob/main/r8_distances.ipynb)

### [Evaluate SVM](https://github.com/ArelyA/TextClassification/blob/main/r8_evaluate_SVM.ipynb)

### [Evaluate Distances](https://github.com/ArelyA/TextClassification/blob/main/r8_evaluate_distances.ipynb)

### Evaluate Distances with Outlier Removal
#### [IQR](https://github.com/ArelyA/TextClassification/blob/main/r8_evaluate_distances_IQR.ipynb)
#### [Z-Score](https://github.com/ArelyA/TextClassification/blob/main/r8_evaluate_distances_Z.ipynb)
