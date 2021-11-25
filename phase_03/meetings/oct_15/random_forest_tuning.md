# Recap

* We had selected Data processing technique
* Identified best Network .

![sc](norm.png)

![sc](imp.png)

## Random Forest classifier

> RF Example illustration

![rf](rf.png)

> Does RF always works better

* Different from Neural Network or Deep learing algorithms
* RF can not do feature extraction

# PCA Dimensionality Reduction

> ![el](ellipse_fitting.png)
> Source : https://nextjournal.com/tempdata73/dimensionality-reduction

> Where To use dim reduction

> Where Not to use dim reduction

---

![pca](pca_dim_plot.png)

# Hyper Parameter Tuning For Random Forest

![pt](param_tuning.png)

---

# Result

### Network Variance

![ts](tuning_res.png)

| Param           | Vanila RF | Tuned RF |
| --------------- | --------- | -------- |
| Mean Accuracy   | 0.916     | 0.926    |
| Acc Variance    | 0.026     | 0.03     |
| Ambiguous Class | 62 / 460  | 42 / 460 |

As far as accuracy is concerned , hyperparameter tuning has not resulted in much improvement , but let's dig deeper into the probability confidence .

### Probability Quality

![ecdf](prob_comparison.jpg)

### Feature Importance

> NS Feature Importance

![ns](ns_feat_imp.png)

> BH Feature Importance

![bh](bh_feat_imp.png)

---

# Next

* Add CV , Isolated Pulsar