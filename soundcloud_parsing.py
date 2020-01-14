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

a_angl_list_1 = [
'A & P Project feat. Zemya Hamilton',
'A & Z',
'A Boogie Wit Da Hoodie',
'A Broken Silence',
'A Class feat. Valeria Sibaja & Baby Tony',
'A Day To Remember',
'A Fine Frenzy',
'A Friend In London',
'A Great Big World',
'A Kay BJ',
'A LEX',
'A Lightning',
'A Lisa',
'A Paul',
'A Perfect Circle',
'A R I Z O N A',
'A Silent Film',
'A Skylit Drive',
'A-Europa',
'A-Ha',
'A-Lee feat. Eric Saade',
'A-Lina',
'A-Mase',
'A-Minor',
'A-Peace feat. Drea Delacruz',
'A-Rockz',
'A-Sen',
'A-teens',
'A-Side',
'A-VIA',
'Aaron Keylock',
'Aaron Lead',
'Aaron May',
'Aaron McClelland',
'Aaron Michael Cox',
'Aaron Neville',
'A.Boldar',
'A.C.K. & Oliver Meadow',
'A.L.T.O.',
'A.M. SNiPER',
'A.M.L.',
'A.M.T feat. Julian C',
'A.N.T.O.N.',
'A.Shine',
'A.U.D.I.E.N.C.E.',
'A"Las Lito',
'A+',
'A$AP Rocky',
'A1',
'A5',]

a_angl_list_2 = [
'Bondy',
'Aadagio',
'AaLai',
'Aali',
'Aamin',
'Aandra',
'Aaliyah',
'Aaricia',
'Aaron Camz',
'Aaron Carpenter',
'Aaron Carter',
'Aaron Fresh',
'Aaron Keylock',
'Aaron Lead',
'Aaron May',
'Aaron McClelland',
'Aaron Michael Cox',
'Aaron Neville',
'Aaron North feat. Alessa',
'Aaron Smith',
'Aaron Snapes',
'Aarophat',
'Aarre',
'Ab-Soul feat. Aloe Blacc',
'Abandoned Rainbow',
'Abaz & Артём Татищевский',
'ABBA',
'Abbi',
'Abbie',
'Abbsynth',
'Abby',
'abdr.',
'Abel Almena',
'Abel Ramos',
'Abel Romez',
'Abendrot',
'Abeyance',
'Abi',
'Abigail',
'Abir',
'Abisha',
'Above & Beyond',
'Abraham Laboriel',
'Abraham Mateo',
'Abrax Phaeton',
'Abrina feat. Baby Bash',
'Abrina feat. Eric Bellinger',
'Abrina feat. Jeremih',
'Abror Filar',
'Absolute Dancefloor',]

a_angl_list_3 = [
'Absolute feat. Mozhdah',
'Absound feat. BianK',
'Abune Dharay',
'Aburden',
'Aby Jackley feat. Sheera Soul',
'Abyss',
'Ac Slater',
'AC/DC',
'Academia',
'Accept',
'Access',
'Accet',
'Accordi Disaccordi',
'Ace Aura',
'Ace Cape',
'Ace Hood',
'Ace Miller',
'Ace Of Base',
'Ace Wilder',
'Acedias',
'Acento Latino',
'Achtabahn',
'Acid Mondays',
'Acidfonk',
'Acoran',
'Acoustic Alchemy',
'Acracia',
'ACTION',
'Activ',
'Activa & Lostly',
'Activa feat. Cat Martin',
'Activate',
'Ad Brown',
'Ada',
'Ada Reina',
'Ada Richards',
'ADAM,'
'Adam Daniel',
'Adam Easter',
'Adam Ellis',
'Adam Foster',
'Adam French',
'Adam Lambert',
'Adam Levine',
'Adam Navel',
'Adam Nova',
'Adam Rafferty',
'Adam Rickitt',
'Adam Rom',
'Adam Seal',]

a_angl_list_4 = [
'Adam Sick',
'Adam Szabo',
'Adam Tyler',
'Adam Walker',
'Adamant',
'Adamlar',
'Adams Bryan',
'Adaptiv & Mingue',
'Adda',
'Addal',
'Addiction',
'Addictive Elements',
'Adee',
'Adel',
'Adele',
'Adele Erichsen',
'Adelen',
'Adeli',
'Adeli Ray',
'Adelina',
'Adelitas Way',
'Adelly',
'Adelphia',
'Adem & Murat',
'Adena',
'Adept',
'Adeve',
'Adi Barar Band',
'Adia',
'Adiam',
'Adict',
'Adiemus',
'Adil',
'Adina Howard',
'Adip Kiyoi',
'Admiral Grey',
'Adnane Touzani',
'Adoette',
'Adolphe Deprince',
'Adon',
'Adonis',
'Adonx',
'Adora',
'Adrees',
'Adrenaline Mob',
'Adress 27',
'Adria Ortega',
'Adrian Eftimie',
'Adrian Lulgjuraj & Bledar Sejko',
'Adrian Lux',]

