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

g_rus_list_1 = [
"G & G",
"G Flip",
"G Girls",
"G Malone feat. Demrick & Brooke Taylor",
"G-ash",
"G-Eazy",
"G-Light feat. MarQ Markuz",
"G-Mark",
"G-Nise",
"G-Spliff",
"G-Unit feat. Drake",
"G-Wizard & Joey Kaz vs. Shotgun Cubs",
"G.Adam",
"G.E.N.E.",
"G.R.E.Y.",
"G.R.L.",
"G.S",
"G.Smith",
"G.T.M. Life",
"G's Incorporated",
"G&G",
"G4bby feat. Bazz Boyz & Danny Gee",
"Ga.Ma",
"Gaba",
"Gabbie Hanna",
"Gabbo",
"Gabe",
"GABI",
"Gabib",
"Gabin",
"Gaboo",
"Gaboo, Fran Denia",
"Gabor Deutsch",
"Gabriel & Castellon",
"Gabriel & Dresden",
"Gabriel Antonio",
"Gabriel Davi",
"Gabriel Delgado",
"Gabriel M feat. Tobi Ibitoye",
"Gabriel Marian",
"Gabriel Salgado",
"Gabriel Valim",
"Gabriela Geneva",
"Gabriela Guncikova",
"Gabriela Penn",
"Gabriela Richardson",
"Gabriele Esteriore",
"Gabriella Cilmi",
"Gabriellas",
"Gabrielle",]

g_rus_list_2 = [
"Gabros, Ader",
"Gabros, Valiant Coos",
"Gabry Pontell, Sophia Del Carmen",
"Gabry Ponte feat. Shaggy",
"Gabry Venus",
"Gaby Borromeo",
"Gad Elbaz feat. Alon De Loco",
"Gad Fadget feat. Martin Sola",
"Gadiel feat. Yandel",
"Gael Boom",
"Gafur",
"Gaga",
"Gaia",
"Gaia Cauchi",
"Gaia Project",
"Gail Scott",
"Gainworx",
"Gajendra Verma",
"Gajini feat. Ahimas & А.Воззрени",
"Gal Abutbul",
"Gala",
"Galactic Marvl",
"Galactic Marvl feat. Caroline Vreeland",
"Galantis",
"Galardo",
"Galat",
"Galavanth",
"Gale feat. Laurell",
"Galeja",
"Galena",
"Gali",
"Galimatias",
"Galisteo",
"Gallant",
"Gallina",
"Gallya",
"Galstyan",
"Gambino Sound Machine",
"Gambit 13",
"Game feat. Drake",
"Game feat. Kanye West & Common",
"Game feat. Nelly Furtado",
"Game feat. Pharrell & Snoop Dogg",
"Gamma Ray",
"Gamper & Dadoni",
"Gana",
"Gancci",
"Ganesh Del Vescovo",
"Ganga Project",
"GanGuBaS",]

g_rus_list_3 = [
"Gani Anuar feat. Asel Sadakova",
"Ganon & BloodThinnerz",
"Gans Ganses feat. Storied Boy",
"Ganymed",
"Ganz",
"Ganzfeld Effect feat. KYE",
"Garabatto feat. Charlee Muse",
"Garbage",
"Garcia",
"Gardeweg vs. Sanders",
"Gareth Emery",
"Gareth Gates",
"Garik Balayan",
"Garland Jeffreys",
"Garleem",
"Garmiani",
"Garou",
"Garrido",
"Garry B",
"Garry Morrison",
"Garry Noon",
"Garry Ocean & Katt Rose",
"Garuda",
"Gary Barlow",
"Gary Barlow & Elton John",
"Gary Beck",
"Gary Brooken",
"Gary Caos",
"Gary Clark Jr.",
"Gary Hoey",
"Gary Jules",
"Gary Maguire",
"Gary Moore",
"Gary O'Shaughnessy",
"Gary Schocker",
"Gascar",
"GASHI",
"Gasoline Outlaws",
"Gass Krup",
"Gaston Zani",
"GasTroлеR",
"Gathania",
"Gathier",
"Gato Barbieri",
"Gattaka",
"Gatto Gabriel",
"Gattuso",
"Gaudi",
"Gaullin",
"Gaute Ormase feat. Александр Рыбак",]

