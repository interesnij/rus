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

p_rus_list_1 = [
"P Money & Giggs",
"P-Square",
"P-TAB & Concourse feat. Max Landry",
"P!nk",
"P?nar Ayhan & S.O.S.",
"P. Diddy Ft. Keyshia Cole",
"P.A.T.R.I.X",
"P.Lion",
"P.M. Sampson",
"P.R.i.D.E feat. VoskoboynikoV & Daff Dee",
"P.S 343",
"P22",
"PA Sports feat. Jamule & Motrip",
"Pabl.A",
"Pabllo Vittar",
"Pablo Alboran",
"Pablo Bendr",
"Pablo Caballero",
"Pablo Ferrero",
"Pablo Gigliotti",
"Pablo Ju",
"Pablo Lago feat. Laura Elece",
"Pablo Nouvelle",
"Pac Scherhag feat. Hernan Madison",
"Paces",
"Pacha Man feat. Alex Velea",
"Pachanga feat. Massari",
"Pachi",
"Pacho El Antifeka & Farruko",
"Pacific State",
"Pacific, VanDyck & Boogshe",
"Pack The Arcade feat. Akcent",
"Packy",
"Paco Cruzado",
"Paco De Lucía",
"Paco Di Lucia",
"Paddy Kelly",
"Pade",
"Pael",
"Paenda",
"Paf feat. Veronika Hale",
"Paffendorf feat. Sydney-7",
"Pagadixx feat. Adixia",
"Paganini",
"Page Jimmy",
"Paif & Vnuk",
"Paige",
"Pain Of Salvation",
"Painted Heart",
"Paintrain",]

p_rus_list_2 = [
"Paj",
"Paji feat. Yves Paquet",
"Pakalena",
"Paki & Jaro feat. Zoe Badwi",
"Paki feat. Jaro & Emanuel Nava",
"Pakito",
"Paky Francavilla & Fred feat. Jonny Rose",
"Palace",
"Palach feat. Hawaiian",
"Palaraga feat. Ewa Ice",
"Palastic",
"Palisades",
"Palm Trees",
"Palmer & Stone",
"Palmez & Andy Junior",
"Palmez & Nicky B feat Tanya",
"Paloma Faith",
"Paloma Ford",
"Paloma Mami",
"Palyur feat. Radicalfashion & Макс Лоренс",
"Pam Taylor",
"Pamela Moore",
"Panacea",
"Panacea86",
"Panam Panic",
"Panamah",
"Panamera",
"Pancronic",
"Panda Eyes",
"Panda Junior feat. Rux",
"Pandaboyz feat. Kelly",
"Pandalay",
"Pandora",
"Panetoz",
"Pang",
"PANG!",
"Panic City feat. Reid Stefan & Mike Taylor",
"Panic Era",
"Panic! At The Disco",
"Paniek",
"Panivalkova",
"Panjabi Mc",
"Pankratov feat. JK",
"Panopticum",
"Panova",
"Pansil",
"Pantera",
"Panteros666 feat. Woodkid",
"Panuma & Tokyo Project & Emiah",
"Panzer Flower",]

p_rus_list_3 = [
"Paola & DJ Fisun",
"Paola feat. Free Deejays",
"Paolo Aliberti feat. Carl",
"Paolo Campidelli",
"Paolo Conte",
"Paolo De Ceglie",
"Paolo Fresu Devil Quartet",
"Paolo Gonzalez",
"Paolo Martinez",
"Paolo Meneguzzi",
"Paolo Noise feat. LeRoy Bell",
"Paolo Nutini",
"Paolo Ortelli & DJ Antoine",
"Paolo Pellegrino feat. Susan Tyler",
"Paolo Vivaldi",
"Papa J. Ruiz",
"Papa Marlin & Andrew Rai feat. Veselina Popova",
"Papa Roach",
"Papa Ya",
"Papa Zeus",
"Papai Joci",
"Papajam",
"Papayo",
"Paper & Places",
"Paperchaser",
"Papermind",
"Paperwhite",
"Pappa Bear",
"Pappa Razzi feat. Laureen",
"Pappers Against Racism Feat. Down Low",
"PAPY Kerro feat. Mohombi & Lumino",
"Para One",
"Para X",
"Para-Dox feat. Max",
"Parabellum & T1One",
"Parachute",
"Parachute Youth",
"Parade Of Lights",
"Parade Of Planets",
"Paradisco feat. Giorgio",
"Paradise Blue",
"Paradise Oskar",
"Paradiso",
"Paradox Factory",
"paragone",
"Parah Dice",
"Paralleli",
"Paramore",
"Parijat",
"Paris & Simo",]