a_angl_list_5 = [
'Adrian Melbrand',
'Adrian Mesu feat. Diana Francesco',
'Adrian Milena',
'Adrian Niles Band',
'Adrian Oblanca',
'Adrian Rooz',
'Adrian Sina',
'Adrian Zenith',
'Adriana',
'Adriana Mezzadri',
'Adriana Rusu',
'Adrianna Marie',
'Adrianne',
'Adriano Celentano',
'Adrienne Bailon',
'Adriiana',
'Adriiana feat. iSH',
'Adrijana',
'Adrima',
'Adryano',
'Adult Karate feat. Adaline',
'AduShinova',
'ADVANCE',
'Adventure Club',
'Ady Jara',
'Ady Suleiman',
'Aedanz',
'Aedee',
'AELYN',
'Aeora',
'Aeph',
'Aeris',
'Aero',
'Aerofoil',
'Aeron Komila',
'Aeroplane',
'Aeroplane Mode',
'Aerosmith',
'Aerosoul',
'Aevion',
'Affiance',
'Affinis',
'Afflection',
'Afrochuck',
'Afrojack',
'AFSHeeN',
'Afshin Amini & Ali Aminian',
'After School',
'Afterlife',
'Afternova',]

a_angl_list_6 = [
'Agamemnon Project',
'Agamma',
'AGAYA',
'Age Of Days',
'Age Pee',
'Agebeat & KFT',
'Agent Juno',
'Agent Stereo',
'Ages Apart',
'Aggro Santos',
'Agitti',
'Agnes',
'Agnete Johnsen',
'Agomel',
'Agoney',
'Agoria',
'Agressor Bunx',
'Agronom feat. Helena-Shadia',
'Agua Roja',
'Ahimas',
'Ahmad Jamal',
'Ahmad Saeedi',
'Ahmed Chawki',
'Ahmed Helmy',
'Ahmed Shad',
'AhmedShad',
'Ahmet Kilic',
'Ahmir',
'Ahren System',
'Ahtam',
'Ahzee',
'Ai Mori',
'Ai Ome',
'AIDA',
'Aidan Black',
'Aiden',
'Aiden Grimshaw',
'Aiden Rey',
'Aidino',
'Aika',
'Aimable',
'Aiman Beretta',
'Aimee',
'Aimi',
'Aimless',
'Aimoon',
'Aina Maro',
'Aine Aura',
'Ainhoa',
'Aint',
'Air Bag One',]

a_angl_list_7 = [
'Air Station',
'Air Traffic Controller',
'Airbase',
'Airbeat One Project',
'Airborne Cities',
'Airbourne',
'Airdream',
'Airdroрs',
'AirLab7',
'Airling',
'Airplace',
'Airports',
'Airstream',
'Airub',
'Airwolf',
'Aisa',
'Aisel',
'Aisen',
'Aisha',
'Aisha Vyskubova',
'Aislin Evans',
'Aivaras',
'Aivarask',
'Aiwake',
'Aiyana',
'Aize',
'AJ Mitchell',
'AJ Tracey',
'Ajeet Kaur',
'Ajow',
'AJR',
'Ajow',
'AJR',
'AKA George',
'Akapella',
'Akay',
'AKBA',
'Akcent',
'Akces',
'AkeLLa',
'Akentaly',
'Aki',
'Akim',
'Akimtsov',
'Akira Yamaoka',
'Akon',
'Akord',
'Akris & Teddy',
'Akritis',
'AkroSonix',]

a_angl_list_8 = [
'Aksioma Project',
'AkTi & Al’Ba',
'Aktive',
'Akustikrausch',
'Akustix',
'AKVA',
'Al Bairre',
'Al Barry',
'Al Bizzare',
'Al feat. Tasha',
'Al Jarreau',
'Al Joseph',
'Al Stewart',
'Alaa Wardi',
'Aladdino',
'Alagui',
'Alai Oli',
'Alampa',
'Alan Brando',
'Alan Jackson',
'Alan Maciel',
'Alan Morris',
'Alan Parsons',
'Alan Peter',
'Alan Pinheiro',
'Alan Price',
'Alan Roy',
'Alan Silvestri',
'Alan Smith',
'Alan Walker',
'Alan White',
'Alana',
'Alana Lee',
'Alania',
'Alanis Morissette',
'AL-B',
'Alanna Clarke',
'Alannah Myles',
'Alar & Zamffo',
'Alari & Vane',
'ALas Lito',
'Alaska Thunderfuck',
'Alawn & Dyson',
'Alawn & Liam Ferrari',
'Alaya',
'Alayna',
'Alb',
'Alb Negru',
'Alba Soler',
'Alba Wings',]