g_rus_list_4 = [
"GauTi feat. DIESTO",
"Gavin DeGraw",
"Gavin Haley",
"Gavin Haley & Ella Vos",
"Gavin James",
"Gavin Luke",
"Gavin Moss & Yall feat. Dalvin",
"GAWP",
"Gayana",
"Gayle San",
"Gaysin",
"Gaz & Dmitriy Rs",
"Gaz feat. DJ Geny Tur & Techno Projec",
"Gaz feat. Mike Temoff",
"Gazan",
"Gazebo",
"Gazelle",
"Gazi Demirel",
"Gazo",
"Gazzo",
"Gb & Max Marani",
"Gecko feat. Samba Man",
"Gee Road",
"Geek & Zookeepers",
"Geek feat. Taylor Jones",
"Geelena",
"Geeno Fabulous",
"Geeno Smith",
"Geezer",
"Geir Ronning",
"Geirmund",
"Geko feat. French Montana & Ay Em",
"Gektor Tvist",
"Gelab",
"Gelka",
"GEM",
"Gemini",
"Gemini Club",
"Gemini feat. Fabienne",
"Gena VITER feat. Полиграф ШарикOFF",
"Gene Karz",
"Gene Vincent",
"Gene Wilder",
"Gene Xander",
"Genealogy",
"GENER8ION & Tayla Parx",
"General Base",
"General Levy",
"General Rest In Peace",
"General Tosh",]

g_rus_list_5 = [
"General Wooky",
"Generation Moombahton",
"Generationals",
"Generik",
"Genesis",
"Genetikk",
"Geneva",
"Genevieve Somers",
"Genial",
"Genimi",
"Genio & Baby Johnn feat. Nengo Flow",
"Genius Force",
"Genix",
"Gent & Ardian Bujupi",
"Genta Ismajli",
"Gente De Zona",
"Gentleman",
"Gentleman feat. Sean Paul",
"Gentlemen's Blues Club",
"Gentry Bronson",
"Genuine Brothers",
"Geo Da Silva",
"Geo Louis",
"Geo Raphael & Adena",
"Geo Raphael feat. Adena",
"Geo Tribe",
"Geodesium",
"Geoff Achison",
"Geom",
"Geomax feat. Dakky",
"Geordie Piseri-Diaz",
"George Aaron",
"George Acosta",
"George Benson",
"George Castratos",
"George Davidson",
"George Dekker",
"George Dyer Band",
"George Ezra",
"George Fetcher",
"George Fitzgerald feat. Boxed In",
"George Frideric Handel",
"George Harrison",
"George Hora",
"George Hora feat. Puya",
"George Howard",
"George K feat. Tonia Kar",
"George Kwali feat. Lonestate",
"George Lee & The Rudies",
"George Maple",]

g_rus_list_6 = [
"George Michael",
"George Michelle & Separate Ways",
"George Privatti, Guille Placencia, Mario Biani",
"George Royal",
"George Sava feat. Christen Kwame",
"George Saxon",
"George Skaroulis",
"George Taylor",
"George Thomas",
"George Thorogood",
"George Von Liger",
"George Winston",
"George Wonder",
"Georgel feat. Kat Dahlia",
"Georgi Jacobs",
"Georgia Denton",
"Georgia Holt feat. Cher",
"Georgia Ku",
"Georgia Mos & Alex Pizzuti",
"Georgia Reign feat. Chris Brown",
"Georgio Schultz, Steven Quarre",
"Georgio Star & Levy Pro",
"Georgios Antoniadis",
"Georgios Michailidis",
"Georgius",
"Georgy Om",
"Georgya",
"Gera Je",
"Gerald Albright",
"Gerard Exposito",
"Gerard Way",
"Geri Halliwell",
"GeRich & Cool Project feat. Asie",
"Gerina",
"Gerli Padar",
"Germante Kinderyte",
"Gerome feat. Pamela Baz",
"Geron Hoy",
"GerP feat. Vladislove Gaydovsky",
"Gerrit Van Der Meer",
"Gerry Gonza",
"Gerry Mulligan",
"Gert Wilden",
"Gery-Nikol",
"Gesaffelstein",
"Gesek",
"Gesso feat. Maya",
"Gestort Aber Geil",
"Gesualdi & Pablo Capeto",
"Get Far",]

