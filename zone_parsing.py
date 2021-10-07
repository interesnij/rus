import sys,os
import re
import requests
import time
from bs4 import BeautifulSoup

project_dir = '../tr/tr/'

sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

domains_zons = [
    '.рф', '.com.ru', '.exnet.su', '.net.ru', '.org.ru', '.pp.ru', '.ru', '.ru.net', '.su', '.aero', '.asia',
    '.biz', '.com', '.info', '.mobi', '.name', '.net', '.org', '.pro', '.tel', '.travel', '.xxx', 'adygeya.ru',
    'arkhangelsk.su', 'balashov.su', 'bashkiria.ru', 'bashkiria.su', 'bryansk.su', 'cbg.ru', 'dagestan.ru',
    'dagestan.su', 'grozny.ru', 'kalmykia.ru', 'kalmykia.su', 'kaluga.su', 'karelia.su', 'khakassia.su',
    'kurgan.su', 'lenug.su', 'marine.ru', 'mordovia.ru', 'mordovia.su ', 'msk.ru', 'msk.su', 'murmansk.su',
    'mytis.ru', 'nalchik.ru', 'nalchik.su', 'nov.ru', 'nov.su', 'obninsk.su', 'penza.su', 'pokrovsk.su',
    'pyatigorsk.ru', 'sochi.su', 'spb.ru', 'spb.su', 'togliatti.su', 'troitsk.su', 'tula.su', 'tuva.su',
    'vladikavkaz.ru', 'vladikavkaz.su', 'vladimir.ru', 'vladimir.su', 'vologda.su', '.ad', '.ae', '.af', '.ai',
    '.al', '.am', '.aq', '.as', '.at', '.aw', '.ax', '.a z', '.ba', '.be', '.bg', '.bh', '.bi', '.bj', '.bm',
    '.bo', '.bs', '.bt', '.ca', '.cc', '.cd', '.cf', '.cg', '.ch', '.ci', '.cl', '.cm', '.cn', '.co', '.co.ao',
    '.co.bw', '.co.ck', '.co.fk', '.co.id', '.co.il', '.co.in', '.co.ke', '.co.ls', '.co.mz', '.co.no', '.co.nz',
    '.co.th', '.co.tz', '.co.uk', '.co.uz', '.co.za', '.co.zm', '.co.zw', '.com.ai', '.com.ar', '.com.au',
    '.com.bd', '.com.bn', '.com.br', '.com.cn', '.com.cy', '.com.eg', '.com.et', '.com.fj', '.com.gh', '.com.gn',
    '.com.gt', '.com.gu', '.com.hk', '.com.jm', '.com.kh', '.com.kw', '.com.lb', '.com.lr', '.com.mt', '.com.mv',
    '.com.ng', '.com.ni', '.com.np', '.com.nr', '. com.om', '.com.pa', '.com.pl', '.com.py', '.com.qa', '.com.sa',
    '.com.sb', '.com.sg', '.com.sv', '.com.sy', '.com.tr', '.com.tw', '.com.ua', '.com.uy', '.com.ve ', '.com.vi',
    '.com.vn', '.com.ye', '.cr', '.cu', '.cx', '.cz', '.de', '.dj', '. dk', '.dm', '.do', '.dz', '.ec', '.ee',
    '.es', '.eu', '.fi', '.fo', '.fr', '.ga', '.gd', '.ge', '.gf', '.gg', '.gi', '.gl', '.gm', '.gp', '.gr',
    '.gs', '.gy', ' .hk', '.hm', '.hn', '.hr', '.ht', '.hu', '.ie', '.im', '.in', '.in.ua', '.io ', '.ir',
    '.is', '.it', '.je', '.jo', '.jp', '.kg', '.ki', '.kiev.ua', '.kn', '.kr', '.ky', '.kz', '.li', '.lk', '.lt',
    '.lu', '.lv', '.ly', '.ma', '.mc', '.md', ' .me.uk', '.mg', '.mk', '.mo', '.mp', '.ms', '.mt', '.mu', '.mw',
    '.mx', '.my', ' .na', '.nc', '.net.cn', '.nf', '.ng', '.nl', '.no', '.nu', '.nz', '.org.cn', '.o rg.uk',
    '.pe', '.ph', '.pk', '.pl', '.pn', '.pr', '.ps', '.pt', '.re', '.ro', '. rs', '.rw', '.sd', '.se', '.sg',
    '.si', '.sk', '.sl', '.sm', '.sn', '.so', '.sr', '.st', '.sz', '.tc', '.td', '.tg', '.tj', '.tk', '.tl',
    '.tm', '.tn', '.to', ' .tt', '.tw', '.ua', '.ug', '.uk', '.us', '.vc', '.vg', '.vn', '.vu', '.ws', '.academy',
    'accountant', 'accountants', 'actor', 'adult', 'africa', 'agency', 'airf orce', 'apartments', '.app', 'army',
    'art', 'associates', 'attorney', 'auction', 'audio', 'auto', 'band', 'bank', 'bar', 'bargains', 'bayern', 'beer',
    'berlin', 'best', 'bet', 'bid', 'bike', 'bingo', 'bio', 'black', 'blackfriday', 'blog', ' blue', 'boutique',
    'broker', 'brussels', 'build', 'builders', 'business', 'buzz', 'cab', 'cafe', 'cam', 'camera', 'camp', 'capital',
    'car', 'cards', 'care', 'career', 'careers', 'cars', 'casa ', 'cash', 'casino', 'cat', 'catering', 'center',
    'ceo', '.charity', 'chat', 'cheap', 'christmas', 'church', 'city', 'claims', ' cleaning', 'click', 'clinic',
    'clothing', 'cloud', 'club', 'coach', 'codes', 'coffee', 'college', 'cologne', 'community', 'company', 'computer',
    'condos', 'construction', 'consulting', 'contractors', 'cooking', 'cool', 'coop', 'country', 'coupons', 'courses',
    'credit', 'creditcard', 'cricket', 'cruises', 'dance', 'date', 'dating', 'deals', 'degree', 'delivery', 'democrat',
    'dental', 'dentist', 'desi', 'design', 'diamonds', 'diet', 'digital', 'direct', 'directory', 'discount', 'doctor',
    'dog', 'domains', 'download', 'earth', 'education', 'email', 'energy', 'engineer', 'engineering', 'enterprises',
    'equipment', 'estate', 'events', 'exchange', 'expert', 'exposed', 'express', 'fail', 'faith', 'family', 'fans',
    'farm', 'fashion', 'film', 'finance', 'financial', 'fish', 'fishing', 'fit', 'fitness', 'flights', 'florist',
    'flowers', 'fm', 'football', 'forex', 'forsale', 'foun dation', 'fun', 'fund', 'furniture', 'futbol', 'fyi',
    'gallery', 'game', 'games', 'garden', 'gent', 'gift', 'gifts', 'gives', 'glass', 'global', 'gmbh', 'gold', 'golf',
    'graphics', 'gratis', 'green', 'gripe', 'group', 'guide', 'guitars', 'guru', 'haus', 'healthcare', 'help',
    'hiphop', 'hockey', 'holdings', 'holiday', ' horse', 'hospital', 'host', 'hosting', 'house', 'how', 'immo',
    'immobilien', 'in dustries', 'ink', 'institute', 'insure', 'international', 'investments', 'irish', 'jewelry',
    'jobs', 'juegos', 'kaufen', 'kim', 'kitchen', 'kiwi', 'land', 'lawyer', 'lease', 'legal', 'life', 'lighting',
    'limited', 'limo', 'link', 'live', '.llc', 'loan', 'loans', 'lol', 'london', 'love', 'ltd', '.luxe', 'luxury',
    'maison', 'management', 'market', 'marketing', 'mba', 'media', 'memorial', 'men', 'men u', 'miami', 'moda', 'moe', 'mom', 'money', 'mortgage', 'moscow', 'movie', 'navy ', 'network', 'news', 'ninja', 'observer', 'one', 'onl', 'online', 'ooo', '.page ', 'paris', 'partners', 'parts', 'party', 'pet', 'photo', 'photography', 'photos ', 'pics', 'pictures', 'pink', 'pizza', 'plumbing', 'plus', 'poker', 'press', 'p roductions', 'promo', 'properties', 'property', 'protection', 'pub', 'qpon', 'ra cing', 'radio', 'radio.am', 'radio.fm', '.realty', 'recipes', 'red', 'rehab', 'r eisen', 'rent', 'rentals', 'repair', 'report', 'republican', 'rest', 'restaurant ', 'review', 'reviews', 'rich', 'rip', 'rocks', 'rodeo', 'run', 'sale', 'salon', 'sarl', 'school', 'schule', 'science', 'security', 'services', 'sex', 'sexy', ' shiksha', 'shoes', 'shop', 'shopping', 'show', 'singles', 'site', 'ski', 'soccer ', 'social', 'software', 'solar', 'solutions', 'soy', 'space', '.sport', 'store', 'stream', 'studio', 'study', 'style', 'sucks', 'supplies', 'supply', 'support', 'surf', 'surgery', 'systems', 'tatar', 'tattoo', 'tax', 'taxi', 'team', 'tech', 'technology', 'tennis', 'theater', 'theatre', 'tickets', 'tienda', 'tips', 'ti res', 'tirol', 'today', 'tools', 'top', 'tours', 'town', 'toys', 'trade', 'tradi ng', 'training', 'tube', 'tv', 'university', 'uno', 'vacations', 'vegas', 'ventu res', 'vet', 'viajes', 'video', 'villas', '.vin', 'vip', 'vision', 'vodka', 'vot e', 'voting', 'voto', 'voyage', 'watch', 'webcam', 'website', 'wedding', 'wien', 'wiki', 'win', 'wine', 'work', 'works', 'world', 'wtf', 'xyz', 'yoga', 'zone', 'дети', 'москва', 'онлайн', 'орг', 'рус', 'сайт']

def get_html(url):
    r = requests.get(url)
    return r.text

def get_links(url):
    soup = BeautifulSoup(url, 'lxml')
    list = []
    #container = soup.find('div', class_='view-container')
    links = soup.find_all('a')
    for a in links:
        list.append(a.text)
    print (list)


def main():
    new_list = []
    for a in domains_zons:
        a.replace(" ", "")
        if a[0] == ".":
            pass
        else:
            a = "." + a
        new_list.append(a)
    print(new_list)

if __name__ == '__main__':
    main()
