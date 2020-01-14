# -*- coding: utf-8 -*-
from locale import *
import sys,os

project_dir = '../tr/tr/'

sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django
django.setup()

import soundcloud
from music.models import *
from datetime import datetime, date, time


client = soundcloud.Client(client_id='dce5652caa1b66331903493735ddd64d')
page_size = 200
genres_list = SoundGenres.objects.values('name')
genres_list_names = [name['name'] for name in genres_list]

b_rus_list_1 = [
"B & W",
"B Robin",
"B-15 Project & Ekko City feat. Crissy D & Lady G",
"B-Bros",
"B-Case",
"B-Fly",
"B-Funky feat. Max C",
"B-Legit feat. J Boog",
"B-O-S feat. Olivera",
"B-OK feat. Roxie & Kristian Kostov",
"B-Real",
"B-Sensual feat. Abbey Lewis",
"B-Tribe",
"B. J. Thomas",
"B. Smyth",
"B.B. King",
"B.D.V",
"B.F.I",
"B.F.M.V.",
"B.L. Lover",
"B.o.B",
"B.O.O.N. Feat. Xl Singleton",
"B.U.S.",
"B*star feat. Kreayshawn",
"B&S Project",
"B2T feat. Bizaro",
"B3rror",
"B5",
"Baako feat. Nomeli",
"Baard",
"Baauer",
"Babak",
"Babay",
"Babe feat. Mirka",
"Babe Ruth",
"Babeheaven",
"Babek Mamedrzaev",
"Babou",
"Baby Alice",
"Baby Ariel",
"Baby Bash feat. Mickael, Paula DeAnda & Lucky Luciano",
"Baby Bino feat. Lil Hawaii",
"Baby Blue",
"Baby Charles",
"Baby Huey",
"Baby K",
"Baby Lullaby",
"Baby Noel",
"Baby Rasta & Gringo feat. Jowell & Randy, Guelo Star & De La Ghetto",
"Baby Tash",]

b_rus_list_2 = [
"Baby.Lil feat. Sean Kingston & Far East Movement",
"Baby's Gang",
"Babyface",
"Babylon Zoo",
"Babyroots",
"Baccara",
"Back 2 Back",
"Back 2 Base",
"Back Bone Slip",
"Back Door Slam",
"Background Music Masters",
"Backstreet boys",
"Bacon Tree feat. Daimy Lotus & Nino Lucarelli",
"Bad Balance",
"Bad Booty Brothers",
"Bad Boys Blue",
"Bad Bunny",
"Bad Catholics & Dec3mber",
"Bad Company",
"Bad Computer",
"Bad English",
"Bad Gyal",
"Bad Hombre",
"Bad Manners",
"Bad Paris feat. Mimoza",
"Bad Royale",
"Bad Suns",
"Bad Wolves",
"Badalamenti",
"Badboys Brothers",
"BadBoySwiss",
"Badflite",
"Badpojken feat. Panetoz",
"Badr Avsar",
"Badshah",
"BadVice DJ",
"Badybangers",
"BadКузя & Zharova",
"BAELI",
"Baer feat. The Crushboys",
"Bag Raiders feat. The Kite String Tangle",
"Bageerov",
"BaGGer feat. Nina",
"Baggi Begovic",
"Baha Men",
"Bahar feat. Nitro",
"Bahari",
"Bahh Tee",
"Bahriddin Zuhriddinov",
"Bahroma",
"BAI",
"Bai Bang",
"Baintermix",
"Bajofondo",
"Baka Not J",
"Bakaro",]

b_rus_list_3 = [
"Baker Boy feat. JessB",
"Baker Grace",
"Bakermat",
"Bakina",
"Baktuns feat. Nara D",
"Bakun",
"Balcony",
"Bald Bros",
"Balduin & Wolfgang Lohr feat. Andrea Carolina",
"Balearic Kings",
"Balewa",
"Bali Bandits",
"Balkan Avenue feat. Karym",
"Balkan Girls",
"Balma & Low Disco feat. Marina Scripilliti",
"Balma & Murilo March.",
"Balthazar",
"Baltimora",
"Balu & Бронс",
"Bananarama",
"Bancali",
"Band Aid 30",
"Band Odessa",
"Band Of Horses",
"BAND1T",
"Banda Black Rio",
"Bandana",
"Bande Dessinee",
"Bandee feat. Tonyjay",
"Bandito",
"Bando Jonez feat. Twista, B.o.B & T-Pain",
"Bandolero feat. Syntheticsax, DJ Flight, DJ Zhukovsky",
"Banev!",
"Bang Bang",
"Bang La Decks",
"Bangboyz",
"Banghook",
"Bangladesh",
"Bankomat & Mc Zali",
"Banks",
"BannanaFox & Sema Stealth feat. Kena",
"Banners",
"Banoffee feat. Empress Of",
"Bantu",
"Banx & Ranx",
"Banzay",
"Banzayo",
"Baptiste Giabiconi",
"Bar Matari & Tomer Aaron",
"Bar Rouge",
"Bara & Ayamat",
"Barak Yalad",
"Barakooda",
"Baran",
"Barbara Lynn",]

