## Black hole confirmation methods 
Black hole transients are also referred as X-ray novae , microquasars , soft-xray transients. Low mass x-ray biaries are for a prolonge period of quiescence , typically decades and are sometimes punctuated by dramatic x-ray and optical outbursts,  (cite orosz2001 A BLACK HOLE IN THE SUPERLUMINAL SOURCE SAX J1819.3[2525 (V4641 SGR)1)

what happens during outburst - X-ray emission is dominated by thermal emission from hot inner disc , and UV , optical and IR emission i produced by the outer disc by reprocessing x-ray. We can study the structure of disc by correlation of x-ray with other bands.

Outburst in accreting NS x-ray binary results in pulsuations or thermonuclear flashes and spectrum is relatively soft at the onset of outburst .(\cite{zand2002} , 10.1051/0004-6361:20021123)

## What was wrong with lase analysis and NN result 
> THere were lot of repeated data in BH source list I used. and hence I wrongly reported 123 sources.
There are in-total 33 sources (23 galactic, 10 in NGC-) ,
Source of repotition - 
* Same source were there in different catalogues with different names
* For same source , within cone search radius (2 asrcsec) for a given RA/DEC chandra catalogue had more than one source


## Steps for catalogue making 

First extract information for RA/DEC , may come from FITS file (from HEASARC > Chandra cross-correlation )
run script [download_data.py]
Data will be stored in corresponding folter > all the observations as seperate csv files

Open fits file or use notebook - cat info to load only reqd data columns , export in CSV format , open excel sheet
in excel sheet - 
    first sort by chandra names - flag all the repeated sources (this removes same source but different names in different catalogues) copy all unflagged rows into next sheet
    
    Now sort by source names , more than one different chandra sources might be there for the same source , this means that due to high resolution of CHANDRA, it has resolved more source in the given search radius , we need to select our source of concern.If one of them is haveing very small X-offset choose it. or in chandra observation file and in the original catalogue file tyr to find whose properties matches the most and keep that and flag other rows

    now run script [remove_not_needed_obs.py] , it will copy only the required observation to a destination folder

    run script [prepare_data.py] 

    run neural network


TO-DO 

> Catalogue of Neutron STAR

> Probe Network 

> Distance to globular cluster


## Problem in current training scheme 

We have increased our dataset by considering each observations as seperate source.
We are taking all the "observations" and reshuffling them and then splitting them into training and test data
But it is very likely that some observations from test sources went into training set.

Likely solution - make train-test split before reshuffling 

## Improvements from version 3 

Here we have split train and test data before processing
before running 'remove_not_needed'  need to run 'split_source_list'


# params used

var_inter_sigma
var_inter_prob
var_inter_index

var_max
var_min
var_mean
var_sigma
kp_prob
ks_prob
var_prob
var_index

flux_aper_hilim
flux_aper_lolim
flux_aper
photflux_aper_hilim
photflux_aper_lolim
photflux_aper

hard_hm
hard_hs
hard_ms

flux_powlaw
powlaw_gamma
powlaw_nh
powlaw_ampl
powlaw_stat
flux_bb
flux_bb_hilim
flux_bb_lolim
bb_kt
bb_nh
bb_ampl
bb_stat
flux_brems
brems_kt
brems_nh
brems_stat


hard_hm_hilim
hard_hm_lolim
hard_hs_hilim
hard_hs_lolim
hard_ms_hilim
hard_ms_lolim


flux_powlaw_hilim
flux_powlaw_lolim
powlaw_gamma_hilim
powlaw_gamma_lolim
powlaw_nh_hilim
powlaw_nh_lolim
powlaw_ampl_hilim
powlaw_ampl_lolim
bb_ampl_lolim
bb_ampl_hilim
flux_brems_lolim
flux_brems_hilim
brems_kt_hilim
brems_kt_lolim
brems_nh_hilim
brems_nh_lolim
bb_kt_hilim
bb_kt_lolim
bb_nh_hilim
bb_nh_lolim
