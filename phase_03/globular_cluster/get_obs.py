
#print(data['B_RA'])
from astropy.io import fits 
import numpy as np 
import pandas as pd 
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
            #sys('search_csc outfile=trial.csv radunit=arcsec columns="SOS,SOP,SOV , o.gti_obs m.flux_aper_b" bands=broad clobber=yes radius=1 pos="65.428058,32.907468"')
            #print(s)
            
            data = pd.read_csv(f_name, delimiter='\t' , comment='#')
            #save only non-empty dataframe
            data = data[data['match_type']=='u          ']
            data = data[data['instrument']=='ACIS']
            print(data)
            #------master info 
            '''
            master= {
                "name" : data_fits['A_NAME'][count] , 
                "ch_name" : data['name'][0] , 
                "flux_b" : float(data['mstr_flux_aper_b'][0]) ,
                "var" : float(data['var_inter_index_b'][0]) , 
                "num_obs" : int(data['acis_num'][0])
            }
            '''

            '''
            hard_hm = np.asarray([float(f) for f in data['hard_hm']])
            hard_ms = np.asarray([float(f) for f in data['hard_ms']])
            hard_ratio =  hard_hm/hard_ms
            
            data.sort_values(by=['gti_obs'] , inplace=True)
            rows = ['livetime' ,'gti_obs']
            for f in filters:
                for r in use_f:
                    rows.append(r+f)
            #print(rows)
            data_all = data[rows]
            dates =data_all['gti_obs']
            data_all = data_all.drop(columns=['gti_obs'])
            #print(data_all)
            for j in data_all[:10]:
                data_all[j] = to_float(data_all[j])
            #print(data_all)
            data_mean = pd.DataFrame()
            i = 0
            for r in use_f:
                prop = []
                for f in filters:
                    prop.append(r+f)
                temp = data_all[prop].mean(axis=1)
                data_mean.insert(i , r , temp)
                i+=1
            
            
            data_mean.insert(0 , 'hardness' , hard_ratio)
            data_mean.insert(0 , 'date' , dates)
            data_mean.insert(0 , 'exp_time' , data_all['livetime'])
            
            print(data_mean)
            make_plot(data_mean , master , str(count))
            hr()
            print('saving data.....')
            data.index.name='index'
            data_mean.index.name='index'
            data.to_csv('sources/NS/tables/'+str(count)+'all.csv')
            data_mean.to_csv('sources/NS/tables/'+str(count)+'obs.csv')
            '''
        except Exception as e:
            print(e)
            print('Error Occured , manual inspetion needed ')
        hr()
        count+=1


#hdu = fits.open('../data/LMXB_NS.fits')
#data_fits =  hdu[1].data 
#source_info(data_fits)