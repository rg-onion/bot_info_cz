# mvcr link url
import httpx

timeout = httpx.Timeout(connect=5, read=5 * 60, write=5, pool=5)

# Южночешский край
ceske_budejovice_url = httpx.get('https://www.firmy.cz/detail/2675100-ministerstvo-vnitra-regionalni-oddeleni-pobytu-cizincu-ceske-budejovice-ceske-budejovice-3.html', verify=False, timeout=timeout)
pisek_url = httpx.get('https://www.firmy.cz/detail/2675117-ministerstvo-vnitra-oddeleni-pobytu-cizincu-pisek-pisek-prazske-predmesti.html', verify=False, timeout=timeout)
jindrichuv_hradec_url = httpx.get('https://www.firmy.cz/detail/2675113-ministerstvo-vnitra-oddeleni-pobytu-cizincu-jindrichuv-hradec-jindrichuv-hradec-ii.html', verify=False, timeout=timeout)

# карловарский
karlovy_vary_url = httpx.get('https://www.firmy.cz/detail/2675155-ministerstvo-vnitra-regionalni-oddeleni-pobytu-cizincu-karlovy-vary-karlovy-vary.html', verify=False, timeout=timeout)
# краловоградетский
hradec_kralove_url = httpx.get('https://www.firmy.cz/detail/2675171-ministerstvo-vnitra-regionalni-oddeleni-pobytu-cizincu-hradec-kralove-hradec-kralove.html', verify=False, timeout=timeout)
# либерец
liberec_url = httpx.get('https://en.firmy.cz/company/2675187-ministerstvo-vnitra-regionalni-oddeleni-pobytu-cizincu-liberec-liberec-i-stare-mesto.html', verify=False, timeout=timeout)

# Моравскосилезский
ostrava_url = httpx.get('https://www.firmy.cz/detail/2675199-ministerstvo-vnitra-regionalni-oddeleni-pobytu-cizincu-ostrava-ostrava-vitkovice.html', verify=False, timeout=timeout)
frydekMistek_url = httpx.get('https://www.firmy.cz/detail/2675206-ministerstvo-vnitra-oddeleni-pobytu-cizincu-frydek-mistek-frydek-mistek-mistek.html', verify=False, timeout=timeout)

# Оломоуцкий
olomouc_url = httpx.get('https://www.firmy.cz/detail/2675212-ministerstvo-vnitra-regionalni-oddeleni-pobytu-cizincu-prerov-prerov-i-mesto.html', verify=False, timeout=timeout)

# Пардубицкий
pardubice_url = httpx.get('https://www.firmy.cz/detail/2675226-ministerstvo-vnitra-regionalni-oddeleni-pobytu-cizincu-pardubice-pardubice-zelene-predmesti.html', verify=False, timeout=timeout)

# Пльзенский
plzen_url = httpx.get('https://www.firmy.cz/detail/2675242-ministerstvo-vnitra-regionalni-oddeleni-pobytu-cizincu-plzen-plzen-vychodni-predmesti.html', verify=False, timeout=timeout)

# прага
# прага1
prague1_url = httpx.get('https://www.firmy.cz/detail/2675027-ministerstvo-vnitra-oddeleni-pobytu-cizincu-praha-i-praha-ruzyne.html', verify=False, timeout=timeout)
prague2_url = httpx.get('https://www.firmy.cz/detail/2675050-ministerstvo-vnitra-oddeleni-pobytu-cizincu-praha-ii-praha-chodov.html', verify=False, timeout=timeout)
prague3_url = httpx.get('https://www.firmy.cz/detail/2675037-ministerstvo-vnitra-oddeleni-pobytu-cizincu-praha-iii-praha-stresovice.html', verify=False, timeout=timeout)
prague_letna_url = httpx.get('https://www.firmy.cz/detail/2675043-ministerstvo-vnitra-oddeleni-pobytu-cizincu-praha-letna-praha-holesovice.html', verify=False, timeout=timeout)

# среднечешский
benesov_url = httpx.get('https://www.firmy.cz/detail/12700677-ministerstvo-vnitra-oddeleni-pobytu-cizincu-benesov-benesov.html', verify=False, timeout=timeout)
kladno_url = httpx.get('https://www.firmy.cz/detail/2675081-ministerstvo-vnitra-oddeleni-pobytu-cizincu-kladno-kladno.html', verify=False, timeout=timeout)
kutna_hora_url = httpx.get('https://www.firmy.cz/detail/2675090-ministerstvo-vnitra-oddeleni-pobytu-cizincu-kutna-hora-kutna-hora-vnitrni-mesto.html', verify=False, timeout=timeout)
mlada_boleslav_url = httpx.get('https://www.firmy.cz/detail/2675096-ministerstvo-vnitra-oddeleni-pobytu-cizincu-mlada-boleslav-mlada-boleslav-iii.html', verify=False, timeout=timeout)
pribram_url = httpx.get('https://www.firmy.cz/detail/2675077-ministerstvo-vnitra-oddeleni-pobytu-cizincu-pribram-pribram-v-zdabor.html', verify=False, timeout=timeout)

# Устецкий
usti_nad_labem_url = httpx.get('https://www.firmy.cz/detail/2675261-ministerstvo-vnitra-regionalni-oddeleni-pobytu-cizincu-usti-nad-labem-usti-nad-labem-centrum.html', verify=False, timeout=timeout)

# высочина
jihlava_url = httpx.get('https://www.firmy.cz/detail/13033324-ministerstvo-vnitra-regionalni-oddeleni-pobytu-cizincu-jihlava-jihlava.html', verify=False, timeout=timeout)
zlin_url = httpx.get('https://www.firmy.cz/detail/2675293-ministerstvo-vnitra-regionalni-oddeleni-pobytu-cizincu-zlin-zlin.html', verify=False, timeout=timeout)

# брно
brno_url = httpx.get('https://www.policie.cz/clanek/sprava-jihomoravskeho-kraje-kontakty-oddeleni-pobytovych-agend.aspx', verify=False, timeout=timeout)











