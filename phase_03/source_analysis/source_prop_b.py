import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd 
from os import system as sys 
import seaborn as sns 

from astropy.io import fits 
hdu = fits.open('../data/LMXB_BH.fits')
data =  hdu[1].data 

fields="m.name,m.ra,m.dec,o.instrument,o.obsid,o.obi,o.src_rate_aper_m,o.src_rate_aper_lolim_m,o.src_rate_aper_hilim_m,o.src_cnts_aper_u,o.src_cnts_aper_lolim_u,o.src_cnts_aper_hilim_u,o.photflux_aper_w,o.photflux_aper_lolim_w,o.photflux_aper_hilim_w,o.photflux_aper_s,o.photflux_aper_lolim_s,o.photflux_aper_hilim_s,o.flux_aper_s,o.flux_aper_lolim_s,o.flux_aper_hilim_s,o.streak_src_flag,o.src_cnts_aper_h,o.src_cnts_aper_lolim_h,o.src_cnts_aper_hilim_h,o.sat_src_flag,o.src_rate_aper_s,o.src_rate_aper_lolim_s,o.src_rate_aper_hilim_s,o.src_cnts_aper_w,o.src_cnts_aper_lolim_w,o.src_cnts_aper_hilim_w,o.likelihood_b,o.likelihood_h,o.likelihood_m,o.likelihood_s,o.likelihood_u,o.likelihood_w,o.gti_start,o.gti_stop,o.gti_elapse,o.gti_obs,o.gti_end,o.gti_mjd_obs,o.mjd_ref,o.photflux_aper_b,o.photflux_aper_lolim_b,o.photflux_aper_hilim_b,o.src_rate_aper_b,o.src_rate_aper_lolim_b,o.src_rate_aper_hilim_b,o.dither_warning_flag,o.theta,o.phi,o.src_rate_aper_w,o.src_rate_aper_lolim_w,o.src_rate_aper_hilim_w,o.region_id,o.flux_aper_h,o.flux_aper_lolim_h,o.flux_aper_hilim_h,o.src_cnts_aper_m,o.src_cnts_aper_lolim_m,o.src_cnts_aper_hilim_m,o.photflux_aper_u,o.photflux_aper_lolim_u,o.photflux_aper_hilim_u,o.src_cnts_aper_s,o.src_cnts_aper_lolim_s,o.src_cnts_aper_hilim_s,o.src_rate_aper_h,o.src_rate_aper_lolim_h,o.src_rate_aper_hilim_h,o.flux_significance_b,o.flux_significance_h,o.flux_significance_m,o.flux_significance_s,o.flux_significance_u,o.flux_significance_w,o.src_rate_aper_u,o.src_rate_aper_lolim_u,o.src_rate_aper_hilim_u,o.flux_aper_b,o.flux_aper_lolim_b,o.flux_aper_hilim_b,o.flux_aper_u,o.flux_aper_lolim_u,o.flux_aper_hilim_u,o.flux_aper_m,o.flux_aper_lolim_m,o.flux_aper_hilim_m,o.flux_aper_w,o.flux_aper_lolim_w,o.flux_aper_hilim_w,o.photflux_aper_h,o.photflux_aper_lolim_h,o.photflux_aper_hilim_h,o.src_cnts_aper_b,o.src_cnts_aper_lolim_b,o.src_cnts_aper_hilim_b,o.photflux_aper_m,o.photflux_aper_lolim_m,o.photflux_aper_hilim_m,o.hard_hm,o.hard_hm_lolim,o.hard_hm_hilim,o.hard_hs,o.hard_hs_lolim,o.hard_hs_hilim,o.hard_ms,o.hard_ms_lolim,o.hard_ms_hilim,o.flux_powlaw,o.flux_powlaw_lolim,o.flux_powlaw_hilim,o.powlaw_gamma,o.powlaw_gamma_lolim,o.powlaw_gamma_hilim,o.powlaw_gamma_rhat,o.powlaw_nh,o.powlaw_nh_lolim,o.powlaw_nh_hilim,o.powlaw_nh_rhat,o.powlaw_ampl,o.powlaw_ampl_lolim,o.powlaw_ampl_hilim,o.powlaw_ampl_rhat,o.powlaw_stat,o.flux_bb,o.flux_bb_lolim,o.flux_bb_hilim,o.bb_kt,o.bb_kt_lolim,o.bb_kt_hilim,o.bb_kt_rhat,o.bb_nh,o.bb_nh_lolim,o.bb_nh_hilim,o.bb_nh_rhat,o.bb_ampl,o.bb_ampl_lolim,o.bb_ampl_hilim,o.bb_ampl_rhat,o.bb_stat,o.flux_brems,o.flux_brems_lolim,o.flux_brems_hilim,o.brems_kt,o.brems_kt_lolim,o.brems_kt_hilim,o.brems_kt_rhat,o.brems_nh,o.brems_nh_lolim,o.brems_nh_hilim,o.brems_nh_rhat,o.brems_norm,o.brems_norm_lolim,o.brems_norm_hilim,o.brems_norm_rhat,o.brems_stat,o.flux_apec,o.flux_apec_lolim,o.flux_apec_hilim,o.apec_kt,o.apec_kt_lolim,o.apec_kt_hilim,o.apec_kt_rhat,o.apec_abund,o.apec_abund_lolim,o.apec_abund_hilim,o.apec_abund_rhat,o.apec_z,o.apec_z_lolim,o.apec_z_hilim,o.apec_z_rhat,o.apec_nh,o.apec_nh_lolim,o.apec_nh_hilim,o.apec_nh_rhat,o.apec_norm,o.apec_norm_lolim,o.apec_norm_hilim,o.apec_norm_rhat,o.apec_stat,o.var_index_b,o.var_prob_b,o.ks_prob_b,o.kp_prob_b,o.var_sigma_b,o.var_mean_b,o.var_min_b,o.var_max_b,o.var_index_h,o.var_prob_h,o.ks_prob_h,o.kp_prob_h,o.var_sigma_h,o.var_mean_h,o.var_min_h,o.var_max_h,o.var_index_m,o.var_prob_m,o.ks_prob_m,o.kp_prob_m,o.var_sigma_m,o.var_mean_m,o.var_min_m,o.var_max_m,o.var_index_s,o.var_prob_s,o.ks_prob_s,o.kp_prob_s,o.var_sigma_s,o.var_mean_s,o.var_min_s,o.var_max_s,o.var_index_u,o.var_prob_u,o.ks_prob_u,o.kp_prob_u,o.var_sigma_u,o.var_mean_u,o.var_min_u,o.var_max_u,o.var_index_w,o.var_prob_w,o.ks_prob_w,o.kp_prob_w,o.var_sigma_w,o.var_mean_w,o.var_min_w,o.var_max_w,o.livetime,o.detector,a.match_type,o.cnts_aper_b,o.cnts_aperbkg_b,o.cnts_aper_h,o.cnts_aperbkg_h,o.cnts_aper_m,o.cnts_aperbkg_m,o.cnts_aper_s,o.cnts_aperbkg_s,o.cnts_aper_u,o.cnts_aperbkg_u,o.cnts_aper_w,o.cnts_aperbkg_w"

