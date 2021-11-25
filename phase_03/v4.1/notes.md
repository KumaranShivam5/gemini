# Result Analysis
## Aim
* Probility output study
* Same Source different observation different classification issue
* CLuster of parameter correlation 

---
## Probablity Output Study 
 For now the classification scheme is, we assign a class to a source if the output prob is more than 0.5 , but there is a fundamental problem with this approach. 0.5 prob means that next time if we predict the same source then 50 percent chances are there that the same source will be classified correctly. SO we should set a certain threshold.

 ### Posterior probabilities

 To evaluate the perofmance of how good out netwrk is performing for certain class , we check the probability distrbution for certain class predicted class.
 Density distribution of output probabilities corresponding to predicted class

> Result 

![ecdf](pred_result/ns_bh_post_prob_ecdf.jpg)

![kde](pred_result/ns_bh_post_prob_kde.jpg)

> Inference 

From the posterior probability distribution plot above, we see that NS curve has a steep rise about 1.0 . BH curve peaks before 1.0 and has a broader distribution. This means that 0