b_rus_list_4 = [
"Barbara Moleko",
"Barbara Opsomer",
"Barbara Streisand",
"Barbarellas",
"Barbra Streisand",
"BarBus feat. Breakkker & Валерия Демешко",
"Barcelona",
"Barcode",
"Barcode Brothers",
"Bardalimov",
"Bardo feat. Talia",
"Bare",
"Barei",
"Barei feat. Porta",
"Barely Alive",
"Baris Turna",
"Bariscan Demir",
"Barkley",
"Barlow Girl",
"BarlowGirl",
"BarlowLN",
"Barnes & Heatcliff",
"Barns Courtney",
"Barock Project",
"Barrax feat. Haley Joelle",
"Barrie Gledden",
"Barrington Lawrence & Aren B",
"Barrington Spence",
"Barry Harris & Dmitriy B.",
"Barry Manilow",
"Barry White",
"Bars And Melody",
"Bart B More",
"Bart Claessen",
"Barthezz",
"Bartoo feat. Shayd, Skee, Meowli",
"Basada",
"Basador",
"Basak Calik",
"Base Attack feat. LayZee",
"Base Elements",
"Base feat. Zambezi",
"Base Stylez",
"BaseFace & Saint Rider feat. Stevie B",
"Baselaut",
"Basement Crew",
"Basement Jaxx",
"Bashir Abdel Al",
"Bashment YC",
"Bashy feat. Jareth",]

b_rus_list_5 = [
"Basic Boy",
"Basic Element",
"Basic Tape",
"Basilica",
"Basilio Baio",
"Basim",
"Basis",
"Bask",
"Basker",
"Bass Ace",
"Bass deejay",
"Bass Expanders",
"Bass Farmers feat. Nathan Brumley",
"Bass Fun",
"Bass Inferno Inc.",
"Bass King",
"Bass Kleph",
"Bass Modulators",
"Bass Monta",
"Bass Turbat",
"Bass-T & Friends",
"Bassanova",
"Basshunter",
"Bassile",
"Bassjackersl",
"Bassline",
"Basslouder",
"Basslovers United",
"Bassment 4",
"Bassnectar",
"Basstype",
"Bastian Basic feat. Nijana",
"Bastian feat. Veronika",
"Bastian Harper vs. Kevin Iszard",
"Bastian K feat. Gustavo Trebie",
"Bastian Salbart",
"Bastian Smilla",
"Bastian Van Shield",
"Bastida feat. Dani Mata",
"Bastille",
"Basto",
"Basto!",
"Bat For Lashes",
"Baters (DoubleSense)",
"Batousai",
"Batrai",
"BatStab",
"Battata",
"Battle Beast",
"Batu Onat",]

b_rus_list_6 = [
"Batuhan Ates",
"Batya",
"Bauer & Lanford feat. Sara Josefsson",
"BAUM",
"Baxxter, Simon & DDY",
"Bay Area",
"Baya",
"Bayless",
"Bazalai",
"Bazhen Sysoev",
"Bazuka",
"Bazutin",
"Bazzflow feat. Jarah Damiel & LZRZ",
"Bazzi",
"BB Diamond",
"BBX",
"BC Unidos feat. Shungudzo",
"BCX",
"Be Charlotte",
"Be Free",
"Bea Miller",
"Beach Boys",
"Beach Club Band",
"Beach Guys",
"Beach House",
"Beach Monkey feat. Nila",
"Beachbag",
"Bean",
"Beanie Sigel feat. Akon",
"Beans & Fatback",
"Bear Grillz",
"Bear Hands",
"Bear McCreary feat. Serj Tankian",
"Bear S Den",
"Bearcubs",
"Bearson",
"Beastie Boys",
"Beat Faction feat. Dennis Wonder",
"Beat Kat",
"Beat Music",
"Beat Service",
"Beata Beatz feat. I Desideri",
"BeatauCue",
"Beatcore",
"Beatcreator",
"BeatGhosts",
"Beatgrooverz",
"BeatItPunk",
"Beatmaker",
"Beatone",]

b_rus_list_7 = [
"Beatrice Eli",
"Beatrich",
"Beats & Styles",
"Beats Inc.",
"Beats Sounds",
"BeatSmash",
"Beatsnbeauty",
"Beatsole & Kimberly Hale",
"Beatz",
"Beau Vallis feat. Kelly Rowland",
"Beautiful Bodies",
"Beautiful Lou",
"Beautiful People",
"Beauty And The Beast",
"Beauty Brain",
"Beauty In The Machine",
"BEAUZ",
"Bebe",
"Bebe Rexha",
"Beburi",
"Beca",
"Beck",
"Beckah Shae",
"Becky G",
"Becky Hill",
"Becquer",
"Bedlam",
"Bedtime Baby",
"Bee Gees",
"Bee's Knees feat. Marty Rod",
"Beenie Becker vs. AndreEA",
"Beenie Man",
"Beerg & Haal",
"Beethoven TBS & Florida feat. Joe Capalbo",
"Before You Exit",
"Bei Maejor",
"Beibit feat. Romano",
"Beissoul & Einius",
"Bekker",
"Beky feat. Danny C",
"Bel Suono & DJ Magic Finger",
"Bel-Agio feat. Vybrate",
"Belanova",
"Belarbi",
"Beldina",
"Belen",
"Beli feat. Баста",
"Belinda",
"Belindoza feat. CT & Rox",
"Beliy",]

b_rus_list_8 = [
"Belkal",
"Bella Hunter",
"Bella Santiago",
"Bella Thorne",
"Bella Vida",
"Bellagio feat. Jade Sommerville",
"Bellak",
"Bellani & Spada feat. Tasita D'mour",
"Bellatrax feat. Sophia May",
"Belle & Sebastian",
"Belle Amie",
"Belle Epoque",
"Belle Lucia",
"Belle Perez",
"Belleamy",
"Belleruche",
"Bellevue Cadillac",
"Bellezzo",
"Bellhouse",
"Bellini",
"Bellis",
"Bellorum",
"Bellusira",
"Belly",
"Belmond & Parker",
"Beltek",
"Belucca & Ramos",
"Beluga's Trio",
"Ben Arrows",
"Ben Cocks",
"Ben Delay",
"Ben DJ",
"Ben E. King",
"Ben Fisher, Kuzko",
"Ben Folds Five",
"Ben Gold",
"Ben Granfelt Band",
"Ben Grunnell",
"Ben Haenow",
"Ben Hammersley",
"Ben Harper",
"Ben Hartley",
"Ben Howard",
"Ben La Pompe, Pedro De Cabra",
"Ben Mitkus",
"Ben Montague",
"Ben Montgue",
"Ben Morris",
"Ben Muetsch",
"Ben Nichols",]