g_rus_list_7 = [
"Geta Burlacu",
"Getsby",
"Getter",
"GFDM & MD Electro feat. Neonheart",
"GG Magree",
"Ghaderi & Ikus",
"Ghali",
"Ghastly & Mija feat. Lil Jon",
"Ghastly",
"Ghetts feat. Nelly Furtado",
"GHG",
"Ghita",
"Ghost",
"Ghost Beach",
"Ghost Masta & Som (Ginex)",
"Ghost Stars feat. Sam Trock",
"Ghost Town",
"Ghosthouse",
"Ghostkick feat. Jeanie",
"Ghosts Of August",
"Ghosts Of Paraguay feat. Aidan Dullaghan",
"Gia Woods",
"Giabiconi",
"Giacca & Flores",
"Gian Nobilee",
"Giana Factory",
"Gianluca Bezzina",
"Gianluca Fanteria",
"Gianluca Maccarrone",
"Gianluca Vacchi",
"GiAnna",
"Gianni Blu",
"Gianni Don Carlo feat. RAiK",
"Gianni Kosta",
"Gianni Romano",
"Giannis Karagiannis",
"Giannis Moraitis feat. Polina",
"Gianpiero Ibiza feat. Luis Navarro",
"Giants",
"Gibo",
"Gidayyat",
"Gidge",
"Gierto",
"Giga Dance feat. Morano",
"Gigi Barocco feat. Whiskey Pete",
"Gigi D'agostino",
"Gigi D'agoustino",
"Gigi De Martino",
"Gigi Fuscaldo feat. Buttiny",
"Gigi Fuscaldo feat. Mr. Papi Ramos",]

g_rus_list_8 = [
"Gigi Lav & Simon J Bergher",
"Gigolo's At Work",
"Giiants",
"Gil Glaze",
"Gil Sanders",
"Gil Ventura",
"Gilbere Forte",
"Gilbert Becaud",
"Gili Brown",
"Gill Bondy",
"Gill Chang & Danni Carra",
"Gilla",
"Gillepsy",
"Gilles Luka Feat. Нюша",
"Gilli & Branco",
"Gillian Gordon",
"Gilo & Trvpers",
"Gilotina",
"Gimbal & Sinan",
"Gimmy Weaver feat. Tony T.",
"Gims",
"Gin Wigmore feat. Suffa & Logic",
"Gina Dirawi",
"Gina G",
"Gina Kushka",
"Gina Lee feat. Vinny Chase",
"Gina Sicilia",
"Gina Star",
"Gina T",
"Ginette Claudette",
"Ginger Ninja",
"GingerAle",
"Ginny Blackmore & Stan Walker",
"Gino",
"Gino Binelli",
"Gino D'auri",
"Gino G",
"Gino Manzotti feat. Damon",
"Gino Soccio",
"Gino Vannelli",
"Gintoos",
"Ginuwine",
"Gio Bartia",
"Gio Di",
"Gio Nailati",
"Gioacchino Rossini",
"Giodanew feat. Moona & Delirio",
"Gioli & Assia",
"Giona Guidi & Fabrizio Piccinno feat. Lu Tony Man & DJ Roma",
"Gionny Scandal",]