a_angl_list_9 = [
'Albannach',
'Albert Brite',
'Albert Castiglia',
'Albert Collins',
'Albert Cummings',
'Albert Glimma',
'Albert Keyn',
'Albert Kick',
'Albert One',
'Albert Marzinotto',
'Albert St. Barth',
'Alberto Asso',
'Alberto Bandiera',
'Alberto Ciccarini feat. Beatrich',
'Alberto Feria, Alvaro Mnml',
'Alberto Giurioli',
'Alberto Remondini & Alberto Vega',
'Alberto Ruiz',
'Alberto Simone',
'Albin & Mattias Andreasson',
'Albin Lee Meldau',
'Albin Myers',
'Albin Myers and John Dahlback',
'Albina Mango & Bass Ace',
'Albina Mango & Tim Gorgeous',
'Alborosie',
'Alca & Zar',
'Alcazar',
'Alchemist',
'Alchemist Project',
'Aldair Silva feat. Buju',
'Aldaria',
'Aldo Henrycho, Thea Riley',
'Aldo Lesina',
'Aldridge x Katerina Letto',
'Ale Blake feat. Hevito',
'Alec Benjamin',
'ALEDON & Nahide Babasli',
'Alee',
'Aleena',
'Aleesha',
'Aleesia',
'Aleesia feat. Big Sean',
'Alejandro De Pinedo',
'Alejandro Diego feat. Duncan',
'Alejandro Fernandez & Morat',
'Alejandro Gonzalez & Yera',
'Alejandro Laska',
'Alejandro Montero',
'Alek Sandar',]

a_angl_list_10 = [
'Alek Sandar, Dess & Boyplay',
'Alek Trance',
'Aleks Ache',
'Aleksi P',
'Alemond',
'Alen Hit',
'Alen Hits Band',
'Alen Wizz',
'Alena Grand',
'Alena Grigorevskaya',
'Alena Pak',
'Alena Roxis',
'Alena Tverskaya',
'Alenka Gotar',
'Alenna feat. T-RoMaN',
'AlenTJ',
'Alesha',
'Alesha Dixon',
'Alesia',
'Alessandro Cocco',
'Alessandro Martire',
'Alessia',
'Alessia Cara',
'Alessia Voice',
'Alessiee',
'Alesta',
'Aletov',
'Alex Aark',
'Alex Adair',
'Alex Aiono',
'Alex Alexander',
'Alex Alta',
'Alex Aris',
'Alex Bah',
'Alex Balog feat. Edward McEvenue',
'Alex Band',
'Alex Barattini',
'Alex Belak',
'Alex Blue',
'Alex Byrka',
'Alex C',
'Alex Cery',
'Alex Chroma Band',
'Alex Clare',
'Alex D"Elia & Nihil Young feat. Gosha',
'Alex D"Rosso',
'Alex Dars',
'Alex Dobson',
'Alex Ferrari',
'Alex G',]

a_angl_list_11 = [
'Alex Gaudino',
'Alex Gaudino, Bottai',
'Alex Geralead',
'Alex Good & Kolya Funk',
'Alex Goot',
'Alex Great',
'Alex Guesta',
'Alex Henley',
'Alex Hepburn',
'Alex Hide',
'Alex Hill',
'Alex Hook',
'Alex Hosking',
'Alex Hough',
'Alex House',
'Alex Hurst',
'Alex Hutchings',
'Alex Iman',
'Alex Jacke',
'Alex Kafer',
'Alex Kenj',
'Alex Kenji',
'Alex Kozobolis',
'Alex Krit',
'Alex L',
'Alex Leavon',
'Alex M.',
'Alex M.O.R.P.H.',
'Alex Madden',
'Alex Mattson',
'Alex Max Band',
'Alex Maxwell',
'Alex Mazzaev',
'Alex Medina Violin',
'Alex Megane',
'Alex Menco',
'Alex Mica',
'Alex Midi',
'Alex Mills',
'Alex Moreno',
'Alex Morph',
'Alex Newell',
'Alex Nikov',
'Alex Noiss',
'Alex O"Rion',
'Alex Opium',
'Alex Oshean',
'Alex Palmieri',
'Alex Preston',
'Alex Price',]

a_angl_list_12 = [
'Alex Rosales',
'Alex Saidac',
'Alex Sayz',
'Alex Schulz',
'Alex Simons',
'Alex Sin',
'Alex Skrindo',
'Alex Sonata',
'Alex Sparrow',
'Alex Spite',
'Stavi',
'Alex Stone',
'Alex Storm',
'Alex Tofan',
'Alex Toma',
'Alex Van Love',
'Alex Vargas',
'Alex Velea',
'Alex Young feat. Fatman Scoop',
'Alex"n"Ra Alma',
'Alex&Rus',
'Alexa',
'Alexa Goddard',
'Alex Zakharchuk',
'Alexander Brown',
'Alexander Cardinale',
'Alexander Forest',
'Alexander Gagarin',
'Alexander Geon',
'Alexander Holmgren',
'Alexander John',
'Alexander Lewis',
'Alexander O"neal',
'Alexander Oscar',
'Alexander Popov',
'Alexander Project',
'Alexander Reyes',
'Alexander Ross-Iver',
'Alexander Saykov',
'Alexander Shiva',
'Alexander Slash',
'Alexander Sommer',
'Alexander Star feat. Toi',
'Alexander Turok',
'Alexander Volosnikov',
'Alexandra Burke',]