p_rus_list_4 = [
"Paris Blohm",
"Paris France Transit",
"Paris Hilton",
"Paris Motel",
"Paris Tango",
"Parix Hilton feat. Ernia",
"Park Place",
"Parker",
"Parks, Squares And Alleys",
"Parkway Drive",
"Parkx feat. Charlotte Haining",
"Parmalee feat. Blanco Brown",
"Parov Stelar",
"Parra For Cuva & Senoy",
"Parris Franz feat. Akon",
"Parsifal",
"Parson James",
"Part Company",
"Part Time",
"Party Animals",
"Party Collective",
"Party Favor",
"Party Ghost & Spock",
"Party Nails",
"Party On Demand",
"Party People",
"Party Rockerz",
"Party Thieves & JayKode",
"PartyNextDoor & Halsey",
"Parx",
"Pasabordo",
"Pascal & Pearce",
"Pascal Dubois",
"Pascal Geiser",
"Pascal Junior",
"Pascal Letoublon",
"Pasdat",
"PasDee feat. Eleven",
"Pasha Clim & Gridasoff",
"Pasha Lee & Vitaco feat. Elia",
"Pasha Leem",
"Pasha Lim feat. Katrin Moro",
"Pasha Parfeny",
"Pasha Proorok & Seewoow",
"Pashe feat. Panther",
"Pashtet",
"Paskal Daze",
"Passenger 10",
"Passengers",
"Passion",]

p_rus_list_5 = [
"Passion Fruit",
"Passion Pit",
"Passpar-2 Feat. Sydney Fresh",
"Pastel feat. Dark Blue",
"Pasten Luder",
"Pastor T.L. Barrett & The Youth For Christ Choir",
"Pastora Soler",
"Pat Benedetti & Kimaru",
"Pat Bone",
"Pat Farrell",
"Pat Lok",
"Pat Travers",
"Pata Negra",
"Pataki",
"Patric Brown",
"Patric La Funk",
"Patrice Pharelle",
"Patricia Kaas",
"Patricia Kazadi",
"Patricia Spero",
"Patrick Abrial",
"Patrick Arbez",
"Patrick Ball",
"Patrick De Giorgi feat. Donnie Ozone",
"Patrick Dorgan",
"Patrick Dyco & Lela Diaz",
"Patrick G",
"Patrick Hagenaar",
"Patrick Hofmann",
"Patrick Hofmann, Jason Amador",
"Patrick Juvet",
"Patrick Kelly",
"Patrick Lite feat. Vitaly Gray",
"Patrick Martin",
"Patrick Mc Perfady",
"Patrick Miller",
"Patrick Mitchel Porter",
"Patrick Ouchene",
"Patrick Pizzorni feat. Kat Dahlia",
"Patrick Reza feat. Jilian",
"Patrick Roos",
"Patrick Rosa",
"Patrick Sandim & Nicky Valentine feat. Natalia Damini",
"Patrick Slayer",
"Patrick Stump feat. Lupe Fiasco",
"Patrick Wolf",
"PatrickReza",
"Patrik Almkvisth",
"Patrik Jansson Band",
"Patrix",]