b_rus_list_9 = [
"Ben Nicky",
"Ben Phipps",
"Ben Platt",
"Ben Preston",
"Ben Rector",
"Ben Remember feat. Bex Jackson",
"Ben Rivers feat. Sandy Del",
"Ben Saber",
"Ben Stevenson",
"Ben Webster",
"Ben Wheeler",
"Ben'Do",
"Ben'yala",
"Benab",
"Benad",
"Benami",
"Benasis",
"Benassi Bros",
"Bender",
"Bendj feat Sushy",
"Bene",
"Benedict Cork",
"BENEE",
"Benefit",
"Benga feat. Marlene",
"Bengalsky feat. Нафиса Старкова",
"Bengels",
"Bengro feat. Priscila Due",
"Benj Heard",
"Benjamin Braxton",
"Benjamin Clementine",
"Benjamin Earl Turner",
"Benjamin feat. Sweet California",
"Benjamin Ingrosso",
"Benjamin Lasnier",
"Benjamin Led",
"Benjamin Leung & Jim Neild",
"Benjamin Rivalet",
"Benjamin Zane",
"Benji & Fede",
"Benji Lewis",
"Benni Cinkle",
"Bennson",
"Benny Bee",
"Benny Benassi",
"Benny Blanco",
"Benny Camaro",
"Benny Demus",
"Benny G vs. BBX",
"Benny La Malice",
"Benny Page",]

b_rus_list_10 = [
"Benny Royal feat. Mr. Eyez",
"Benrezheb",
"Bensley",
"Benson feat. KLP",
"Bentley Grey & LaKayte",
"Benya feat. Emma Lock",
"Benzi feat. Bhad Bhabie & Rich The Kid & 24Hrs",
"Benzino feat. Rick Ross",
"Beoga feat. Devin Dawson",
"Beowulf & Diskover",
"Beowulf & DOM",
"Beowulf & Dualmind feat. Vic Brow",
"Beowulf & Guz Zanotto feat. Zattera",
"Beowulf feat. Jotta",
"Beqa Zaqradze",
"Bera",
"Berat Oz",
"Berc Polat",
"Berenguer Adrian",
"Beret",
"Berezina",
"BergU",
"Berhana",
"Bering Strait",
"Berk & The Virtual Band",
"Berkay Sukur",
"Berkcan Demir",
"Berke Yurdakul",
"Berkhan Baser",
"Berksan",
"Berlin",
"Berlin Philharmonic Orchestra",
"Bermuda Twins",
"Bernabe De Moron",
"Bernard Allison",
"Bernard Herrmann",
"Bernasconi",
"Bernd Hall & Marco Zanfardino feat. Gosia",
"Berner",
"Bernward Koch",
"Bert And Vern",
"Bert H & High N Sick",
"Berto & The Border Boys",
"Bes & Meret",
"Besa feat. Mattyas",
"Besford",
"BesNine feat. Marguerite",
"Besomorph & Dekay",
"Bess",
"Bessiff",]

b_rus_list_11 = [
"Best & shaMan",
"Best Coast",
"Bestli",
"Beta Radio",
"Beth Ditto",
"Beth Garner",
"Beth Hart & Joe Bonamassa",
"Bethany Marcus",
"Bethany Mota feat. Mike Tompkins",
"Beto Cuevas",
"Betobahia",
"Beton",
"Betsie Larkin",
"Betta Lemme",
"Bette Midler",
"Better",
"Betty Blue",
"Betty Carter",
"Betty Everett",
"Betty Sinclaire",
"Betty Stroe",
"Betty Who",
"Betty Wright",
"Bettye LaVette",
"Beverly Pills",
"Beware Of Darkness",
"BEX",
"Bexey",
"Bexy",
"Beyonce",
"Beyond Today",
"Beyond Vibes ft. Raluca Nastase",
"Beyond Vision",
"Bezorbit",
"Bezos' Hawaiian Orchestra",
"BFF & Kane meets Miami Inc.",
"BFF Girls",
"BH feat. Progley",
"Bhad Bhabie",
"Bhangra Nights",
"Bhaskar",
"Bia",
"Bianca",
"BianK",
"Bias",
"Bibi Bourellya",
"Bietto feat. Adriana Vitale",
"Big Ali",
"Big Bang",
"Big Ben (Phats & Small) feat. Пьер Нарцисс",]

b_rus_list_12 = [
"Big Boi",
"Big Boss",
"Big Daddy Kinsey",
"Big Data",
"Big Diddy",
"Big Eli B",
"Big Fish & Anastacia",
"Big Freedia",
"Big Gigantic",
"Big Gipp",
"Big Hastler",
"Big House",
"Big Ilich",
"Big Iyz",
"Big Jack Johnson",
"Big Joe",
"Big K.R.I.T.",
"Big Marvel",
"Big Mountain",
"Big Old Sun﻿",
"Big Pineapple",
"Big Russian Boss feat. MOLLY",
"Big Sean",
"Big Sean feat. Rick Ross & Travis Scott",
"Big Som & Luina, HM",
"Big Stat",
"Big Time Operator",
"Big Time Rush",
"Big Wolf Band",
"Big Zero",
"BigBang",
"Bigflo & Oli",
"Biggie Mote feat. Maestro A-Sid",
"BIGkids",
"Bigstat",
"Bigtopo",
"Biicla",
"Biig Piig",
"Bijou",
"Bijue",
"Bikini Sounds",
"Bilal Africano feat. Jamoul",
"Bilal feat. Kendrick Lamar",
"Bilal Hassani",
"Bilal Shahid",
"Bill Douglas",
"Bill Evans",
"Bill Haley & His Comets",
"Bill Roundtree",
"Bill Wharton",]