g_rus_list_9 = [
"Giorgia & Alicia Keys",
"Giorgia & Olly Murs",
"Giorgio Moroder",
"Giorgio Prezioso",
"Giorgio Sainz",
"Giorgos Alkeos & Friends",
"Giorgos Giannias",
"Giorgos Mazonakis",
"Giorgos Tsalikis & Rec",
"Giorno",
"Giovani",
"Giovanni",
"Giovanni Allevi",
"Giovanni Marradi",
"Gipp feat. Cee-Lo Green",
"Gipsy Casual",
"Gipsy King (Три Кита, ЦАО)",
"Gipsy Kings",
"Gipsy.cz",
"Girl Radical",
"Girl's Can't Catch",
"Girl's Day",
"Girli",
"Girlicious",
"Girls Aloud",
"Girls Generation",
"Girls Love DJs",
"Girls' Generation",
"Gisele & Bob Sinclar",
"Git Fresh",
"Giu Vela, Cerato",
"Giulia",
"Giulia Be",
"Giulia Y Los Tellarini",
"Giulianna",
"Giuliano Rascan feat. Nic Joseph & Chris Lee",
"Giulietta",
"Giulio Silvestris",
"Giuseppe Bottone",
"Giuseppe del Monaco",
"Giuseppe Francaviglia",
"Giuseppe Giofre",
"Giuseppe Morelli feat. Nik",
"Giuseppe Ottavian feat. Jennifer Rene",
"Giuseppe Ottaviani",
"Giuseppe Ottaviani feat. Tim Hilberts",
"Giuseppe Parisi feat. David Broderick",
"Giusy Ferreri",]

g_rus_list_10 = [
"Giwmik",
"Giyo",
"GJan",
"Gjoko Taneski",
"GK",
"GL",
"Glaceo",
"Glaceo feat. Eliine",
"Glad You Came",
"Glades",
"Gladushevskyy & Новые Интеллигенты",
"Gladyshev",
"GLAED",
"Glam Girls",
"Glamour",
"Glamrock Brothers",
"Glance feat. Mandinga",
"Glashka",
"GLASLYN",
"Glasperlenspiel",
"Glass Petals",
"Glasses Malone feat. Kirko Bangz & The Game",
"Glaucoma",
"Glaukor & DJ Bovoli feat. Gianluca Conca",
"Glaza",
"Glazur",
"GLDN & Astra feat. Jonny Rose",
"Glee Cast",
"Glen Adams & The Hippy Boys",
"Glen Brown",
"Glen Miller",
"Glen Miller Orchestra",
"Glen Vella",
"Glen Walker",
"Glen Washington",
"Glendon Smith",
"Glenn Hughes",
"Glenn Morrison",
"Glenn Tipton",
"Glennis Grace",
"Gli Autogol & Papu Gomez",
"Glitter",
"Glitterboys",
"GLN",
"GLNNA",
"Global Deejays",
"Global Dj",
"Global Kryner",
"Gloomball",
"Gloria Estefan",]

g_rus_list_11 = [
"Gloria Gaynor",
"Gloria Groove",
"Gloria Jones",
"Gloria Trevi",
"Gloriana",
"Glorious Inc",
"Gloryland",
"Glova feat. Edny",
"Glovecats feat. Jay Jacob",
"Gloves Off",
"Glovibes feat. Paul K",
"Glow",
"Glowal",
"Glowie",
"Glowinthedark",
"GLXY",
"GLXY feat. Zero T & Solah",
"GLZ (Галяцэнаген)",
"Gnarly World feat. Flo Rida",
"Gnash",
"Gnothi Seauton",
"GNR",
"GNTLS feat. Russell Ray",
"Go Go Berlin",
"Go Green",
"Go Radio",
"GO!",
"Go.nA",
"GO9",
"Goa & TRUEтень",
"Goapele feat. Snoop Dogg",
"Goar Avetisyan",
"Goartur",
"Goblin",
"Goblin-X",
"Goblins From Mars",
"God Bless The Monkey Astronaut",
"God Is An Astronaut",
"Goddard",
"Goddess Andreea",
"Godfather of Harlem feat. Cruel Youth",
"Godlands & BOI",
"Godlike Music Port",
"Godsmack",
"Godunova",
"GoGo Morrow",
"Gogol Bordello",
"Going Deeper",
"Gokhan Sivri",
"Gold 1",]

