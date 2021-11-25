import numpy as np 
from matplotlib import pyplot as plt 
import pandas as pd 
import os 

cat = pd.read_csv('gc_cat.csv' , delimiter=',')
cat.index_name ='index'
print(cat[['RA(2000)' , 'DEC']])

#from get_obs import source_info 
#source_info(cat['RA(2000)'] , cat['DEC'])
print(cat['ID'][0])
IDS = [c[1:] for c in cat['ID']]
cat.insert(0, 'name', IDS)
print(cat['name'][0])


from ciao_contrib.runtool import search_csc
fields="m.name,m.ra,m.dec,o.obsid,o.obi,o.src_rate_aper_m,o.src_rate_aper_lolim_m,o.src_rate_aper_hilim_m,o.src_cnts_aper_u,o.src_cnts_aper_lolim_u,o.src_cnts_aper_hilim_u,o.photflux_aper_w,o.photflux_aper_lolim_w,o.photflux_aper_hilim_w,o.photflux_aper_s,o.photflux_aper_lolim_s,o.photflux_aper_hilim_s,o.flux_aper_s,o.flux_aper_lolim_s,o.flux_aper_hilim_s,o.streak_src_flag,o.src_cnts_aper_h,o.src_cnts_aper_lolim_h,o.src_cnts_aper_hilim_h,o.sat_src_flag,o.src_rate_aper_s,o.src_rate_aper_lolim_s,o.src_rate_aper_hilim_s,o.src_cnts_aper_w,o.src_cnts_aper_lolim_w,o.src_cnts_aper_hilim_w,o.likelihood_b,o.likelihood_h,o.likelihood_m,o.likelihood_s,o.likelihood_u,o.likelihood_w,o.gti_start,o.gti_stop,o.gti_elapse,o.gti_obs,o.gti_end,o.gti_mjd_obs,o.mjd_ref,o.photflux_aper_b,o.photflux_aper_lolim_b,o.photflux_aper_hilim_b,o.src_rate_aper_b,o.src_rate_aper_lolim_b,o.src_rate_aper_hilim_b,o.dither_warning_flag,o.theta,o.phi,o.src_rate_aper_w,o.src_rate_aper_lolim_w,o.src_rate_aper_hilim_w,o.region_id,o.flux_aper_h,o.flux_aper_lolim_h,o.flux_aper_hilim_h,o.src_cnts_aper_m,o.src_cnts_aper_lolim_m,o.src_cnts_aper_hilim_m,o.photflux_aper_u,o.photflux_aper_lolim_u,o.photflux_aper_hilim_u,o.src_cnts_aper_s,o.src_cnts_aper_lolim_s,o.src_cnts_aper_hilim_s,o.src_rate_aper_h,o.src_rate_aper_lolim_h,o.src_rate_aper_hilim_h,o.flux_significance_b,o.flux_significance_h,o.flux_significance_m,o.flux_significance_s,o.flux_significance_u,o.flux_significance_w,o.src_rate_aper_u,o.src_rate_aper_lolim_u,o.src_rate_aper_hilim_u,o.flux_aper_b,o.flux_aper_lolim_b,o.flux_aper_hilim_b,o.flux_aper_u,o.flux_aper_lolim_u,o.flux_aper_hilim_u,o.flux_aper_m,o.flux_aper_lolim_m,o.flux_aper_hilim_m,o.flux_aper_w,o.flux_aper_lolim_w,o.flux_aper_hilim_w,o.photflux_aper_h,o.photflux_aper_lolim_h,o.photflux_aper_hilim_h,o.src_cnts_aper_b,o.src_cnts_aper_lolim_b,o.src_cnts_aper_hilim_b,o.photflux_aper_m,o.photflux_aper_lolim_m,o.photflux_aper_hilim_m,o.hard_hm,o.hard_hm_lolim,o.hard_hm_hilim,o.hard_hs,o.hard_hs_lolim,o.hard_hs_hilim,o.hard_ms,o.hard_ms_lolim,o.hard_ms_hilim,o.flux_powlaw,o.flux_powlaw_lolim,o.flux_powlaw_hilim,o.powlaw_gamma,o.powlaw_gamma_lolim,o.powlaw_gamma_hilim,o.powlaw_gamma_rhat,o.powlaw_nh,o.powlaw_nh_lolim,o.powlaw_nh_hilim,o.powlaw_nh_rhat,o.powlaw_ampl,o.powlaw_ampl_lolim,o.powlaw_ampl_hilim,o.powlaw_ampl_rhat,o.powlaw_stat,o.flux_bb,o.flux_bb_lolim,o.flux_bb_hilim,o.bb_kt,o.bb_kt_lolim,o.bb_kt_hilim,o.bb_kt_rhat,o.bb_nh,o.bb_nh_lolim,o.bb_nh_hilim,o.bb_nh_rhat,o.bb_ampl,o.bb_ampl_lolim,o.bb_ampl_hilim,o.bb_ampl_rhat,o.bb_stat,o.flux_brems,o.flux_brems_lolim,o.flux_brems_hilim,o.brems_kt,o.brems_kt_lolim,o.brems_kt_hilim,o.brems_kt_rhat,o.brems_nh,o.brems_nh_lolim,o.brems_nh_hilim,o.brems_nh_rhat,o.brems_norm,o.brems_norm_lolim,o.brems_norm_hilim,o.brems_norm_rhat,o.brems_stat,o.flux_apec,o.flux_apec_lolim,o.flux_apec_hilim,o.apec_kt,o.apec_kt_lolim,o.apec_kt_hilim,o.apec_kt_rhat,o.apec_abund,o.apec_abund_lolim,o.apec_abund_hilim,o.apec_abund_rhat,o.apec_z,o.apec_z_lolim,o.apec_z_hilim,o.apec_z_rhat,o.apec_nh,o.apec_nh_lolim,o.apec_nh_hilim,o.apec_nh_rhat,o.apec_norm,o.apec_norm_lolim,o.apec_norm_hilim,o.apec_norm_rhat,o.apec_stat,o.var_index_b,o.var_prob_b,o.ks_prob_b,o.kp_prob_b,o.var_sigma_b,o.var_mean_b,o.var_min_b,o.var_max_b,o.var_index_h,o.var_prob_h,o.ks_prob_h,o.kp_prob_h,o.var_sigma_h,o.var_mean_h,o.var_min_h,o.var_max_h,o.var_index_m,o.var_prob_m,o.ks_prob_m,o.kp_prob_m,o.var_sigma_m,o.var_mean_m,o.var_min_m,o.var_max_m,o.var_index_s,o.var_prob_s,o.ks_prob_s,o.kp_prob_s,o.var_sigma_s,o.var_mean_s,o.var_min_s,o.var_max_s,o.var_index_u,o.var_prob_u,o.ks_prob_u,o.kp_prob_u,o.var_sigma_u,o.var_mean_u,o.var_min_u,o.var_max_u,o.var_index_w,o.var_prob_w,o.ks_prob_w,o.kp_prob_w,o.var_sigma_w,o.var_mean_w,o.var_min_w,o.var_max_w,o.livetime,o.detector,a.match_type,o.cnts_aper_b,o.cnts_aperbkg_b,o.cnts_aper_h,o.cnts_aperbkg_h,o.cnts_aper_m,o.cnts_aperbkg_m,o.cnts_aper_s,o.cnts_aperbkg_s,o.cnts_aper_u,o.cnts_aperbkg_u,o.cnts_aper_w,o.cnts_aperbkg_w , m.significance,m.likelihood,m.pileup_flag,m.sat_src_flag,m.streak_src_flag,m.flux_aper_b,m.flux_aper_lolim_b,m.flux_aper_hilim_b,m.var_inter_index_b,m.var_inter_prob_b,m.var_inter_sigma_b,m.var_inter_index_h,m.var_inter_prob_h,m.var_inter_sigma_h,m.var_inter_index_m,m.var_inter_prob_m,m.var_inter_sigma_m,m.var_inter_index_s,m.var_inter_prob_s,m.var_inter_sigma_s,m.var_inter_index_u,m.var_inter_prob_u,m.var_inter_sigma_u,m.var_inter_index_w,m.var_inter_prob_w,m.var_inter_sigma_w,m.acis_num,m.acis_hetg_num,m.acis_letg_num,m.hrc_num,m.hrc_hetg_num,m.hrc_letg_num"

use_f = ['var_mean' , 'var_sigma','cnts_aper', 'flux_aper','flux_aper_hilim' , 'flux_aper_lolim' , 'flux_significance']
filters = ['_h' ,'_m' ,'_s' ,'_u' ,'_b']
def hr():
    print('-----------------------------------------------------------------------------')

def source_info(RA , DEC  , name):

    count = 0 
    for ra,dec , n in zip(RA , DEC , name):
        hr()
        print('source Number :  ' , count )
        print(ra,dec)
        try:
            f_name = 'cluster_obs_data/'+str(count)+'_'+n+'.csv'
            s = search_csc(
                radunit="arcmin", 
                columns=fields,
                bands="broad",
                clobber="yes" ,
                radius=20, 
                pos= str(ra)+','+str(dec)  ,
                outfile=f_name)
            data = pd.read_csv(f_name, delimiter='\t' , comment='#')
            print(data)
            print('removing empty cluster')
            if(len(data)==0):
                print('rm '+f_name)
                os.system('rm '+f_name)
        except Exception as e:
            print(e)
            print('Error Occured , manual inspetion needed ')
        hr()
        count+=1

# search and save sources file
source_info(cat['RA(2000)'] , cat['DEC'] , cat['name'])