
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