def hr():
    print('____________________________________________________')

def to_float(d):
    temp = []
    for di in d:
        try:
            temp.append(float(di))
        except Exception as e:
            print(e)
            print('NaN detectedresetting value')
            temp.append(np.NAN)
    temp = np.asarray(temp)
    return temp 
#print(data['B_RA'])
from ciao_contrib.runtool import search_csc
i = 1
for ra,dec in zip(data['B_RA'][60:61] , data['B_DEC'][60:61]):
    hr()
    print('source Number :  ' , i)
    print(ra,dec)
    try:
        '''
        s = search_csc(
            radunit="arcsec", 
            columns=fields, 
            bands="broad",
            clobber="yes" ,
            radius=1, 
            pos= str(ra)+','+str(dec)  ,
            outfile='temp.csv')
        #sys('search_csc outfile=trial.csv radunit=arcsec columns="SOS,SOP,SOV , o.gti_obs m.flux_aper_b" bands=broad clobber=yes radius=1 pos="65.428058,32.907468"')
        #print(s)
        '''
        data = pd.read_csv('temp.csv', delimiter='\t' , comment='#')
        data = data[data['match_type']=='u          ']
        #data = data[data['match_type']=='u          ']
        data.sort_values(by=['gti_obs'] , inplace=True)
        #display(np.unique(data['instrument']))
        print(data)

        hard_hm = np.asarray([float(f) for f in data['hard_hm']])
        hard_ms = np.asarray([float(f) for f in data['hard_ms']])
        hard_ratio =  hard_hm/hard_ms


        data_all =  pd.DataFrame()
        data_all.insert(0, 'date', data['gti_obs'])
        data_all.insert(1,'var' , to_float(data['var_mean_b']))
        data_all.insert(2,'counts' , to_float(data['cnts_aper_b']))
        data_all.insert(3,'rate' , to_float(data['src_rate_aper_b']))
        data_all.insert(4,'flux' , to_float(data['flux_aper_b']))
        data_all.insert(5,'flux_hi_lim' , to_float(data['flux_aper_hilim_b']))
        data_all.insert(6,'flux_lo_lim' , to_float(data['flux_aper_lolim_b']))
        data_all.insert(7,'significance' , to_float(data['flux_significance_b']))
        data_all.insert(8,'exp_time' , to_float(data['livetime'])/1000)
        data_all.insert(9,'hardness' , hard_ratio)

        var = np.asarray([float(v) for v in data_all['var']])
        var_err = np.asarray([float(v) for v in data['var_sigma_b']])

        flux_lolim =  np.asarray([float(v) for v in data_all['flux_hi_lim']])
        flux_hilim =  np.asarray([float(v) for v in data_all['flux_lo_lim']])
        

        #display(data_all)
        data_all.sort_values(by=['date'] , inplace=True)
        print(data_all)
        dates = [d[:10] for d in data_all['date']]

        #data_all = pd.to_numeric(data_all , downcast='float')

        plt.style.use('seaborn-dark-palette')
        f, ax = plt.subplots(3, 2, sharex=True , figsize=(12,8) ,constrained_layout=False)
        plt.xticks(rotation=45)
        ax = np.reshape(ax, (6))
        #ax[0].plot(dates, var , label='Variability')
        ax[2].errorbar(dates , var , yerr=var_err , fmt='.k' , capsize=2 , markersize=10 , label='variability')
        ax[2].set_ylabel('B , counts/s')
        
        ax[1].errorbar(dates , data_all['flux'] , uplims=flux_hilim,lolims=flux_lolim, fmt='.k' , capsize=2 , markersize=10 , label='flux')
        ax[1].set_ylabel('erg/s/cm^2')
        
        ax[4].plot(dates, data_all['hardness'] , label='Hardness ratio')
        ax[4].set_ylabel('hard/soft')
        
        ax[3].plot(dates, data_all['exp_time'] , label='exposure time')
        ax[3].set_ylabel('kS')
        
        ax[5].plot(dates, data_all['significance'] , label='Source Significance')
        ax[5].set_ylabel('hard/soft')

        for a in ax:
            a.legend(loc='upper right')
            plt.setp(a.xaxis.get_majorticklabels(), rotation=45)

        f.suptitle('NS , V1037 CAS')
        plt.subplots_adjust(hspace=0 , bottom=0.2)
        plt.show()

        
    except Exception as e:
        print(e)
        print('Error Occured , manual inspetion needed ')
    hr()
    i+=1