a_angl_list_13 = [
'Alexandra Damiani',
'Alexandra Joner',
'Alexandra Moon',
'Alexandra Rado',
'Alexandra Shine',
'Alexandra Stan',
'Alexandra Ungureanu',
'Alexandre Bergheau',
'Alexandre Desplat',
'Alexandros Tsopozidis',
'Alexandrov Project',
'Alexandru',
'Alexdoparis feat. Maelyn',
'Alexenn',
'Alexey Romeo',
'Alexey Stepantsov',
'Alexey Yakimov',
'Alexi Blue',
'Alexi Murdoch',
'Alexiane',
'Alexis',
'Alexis Ffrench',
'Alexis Jordan',
'AlexNo',
'AlexSkill',
'AlexunderVibe',
'Alexx',
'Alexx Cay',
'Alexys',
'Alexz Johnson',
'Aleyna Tilki',
'Alf Poier',
'Alfie Acuri',
'Alfie Templeman',
'Alfina',
'Alfons feat. Sayfro',
'Alfonso Bz',
'Alfonso Muchacho',
'Alfonzo Blackwell',
'Alfr3d',
'Alfred Money',
'Ali',
'Ali Bakgor',
'Ali Brustofski',
'Ali Deger',
'Ali Gatie',
'AliMcGuirk',
'Ali Sotoodeh',
'Ali Wilson',
'Alia',]

a_angl_list_14 = [
'Alice',
'Alice Berg',
'Alice Chater',
'Alice Coltrane',
'Alice Cooper',
'Alice Cooper feat. Kesha',
'Alice Deejay',
'Alice Francis',
'Alice Glass',
'Alice Gold',
'Alice Gray',
'Alice Ivy',
'Alice Ivy feat. Ecca Vandal',
'Alice Merton',
'Alice Olivia',
'Alice On The Roof',
'Alice-D',
'Alicia Gil',
'Alicia Keys',
'Alicja',
'Alida',
'Alien Ant Farm',
'Alicja',
'Alien Ant Farm',
'Alien24',
'Alien24 feat. Esc.Ape',
'Aliesa Nicole',
'Alika',
'Alikyas',
'Alil A',
'Alim Zairov',
'Alimovs DJs',
'Alin Dimitriu',
'Alina Alison',
'Alina Baraz',
'Alina Libkind',
'Alina Os',
'Alina Tan',
'Alinka',
'Aliona Chikovani',
'Aliona Moon',
'Alisa',
'Alisa Franka',
'Alisa Geliss',
'Alisa Sweet',
'Alisa Trifonova',
'Alisan Aslan',
'Alisan Porter',
'Alisha',
'Alisher',]

a_angl_list_15 = [
'Alison Wonderland',
'Alisse Wendel',
'Alisson & Turner',
'Alive Like Me',
'AliveTeen',
'Alizee',
'Alkasar',
'Alkilados',
'All 4 One',
'All Good Things',
'All In 1',
'All India Radio',
'All Mankind',
'All Native',
'All Saints',
'All That Remains',
'All The Lights',
'All Time Low',
'All"nity',
'Allah-Las',
'Allan Casso',
'Allan Kutos',
'Allan Silveross',
'Allayz',
'AllDavay',
'Alle',
'Alle Farben',
'Allegro & Julie Thompson',
'Allen',
'Allen Folk',
'Allen King',
'Allen Stone',
'Allena',
'Allesandro Boschi',
'Allexa',
'Alli Simpson',
'Allie & Ivy',
'Allie Kay Lash',
'Allie X',
'Alliel',
'Allissa',
'Alloise',
'Allstar Weekend',
'Allure',
'Ally Barron',
'Ally Brooke',
'Ally Sereda',
'Allysia',
'Alma',
'Almadrava',]

a_angl_list_16 = [
'Almira',
'Almost Home',
'Almy & G.O.D.',
'Almyron',
'Alnair Lindalwe',
'Alo Lee',
'Aloe Blacc',
'Alok',
'Aloma Steele',
'ALON',
'Alpha 9',
'Alpha Raw',
'Alpha Squad',
'Alphadelta',
'AlphaGerius',
'Alphalove',
'Alpharock',
'Alphascan',
'Alphatown',
'Alphavite',
'Alphy Nics',
'Alpine',
'Alpines',
'Alseyda',
'Alphaville',
'Alt-J',
'Alta',
'Altar Red',
'Alter Bridge',
'Altione',
'Alton Ellis',
'AlunaGeorge',
'Alus',
'Alux Studio',
'Alvan feat. Velvet',
'Alvaro',
'Alvin And The Chipmunks',
'Alvin Lee',
'AlvinToday feat. The Limba',
'Alvita',
'Always Never',
'ALXXA',
'Aly',
'Aly Ryan',
'Alya',
'Alya feat. Shayan',
'Alyanna',
'Alyanna Lu',
'Alycia',
'Alycia Stefano',]

a_angl_list_17 = [
'Alys Lopez',
'Alysha',
'Alyson Stoner',
'Alyssa Bernal',
'Alyssa Reid',
'Alyssa Rubino',
'Alyssa Salt',
'Alyx Ander',
'Ama Lou',
'Amaanda',
'Amadin',
'Amador Rivas',
'Amain Johnson',
'Amalin',
'Amaloa',
'AmaMama',
'Amanaki',
'Amanda',
'Amanda Alexander',
'Amanda Batista',
'Amanda Bloom',
'Amanda Delara',
'Amanda Fondell',
'Amanda Larson',
'Amanda Lear',
'Amanda Mair',
'Amanda Seyfried',
'Amanda Wilson',
'Amanda Winberg',
'Amandine Bourgeois',
'Amar',
'Amareta and Zoora',
'Amari',
'Amarily',
'Amarily',
'Amaury Vassili',
'Amazing Grace',
'Amba Shepherd',
'Amber',
'Amber Hall',
'Amber Liu',
'Amber Rose',
'Amber Run',
'Amber Skye',
'Amber-Simone',
'Amberianne',
'Ambiworx',
'Ambray',
'Ambre feat. G-Eazy & BJ The Chicago Kid',
'Ambre Perkins & Kehlani',]