b_rus_list_13 = [
"Bill Withers",
"Bill Wyman's",
"Rhythm Kings",
"Billi Insane feat. Павел Яшков",
"Billie Holiday",
"Billie Joe & Norah",
"Billie Marten",
"Billie Myers",
"Billon feat. Maxine Ashley",
"Bills & Hurr",
"Billy Boy Arnold",
"Billy Branch",
"Billy D & The Hoodoos",
"Billy Davis feat. Jordan Dennis & Kye",
"Billy Eckstine",
"Billy Esteban",
"Billy Gilman",
"Billy Hector",
"Billy Idol",
"Billy Joel",
"Billy Lee Riley",
"Billy Lockett",
"Billy May's Rico Mambo Orchest",
"Billy Milli",
"Billy Milligan",
"Billy Milligan (St1m)",
"Billy Ocean",
"Billy Paul",
"Billy Preston",
"Billy Price's & Fred Chapellier",
"Billy Raffoul",
"Billy Ray Cyrus",
"Billy Ronca",
"Billy Stewart",
"Billy Talent",
"Billy The Kit",
"Billy Wes feat. Tyga",
"Bily",
"Bim",
"Bimbo Jones feat. Ida Corr",
"Binary Finary & Dreamy feat. Natalie Gioia",
"Bing Crosby",
"Bingo Boys",
"Bingo Players",
"Bingo Staar & Lemon Turn",
"Bink",
"Biologik",
"Biometrix feat. Nath Hallet",
"Biondo",
"Biosystem 55",]

b_rus_list_14 = [
"Biplan",
"Bipolar Sunshine",
"Biray",
"Bird Dogs",
"Birdman & Juvenile feat. NLE Choppa",
"Birdman Ft. Tyga & Lil Wayne",
"Birdy",
"Birdy Nam Nam feat. Elliphant",
"Birgir",
"Birgit Oigemeel",
"Birgitta Haukdal",
"Birizdo I Am",
"BIS с.а.ю.з FlooW",
"BisBand",
"Bisbetic",
"Bishop Briggs",
"BISHU & Anjulie",
"BISHU feat. Sophie Rose",
"Biskvit & DimixeR",
"Bisquit",
"Bissen & Shannon Hurley",
"Bit Pythagoras",
"Bitch Hawk",
"Bite My A",
"Biting Elbows",
"Bitter Cupcakes feat. Miloud",
"Bitter Sweet feat. Paola Belletti",
"Bitz",
"Bix",
"Bizaro",
"Bizz Nizz",
"Bizzare",
"BJ The Chicago Kid",
"Bjonr feat. Tom Bailey",
"Bjork",
"Bjorn Akesson",
"Bjorn Winter",
"Bjornskov",
"BK Duke",
"Bks",
"Blacastan",
"Black & White Brothers",
"Black Angels",
"Black Atlass",
"Black Attack",
"Black Boots",
"Black Bros.",
"Black Caviar",
"Black Coast",
"Black Coffee",]

b_rus_list_15 = [
"Black Country Communion",
"Black Denim",
"Black Diamond",
"Black Eyed Peas",
"Black FOX",
"Black Gryph0n & Baasik",
"Black Heat",
"Black Jack",
"Black Label",
"Black Lego feat. AquaLiquid & Jay Weli",
"Black M",
"Black Market",
"Black Mesa feat. Nigorah",
"Black Mike",
"Black Mountain Prophet",
"Black Pata & Dam Dash",
"Black Philly",
"Black Rainbows",
"Black Rebel Motorcycle Club",
"Black Rose",
"Black Rozzze",
"Black Sabbath",
"Black Saint",
"Black Snow feat. Marisa & Mark Wild",
"Black Star Mafia",
"Black Swamp Water",
"Black Tide",
"Black Veil Brides",
"Black Velvet & Koit Toome",
"Black Vox Recorder",
"Blackbear",
"Blackfeel Wite",
"BlackFL (Sotanurh)",
"Blackfoot",
"BlackGummy",
"BLACKI",
"Blackis feat. Timos",
"Blackka feat. Wild",
"Blacklist",
"Blackmagic & Fetty Wap",
"Blackmill",
"Blackmore's Night",
"Blackout & Vitor Cruz",
"BlackPink",
"Blackstreet And Dr. Dre",
"BLAcKxxl",
"Bladi feat. Dr Mako",
"Blaikz",
"Blaise",
"Blak",]

b_rus_list_16 = [
"Blake Jarrell",
"Blake Lewis",
"Blake Rose",
"Blake Shelton",
"Blanc Dragons feat. Daisy Guttridge",
"Blanc Faces",
"Blanca",
"Blanche",
"Blanco Brown",
"Blando",
"BLANK",
"Blaq Tuxedo feat. Chris Brown",
"Blas Canto",
"Blasterjaxx",
"Blasterz",
"Blau Ton feat. Lara Loft",
"Blaxy Girls",
"Blaze Sulinski",
"Blazetools & Sick Days feat. Jonny Rose",
"Blazon",
"Bleach Baby",
"Bleachers",
"Bleeding Heart",
"Blend-It",
"Bleona",
"Blessed",
"Blewbird feat. Sleo",
"Blind Brew",
"Blind Channel",
"Blind Date",
"Blind Guardian",
"Blind Pilot",
"Blind Tyler",
"Blindcat & Mamacat",
"Blinddog Smokin'",
"Blinded Hearts feat. Louise CS",
"Blinders",
"Blindstone",
"Blink-182",
"Blinkie",
"Bliss",
"Blithe",
"Blizzard",
"BLKMGK feat. Otis Parker",
"Bloc Party",
"BlocBoy JB",
"Block",
"Blonde",
"Blonde feat. Karen Harding",
"Blondee",]

