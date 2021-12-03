test_src_bh = [
       'CXOU J100518.5-07413',
       'GINGA 1354-645      ',
       'GRO J1655-40        ',
       'GX 339-4            ',
       'CXOU J100516.5-07420',
       'CXOU J100517.1-07421',
       'GS 1354-645         ',]
train_src_bh = ['1A 0620-00          ', 'CJ0422+32           ',
       'CXOU J100506.7-07443', 'CXOU J100508.7-07444',
       'CXOU J100510.0-07452', 'CXOU J100510.9-07453',
       'CXOU J100514.2-07423', 'CXOU J100515.4-07425',
       'CXOU J100516.2-07423', 
       'IGR J17464-3213     ', 'J1047+1234          ',
       'J1242+3232          ', 'J1745-2900          ',
       'KV UMA              ', 'SAX J1819.3-2525    ',
       'SAXWFC J1819.4-2524.', 'V404 CYG            ',
       'XTE J1550-564       ', 'XTE J1650-500       ',
       'XTE J1859+226       ']


test_src_cv = [
     '2XMM J231519.0-591029 ', 'CHI J162011-5002 1    ',
       'CHI J172550-3533 2    ','IGR J15529-5029       ', 
       'XSS J12270-4859       ','1WGA J1617.0-2258     ',
       '1WGA J1910.8-5958     ',
       '2XMM J004414.4+412204 ', '2XMM J020052.2-092431 ',
]
train_src_cv = ['1RXS J134210.2+282250 ', 'XMMSL2 J004231.9+41162',
       '1WGA J1740.6-5340     ', 
       '2XMM J174816.9-280750 ', '2XMM J175013.1-064227 ',
       '2XMM J180507.1-274308 ', '2XMM J190109.3-220003 ',
        'CHI J194939+2631 1    ',
       'CXOGLB J002359.3-72043', 'CXOGLB J002401.4-72044',
       'CXOGLB J002402.1-72045', 'CXOGLB J002402.1-72054',
       'CXOGLB J002402.5-72051', 'CXOGLB J002403.1-72044',
       'CXOGLB J002403.6-72045', 'CXOGLB J002403.7-72042',
       'CXOGLB J002403.8-72062', 'CXOGLB J002404.2-72045',
       'CXOGLB J002404.9-72045', 'CXOGLB J002404.9-72050',
       'CXOGLB J002405.3-72042', 'CXOGLB J002405.6-72044',
       'CXOGLB J002406.0-72045', 'CXOGLB J002406.3-72044',
       'CXOGLB J002407.1-72054', 'CXOGLB J002407.7-72052',
       'CXOGLB J002407.9-72045', 'CXOGLB J002408.2-72043',
       'CXOGLB J002408.4-72050', 'CXOGLB J002409.2-72054',
       'CXOGLB J002410.0-72044', 'CXOGLB J002410.6-72051',
       'CXOGLB J002410.7-72042', 'CXOGLB J002411.8-72044',
       'CXOGLB J002415.8-72043', 'CXOGLB J002416.9-72042',
       'CXOU J192035.7+374452 ', 'CXOU J192056.3+374613 ',
       'CXOU J192105.4+374457 ', 'CXOU J192107.4+374756 ',
       'IGR J15529-5029       ',  '[DSH2013] 24          ',
       '[HPH2013] 100         ', '[HPH2013] 108         ',
       '[HPH2013] 123         ', '[HPH2013] 143         ',
       '[HPH2013] 146         ', '[HPH2013] 150         ',
       '[HPH2013] 160         ', '[HPH2013] 176         ',
       '[HPH2013] 192         ', '[HPH2013] 196         ',
       '[HPH2013] 252         ', '[HPH2013] 273         ',
       '[HPH2013] 50          ', '[HPH2013] 81          ']


train_src_ns = ['1A 1742-289         ', '1A 1743-288         ',
       '1A 1744-361         ', '1H 1715-321         ',
       '1WGA J0514.1-4002   ', '1WGA J0748.5-6745   ',
       '1WGA J1747.4-3002   ', '1WGA J1911.2+0035   ',
       '2E 1613.5-5053      ', 
       'EXO 1745-248        ', 'GRO J1744-28        ',
       'GRS 1741.9-2853     ', 'H 1658-298          ',
       'IGR J00291+5934     ', 'IGR J17464-2811     ',
       'J1748-2021#1        ', 'J1748-2021#2        ',
       'J1748-2446          ', 'J1748-3607          ',
       'J1749-2808          ', 'J1749-2919          ',
       'J1751-3037          ', 'SAX J1750.8-2900    ',
       'SAX J1810.8-2609    ', 'SAXWFC J1734.2-2605.',
       'SAXWFC J1740.7-2818.', 'SAXWFC J1744.9-2921.',
       'SAXWFC J1747.0-2853.', 'SAXWFC J1748.1-2446.',
       
       'XTE J1739-285       ', 'XTE J2123-058       ',
       'XMMU J004245.2+41172',
       'XMMU J004414.0+41220',]