a_angl_list_18 = [
'Ambrela',
'AMCHI',
'AmeD & DJ MriD',
'Amel Bent',
'Amel Larrieux',
'Amelia Lilly',
'Amelia Lily',
'Amelie',
'Amelle Berrabah',
'Amer Bros',
'Ameria',
'America',
'American Authors',
'American Gang',
'American Groove Junkies',
'American Yard',
'Amerie',
'Ameriie',
'Amery',
'Ames',
'Amethystium',
'Ametisto',
'Amfree',
'Amfree feat. Ziya',
'AMI',
'Amigo',
'Amigos',
'Amigo',
'Amii Stewart feat. Gabry Ponte',
'Amila',
'Amin Gheydari',
'Aminata',
'Amine',
'Amir',
'Amir Acid',
'Amir Acid feat. Arghavan',
'Amir Afargan',
'Amira',
'Amisina',
'Amloop',
'AMME',
'Amo',
'Amon Amarth',
'Amor Del Mar',
'Amor Kismet',
'AMPATI',
'Amplify Dot',
'Amplite',
'AMPR feat. PRXZM',
'Amr Diab',]

a_angl_list_19 = [
'Amsterdam',
'Amsterdam Avenue',
'AMTRAC',
'Amura',
'AMWIN',
'AmY',
'Amy Irving',
'Amy Kucharik',
'Amy Lee',
'Amy Pieterse',
'Amy Shark',
'Amy Stroup',
'Amy Weber',
'Amy Winehouse',
'Amy Winehouse feat. Nas',
'An-Ya May',
'Ana Baston',
'Ana Cheva',
'Ana Criado',
'Ana Gianni',
'Ana Munteanu',
'Ana Oh',
'Ana Mena',
'Ana Popovic',
'Ana Torroja',
'Ana Whiterose',
'Ana Zimmer',
'Anabeoz',
'Anacondaz',
'Anadel',
'Analog Love Live',
'Analogia',
'Anandmurti Gurumaa',
'Anania',
'Anansi',
'AnAntA',
'Ananya Birla',
'Anastacia',
'Anastasia Belya',
'Anastasia Midnight',
'AnasteziA',
'Anathema',
'Anaсondaz',
'Anberlin',
'Anca Badiu',
'Anca Duma',
'Anca Florescu',
'Anca Pop',
'Ancelada',
'Ancorah',]

a_angl_list_20 = [
'And One',
'Anda Adam',
'Anda Allexa',
'Andain',
'Andamiro',
'Ander & Jey',
'Anders & Fahrenkrog',
'Anders Fernette',
'Anderson',
'Anderson & Lato El',
'Andery Toronto',
'Andgelina Di',
'Andi Vax',
'Andia',
'Andie Case',
'Andomalix',
'Andra',
'Andra Day',
'Andrada Popa',
'Andranik',
'Andras Kallay-Saunders',
'Andre Andreo',
'Andre Durgaryan',
'Andre Fennell',
'Andre Gagnon',
'Andre Merrit',
'Andre Merritt',
'Andre Nikkensen & Angelika Borof',
'Andre Rizo',
'Andre Tay',
'Andre Verchuren',
'Andre Zuniga',
'Andrea',
'Andrea Begley',
'Andrea Bertolini',
'Andrea Bocelli',
'Andrea Carnell',
'Andrea Coluzzi',
'Andrea Damante',
'Andrea Decibel',
'Andrea Del Vescovo feat. Jay',
'Andrea Demirov',
'Andrea Dieffe',
'Andrea feat. Gabriel Davi',
'Andrea feat. Mario Joy',
'Andrea feat. Suzanita',
'Andrea Ferrini',
'Andrea Ghirotti',
'Andrea Manzoni Trio',
'Andrea Martin',]

a_angl_list_21 = [
'Andrea Prete, Dj Ciruzz',
'Andrea Ribeca',
'Andrea Rincon',
'Andrea Rosario',
'Andrea Ross',
'Andrea Valeri',
'Andrea Verona',
'Andrea_T',
'Andreas',
'Andreas Kanellos',
'Andreas Silberrucken',
'Andreas Weise',
'Andreea',
'Andreea Andrei',
'Andreea Balan',
'Andreea Banica',
'Andreea D',
'Andreea Ignat',
'Andreea Olaru',
'Andreena',
'Andreew',
'Andrei Barbu & Octavian',
'Andrei Ciobanu',
'Andrei Leonte',
'Andreias',
'Andrej Rusty',
'Andres',
'Andres Cuartas',
'Andres Cuervo',
'Andres Linetzky Y Ernesto Romeo',
'Andres Selada',
'Andrew Bayer',
'Andrew Belize',
'Andrew Belle',
'Andrew Bennett',
'Andrew Garcia',
'Andrew Harris',
'Andrew Krivushkin',
'Andrew Lias',
'Andrew McMahon',
'Andrew Odd',
'Andrew Rai Ft. Alloise',
'Andrew Rayel',
'Andrew Ross',
'Andrew Shiller',
'Andrew Spencer',
'Andrew Stark',
'Andrew Starkoff',
'Andrew Strong',
'Andrew Whitman',]