g_rus_list_12 = [
"Gold Fields",
"Gold Fir",
"Gold Line & Safira. K",
"Gold Lounge",
"Gold Roger",
"Gold Star",
"Gold/Shade feat. Juliette Claire",
"Gold1",
"Golden Coast",
"Golden Crew",
"Golden Echoes",
"Golden Features feat. Thelma Plum",
"Golden Vessel feat. Emerson Leif",
"GoldFish",
"Goldfrapp",
"Goldhand feat. Goldsound",
"Goldhouse",
"Goldilox",
"Goldroom",
"Goldroom feat. George Maple",
"Goldsound",
"Goldtripp",
"Goldwash",
"Gomad! & Monster feat. Matt Rose",
"Goman",
"GOMZ",
"Gon Haziri feat. Luar",
"GonSu",
"Goo Goo Dolls",
"Good Charlotte",
"Good Lyfe & Vermosa feat. BRKLN",
"Goodbye June",
"Goodcat",
"Gooddiny",
"Goodini",
"Goodluck",
"GoodVibez",
"Goodwill feat. Ron Carroll",
"Goody Grace feat. Blink-182",
"Googoosha",
"Goombay Dance Band",
"Goondocks Project",
"GOOROO",
"Goose Bumps & Squib",
"Gooty One",
"Goran Karan",
"Gorchitza",
"Gord Bamford",
"Gordi",
"Gordon & Doyle",]

g_rus_list_13 = [
"Gordon Burn",
"Gordon Geco",
"Gore",
"Gorgon City",
"Gorilla Zoe feat. Flo-Rida & Afrojack",
"Gorillaz",
"Gorkiz",
"Gorky Park",
"Gorm Sorensen",
"Gorovoy Sasha Music",
"Gosh Crach feat. Kir Angels",
"Goshanskiy",
"Gospod",
"Gosselt feat. Robin Vane",
"Gostan",
"Gotan Project",
"Gotay feat. Daddy Yankee",
"Gotthard",
"Gottlieb",
"Gotye",
"Gouryella",
"Government Band",
"Govinda",
"Govor",
"Graal",
"Grabbitz",
"Grabbitz & Swagglerock",
"Grace Carter",
"Grace feat. G-Eazy",
"Grace Gracie feat. Bre",
"Grace Hughes",
"Grace Mesa",
"Grace Mitchell",
"Grace Savage",
"Grace VanderWaal",
"Grace Weber feat. Vic Mensa",
"Gracia Baur",
"Grades",
"Graffiti & Charmani vs. Flo Rida & Tonez",
"Grafix",
"Graham Bell",
"Graham Bonnet",
"Graham Gouldman",
"Graig David",
"Grainne Duffy",
"Gramatik",
"Gran Error feat. Spania '99",
"Grana Louise",
"Grand Garden",
"Grand Plaz",]

g_rus_list_14 = [
"Grandson",
"Grandtheft",
"Grani Reali & Anivar",
"Granity feat. Jo Angel",
"Grant",
"Grant feat. Nevve",
"Grant Lee Phillips",
"Grant Miller",
"Grant Saxena",
"Grant Smillie & Walden feat. Zoe Badwi",
"Grapes Grey",
"Grasu XXL feat. Guess Who",
"Grave Digger",
"Graver",
"Graves & BISHU",
"Gravitonas",
"Gravity",
"Grax",
"Grayson Capps",
"Grazze",
"Great Good Fine OK",
"Great Lake Swimmers",
"Greate White",
"Grechanik",
"Greeicy",
"Green 10",
"Green Day",
"Green Grey",
"Green Ketchup",
"Green Noise",
"Green Sound",
"Green Sun",
"Greenbaum",
"Greench",
"Greenjelin",
"Greer",
"Greg Abek",
"Greg Basso & Theodora",
"Greg Basso ft. Theodora",
"Greg Beattie",
"Greg Cerrone feat. Koko LaRoo",
"Greg Dean feat. Natalie Weiss & Amber Iman",
"Greg Dela",
"Greg Downey",
"Greg feat. Sk1nnydave",
"Greg Gatsby feat. Stef Kalloo & Braveboy",
"Greg Gelis feat. FAB",
"Greg Gold & Hugh Way",
"Greg Koch",
"Greg Marks",]