b_rus_list_17 = [
"Blondfire",
"Blondie",
"Blondie Beat",
"Blondin",
"Blondrock (Катя Гордон)",
"Blonker",
"Blood Dance Project",
"Blood God",
"Blood On The Dance Floor feat. Deuce",
"Blood Orange",
"Blood, Sweat & Tears",
"Bloodboy",
"Bloodhound Gang",
"Bloodstone",
"Bloodthinnerz & Axel Boy",
"Bloom 06",
"Bloom Twins",
"Bloqshot",
"Blosh feat. Siri Nilsen",
"Blossoms",
"Blow feat. Alexia",
"BLR",
"Blu DeTiger",
"BLU J feat. New Haven",
"Blu Lyon feat. Lady Ali",
"Blu Mar",
"Blu3cat feat. Talina Rae",
"Bluckther",
"Blud Red Roses",
"Blue & Elton John",
"Blue Ace",
"Blue Affair and Sasha Dith",
"Blue Americans",
"Blue Cafe",
"Blue Feat. Elton John",
"Blue Foundation",
"Blue Heaven",
"Blue Ivy",
"Blue Jay",
"Blue Metheny",
"Blue Mink",
"Blue October",
"Blue On Blonde",
"Blue Oyster Cult",
"Blue Sector",
"Blue Stahli",
"Blue Star Project",
"Blue Stone",
"Blue System",
"Blue Tente feat. Stine Grove",]

b_rus_list_18 = [
"Blue The Misfit feat. Kendrick Lamar",
"Blue Zone feat. DJ Yulis",
"Blue5even",
"Bluecrack",
"Blues Company",
"Blues Cousins",
"Blues Merchants",
"Blues Mobile Band",
"Blues Saraceno",
"Bluesille",
"Bluespam",
"Blueville",
"Bluezzcontrol",
"Blufeld",
"Bluford Duck",
"BlumBros & MAKJ",
"Blur",
"Blush",
"Bluskay & Chloe Ama",
"Blusoul",
"Blut Own & Blure",
"Blutpumpe ft. The Iron Shirt",
"BLV feat. Jim Bauer",
"Blxckowl",
"Bmark",
"BMT",
"BO & Serhat Durmus feat. Ecem Telli",
"Bo Diddley",
"Bo Le Roy feat. Klaudya",
"Bo Ramsey",
"Bo Rocha",
"BOA",
"Boatpeople DJs feat. Mosean",
"Boaz Mauda",
"Boaz Van De Beatz",
"Bob Bradley & Tim Garland",
"Bob Chance",
"Bob Dylan",
"Bob Garcia",
"Bob Hanson",
"Bob James",
"Bob Jop & Mr.Racha",
"Bob Marley",
"Bob Moses",
"Bob Rovsky feat. Anya Shesternina",
"Bob Seger",
"Bob Sinclair",
"Bob Sinclar",
"Bob Taylor",
"Boba K",]

b_rus_list_19 = [
"Boba Prime feat. Олег Кензов, TimBigFamily",
"Bobak & Eximinds",
"Bobbie Gentry",
"Bobble Head",
"Bobby Blue Bland",
"Bobby Boris Pickett",
"Bobby Brackins",
"Bobby Burns feat. Hannah Robinson",
"Bobby Caldwell",
"Bobby Darin",
"Bobby Deep",
"Bobby Escobar",
"Bobby Flurie",
"Bobby Fuller Four",
"Bobby Green feat. Whitney Phillips",
"Bobby Hebb",
"Bobby Helms",
"Bobby Love",
"Bobby Lyle",
"Bobby Mcferrin",
"Bobby Messano",
"Bobby Moore feat. Keo",
"Bobby Neon feat. Jonny Rose",
"Bobby Nourmand feat. DOC & Goodmorning",
"Bobby O",
"Bobby Puma",
"Bobby Rock",
"Bobby Sanabria",
"Bobby Snake & Marvio",
"Bobby Tamiri",
"Bobby V",
"Bobby Vinton",
"Bobby Womack",
"Bobina",
"BOCHA",
"Bodak feat. Ava",
"Bode feat. Natalie Wood",
"Bode feat. Tailor",
"Bodin",
"Bodr9k feat. Кристина Сарамуд & DiLes",
"Body & Soul",
"Body Heat",
"Body Logic",
"Body M",
"Body Parts",
"Body Power",
"Body&Soul",
"Bodya",
"Bodya (MMDance)",
"Bodybangers",]

b_rus_list_20 = [
"Bodybangers Inc.",
"Bodyfunkers",
"Bodyrox feat. Chipmunk & Luciana",
"Bodyshakers",
"Boehm",
"Boeoes Kaelstigen feat. Asha Ali",
"Bogdan Ioan",
"Bogdan Vix",
"Bogdan Vladau",
"Bogdanl",
"Boggie",
"Bohemians",
"Bohemic, Lukas",
"BOHO & Maksim Dark",
"Boi",
"Boier Bibescu",
"Bojana Stamenov",
"Bojena",
"Bok Nero feat. Jahlil Beats",
"Boks 99",
"Bold Action",
"Bolier & Diskover",
"Bolier & Joe Stone",
"Bolier & Lvndscape",
"Bolier & Natalie Peris",
"Bolier & Trobi",
"Bolier feat. NBLM",
"Bolier feat. Tiggi Hawke",
"Bolin",
"Bolla",
"Bolshevseh",
"Bom Dia",
"Bomb 'N Amato",
"Bomb The Base",
"Bomba Estereo & Will Smith",
"Bombalurina feat. Timmy Mallett",
"Bomberjak feat. Jessica Jolia",
"Bombs Away",
"Bomfunk Mc's",
"Bomfunk Mcs",
"Bon Iver",
"Bon Jovi",
"Bonah",
"Bonaparti. LV",
"Bondax",
"Bone N Skin",
"Bone Thugs-N-Harmony",
"Boney James",
"Boney M",
"Bonka feat. Bianca",
"Bonka feat. Kris Kiss",
"Bonkers",
"Bonnie Anderson",]