a_angl_list_22 = [
'Andrey Aponik',
'Andrey Kravtsov',
'Andrey Lucky',
'Andrey Nova',
'Andrey Santin',
'Andrey Subbotin',
'Andrey Uniqque feat. Katrin',
'Andrey Vakulenko',
'Andreya Triana',
'AndrID',
'Andriel Of Mirkwood',
'Andrius Pojavis',
'Andro',
'Androma',
'Andromedik',
'ANDROPOV',
'Andru Donalds',
'Andruss',
'Andry J',
'Andy Abraham',
'Andy B Jones',
'Andy B. Jones',
'Andy Bey',
'Andy Bianchini & Rivas',
'Andy Blackwood',
'Andy Bull',
'Andy C',
'Andy C feat. Fiora',
'Andy Cooper',
'Andy Darling feat. Xnova',
'Andy Duguid',
'Andy Flores',
'Andy Grammer',
'Andy James',
'Andy Jay Powell',
'Andy McKee',
'Andy Moor',
'Andy Nicolas',
'Andy P',
'Andy Panda',
'Andy Rey',
'Andy Stott',
'Andy Stroke',
'Andy Viva',
'Andy Wait',
'Andy Williams',
'Andybody',
'Andyskopes',
'Aneela',
'Aneesh Gera & Lisa Williams',]

a_angl_list_23 = [
'Anelya',
'Anes',
'Aneta Sablik',
'ANFiLL',
'ANG',
'ANG & Trilane feat. David Shane',
'Angel',
'Angel Falls',
'Angel Forrest',
'Angel Haze',
'Angel LaShonn',
'Angel Rios',
'Angel Stoxx feat. Drew',
'Angel y Khriz',
'Angela Puxi',
'Angelica Salem',
'Angelico',
'Angelika Dusk',
'Angelika Vee',
'Angelika Yutt',
'Angelique Jerome',
'Angell',
'Angelo Di Pippo',
'Anger',
'Anggun',
'Angie',
'Angie Miller',
'Angie Van Burg',
'Angie Vu Ha',
'Angus Macrae',
'Ani',
'Ani Karo',
'ANi"E',
'Ania',
'Anica Russo',
'Aniello',
'Anika',
'Anika Meil',
'Anikdote',
'ANIKV',
'Animal Jazz',
'Animal Liberation Orchestra',
'Animal X',
'Animals',
'Animic',
'Anira',
'Aniri',
'Anis Don Demina',
'Anita Baker',
'Anita Feat Chris Oliver',]

a_angl_list_24 = [
'Anita O"day',
'Anitta',
'Anivar',
'Anja',
'Anja Nissen',
'Anjali World',
'Anjey',
'Anjeza Shahini',
'Anjulie',
'Anka',
'Ankerstjerne',
'Ankhen',
'Ankla',
'Ann Clue',
'Ann Jarel',
'Ann Lee',
'Ann Sophie',
'Anna',
'Anna Abreu',
'Anna Bauer',
'Anna Clendening',
'Anna D',
'Anna David',
'Anna FOX',
'Anna Golubeva',
'Anna Grace',
'Anna Lee',
'Anna Lesko',
'Anna Lidman',
'Anna Lunoe',
'Anna May',
'Anna Miracles',
'Anna NewSea',
'Anna Odobescu',
'Anna Of The North',
'Anna Petrash',
'Anna Rossinelli',
'Anna Savanna',
'Anna Straker',
'Anna Turska',
'Anna Vissi',
'Anna Wilson',
'Anna Wise',
'Anna Zak',
'Annabel Jones',
'AnnaGrace',
'Annah Mac',
'Annakin',
'Annalia',
'Annalisa',]

a_angl_list_25 = [
'Anne Dereaux',
'Anne-Marie',
'Annelie',
'Annely Cole',
'Annemie',
'Annet',
'Annet Artani',
'Annet Lev',
'Annica',
'Annie',
'Annie Drury',
'Annie Lennox',
'Annie Warden',
'Anniela',
'Annihilator',
'Annisokay',
'Anno Domini Beats',
'Annsofi Pettersen',
'Anny Alex',
'Annybell',
'Anonymous',
'Anonymously Yours',
'Anoop Desai',
'Another Nation',
'Anouk',
'ANREE',
'Anri Jokhadze',
'Anrise',
'Ansah',
'Ansel Collins',
'Antanta',
'Antarcticats',
'Ante',
'Anteca',
'Antew',
'Anth',
'Anthem Kings',
'Anthony',
'Anthony Attalla',
'Anthony C feat. Claire Woodley',
'Anthony Callea',
'Anthony El Mejor',
'Ansel Elgort',
'Anthony Frank',
'Anthony Hamilton',
'Anthony Harm',
'Anthony Jasmin',
'Anthony Keyrouz',
'Anthony Ragni',
'Anthony Rother',]

