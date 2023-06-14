# integration link url
import httpx

timeout = httpx.Timeout(connect=5, read=5 * 60, write=5, pool=5)

brno_integ_url = httpx.get('https://www.firmy.cz/detail/13220286-centrum-pro-cizince-jmk-brno-veveri.html', verify=False, timeout=timeout)

zlin_integ_url = httpx.get('http://www.integracnicentra.cz/zlinsky-kraj/#kontakty', verify=False, timeout=timeout)
zlin_ru_integ_url = httpx.get('http://www.integracnicentra.cz/zlinsky-kraj/?lang=ru', verify=False, timeout=timeout)

praha_integ_url = httpx.get('https://www.firmy.cz/detail/576633-centrum-pro-integraci-cizincu-o-p-s-praha-karlin.html', verify=False, timeout=timeout)

plzen_integ_url = httpx.get('http://www.integracnicentra.cz/plzensky-kraj/#kontakty', verify=False, timeout=timeout)
plzen_ru_integ_url = httpx.get('https://www.integracnicentra.cz/plzensky-kraj/?lang=ru', verify=False, timeout=timeout)

kladno_integ_url = httpx.get('https://www.firmy.cz/detail/12966446-centrum-pro-integraci-cizincu-o-p-s-kladno.html', verify=False, timeout=timeout)
teplice_integ_url = httpx.get('https://www.firmy.cz/detail/12911013-poradna-pro-integraci-teplice.html', verify=False, timeout=timeout)
benesov_integ_url = httpx.get('https://www.integracnicentra.cz/benesov/?lang=ru', verify=False, timeout=timeout)
olomouc_integ_url = httpx.get('https://www.integracnicentra.cz/olomoucky-kraj/?lang=ru', verify=False, timeout=timeout)
jihlava_integ_url = httpx.get('https://www.integracnicentra.cz/kraj-vysocina/?lang=ru', verify=False, timeout=timeout)
liberec_integ_url = httpx.get('https://www.firmy.cz/detail/12966448-centrum-pro-integraci-cizincu-o-p-s-liberec-iv-perstyn.html', verify=False, timeout=timeout)
ostrava_integ_url = httpx.get('https://www.integracnicentra.cz/moravskoslezsky-kraj/?lang=ru', verify=False, timeout=timeout)
pribram_integ_url = httpx.get('https://www.integracnicentra.cz/pribram/?lang=ru', verify=False, timeout=timeout)
pardubice_integ_url = httpx.get('https://www.integracnicentra.cz/pardubicky-kraj/?lang=ru', verify=False, timeout=timeout)
kutnah_integ_url = httpx.get('https://www.integracnicentra.cz/kutna-hora/?lang=ru', verify=False, timeout=timeout)
karlovyv_integ_url = httpx.get('https://www.integracnicentra.cz/karlovarsky-kraj/?lang=ru', verify=False, timeout=timeout)
mladab_integ_url = httpx.get('https://www.firmy.cz/detail/2666451-centrum-pro-integraci-cizincu-o-p-s-mlada-boleslav-iii.html', verify=False, timeout=timeout)
ustinl_integ_url = httpx.get('https://www.firmy.cz/detail/429676-poradna-pro-integraci-usti-nad-labem-centrum.html', verify=False, timeout=timeout)
hradeck_integ_url = httpx.get('https://www.firmy.cz/detail/12899080-diecezni-katolicka-charita-hradec-kralove-integracni-centrum-pro-cizince-hradec-kralove.html', verify=False, timeout=timeout)
ceskeb_integ_url = httpx.get('https://www.integracnicentra.cz/jihocesky-kraj/?lang=ru', verify=False, timeout=timeout)