p_rus_list_6 = [
"Patsy Cline",
"Patti Drew",
"Pattraxx",
"Patty Ryan",
"Patz & Grimbard",
"Paul & Starry Knights",
"Paul Anka",
"Paul Arthur King",
"Paul Bingham feat. Nanje Nowack",
"Paul Black",
"Paul Carpenter & Manuel Molina",
"Paul Cesar",
"Paul Cless & Brixx",
"Paul Colmer",
"Paul Courbet",
"Paul Damixie",
"Paul Damixie feat. Feli",
"Paul Daniel",
"Paul Daniel & Kate Linn",
"Paul Dave",
"Paul Denton",
"Paul Desmond & Jim Hall",
"Paul Dima feat. Dj Deelyte & Edwardo Base",
"Paul End",
"Paul Hama",
"Paul Hank",
"Paul Hardcastle",
"Paul Harris feat. Dragonette",
"Paul Iorga",
"Paul Johnson",
"Paul Lawler",
"Paul Manandise",
"Paul Marshman feat. Omz",
"Paul Mauriat",
"Paul Mayson",
"Paul Mc Cartney",
"Paul McCartney",
"Paul Morrell feat. Vicky Jackson",
"Paul Oakenfold",
"Paul P feat. DJ Saftik",
"Paul P.",
"Paul Parker",
"Paul Reed Smith Band",
"Paul Reeves",
"Paul Rey",
"Paul Richard feat. Very Thompson",
"Paul Richmond",
"Paul Rudd feat. Sam Calver",
"Paul Schmitz",
"Paul Sharada",]

p_rus_list_7 = [
"Paul Simon",
"Paul Taylor",
"Paul Thomas feat. Ladystation",
"Paul Tuvman",
"Paul Van Dyk",
"Paul Van Hyden & Michael Fall",
"Paul Van Tremer",
"Paul Vax & Ultrabazz",
"Paul Veth feat. Elton Jonathan Kroon",
"Paul Vinitsky",
"Paul Wall feat. Kid Ink & YG",
"Paul Warren",
"Paul Webster feat. Angelic Amanda",
"Paul Woolford feat. Karen Harding",
"Paul2Paul",
"Paula Abdul",
"Paula Deanda",
"Paula Evans",
"Paula Seling",
"Paulina Czapla",
"Paulina Rubio",
"Paulina Starborn",
"Paulman",
"Paulo Londra feat. A Boogie Wit Da Hoodie",
"Paulo Tella",
"Paulos Bouros",
"Pav Dharia",
"PAVAND",
"Pavand",
"Pavel Kempel feat. Хасан",
"Pavel Khvaleev",
"Pavel Svetlove feat. Dina Eve",
"Pavel Velchev & Dmitriy Rs",
"Pavell & Venci Venc' & Alma",
"Pavell & Venci Venc' x Monoir",
"Pavelsky",
"Pavlo",
"PavLova",
"Pavlovskaya feat. Sasha Lacoste",
"Paw&Lina",
"Pawl",
"PAX feat. Minelli",
"PAX Paradise Auxiliary",
"PAY feat. NODE",
"Payman & Paula Douglas",
"Payton Rae",
"Payy feat. Ardian Bujupi",
"Paz Yenni feat. Papa",
"PBH & Jack",
"PBSR",]

p_rus_list_8 = [
"Peabod feat. Chad Mattson",
"Peaceful Romantic Piano Music Consort",
"PeaceTreaty",
"Peaches",
"Pearl",
"Pearl Feat. Zaradika",
"Pearl Harbor",
"Pearl Jam",
"Peat Jr.",
"Pedro Capo & Farruko",
"Pedro Ibanez",
"Peer Waibel-Fischer & Mike Singer",
"Peet & Breeth",
"PeeWee",
"Peg Parnevik",
"Pegato feat. Eklo",
"Pegazus",
"Pegboard Nerds",
"Peggy Gou",
"Peggy Lee",
"Peking Duk",
"Pelageya Stefoglo",
"Pelago feat. Maximus",
"Pelari & CollinWex feat. Dominique Fricot",
"Pell",
"Pendragon",
"Pendulum",
"Pennines",
"Penny Foster feat. Felix Leiter",
"Pentatonix",
"Penthox",
"Peony",
"People Without Shoes",
"Pep & Rash",
"Pepe & Shehu feat. Morgana",
"Pepe feat. Arando Marquez",
"Pepe Habichuela",
"Peppelino",
"Peppino Gagliardi",
"PeR",
"Per Frost",
"Pere Ubu",
"Perez & Saintana",
"Perfect Pitch",
"Perfect Point",
"Perfume Genius",
"Periphery",
"Pernilla Karlsson",
"Perpetuous Dreamer",
"Perry Como",]