a_angl_list_26 = [
'Anthony Wilson',
'Anthya',
'Anti Up',
'Anti-P.L.U.R',
'Antinia',
'Antique',
'Anto',
'Antoine Andary',
'Antoine Clamaran',
'Anton Blagushin',
'Anton Brasko',
'Anton Ger',
'Anton Greco',
'Anton Gronholm',
'Anton Ishutin',
'Anton Liquid',
'Anton Liss',
'Anton Markus',
'Anton Pavlovsky',
'Anton Powers',
'Antonia',
'Antonia Markova',
'Antonio Campos',
'Antonio Carlos Jobim',
'Antonio Cobo',
'Antonio Giacca',
'Antonio Gonzalez',
'Antonio Jose',
'Antonio Picikato',
'Antonio ST',
'Antonio Vivaldi',
'Antonique Smith',
'Antony & Cleopatra',
'Antonymes',
'Anugama',
'Anuryh',
'Anushka',
'Anushqa',
'ANVAR',
'Anxious Angelo',
'Anya',
'Anya Rudneva',
'Anya Shesternina feat. Fab Faya',
'Anyfrieva Daria',
'Anymars',
'Anywan & Mystic',
'Anzej Dezan',
'Anzheli',
'Apache Indian',
'Apaches',]

a_angl_list_27 = [
'Apashe',
'Ape Drums',
'Ape School',
'Apex',
'Apexape',
'Aphex Twin',
'Apia',
'Apocalyptica',
'Apollo 440',
'Apollo Brown',
'Apollo feat. Meucci',
'Apollo Four Forty',
'Apollo The Great',
'ApolloJungle',
'Apotheosis',
'Apple Juice',
'Appledream',
'Approaching Black',
'APRE',
'Apres',
'Apres Minuit',
'April Ivy',
'AQU1LA',
'Aqua',
'Aquadrop',
'Aqualung',
'Aquarius',
'Aquilo',
'Ar The Bushmaster',
'Ar-SiDE',
'Ar4i',
'Ara',
'Arabesque',
'Arakain',
'Arakvybez',
'Arash',
'Arcash',
'Archeo',
'Arches',
'ARCHI',
'Archi Rich',
'Archi-M',
'Archies',
'Archive',
'Arco & John Vermont',
'Arctic Jet',
'Arctic Lake',
'Arctic Monkeys',
'Arctic Moon',
'Arctic Night',]

a_angl_list_28 = [
'Arctic Ocean',
'Arcuate',
'Arden Cho',
'Arden Forest',
'Ardian Bujupi',
'Ardit Cuni',
'Aretha Franklin',
'ARF',
'ArGO',
'Argui',
'Argyll & Sutherlands Highlanders',
'Arhod',
'ARi',
'Aria',
'Aria Hennessy',
'Ariadne',
'Ariana Grande',
'Arianna',
'Ariela Jacobs',
'Arif Kasimov',
'Arif Mardin',
'Arijiah',
'Arijit Singh',
'Arik',
'Arik & Lira',
'Arika Kane',
'Arilena Ara',
'Arin Ray & Kehlani',
'ARIS',
'Aris Plaskasovitis',
'Arisen Flame',
'Arisha',
'Arizona',
'Arizona Zervas',
'Arjun',
'Arjun Kanungo',
'Arkay',
'Arkham Knights',
'Arkutec',
'ARLE & L’Tric',
'Arlissa',
'Arma',
'Arma K',
'Arma8',
'Armagedon',
'Arman Bahrami',
'Arman Mardigian',
'Armand Lassagne',
'Armin van Buuren',
'Armitage',]

a_angl_list_29 = [
'Armos',
'Army Of Lovers',
'Arnella',
'Arnilove',
'Arnis Mednis',
'Arno Cost',
'Arno Elias',
'Arnold Palmer',
'Arnon',
'ARO',
'Aroma feat. Lyck',
'Aron Blom',
'Aron Burton',
'AronChupa',
'Around The Sun',
'Arpad-Zsolt Domahidi',
'ARPI',
'Arrhult',
'Arroyo',
'Ars-N',
'Arsenic P',
'Arsenie',
'Arsenium',
'Arseniy Guri',
'Arseniya',
'Arst One',
'Art & Shock',
'Art Key',
'Art of Dying',
'Art Of Noise',
'Art Of Sleeping',
'Art of sound',
'Art Van Damme',
'Arta',
'Artento Divini',
'Arthur Beatrice',
'Artsvik',
'Arturro Mass',
'Arty',
'Aruba Ice',
'Aruna',
'Aruso',
'Arvingarna',
'Ary',
'Arzien',
'As If I Care',
'ASAMMUELL',
'Asammuell',
'ASAP Ferg',
'Asap Rocky',]