test_src_ns = [
    '3A 2129+470         ', 'J1824-2452          ',
       'KS 1731-260         ',
       '4U1745-203          ', 'BW ANT              ',
       'CEN X-4             ', 'EXO 0748-676        ',
       'XB 1732-304         ',  'XTE J1709-267       ',
]


train_src_plsr = [
        'PSR J0525-6607', 'PSR J0537-6910', 'PSR J0100-7211',
       'PSR J0630-2834', 'PSR J0633+0632', 'PSR J0633+1746',
       'PSR J0729-1448', 'PSR J0734-1559', 'PSR J0737-3039',
       'PSR J0835-4510', 'PSR J0908-4913', 'PSR J1016-585',
       'PSR J1023+0038', 'PSR J1023-574', 'PSR J1028-5819',
       'PSR J1044-5737', 'PSR J1048-5832', 'PSR J1057-5226',
       'PSR J1101-6101', 'PSR J1111-6039', 'PSR J1112-610',
       'PSR J1119-6127', 'PSR J1124-3653', 'PSR J1124-591',
       'PSR J1135-6055', 'PSR J1210-5226', 'PSR J1227-4853',
       'PSR J1231-1411', 'PSR J1311-3430', 'PSR J1357-6429',
       'PSR J1400-6325', 'PSR J1413-6205', 'PSR J1417-4402',
       'PSR J1418-605', 'PSR J1429-591', 'PSR J1459-6053',
       'PSR J1509-585', 'PSR J1514-4946', 'PSR J1531-5610',
       'PSR J1550-5418', 'PSR J1614-2230', 'PSR J1617-5055',
       'PSR J1622-4950', 'PSR J1628-3205', 'PSR J1635-4735',
       'PSR J1640-4631', 'PSR J1647-4552', 'PSR J1653-0158',
       'PSR J1658-5324', 'PSR J1702-4128', 'PSR J1709-4429',
       'PSR J1714-3810', 'PSR J1714-3830', 'PSR J1718-3825',
       'PSR J1730-3350', 'PSR J1732-313', 'PSR J1740+1000',
       'PSR J1741-205', 'PSR J1744-1134', 'PSR J1745-2900',
       'PSR J1803-2137', 'PSR J1809-1943', 'PSR J1809-233',
       'PSR J1809-2332', 'PSR J1810+1744', 'PSR J1811-1925',
       'PSR J1813-1246', 'PSR J1813-1749', 'PSR J1816+4510',
       'PSR J1824-2452', 'PSR J1826-125', 'PSR J1826-1334',
       'PSR J1833-0831', 'PSR J1834-0845', 'PSR J1836+592',
       'PSR J1841-0456', 'PSR J1846+091', 'PSR J1849-0001',
       'PSR J1852+0040', 'PSR J1856+0113', 'PSR J1907+060',
       'PSR J1907+0602', 'PSR J1930+1852', 'PSR J1932+1059',
       'PSR J1939+213', 'PSR J1952+3252', 'PSR J1958+284',
       'PSR J1959+2048', 'PSR J2017+0603', 'PSR J2017+3625',
       'PSR J2021+365', 'PSR J2021+3651', 'PSR J2021+4026',
       'PSR J2022+3842', 'PSR J2028+3332', 'PSR J2032+4127',
       'PSR J2043+171', 'PSR J2047+105', 'PSR J2051-0827',
       'PSR J2124-335', 'PSR J2139+471', 'PSR J2214+3000',
       'PSR J2215+5135', 'PSR J2229+6114', 'PSR J2238+5903',
       'PSR J2241-5236', 'PSR J2256-1024', 'PSR J0101-6422',
       ]

test_src_plsr = [
    'PSR J0007+7303', 'PSR J0023+0923',
        'PSR J0205+6449', 'PSR J0357+3205',
       'PSR J0358+5413',  'PSR J0418+5732',
       'PSR J0437-4715','PSR J2339-0533' , 
       'PSR J0359+5414',
]


train_src = list(train_src_bh+train_src_ns+train_src_cv+train_src_plsr)
test_src = list(test_src_bh+test_src_ns+test_src_cv+test_src_plsr)