b_rus_list_21 = [
"Bonnie McKee",
"Bonnie Tyler",
"Bonnie X Clyde",
"Bonobo",
"Bonsai",
"Bonsai Mammal",
"Bonzai",
"Bonzana",
"Boo Seeka",
"Boobie",
"Booby Gibson feat. Elijah Blake",
"Boogie Bitches",
"Boogie Boys",
"Boogie feat. Eminem",
"Boogrov feat. Aluna",
"Booka Shade",
"Booker T and Th Mg's",
"Booker T. & The Mg's",
"Bookworms",
"Boom Bap Project",
"Boom Boom Cash",
"Boom Jinx & Aruna",
"Boom Jinx feat. Justine Suissa",
"Boom Jinx feat. Meredith Call",
"Boombox Cartel",
"Boomdabash",
"Boosie Badazz",
"Boostedkids",
"Boostee",
"Boostereo",
"Boot Camp Clik",
"Boot Cut Rockers",
"Bootik feat. Christina Skaar",
"Bootik feat. Max C",
"BOOTS feat. Beyonce",
"Bootsy Collins Feat. Mc Lyte",
"Booty Luv",
"Bop feat. Elsa Esmeralda",
"Border Crossing",
"Bordertown",
"Borgeous",
"Borgia & Arizona Zervas",
"Borgore",
"Bori",
"Boris (НПМ) feat. Ангелина Рай & Птаха",
"Boris Brejcha",
"Boris Novkovic",
"Boris Rene",
"Boris Roodbwoy, Andrew Rai Feat. Gosha",
"Boris Smith feat. Hero Baldwin",]

b_rus_list_22 = [
"Boris Way",
"Boris Zhivago",
"Borivan (VB) feat. Саша Opium",
"Borja Jimenez",
"Borja Rubio & Juan Magan",
"Bormin' feat. Chelsea Perkins",
"Born Dirty",
"Borns",
"Bossfight",
"Bossicom & Kena",
"Bosson",
"Bosstronic",
"Bossy Love",
"Bostan & TaYa",
"Boston",
"Boston Building feat. Lago",
"Boston Bun",
"Boston feat. Solis",
"Boston George feat. Rick Ross, Slim Thug & Rich Andruws",
"Botanic Project",
"Both Face",
"Botnek & I See Monstas",
"Botnek feat. Go Comet!",
"Botoxx & Tom Belmond",
"Bottai",
"Bouchra",
"Bougenvilla",
"BOULEV4RD",
"Boulevard Des Airs",
"Bounce Bro",
"Bounce Inc.",
"Bounty Killer",
"Bout",
"BoValigura & Алекс Индиго",
"Bow Wow",
"Bow Wow Wow",
"Bowie & Ellusive feat. Hype Turner",
"Boxie",
"Boy Blue",
"Boy Epic",
"Boy Flow",
"Boy Funktastic",
"Boy George",
"Boy Has No Name",
"Boy In Space",
"Boy Kid Cloud & Dack Janiels",
"Boy Kiss Girl",
"Boyboyboy & Remady",
"Boyce Avenue",
"Boye & Sigvardt",]

b_rus_list_23 = [
"Boyhitscar",
"BoyPanda & Jurgaz",
"Boys Like Girls",
"Boys Next Door",
"Boys Noize",
"Boytronic",
"Boyz Ii Men",
"Boyzone",
"Boz Scaggs",
"Bozack Morris",
"Bpm Projects & CornEL",
"Br3nz feat. Isthatkee",
"Bra Zil",
"Braak",
"Braaten & Chrit Leaf",
"Bracelet",
"Brad & Victor H with MAR!NO feat. Chloe Farrell",
"Brad Blondino",
"Brad Lake",
"Brad Paisley",
"Bradley's H",
"Bragaa",
"Braids",
"Brain",
"Brain Damage",
"Brain Masters",
"BrainDeaD feat. MC Fish",
"BrainNebula",
"Brainpain",
"Brains",
"BrainStorm",
"Brainstorm & Марина Кравец",
"Bram Fidder feat. AxR",
"Branan Murphy",
"Brand Image",
"Brand X Music",
"Brandi Carlile feat. Sam Smith",
"Brando",
"Brandon Beal",
"Brandon Flowers",
"Brandon Heath",
"Brandon Ramirez",
"Brandon Skeie",
"Brandon Steel",
"Brandon Stone",
"Brandy",
"Brandyn Burnette",
"BranOnTheTrack feat. Kevin McCall & Sonu",
"Brantley Gilbert & Lindsay Ell",
"Brasco feat. Pusha T & Timbaland",]