a_angl_list_30 = [
'Asbjorn',
'Asgeir',
'Ash',
'Ash King',
'Ash Wilkes',
'Asha',
'Ashanti',
'Ashe',
'Ashea',
'Asheni',
'Asher',
'Asher Monroe',
'Asher Quinn',
'Ashera',
'Ashes Of Ares',
'Ashes Remain',
'Ashlee Littlejohn',
'Ashlee Simpson',
'Ashlex',
'Ashley Roberts',
'Ashley Tisdale',
'Ashley Wallbridge',
'Ashlyne Huff',
'ASHS',
'Ashton Love',
'Ashura',
'Ashy',
'Asia',
'Asia Ash',
'Asia Bryant',
'Asiya',
'Ask Embla',
'Asking Alexandria',
'Aslan',
'Aslove',
'Asmodai',
'Asokin',
'Aspen',
'Aspyer',
'Assaf',
'Astemir',
'Aster Fekre',
'Astero',
'Asteroid',
'Astha',
'Aston Merrygold',
'Aston Wyld',
'Astor Piazzolla',
'Astor Quinquela',
'Astrid',]

a_angl_list_31 = [
'Astrid S',
'Astronomyy',
'Astrud De Mata',
'At Simplicity',
'At Sunset',
'At Vance',
'ATB',
'Atc',
'Atelier Tommy',
'Atesh',
'ATG',
'Athena',
'Athena Manoukian',
'Athletic Mic League',
'Athletixx',
'Atica',
'Atik',
'Atika Patum',
'Atim',
'Atiye',
'ATL',
'Atlantida Project',
'Atlantiic',
'Atlantis Ocean',
'Atlas Genius',
'Atlas Knox',
'Atle',
'Atleha',
'ATLiens',
'Atom',
'Atrium',
'Attack Attack',
'Attila',
'Attila Syah',
'Attlas',
'Atypisk',
'Atze Ton',
'Au/Ra',
'Au5',
'Aubrey O"Day',
'Audien',
'Audio Deluxe',
'Audio Girls',
'Audio Killers',
'Audio Shaman',
'Audioboy',
'Audiolove',
'Audiomachine',
'Audion',
'Audiosoulz',]

a_angl_list_32 = [
'Audium',
'Audley Rollen',
'August',
'August Alsina',
'August Green',
'August Rigo',
'Augustray',
'Auld Town March',
'Aundlang',
'Aundrea Fimbres',
'Aura',
'Aura Dione',
'Aurela Gace',
'Aurelia',
'Aurelien Noel',
'Auri',
'Aurora',
'Aurora Night',
'Auroraw',
'Aurosonic',
'Aurovision',
'Auryn',
'Austen',
'Austin Mahone',
'Autarkic',
'Autoerotique',
'Autograf',
'Autootvetchik',
'Autosky',
'Autumn Hill',
'Autumn Rowe',
'Autumn"s Calling',
'Ava',
'Ava Koci',
'Ava Max',
'Ava Rocks',
'Ava Wolfe',
'Avaion',
'AVAKADO',
'Avakhan',
'Avalanche City',
'Avante Black',
'Avay',
'AVB Brothers',
'Avec Sans',
'Avenged Sevenfold',
'Aventura',
'Avenue One',
'Average White Band',
'Avernus',]

a_angl_list_33 = [
'Avery Storm',
'Avery Watts',
'Avicii',
'Avidan Project',
'Aviva',
'Avlish',
'Avocado feat. Nezlobin',
'AVOLA',
'Avriel Epps',
'Avril Lavigne',
'Avrosse',
'Avsineev',
'Awa',
'Awake',
'Awanging',
'Aware Esperando',
'AWD',
'Aweminus',
'Awnil',
'Awol',
'Awolnation',
'Awoltalk',
'AWS',
'Axel Boy',
'Axel Flovent',
'Axel Hirsoux',
'Axel Johansson',
'Axel Mansoor',
'Axel Moro',
'Axel Rudi Pell',
'Axel Wikner',
'Axen',
'Axento',
'Axis',
'Axwell',
'AYA',
'Aya Katrine',
'Ayah Marar',
'Ayanna Howard',
'AyCrusher',
'Ayda',
'Aydan',
'Ayelle',
'AYER',
'Ayhan Keser',
'Ayla',
'Aylin',
'Ayman El Refaie',
'Aynine',
'Aynsley Lister',]

a_angl_list_34 = [
'Ayo',
'Aysel',
'Aysha',
'Ayumi Hamasaki',
'Ayyan',
'AZALIYA',
'Azara',
'Azary',
'Azealia Banks',
'Azedia',
'Azekel',
'Azell',
'Azet & Zuna',
'Azira',
'Azoto',
'Azov Style',
'AZTX',
'Azul ZK',
'Azusena',
'Azzido Da Bass',
'Azzido Schwarz',
]

litera = SoundSymbol.objects.get(name="A")

count = 0

for tag in a_angl_list_8:
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
                    new_track = SoundcloudParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, created_at=created_at, duration=track.duration, genre=genre, description=description, title=track.title, uri=track.uri, release_year=track.release_year)
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
                        new_track = SoundcloudParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, created_at=created_at, duration=track.duration, genre=genre, description=description, title=track.title, uri=track.uri, release_year=track.release_year)
                    count = count + 1