p_rus_list_9 = [
"Pers Lirik",
"Persia Beatz",
"Persian Raver",
"Perto & Other feat. Dani Poppitt",
"Pertti Kurikan Nimipaivat",
"Perttu feat. Hym",
"Pery Ribeiro",
"Pesco DJ",
"Pesenka N",
"Pesho feat. Kc Nwokoye",
"Pet Shop Boys",
"Petar Della Pietra & Geo Da Silva",
"Pete Bellis & Tommy",
"Pete Ellement",
"Pete Fox",
"Pete K",
"Pete Kingsman feat. Amelia",
"Pete Murray",
"Pete Oak",
"Pete Philly & Perquisite",
"Pete Sabo",
"Pete Sandberg",
"Pete Tha Zouk",
"Pete Tong, Jules Buckley & The Heritage Orchestra feat. Becky Hill",
"Pete Yorn",
"Peter Alejandro feat. Mirza",
"Peter And The Wolves",
"Peter Aristone feat. Melanie C",
"Peter Bailey",
"Peter Bjorn & John",
"Peter Brown",
"Peter Diaz & Carlos Alvarez White",
"Peter Gabriel",
"Peter Groskreutz",
"Peter Hammill",
"Peter Heppner",
"Peter Kai",
"Peter Karp",
"Peter Luts",
"Peter Manos",
"Peter Martin",
"Peter Pearson",
"Peter Pop",
"Peter Pou",
"Peter Sandberg",
"Peter Sax",
"Peter Schanz",
"Peter Schilling",
"Peter Schilperoort Quintet",
"Peter Silence",]

p_rus_list_10 = [
"Peter Sterling",
"Peter Thomas feat. Betty Who",
"Peter Tosh",
"Peter Ward",
"Peter White",
"Petit Biscuit",
"Petite Meller",
"Petra Marklund",
"Petrojvic Blasting Company",
"Petrusco feat. Koko Joy",
"Petty Joy",
"Petty Party",
"Petula Clark",
"Pex L",
"PH Electro",
"Phace",
"Phacematik",
"Phaction feat. Katkin Willow",
"Phandora",
"Phantogram",
"Phantomas",
"Phantoms feat. Anna Clendening",
"PhaNtomX",
"Pharao",
"Pharao & DJ Zyzz",
"Pharaoh",
"Pharenite, Omar J",
"Pharfar",
"Pharien",
"Pharrell Williams",
"Phaseone",
"PhaseOne & Bobby Duque",
"Phases",
"Phat Kat feat. Elzhi",
"Phatjak feat. Drew",
"Phats & Small",
"Phebe Starr",
"Phelin",
"Phelipe",
"Phella feat. Medi",
"Phemales",
"Phentik",
"Phetsta feat. Reija Lee",
"Phil Campbell feat. Alice Cooper",
"Phil Collins",
"Phil Dinner",
"Phil Gates",
"Phil Hancock",
"Phil Jay",
"Phil Jay vs. Da Brozz feat. Landon Gadoci",]

