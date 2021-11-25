# CHANDRA X-ray Source catalogue probabilistic classification using Machine Learning
# Introduction
## Problem Statement

--- 

# Chandra Source Catalogue [CSC-2.0]
## Master Table
## Observation Table 
## Features 
### Flux Parameters
### Model-fit Parameters
### Variability information
### Observation information
---

# Data
## Training data collection
### Catalogue search method
## Data filtering
* Pileup-filter
* Streak Filter
* Saturation filter
* Significace filter
### FLux filter
GLobular cluster analysis


> Final collection

---

# Classifiers

* Logistic regression
* K Nearest Neighbour
* Fully Connected network
* Convolution neural netwrok
* Random Forest classifier


# Pretraining
## Data Scaling
	* Nomralisation
	* Standardisation
	* None
## Data Imputation
	* Zero
	* Mean
	* Median
	* Correlation
	* Random Forest Imputation
## Result
### Validation Scheme
> Monte-Carlo cross validation
---

# Training
## Vanila random Forest
## Vanila RF with PCA
## RF hyperparameter Tuning
	* Num-trees
	* Max-depth

## Training result
* Accuracy
* MC cross validation
* f1-score
* Recall
* Precision
* ROC-AUV
### Feature importance
> How it is defined
#### NS feat importance
#### BH feature importance

---
# Conclusion
# Future roadmap
* Add more classes
* Feature permutation study
* Finding anamolous sources

# Appendix