g_rus_list_15 = [
"Greg Maroney",
"Greg Parys",
"Greg Walker",
"Gregersen",
"Gregg Wright's Left Hook",
"Grego Las",
"Gregoire",
"Gregor Potter",
"Gregor Salto",
"Gregori Klosman",
"Gregorian",
"Gregory Aigersson",
"Gregory Ayuen",
"Gregory Chekhov",
"Gregory Doveman feat. Elle Sandra",
"Gregory Isaacs",
"Gregory Porter",
"Gregory Trejo & Dzasko feat. Zachary MoFat",
"Greice Santo",
"Greta Gray",
"Greta Salome",
"Greta Salome & Jonsi",
"Gretha Ellis & Monkeybeat",
"Grey",
"Greyson Chance",
"Grigory Esayan & Seeya",
"Grilled Flesh Party",
"Grimaldo & Tessa B.",
"Grimass feat. August Alsina",
"Grimes",
"Grimes & I_o",
"Grinnfas",
"Grip",
"Gris",
"Grisha Urgant",
"Grishina",
"Grivanov feat. Michail Rado",
"Grixis feat. Jess Orestano",
"GRiZ",
"Grizfolk",
"Grizzly Bear",
"Grock",
"Grollo-Capitanata",
"Grom",
"Gromee",
"Gronroos & Bravo feat. Chrystal Hart",
"Groove",
"Groovebenderz",
"GrooveBox",
"GrooveBusterz",]

g_rus_list_16 = [
"Groovecult",
"Groover feat. Malo",
"GrooveshakerZ & Whilliam Rise",
"Grooveshifters",
"Groovoriento",
"Gross & Диана Громова",
"Grosu",
"Groundislava feat. Erik Hassle",
"Grover Washington Jr.",
"Groza",
"Groznyi",
"GRRL Pal",
"Grube Hovsepian feat. Tiffany Johnston",
"Grum",
"Gruppa Skryptonite",
"Gruwer",
"Gryffin",
"Grynn",
"Gso-Family",
"GSPR",
"GT feat. Wildfire & Nick Clow",
"GTA",
"GtD",
"Gualbert Teran",
"Guanes",
"Guano Apes",
"Guarana",
"Guard",
"Guaynaa",
"Gubanova",
"Gucci Mane",
"Gue Pequeno",
"Guena LG",
"Guenta K",
"Guenter Haas",
"Guerino",
"Guf",
"Guido Vannes",
"Guild Of Ages",
"Guinevere",
"Guiseppe Ottaviani",
"Guitar Shorty",
"Gulcin Golgem Kilic",
"Gulddreng",
"Guldpige",
"Gulseren",
"Gummy Kid",
"Gums",
"Gunfire",
"Gunplay",]

g_rus_list_17 = [
"Guns N' Roses",
"Gunther",
"Guri Schanke",
"Gurkan Asik feat. Virginia Da Cunha",
"Gurnazar with Groovester",
"Guru Da Beat and Mauro Mondello",
"Guru Groove Foundation",
"Guru Josh",
"Guru Josh Project",
"Guru Project",
"Guru Randhawa feat. Pitbull",
"Gurude",
"GURUDE feat. Ivan KIT",
"Gus Viseur",
"Gushi & Raffunk",
"Gusi feat. Greeicy & Mike Bahia",
"Gustavo Da Silva",
"Gustavo Lima",
"Gustavo Montesano & Royal Phil",
"Gustavo Mota",
"Gustavo Scorpio feat. Junior Hallex",
"Gut1K",
"Gutta Twins feat. Flo Rida",
"Guy Alexander",
"Guy Elberg & Martinna",
"Guy Furious",
"Guy Isaac feat. Nofar Bachar",
"Guy Mitchell",
"Guy Robin feat. Amba Shepherd",
"Guy Scheiman feat. Michal S",
"Guy Sebastian",
"Guy Verlinde",
"Guy'do And DJ Rebel feat M.O.",
"Guyana",
"Guz",
"Gvozdi",
"Gwada & Anuka",
"Gwantinik",
"Gwen McCrae",
"Gwen Stefani",
"Gwev",
"Gyani & Hoop Records feat. Jacob Taylor",
"Gym Class Heroes",
"Gyom",
"Gypsy And The Cat",
"Gyptian",

]

litera = SoundSymbol.objects.get(name="G")

count = 0

for tag in g_rus_list_6:
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