p_rus_list_11 = [
"Phil Phillips & The Twilights",
"Phil Pratt & The Caltone All Stars",
"Phil Tangent & Pennygiles",
"Phil Wilde feat. Danzel",
"Philbeat",
"Philchansky & Paul Murashov",
"Philco Fiction",
"Philip Aelis & Marcus feat. Nate Monoxide",
"Philip De Blue",
"Philip George",
"Philip Guyler",
"Philip Mayer",
"Philip Sayce",
"Philip Wesley",
"Philipp Dinner feat. Diana Liv",
"Philipp Dittberner & Marv",
"Philipp Rayc",
"Philippe El Sisi & Sarah Russell",
"Philippe Reda feat. Noface",
"Philippine",
"Phill Collins",
"Phill Kay feat. Julie C & MC Y2K",
"Phillerz & Xtra J",
"Phillip Cue",
"Phillip J",
"Phillip Larue",
"Phillip Phillips",
"Phillipo Blake & Олеся Астапова",
"Phino",
"Phiso",
"Phlex feat. Daniella McCarthy",
"Phoebe Buffay Ost",
"Phoebe Ryan",
"Phoenyx & Kunala",
"Pholder",
"Phonat",
"Phonique Ft. Rebecca",
"Phosphor",
"Photo Feat Erika Houston",
"Photocomfort",
"Photographer",
"Phreek",
"Phrenik",
"Phunk Investigation",
"Phunktjan feat. Max C",
"Phyllisia feat. Flo Rida",
"Phynn feat. Jets Overhead",
"Phynx & Prettyheartbreak",
"Physical Dreams",
"Physical Phase",]

p_rus_list_12 = [
"Pia Mia",
"Pia Toscano",
"Piano Bar Music Academy",
"Pianochocolate",
"Pianoбой",
"Piar",
"Piccadilly",
"Picco",
"Pickin' On Series",
"Picture This",
"Pieces Of A Dream",
"Pier At House feat. Tyta Eden",
"Pierce",
"Pierce Fulton",
"Piero & MusicStars",
"Piero Piccioni",
"Pierre De La Touche",
"Pierre Pienaar & Dirkie Coetzee",
"Pierre Van Dormael",
"Pietro Lombardi",
"Pig & Dan",
"Piggy Bang",
"Pihlaja",
"Pikassa",
"Pill Collinz",
"Pillows",
"Pilmat feat. Laureen",
"Pilot",
"Pilton feat. Gus",
"Pimpa Girl",
"Pimpie",
"Pimpton feat. Future",
"Pine & Paul Nax",
"Pines",
"Pinetop Perkins",
"Pingpong",
"Pink",
"Pink Elephant",
"Pink Floyd",
"Pink Fluid",
"Pink Guy",
"Pink Is Punk",
"Pink Martini",
"Pink Noisy",
"Pink Panda",
"Pinkman feat. Nica",
"Pins.ku",
"Pinto Wahin",
"Pipe Bueno feat. Pasabordo",
"Piques & Lexy Panterra",]

p_rus_list_13 = [
"Pirates Of The Sea",
"Pirelli & Modica feat. Luca Zeta",
"Piru",
"Piso 21",
"Pistakio",
"Pistol Shrimp feat. Aaronknute",
"Pit Bailay",
"Pitbullbi & Wisin",
"Pitbull feat. Ne-Yo",
"Pitbull feat. Nelly",
"Pitbull feat. Okary La Pauta",
"Pitbull feat. Prince Royce & Ludacris",
"Pitbull feat. Qwote",
"Pitbull feat. R. Kelly & Austin Mahone",
"Pitbull feat. Ray Lavender",
"Pitbull feat. Red Foo, Vein & David Rush",
"Pitbull feat. Rhea",
"Pitbull feat. Robin Thicke, Joe Perry, Travis Barker",
"Pitbull feat. Sean Paul",
"Pitbull feat. Sensato",
"Pitbull feat. Shakira",
"Pitbull feat. Stephen Marley",
"Pitbull feat. Steven A. Clark & Ape Drums",
"Pitbull feat. T-Pain",
"Pitbull feat. Theron Theron",
"Pitbull feat. Tito El Bambino & Guru Randhawa",
"Pitbull feat. TJR",
"Pitbull feat. Trick Daddy",
"Pitbull feat. Trina",
"Pitbull feat. Ty Dolla Sign",
"Pitbull feat. Vein",
"Pitbull feat. Wynter Gordon",
"Pitbull feat. Young Black",
"Pitbull ft. De Zona",
"Pitbull ft. Havana Brown",
"Pitbull ft. Jay Sean",
"Pitbull Ft. Lil Wayne Ft Beeda Weeda",
"Pitbull ft. Marc Anthony",
"Pitbull ft. Shakira",
"Pitbull ft. SherryMix",
"Pitbull, El Chombo & Karol G feat. Cutty Ranks",
"Pitch Dark, Deep Face feat. Shirley Davis",
"Pitch, Corazza feat. Jack Meille",
"Pitsi feat. Animado",
"Pitt Leffer",
"Pixel Terror",
"Pixie Lott",
"Pixie Paris",
"PIXL feat. Cassandra Kay",
"Pixl feat. Q'aila",]

