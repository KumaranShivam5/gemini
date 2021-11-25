# XMM variable source classification

## Instrument

|              | Paper                                                                                               | Our work                                                                                                                                           |
| ------------ | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Obs          | XMM Newton                                                                                          | CHANDRA                                                                                                                                            |
| Instrument   | EPIC-PN                                                                                             | ACIS                                                                                                                                               |
| Resolution   | 3.3 arcsec                                                                                          | 1 arcsec                                                                                                                                           |
| Energy Bands | 0.2 -   0.5 keV<br />0.5 -   1.0 keV<br />1.0 -   2.0 keV<br />2.0 -   4.5 keV<br />4.5 -  12.0 keV | broad band (b) : 0.5-7.0 keV<br />ultrasoft (u): 0.2-0.5 keV<br />soft (s) : 0.5-1.2 keV<br />medium (m) : 1.2-2.0 keV<br />hard (h) : 2.0-7.0 keV |

## Sources

|                           | Paper                                                                                                                                                                                                    | Our work                                                                                                                                       |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Source of interest        | time variable sources                                                                                                                                                                                    | Globular cluster sources                                                                                                                       |
| Source distribution       | All sky                                                                                                                                                                                                  | globular clusters                                                                                                                              |
| Target class              | AGN , SSS , ULX , GRB , XRB , CV , star                                                                                                                                                                  | NS-LMXRB , BH-LMXRB, CV , Pulsars                                                                                                              |
| Training data preparation | They have first identified all the time varaible x-ray sources in 2XMMi catalogue , then cross-matched to find the nature of as many source as possible , and taken those classes as the target classes. | Based on litereature review , we have identified our target class - and then identified sources belonging to those class in Chandra catalogue. |

## Features

In the paper  , they are extracting feature table from the light curve on their own insted of directly taking it from XMM catalogue. Also they are using multi-wavelength (radio / optical / NIR) magnitude values.

We are taking the features available in Chandra source catalogue.

#### Paper

* Time Series features
  * preiodicity
  * Power-law decay of lightcurve
  * Number of flares
  * Statistical features
* Contextual features
  * Hardness ratio
  * Optical / NIR cross match
  * Radio cross maatch
  * Association with galaxies
  * Galactic coordinates

#### Our work

* Aperture photometry
  * Photon flux in different bands
  * energy flux - photon flux in a given band* avg band energy
* Spectral Hardness ratio
* Model spectral fits
  * Black body
  * Powerlaw
* Temproal varability
  * Intra-observation Gregory-Loredo varaibaility
  * Intra-observation Kolmogonorov-Smironov test variabilityFeature importance

## Classifier / Result

| Paper                                                                                             | Our work                                                 |
| ------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Random Forest                                                                                     | Random Forest                                            |
| SMOTE algorithm for class imbalance problem                                                       | No sognificant class imbalance                           |
| Classifying observations and not sources                                                          | Classifying observation and not soures                   |
| GINI Impurity based Feaure importance as give by Random Forest , no class-wise feature importance | Class-wise feature importance                            |
| Report class membership probability for observations                                              | Ambiguous class for prediction below a certain threshold |