b_rus_list_24 = [
"Braska",
"Brasko feat. Сенс",
"Brass",
"Brass Knuckles feat. John Ryan",
"Braulio Stefield",
"Brave Future",
"Bravenus",
"Bravo & Willemijn May",
"Bravour",
"Bravve",
"Braxton feat. Ava James",
"Braxx vs. Hagen",
"Brayton Bowman",
"Brazil Headliner",
"Brazyleros",
"Brazzaville",
"Breach",
"Bread",
"Break feat. Singing Fats",
"Break My Fucking Sky",
"Break Science",
"Breakage",
"Breakdlaw feat. The Glitchfox",
"Breakdown Of Sanity",
"Breakfast Trim",
"Breaking Bed feat. DJ Noiz",
"Breaking Benjamin",
"Bream & Blinders",
"Bream & Ron Carroll",
"Bream Blinders",
"Breathe Carolina",
"Breathe Electric",
"Breathe Me In",
"Bree Runway",
"Breed 77",
"Breeze ft. Lost Witness",
"Breezer feat. Ivy J",
"Breezey Montana feat. Yanix",
"Brenda K. Starr",
"Brenda Lee",
"Brendan Asquith",
"Brendan Murray",
"Brendan Perry",
"Brendan Waters",
"Brennan Heart",
"Brennan Villines",
"Breno & SNYC feat. Lucie M",
"Breno Miranda & Gesualdi",
"Brent Rix",
"Brett Bixby",]

b_rus_list_25 = [
"Brett Ellis Band",
"Brett Gould",
"Bri Tolani & Triste Noir",
"Bria Blessing",
"Bria Lee feat. Fat Joe",
"Brian Brainstorm",
"Brian Crain",
"Brian Fallon",
"Brian Ferry",
"Brian Hyland",
"Brian Ice ft. R.B. Project",
"Brian Kennedy",
"Brian May",
"Brian McFadden",
"Brian Mcknight",
"Brian Mich feat. Alla",
"Brian Setzer Orchestra",
"Brian Smith",
"Brian Van Andel feat. Lewis Beards",
"Brianna",
"Brice Conrad",
"Brice Davoli & Delphine Joutard",
"Brick & Lace",
"Brick Bazuka",
"Brick Top & Brother Bliss",
"BRIDGE",
"Bridge & Veronica",
"Bridge feat. Tonez",
"Bridge feat. Tonez & Wiz Khalifa, Snoop Dogg",
"Bridger",
"Bridget Kelly Band",
"Bridgit Mendler",
"Brie",
"Brielle Von Hugel & Galavant",
"Brieuc & Gregor Potter",
"Brieuc & Gregor Potter feat. Maline",
"Briga feat. Jas & Jay",
"Brighi",
"Bright Lights",
"Brigitte Fontaine feat. Grace Jones",
"Brika",
"Brinck",
"Bring Me The Horizon",
"Brisa Fenoy",
"Brisby & Jingles",
"Brisco feat. Flo Rida & Whyl Chyl",
"Brisco feat. Rico Love",
"Brisk feat. Donna Lugassy",
"Brit Smith feat. Will.i.Am",
"Britney Spears",]

b_rus_list_26 = [
"Britt Nicole",
"Brittany Bridges",
"BRKLN feat. Mariah McManus",
"Brklyn",
"BRLIN feat. Daniela Serey",
"Brmgloth",
"Brny feat. TonyJay",
"Bro Code",
"Bro Safari",
"Broadcast",
"Broadway feat. Fuze (Krec)",
"Broadway Project",
"Brockhampton",
"Brockman & Basti M",
"Brohug",
"Broiler",
"Broke One",
"Broken Back",
"Broken Bells",
"Broken Oath",
"Broken Secret",
"Bronza",
"Broods",
"Brook",
"Brook Benton",
"Brooke Candy",
"Brooke Fraser",
"Brooke Hogan",
"Brooke Valentine",
"Brooke Williams",
"Brooker",
"Brookes Brothers",
"Brooklyn Bounce",
"Brookroyal",
"Brooks & GRX",
"Brooks & Jonas Aden",
"Bros Project",
"Bross & Laurer feat. Tasha Losan",
"Brother Culture",
"Brother Dege",
"Brother Leo",
"Brother Samuel Cheatam",
"Brother Yusef",
"Brothers Dreamers",
"Brothers feat. Ranieri",
"Brothers In Crime",
"Brothers Johnson",
"Brothers On The 4th Floor",
"Brotherwave feat. Dayron Ferguson",
"Brown Sneakers & Dave Manna feat. Lissa",]

b_rus_list_27 = [
"Brs feat. KAF",
"Brs feat. Эрика Лундмоен",
"Bruce & Bongo",
"Bruce Dickinson",
"Bruce Springsteen",
"Bruce Willis",
"Bruna feat. Marseli & Dafi",
"Bruna Repetto",
"Brunelle",
"Brunettes Shoot Blondes",
"Brunkow feat. Violeta White",
"Bruno",
"Bruno & Aida",
"Bruno Alexander",
"Bruno Barudi",
"Bruno Costa",
"Bruno Kauffman & Pakem feat. Anna Buckley",
"Bruno Lorenzoni",
"Bruno Mars",
"Bruno Martini",
"Bruno Motta & Guzwoo feat. Nathan Brumley",
"Bruno Verdugo",
"Bruno и Лилиана Гергель",
"Brunsky (Михаил Брунский)",
"Brutha feat. R.Kelly",
"Brutto",
"Bryan",
"Bryan Adams",
"Bryan Amadeus feat. Anahi & Ale Sergi",
"Bryan Bax feat. Vanessa Green",
"Bryan Clara",
"Bryan Dalton & Undercontrol",
"Bryan Ellis",
"Bryan feat. Matias Endoor & Tyna Cat",
"Bryan Ferry",
"Bryan J",
"Bryan Kearney",
"Bryan Lee",
"Bryan Milton",
"Bryan Rice",
"Bryan Sanders",
"Bryangin",
"Bryce",
"Bryce Fox",
"Bryce Vine",
"Bryce vs. Gerald G!",
"Bryn feat. Dreezy",
"Bryn Liedl Feat. Bethany Marie",
"Brynn Elliott",
"Brytiago & Lary Over feat. De La Ghetto",]