p_rus_list_14 = [
"Pixl Surfers",
"Pizza Brothers",
"Pizzaman",
"PJ Morton",
"PJay Johnson",
"PJU feat. Javi",
"PKCZ & Snoop Dogg & Yultron feat. Crazyboy",
"PL feat. Daria",
"Place Vendome",
"Placebo",
"Placid Larry",
"Plain White T's",
"Plamena",
"Plan B",
"Planet Funk",
"Planet Lounge",
"Planet Paradise",
"Planet Perfecto",
"Planet Seven",
"Planet VI feat. Cassie",
"Planeta Loco",
"PlanetaVE feat. Лиза Small",
"PLANETTU",
"Plankina",
"Plasdance",
"PLASTIC MODE",
"Plastic Robots",
"Plastic Toy & DJ Snake",
"Plastik B",
"Plastik Bass feat. MC Trini",
"Plastik Funk",
"Plastik Joker & Valyum",
"Plastikhead",
"Plastyc Buddha",
"Platin",
"Platinum Doug",
"Platinum Monkeys feat. Ange",
"Platon feat. Joolay",
"Platou",
"PLAY",
"Play & Win feat. Antinia",
"Play and Win",
"Play Boys",
"Play-N-Skillz",
"Playa",
"Playa Limbo",
"Playahitty",
"Playboi Carti",
"Playboy Tre feat. B.o.B",
"PlayDis!",]

p_rus_list_15 = [
"Playdope Deejays feat. Chriss-T",
"Player",
"Playhitty",
"Playinfields feat. Mo Safren",
"Playingtheangel",
"Playme",
"Playmen",
"Plaza",
"Plazma",
"PLC",
"Pleasure P",
"Pleasurekraft",
"PLESTED",
"Pletnev",
"Plies feat. K Camp",
"Plissken",
"PlomBear",
"Plot Twist",
"PLS&TY feat. Bobby Saint",
"Pluckyduck feat. МОС13",
"Plug 'N' Play",
"Plug In Stereo feat. Megan & Liz",
"Pluko feat. Manila Killa & Ilo Ilo",
"Plum",
"Plumb",
"Plumbers feat. Desy Lady",
"Plungerbird, Beard in Dust",
"Plus Minus",
"Pluton & B-Fairy",
"PLYA",
"PNAU",
"PnB Rock",
"Pnfa",
"PNL",
"Pnut & Jelly",
"Pocher & Clyde Trevor",
"Pochill",
"Poediction feat. Trevor Jackson",
"Poema",
"POESY",
"Poetry 'n Motion",
"Poets Of The Fall",
"Point Blank",
"Poison",
"Poke feat. MocroManiac",
"Pol Granch",
"Pol Rossignani feat. Ryk",
"Pola & Bryson",
"Polar Youth",
"Polaris",]

