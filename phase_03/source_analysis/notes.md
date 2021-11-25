# Data preparation

this phase is dedicated to creation of training data .
we need to collect information for each source ,
collect sources examples and their individual observations 
look for whether they are in outburst phase or not 

## Tasks
* Download chandra cross matched sources for different classes
* Use CIAO tools for per observation study 
* plot flux vs observation date for each source
* Mark source as good or bad (maybe some kind of weighting would be better)

## Unsupervised learning idea 
 Instead of preparing training dat , well go in reverse.
 > We'll collect all te chandra x-ray sources which belong to globular clusters ,
 
 > try to cluster them ,using some clustering algorith , maybe VAE or something

 > Now take already classified sources, and try to place them ion our cluster diagram to decide which category they belong to.  