b_rus_list_28 = [
"Bsharry",
"BSTRD (Tony-Gun & Ваня Протест)",
"BT & Aqualung",
"BT & JES, Fractal",
"BT & Matt Fax",
"BT & Senadee feat. Dragon & Jontron",
"BT & Stefan Dabruck",
"BT & TyDi feat. Tania Zygar",
"BT feat. Christian Burns",
"BT feat. Dragon, Jontron & Senadee",
"BT feat. Fractal & Bada",
"BT feat. Jes & Fractal",
"BT feat. Tritonal & Emma Hewitt",
"BT feat. TyDi & JES",
"BT feat. TyDi & Tania Zygar",
"BT, Stefan Dabruck & Christian Burns",
"BTS",
"Bu Bu Man",
"Bubble Gum",
"Bubble Guns",
"Bubnar",
"Buchecha feat. Flo Rida",
"Bucket Street feat. Nieggman",
"Budapest Aires",
"Buddah Heads",
"Buddha",
"Buddy feat. Miley Cyrus",
"Buddy Guy",
"Buddy Holly",
"Buddygirrl feat. Chris James",
"Buedi Siebert",
"Buena Vista Dance Club feat. Lumidee",
"Bueno Clinic",
"Buenos Aires Social Club",
"Bufalo",
"Buffalo Springfield",
"Buga",
"Bugatti Music",
"Bugly feat. MainstreaM One",
"Bugra Atmaca & Mad Flynn",
"Bugra Atmaca feat. Vedat Unal",
"Bugs Henderson",
"Bugzy Malone feat. Rag'n'Bone Man",
"Built By Titan feat. Starxs",
"Buke Badnews",
"Buket Bengisu & Group Safir",
"Bukez Finezt",
"Bukowski",
"Buku",
"Bulava",]

b_rus_list_29 = [
"Bulgakov & Snebastar",
"Bullet For My Valentine",
"Bulletgrims",
"Bullmeister",
"Bulls & Goat",
"Bulow",
"Bumaje",
"Bumble Beezy",
"Bunny feat. Max Landry",
"Bunny Tunes feat. Tiana",
"BUNT.",
"Burak Ayaz feat. Ozlem Ancak",
"Burak Balkan",
"Burak Cilt",
"Burak Gurel",
"Burak Yeter",
"Burani & Busilacchi feat. Stefano Afriyie",
"Buranov",
"Burgundy's & Andrea S feat. Wes Walls",
"Burhan G",
"Burial",
"Burito",
"Burna Boy",
"Burns",
"Burnt Out Wreck",
"Burzhuy & Ivan Demsoff Ft. Ira Champion",
"Burzhuy feat. Tiara",
"Busby Marou",
"Bushi",
"Bust-R & Sharif D",]

b_rus_list_30 = [
"Busta K feat. Joe Cleere",
"Busta Rhymes",
"Bustamante",
"Busted",
"Buster Moe",
"Bustre feat. LaMeduza",
"Busy P",
"Busy Signal & RC",
"Butch",
"Buteratte",
"Butrint Imeri",
"Butterfly",
"Buy One Get One Free & DJ Lutique",
"Buyas & Pelka",
"BVDAR feat. NAYA & Саша Пайро",
"Bvdc feat. Lumidee",
"Bvsic",
"BWAXX & Anna De Ferran",
"BWF feat. Alex Mica",
"Bwo",
"byCity",
"ByeAlex",
"Bynon & Bishop",
"BYNON & Domeno feat. Alice Berg",
"Bynon & Rumors",
"Bynon feat. Taryn Manning",
"Bynon, Feenixpawl & Project 46 feat. Melissa",
"BYOR",
"Bypass Bandits feat. Lars Sparby",
"Byron Keno feat. Fiesta Black",
"Byron Keno vs. Denim feat. Fiesta Black",
"Byz Feat. Airgo",
"Bэtman & Mc Check",
]


litera = SoundSymbol.objects.get(name="B")

count = 0

for tag in b_rus_list_1:
    tracks = client.get('/tracks', q=tag, limit=page_size, linked_partitioning=1)
    if tracks:
        for track in tracks.collection:
            created_at = track.created_at
            created_at = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
            if track.description:
                description = track.description[:500]
            else:
                description=None
            try:
                SoundcloudParsing.objects.get(id=track.id)
            except:
                if track.genre and track.release_year and track.duration > 90000 and track.genre in genres_list_names:
                    try:
                        self_tag = SoundTags.objects.get(name=tag, symbol=litera)
                    except:
                        self_tag = SoundTags.objects.create(name=tag, symbol=litera)
                    genre =SoundGenres.objects.get(name=track.genre.replace("'", '') )
                    new_track = SoundcloudParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, description=description, created_at=created_at, duration=track.duration, genre=genre, title=track.title, uri=track.uri, release_year=track.release_year)
                count = count + 1
        while tracks.next_href != None and count < 2000:
            tracks = client.get(tracks.next_href, limit=page_size, linked_partitioning=1)
            for track in tracks.collection:
                created_at = track.created_at
                created_at = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
                if track.description:
                    description = track.description[:500]
                else:
                    description=None
                try:
                    SoundcloudParsing.objects.get(id=track.id)
                except:
                    if track.genre and track.release_year and track.duration > 90000 and track.genre in genres_list_names:
                        try:
                            self_tag = SoundTags.objects.get(name=tag, symbol=litera)
                        except:
                            self_tag = SoundTags.objects.create(name=tag, symbol=litera)
                        genre =SoundGenres.objects.get(name=track.genre.replace("'", '') )
                        new_track = SoundcloudParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, description=description, created_at=created_at, duration=track.duration, genre=genre, title=track.title, uri=track.uri, release_year=track.release_year)
                    count = count + 1