p_rus_list_16 = [
"Polaroid",
"Polarsea",
"Poli Genova",
"Polikarpov",
"Polina Grace",
"Polina Griffis",
"Polina Griffith",
"Polina Krupchak",
"Polina Smolova",
"Polished Chrome",
"Pollaponk",
"Polly A.",
"Polo",
"Polovinka",
"Polow Da Don",
"Poltinnik (Н.П.М.) feat. БезАдресата",
"Pom Poms",
"Pomaz",
"Pomaz feat. Tatyana Chetvertak",
"Pomo feat. Harrison Brome",
"Pompeii",
"Pompero",
"Pompis",
"Pongo",
"Ponny",
"Ponomariov86",
"Pontifexx",
"Poo Bear",
"Pooh Bear",
"POOLCLVB feat. Natalie Conway",
"Pooma",
"Poonyk and Oxide",
"Poor & Rich",
"Pop Cultur",
"POP ETC",
"Pop Evil",
"Pop Maniacs",
"Pop Smoke feat. Nicki Minaj",
"Popa Chubby",
"Popcorn Poppers",
"Popeska",
"Popkings",
"Poppy Ajudha",
"Pops Staples",
"Poptracker feat. Nathan Trent",
"Porcelain Black",
"Porch feat. Oxxxymiron",
"Porchy",
"Porcupine Tree",
"Porsha Nicole",]

p_rus_list_17 = [
"Portair",
"Porter Robinson",
"Portishead",
"Portrayal Of Guilt",
"Portugal. The Man",
"Poshout feat. Aelyn",
"Poshout feat. Ange",
"Position Music",
"Positive Dj's",
"Pospelov",
"Post Malone",
"Postiljonen",
"Postkay",
"Potehin Band",
"PotehinBand",
"Poupon feat. Sam Moffatt",
"Povi",
"Power Francers",
"PowerDress",
"Powerhouse",
"Powerman 5000",
"Powers",
"Powerwolf",
"Pozitive",
"Pr1nce & Влад Лучкин",
"Pra(Killa'Gramm)",
"PRAANA",
"Prada",
"Pradov Ilya Feat. Liza Novikova",
"Praga",
"Praise Cats",
"Prash",
"Prashant Aswani",
"Pravada",
"Praying Mantis",
"Preacher Stone",
"Precious Affliction",
"Precursor",
"Preditah",
"Preety Girl Rock",
"Preme feat. PartyNextDoor",
"Premium-Art vs. Ксю Крузенштерн",
"Preon",
"Presi On & Renate",
"Preslava feat. Costi",
"PressKit feat. Jelle Van Dael",
"PressPlays",
"Pressure Unit feat. Young Sixx",
"Pretenders",
"Pretty Boys From Saint Tropez feat. Kelly Mueller",]

p_rus_list_18 = [
"Pretty Maids",
"Pretty Pink",
"Pretty Slick",
"Prettymuch",
"Priceless feat. Rhema & Bethel",
"Pride",
"Prides",
"Pries",
"Priest",
"Priestess",
"Primal Fear",
"Primal Scream",
"Prime Circle",
"Prime Time",
"Prime X feat. Tara Louise",
"PrimeTime feat. Adamant",
"Primitive",
"Prince & The Revolution",
"Prince Charles",
"Prince feat. Zooey Deschanel",
"Prince Fox",
"Prince Kas & Сквоз",
"Prince Kay One",
"Prince Kaybee feat. Msaki",
"Prince Malik feat. Flo Rida",
"Prince Max Who",
"Prince Paris feat. Castion",
"Prince Ringo",
"Prince Royce",
"Princesa Alba & Alizzz",
"Princess Nokia",
"Princess Sarah",
"Princess X",
"Princip ZM feat. Юра Лайт (GLSS)",
"Pringlez",
"Prinnie",
"Prinsh & Eddie Ferrer feat. Tareq Lopez",
"Printa feat. Чаян Фамали",
"Prinz Amaho",
"Prinz M.",
"Prinz Ramses",
"Prion Heart",
"Priscila Due",
"Prismatic feat. Srey Davy",
"Prismo",
"Prithvi Sai feat. Sabreena Singh",
"Private Tabby",
"Priya Jay",
"Priyanka Chopra",
"PRMGH",]

p_rus_list_19 = [
"Pro-Gress",
"Pro95",
"Problem feat. Chris Brown & Tank",
"Problem feat. Lil Jon",
"Problem Ft. Glasses Malone",
"Problemaddicts",
"ProblemC & Diana Miro",
"Proco Harum",
"Prod. Martinez feat. Manu More",
"Professor Green",
"Professor Kliq",
"Progresia feat. Linnea Schossow",
"Prohorov",
"Project 46",
"Project 91 & Nikos D feat. Nathan Brumley",
"Project B feat. Kelly Rowland",
"Project Blue Sun",
"Project Exile & Distinction",
"Project Fay",
"Project P.",
"Projekt Black",
"Prok & Fitch, Dosem",
"Prolix & Black Sun Empire",
"Promi5e",
"Promise Land",
"Promnite feat. TZAR",
"Prong",
"Pronoza",
"Propellaheadz feat. Mel",
"Propellerheads",
"Prophet G.",
"Propulsive & Qunzie",
"Prosdo",
"PROSEKINA",
"Prospa feat. Ryan Konline",
"Prospectt feat. Akon",
"Prostoupali",
"Prostyle feat. Jason Derulo",
"Protagonista",
"Proteus",
"Proto & Chin Chilla & Midsplit feat. Teodora",
"Proto Bytez",
"Protoculture",
"ProtoHype",
"Protostar",
"Proud Alone feat. Adamant",
"Proven Alive",
"Provenzano",
"Provi feat. Hannah Young",
"Provincial'e",]

p_rus_list_20 = [
"Proyal feat. Ai Takekawa",
"Proyecto FM",
"Proyecto Loco",
"ProZa",
"Prozet",
"PROвокация",
"Pryce feat. Tejai Moore & DJ Smoove",
"Pryda",
"Prygo feat. Fatlum Muqolli",
"Psirico & Pitbull",
"PsoGnar",
"PSY",
"Psyber",
"Psychotic Waltz",
"Psymun",
"Ptashkin",
"Public Art",
"Public Domain",
"Public Passion",
"Puddle Of Mudd",
"Pudra",
"Puerto Madero",
"Puff Daddy",
"Puffy & Euphoria",
"Pulpy",
"Pulse (DiUv, Solopov, Joodey)",
"Pulse & Sphere",
"Pulse feat. Mr.M (Та Сторона)",
"Pulsedriver",
"Pulser",
"Puma feat. Chateau",
"Pumping Guys",
"Punch Cabbie",
"Puncher, Gene Karz",
"Punk Party feat. Kelly Sweet",
"Punk Ska Covers",
"Punkrockerz feat. Carmen & Camille",
"Punky Boys",
"Pupkulies feat. Rebecca",
"Pupo",
"Puppet",
"Pur Mudd",
"Pur:Pur",
"Purasangre",
"Purdy",
"Pure Playaz",
"Pure Poison feat. Polina",
"Pure Pressure",
"Pure Shores",
"Purebeat",]

p_rus_list_21 = [
"Puremusic",
"Puri & Kilate Tesla & Adje feat. Dopebwoy",
"Puri feat. Jhorrmountain & Adje",
"Purity Ring",
"Purple Aura & Chris Willis feat. Akon",
"Purple Haze",
"Purple Project",
"Push Baby",
"Pusha T",
"Pushkarev",
"Pushking",
"Pussy Cat Dolls",
"Pussy Lovers",
"Pussy Riot",
"Pussycat Dolls",
"Pusteblume",
"Pustohod",
"Puya feat. Inna",
"Puza TGK feat. Taya Mala",
"Puzzle",
"PvR",
"PVRIS",
"Pyjama Pack",
"Pyr0",
"Pyramid Scheme",
"Pyramyth",
"Pyrodox feat. Ina",
]

litera = SoundSymbol.objects.get(name="P")

count = 0

for tag in p_rus_list_1:
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
                    new_track = SoundcloudParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, created_at=created_at, description=description, duration=track.duration, genre=genre, title=track.title, uri=track.uri, release_year=track.release_year)
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
                        new_track = SoundcloudParsing.objects.create(id=track.id, tag=self_tag, artwork_url=track.artwork_url, created_at=created_at, description=description, duration=track.duration, genre=genre, title=track.title, uri=track.uri, release_year=track.release_year)
                    count = count + 1
