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

l_rus_list_1 = [
"L (iZReaL) feat. Сиэл",
"L D R U & Boo Seeka",
"L-Bee",
"L-Gance",
"L-Jane",
"L-Side feat. MC Fava",
"L-Stone",
"L. Young",
"L.A.R.5",
"L.A.X feat. Michelle",
"L.B. One",
"L.F.P.",
"L.I.G.A",
"L.K.N",
"L.K.N & Shakh",
"L.O.K.A.! feat. Adassa & Pitbull",
"L.O.O.P",
"L’One",
"L'adour feat. Max'C",
"L'amour",
"L'Aupaire",
"L'Indecis",
"L'One",
"L'Rist & Денис Океан",
"L'Tric",
"L1LSAN",
"La Boca",
"La Bouche",
"La Bouquet",
"La Brasa",
"La Caina",
"La Chica",
"La Chris",
"La Doble M feat. Brujo Master",
"La Esperanza",
"La Familia Loca vs. Gabry Ponte",
"La FLaim feat. Lucky",
"La Fouine feat. T-Pain & Mackenson",
"La Fuente",
"La Kamila",
"La La Land",
"LA LE",
"La Mica",
"La Nacion",
"La Pelopony",
"La Petty",
"LA Riots",
"La Roux",
"La Scala",
"La Toya Jackson",]

l_rus_list_2 = [
"La-Chris feat. Marlon Bertzbach",
"Laam",
"Laanga feat. Kevin Kelly",
"Laava",
"Labeo",
"Labert",
"Labo",
"Labrat",
"Labrinth",
"Labryenco",
"Labyrinth",
"Lacey Schwimmer",
"Lackmus",
"Lacosh feat. Jaybolt",
"Lacrimosa",
"Lacross",
"Lad DJS feat. DVJ Electra",
"LadBaby",
"Ladder",
"Laden",
"LadieS_N feat. СаняDjs",
"Ladislav Bubnar",
"Ladita",
"Lady Antebellum",
"Lady Aya",
"Lady Bee",
"Lady Diana",
"Lady Fantasy",
"Lady Gaga",
"Lady Gi feat. Smoke Of Field Mob",
"Lady Indiraa",
"Lady Ocean",
"Lady Pink Bitch",
"Lady Saw feat. Flo Rida",
"Lady Shake",
"Ladyhawke",
"Ladytron",
"Laera",
"LaFee",
"LaFryz",
"Lagato Shine",
"Lago",
"Lahar",
"Lahox feat. The EKGs",
"Laibert",
"Laid Back",
"Laidback Luke",
"Laika",
"Lais feat. Skizzy Mars",
"Laka",]

l_rus_list_3 = [
"Lake",
"Lake Malawi",
"Lakeside",
"Laksa",
"LaLa Band",
"LaLa by Babes",
"Lala Kent feat. Sean2 Miles & Mowii Elviz",
"Lala Project",
"Lalabo",
"Lalala Gang",
"Laleh",
"Lali",
"Laliko",
"Lalla",
"Lally",
"Lalo Ebratt & Juanes & Skinny Happy feat. Yera & Trapical",
"Lalo Project",
"Lama",
"Lamar",
"Lamborghini",
"Lambrino",
"Lamer",
"Lamore",
"Lan Sander, No Hope, George Nassau",
"Lana B",
"Lana B & Efiel",
"Lana Del Ray",
"Lana Kenoby feat. Aliyana",
"Lana Tigrana",
"Lanar",
"Lance & Linton",
"Lance Bass & Anise",
"Landis",
"Landon Austin",
"Landon Pigg",
"Lane 8",
"Lanfranchi & Farina",
"Lang & Yep feat. Manon Polare",
"Lange",
"Langston Francis",
"Laniakea",
"Lanks",
"Lanna feat. Tima Dee",
"Lano",
"Lansdowne",
"Lanskoy & Co.",
"Lany",
"Lao Ra",
"Laoise",
"Laola",]

l_rus_list_4 = [
"Lapalux feat. Szjerdene",
"Lapsley",
"Lara & Reyes",
"Lara Fabian",
"Lara Lee & Gabriel",
"Lara Loft",
"Lara Mocco & DJ Raulio",
"Lara Moco",
"Lara Rai",
"Lara Williams",
"Larcy",
"Lariss",
"Larkin Poe",
"LaRoxx Project",
"Larry Coryell",
"Larry Garner",
"Larry Miller",
"Larry Mor",
"Larry Rocca feat. Tanya Michelle",
"Larry Tee feat. Charlie Le Mindu",
"Lars Eric Mattsson",
"Lars Kischkel feat. Vicky",
"Lars Palmas vs. DJ Serenity",
"Lars Vaular & Royksopp",
"Larson",
"Lartiste",
"Laruzo feat. Ardian Bujupi",
"Laruzo feat. Moe Phoenix",
"Lary Over & El Micha",
"Las Aves",
"Las Ketchup",
"Las Ramblas",
"Las Salinas",
"Las Villa",
"LaScala",
"Laselva",
"Laserdance",
"Laserjakk & L.O.O.P",
"Lasgo",
"Lasha & Lasha",
"Lasse",
"Last Autumn's Dream",
"Last Memorial Day",
"Last Midnight Train",
"Last Night",
"LastEDEN",
"Lastep feat. Jex",
"Lastlings",
"Laszlo",
"Late June",]

l_rus_list_5 = [
"Late Night Alumni",
"Latif",
"Latinas feat. Noel Pastor",
"Latino Kreyol feat. Kenza Farah & Soldat Jahman & Luis Guisao",
"Lattos & Riema",
"Lau El Flakito",
"LAUD",
"Lauer",
"Lauge",
"Laura & Lovers",
"Laura Baitoiu",
"Laura Branigan",
"Laura Broad feat. Chris Brown",
"Laura Grig",
"Laura LaRue",
"Laura Lee",
"Laura Lowen",
"Laura Marano",
"Laura Mvula",
"Laura Nox",
"Laura Pausini",
"Laura Pergolizzi",
"Laura Rizzotto",
"Laura Rosca feat. Makru",
"Laura Roy",
"Laura Sullivan",
"Laura Tesoro",
"Laura Vital",
"Laura Voutilainen",
"Laura Welsh",
"Laura White",
"Laurel Zucker & Mark Delpriora",
"Lauren Alaina",
"Lauren Aquilina",
"Lauren Ashleigh",
"Lauren Bennett",
"Lauren Christy",
"Lauren Daigle",
"Lauren Evans",
"Lauren Jauregui",
"Lauren Mann",
"Lauren Mayhew",
"Lauren Rose, Andy S & Raffaell",
"Laurence Olivier",
"Laurent H",
"Laurent Pepper feat. I-V",
"Laurent Sleyter feat. Mad",
"Laurent Veix",
"Laurent Wery",
"Laurent Wolf",]

l_rus_list_6 = [
"Laurentiu Duta",
"Laurentius feat. Hannah Young",
"Laurenzo Davids",
"Laurenzo Tozzi",
"Laurette feat. Balkan",
"Lauriana Mae",
"Laurie Burgess & Roy Merchant",
"Laurieann Gibson",
"Lauryn Hill",
"Lauta",
"Lautner",
"Lauv",
"Lava",
"Laville",
"Lavinia",
"Lavinia Meijer",
"Lavinia Simene",
"Lavrov & Аниса Муртаева",
"Lawrence Lebo",
"Lawrence Taylor",
"Lawson",
"LAXX & Snails",
"LAYAH",
"Layke feat. Snoop Dogg",
"Layton Greene",
"Layzee & Moscow Club Bangaz",
"LaZ (Та Сторона)",
"Laza Morgan feat. Shaggy",
"Lazard",
"Lazee",
"Lazy G vs. Nicco",
"Lazy Hammock",
"Lazy J feat. Faydee",
"Lazy Rich",
"Lazy Weekends",
"Lblvnc & Riell",
"LCA",
"LCAW",
"LDNC feat. Mohombi & Mista Silva",
"Le Bleu",
"Le Boeuf feat. Salvo",
"Le Castle Vania & Addison",
"Le Click",
"Le Flex",
"Le Jac feat. Andrea Weir",
"Le Kid",
"Le Lion",
"Le Malls feat. Imogen Mahdavi",
"Le P",
"Le Park",]

l_rus_list_7 = [
"Le Rock feat. RoxS",
"Le Roy",
"le Shuuk",
"Le Son Du Placard",
"Le Tigre",
"Le Vernissage",
"Le Vin",
"Le Voyage",
"Le Youth",
"Le.To",
"Lea Castel",
"Lea Luna",
"Lea Makhoul",
"Lea Michele",
"Lea Rue",
"Lea Santee",
"Lea Sirk",
"Lead & Christian Stalker",
"Leaf",
"Leah McFall",
"Leaking Shell",
"Leandro Da Silva",
"Leann Rimes",
"Leather Corduruys feat. Chance The Rapper",
"Lecrae",
"Led & Nash",
"Led Zeppelin",
"Ledina Celo",
"Ledisi",
"Lee Baker & The Agitators",
"Lee Brice",
"Lee Carr",
"Lee Charm",
"Lee Dewyze",
"Lee Foss",
"Lee Harvey",
"Lee Haslam",
"Lee Hi feat. B.I",
"Lee Ji Soo",
"Lee Jin Wook",
"Lee Marrow",
"Lee More",
"Lee Osborne",
"Lee Walker vs. DJ Deeon feat. Katy B",
"Leea",
"Leechy Alexej",
"Leela James",
"Leelee",
"Leenad",
"Leeson Bryce feat. Akon",]

l_rus_list_8 = [
"Leeya",
"Leeyou & Danceey feat. Philippe Heithier",
"Leeza B.",
"Lefa feat. Vald",
"Lefay",
"Lefthand Freddy & The Aces",
"LEGA",
"Legato",
"Legend Da Beatslaya Ft. Chalice Serrano",
"Legend Of The Seagullmen",
"LeGo (Digital Squad) & TRUEтень",
"LegoTanko & Такер",
"Leigh Bush",
"Leighton Meester",
"Leikeli47",
"Leila feat. Charlie Brown",
"Lekko & B-Dis feat. Fran Martin",
"Lel'Mezh",
"LELA",
"Leland",
"LELAY",
"Lele",
"Lele Pons",
"Lem",
"Lema & Shafer feat. Roxanne Emery",
"Lema feat. Christina Novelli",
"Lemaitre",
"Lemar",
"LeMarvin",
"Lemay feat. Krime Fyter",
"Lemex",
"Lemon & Einar K feat. Paul Johannessen",
"Lemon Party People",
"Lemonade Mauser",
"Lemonia",
"Lena & Nico Santos",
"Lena Cortes",
"Lena feat. Kat Vinter & Little Simz",
"Lena Horne",
"Lena Katina",
"Lena Katina feat. Ni Ego",
"Lena Kaufman feat. Ada",
"Lena Khann feat. TAG",
"Lena Meyer-Landrut",
"Lena Papadopoulou",
"Lena Philipsson",
"Lenachka",
"Lenadi",
"Lenar",
"Lene Marlin",]

l_rus_list_9 = [
"Lenii",
"Lennard Elliot, Victory & Polgrand",
"Lenni",
"Lenno",
"Lennon Stella",
"Lenny B feat. Roxxett",
"Lenny Fontana",
"Lenny Kravitz",
"LennyGM & Medina",
"Lenx & Denx",
"Lenzman feat. DRS",
"Leo (Of Nemesis)",
"Leo Anderson",
"Leo Delibes",
"Leo Effe DJ feat. Naima",
"Leo feat. Pitbull",
"Leo Kalyan",
"Leo Kaylan",
"Leo Kottke",
"Leo Lycra",
"Leo Mantis",
"Leo Salom",
"Leo Sayer",
"Leo Stannard",
"Leo Stannard feat. Chiara Galiazzo",
"Leo.K feat. TaLila",
"Leon Bolier",
"Leon Bridges",
"Leon Brook feat. OMZ",
"Leon Brooks",
"Leon Else",
"Leon Grant",
"Leon Libre",
"Leon Lour",
"Leon Reverse",
"Leon S & Carlo Sanchez",
"Leon Sash",
"Leon Thomas feat. Wiz Khalifa",
"Leona Avrelina",
"Leona Dios",
"Leona Griffin",
"Leona Lewis",
"Leonail",
"Leonard Cohen",
"Leonardo Bortolotto",
"Leonardo Nioi",
"LeoNia",
"Leonid Orlov",
"Leonid Rudenko",
"Leonor Andrade",]

l_rus_list_10 = [
"Leony!",
"Leowz & Shivers",
"Lera Bueno feat. Rezak (All Native)",
"Lera feat. Folkbeat",
"Lera Kafer",
"Lera Lynn",
"Lerica & Belinda",
"Lerica & Juan Magan",
"Lerica, Gente De Zona, Leslie Shaw",
"Lerocque feat. Carmen Bieri",
"Leroy Sanchez",
"Leroy Styles",
"Les Elephants Bizzares",
"Les Fatals Picards",
"Les Jumo feat. Lena Cortes",
"Les Mc Keown",
"Les McCann",
"Les McKeown",
"Les Paul",
"Lesandro & Lorado",
"Leshakenny feat. Laz (Та Сторона)",
"Lesiem",
"Lesley Gore",
"Leslie & B-Sensual",
"Leslie Clio",
"Leslie Grace",
"Leslie West",
"Less Affair",
"LestatMC feat. S.O.L.J.",
"Lester Lewis",
"Let's Go Project",
"Let's Pretend",
"Lethal Bizzle",
"Lethal Injektion",
"Lethoscorpia feat. Gabrielle",
"Leticia feat. Lisa",
"Leticia Sabater",
"Letizia Romeo",
"LeTo",
"LeToya Luckett",
"Lets Be Friends",
"Letticia",
"Letto",
"Leuchtturm Inkl. Sandberg",
"Lev Santiago feat. Женя F!Nt",
"LevaN BRauN",
"Levan J",
"Levandis",
"Levante",
"LevelUp",]

l_rus_list_11 = [
"Levent",
"Leventina",
"Levi",
"Levianth",
"Leviathan",
"Levina",
"Levon Morozov",
"Levon, Лэм, Luko, Life MC КП, Саша Маст",
"Lew Jetton",
"LeWean feat. Петр Неман",
"Lewis Blissett",
"Lewis Capaldi",
"Lewis Hamilton & The Boogie Brothers",
"Lewis Player feat. Dan Nash & Mikea",
"Lex Boogie and DJ Stress",
"Lex Van Someren",
"Lexer",
"Lexi Jayde",
"Lexi Strate",
"Lexie Shine",
"Lexter",
"Lexus Brave",
"Lexvaz & JJ Mullor feat. Amrick Channa",
"Lexxmatiq & Inkyz",
"Lexxus",
"Lexxx Andrew",
"Lexy Panterra",
"Leya D.",
"Leya Mouse & DJ Komandor",
"LeyeT",
"LeyMiks feat. KostyaFog",
"LF Project feat. Johnel",
"Lfo Feat. M.O.P.",
"Li He",
"Li Raw",
"Lia Gold",
"Lia Love feat. Chaddi",
"Lia Marie Johnson",
"Liam Cacatian Thomassen",
"Liam Gallagher",
"Liam Keegan",
"Liam Lis feat. Nile Rodgers",
"Liam Payne",
"Liam Wilson",
"Lian Ross",
"Liane V feat. Problem & Mucho Dinero",
"Lianne La Havas",
"Liar Liar",
"Liars",
"Libbi",]

l_rus_list_12 = [
"Libertines",
"Libra",
"Lidia Buble",
"Lidia Isac",
"Lidia Kopania",
"Lido",
"Lidus",
"LIEZA",
"LIF",
"Life Of Dillon",
"Life On Mars",
"Lifehouse",
"Lifelike",
"Lifescapes",
"Liga",
"Ligabue vs. Benny Benassi",
"Light In Color",
"Light The Sky feat. Brooke Williams",
"Light Years Away feat. Jasper R",
"Lighthouse Family",
"Lighthouse X",
"Lightney",
"Lightnin' Hopkins",
"Lights",
"Ligia",
"LIION",
"Lika Morgan",
"Lika Morgan & C-Ro",
"Like A Storm",
"Like Chocolate",
"Like In A Lake",
"Like Mike",
"Like Project Music feat. DJ Aletta",
"Like Son",
"LIKE.A",
"Likhnitsky",
"Likky Li",
"LIL A",
"Lil Aaron feat. Skizzy Mars & Brandon Wardell",
"Lil Baby",
"Lil Bow Wow",
"Lil Candy Brownie",
"Lil Chuckee",
"Lil Debbie",
"Lil Dicky",
"Lil Dik",
"Lil Djek",
"Lil Durk",
"Lil Eddie",
"Lil Jon",]

l_rus_list_13 = [
"Lil Kate",
"Lil Keed",
"Lil Kim",
"Lil Mama",
"lil mont",
"Lil Mosey",
"Lil Nas X",
"Lil Peep",
"Lil Pump",
"Lil Silva",
"Lil Skies",
"Lil Smiley",
"Lil Toe",
"lil Tr33zy feat. A Boogie Wit Da Hoodie",
"Lil Tracy",
"Lil Uzi Vert",
"Lil Wayne",
"Lil Xan",
"Lil Yachty",
"Lil' Kim feat. Kevin Gates",
"Lila & Stitch",
"Lila Downs",
"Lila Drew",
"Lila feat. Fargo",
"Lila feat. Rat City",
"Lila Manila",
"Lilac",
"LiLi & DJ Slon",
"Lili & Susie feat. Diamond Dogs",
"Lilian Garcia",
"Lilika",
"Lilit",
"Liljaf",
"Lilly Ahlberg",
"Lilly Martin",
"Lilly Wood",
"LilTwice feat. Vnuk",
"Lilu Vega",
"Lily & Madeleine",
"Lily Allen",
"Lily Elise",
"Lily Lyon & IMKK",
"Lily Moore",
"Lilya Pravda",
"Lima & Chemerisoff",
"Lima Osta",
"Limahl",
"Limelght",
"Limelight",
"Limma & Andrea",]

l_rus_list_14 = [
"Limma feat. Trik FX",
"Limp Bizkit",
"Lina Estes",
"Lina Hedlund",
"Lina Nox",
"Linas & Simona",
"Lincoln Jesser",
"Linda Bengtzing",
"Linda Eder",
"Linda Jo Rizzo",
"Linda Leen",
"Linda Lind",
"Linda Pritchard",
"Linda Sundblad",
"Linda Wagenmakers",
"Linda Wesley",
"Lindi Ortega",
"Lindita",
"Lindo & Sketchy Bongo",
"Lindon",
"Lindsay Dracass",
"Lindsay Lohan",
"Lindsey Lomis",
"Lindsey Stirling",
"Lindstrom & Christabelle",
"Lineki & Bern feat. In-Grid",
"Linette",
"Linger",
"Liniu",
"Link Wray",
"Linkin Park",
"LINL",
"Linnea",
"Linney",
"Linni Meister",
"LinRey",
"Linsey Alexander",
"Linus S",
"Linus Svenning",
"Linuz",
"Linval Thompson",
"Liohn",
"Lion & Dollhouse",
"Lion Babe",
"Liona Boyd",
"Lione feat. Miranda Glory",
"Lionel Richie",
"Lions Head",
"Lior Narkis",
"Lipless",]

l_rus_list_15 = [
"Liquid Cosmo & Stefano Prada",
"Liquid D",
"Liquid Groove Mojo",
"Liquid Kaos feat. Kirsty Hawkshaw",
"Liquid Liquid",
"Liquid Motion feat Georgia",
"Liquid Spill",
"Liquidfive",
"Lira (Та Сторона)",
"Liranov",
"Liria",
"Lisa Aberer",
"Lisa Ajax",
"Lisa Andreas",
"Lisa Angell",
"Lisa Borud",
"Lisa Bregneager",
"Lisa Lois",
"Lisa Lopes",
"Lisa Lynne",
"Lisa May",
"Lisa Millett",
"Lisa Miskovsky",
"Lisa Pac",
"Lisa Rowe feat. Animal",
"Lisa Stansfield",
"Lisa Viola feat. Shaggy",
"Lisandro Cuxi",
"Lisaya & Hanna Finsen",
"Lise Darly",
"Lisio DJ",
"Lisitsyn",
"LissA",
"Lissa Wassabi",
"Lissat & Paul Jockey",
"Lissat & Voltaxx",
"Lissen2",
"Lissie",
"Listenbee feat. Naz Tokio",
"Lit Killah",
"Lita Ford",
"Litagoria",
"Litany",
"Lite.Ru",
"Literu",
"Litesound",
"Little Big Town",
"Little Blue",
"Little Boots",
"Little Daylight",]

l_rus_list_16 = [
"Little Dragon",
"Little G. Weevil",
"Little Giants",
"Little Green Cars",
"Little Jinder",
"Little Mix",
"Little Roy",
"Little Sea",
"Little Simz",
"Little Tybee",
"LittleKings",
"Liu",
"Liuck & Neev Kennedy",
"LIUFO",
"Liv Dawson",
"Live 2 Love",
"Live Erikson",
"Live Montecarlo",
"Livid",
"Livin R",
"Livin' Blues",
"Living Room",
"Liviu Guta",
"Liviu Hodor",
"Liviu Teodorescu",
"Livvi Franc",
"Livvia",
"Liz Elias feat. Flo Rida",
"Liz feat. Tyga",
"Liz Huett",
"Liz Kay",
"Liz Primo",
"LIZ Project",
"Liza Evans",
"Liza Fox",
"Liza Khegai",
"Liza Owen",
"Lizabeth & Victoria Belova",
"LIZER",
"Lizot",
"Lizz Wright",
"Lizzard",
"Lizzie",
"Lizzo",
"Lizzy Land",
"LKA",
"LKN & Ramil'",
"LKX",
"Ll Cool J",
"Lliam & Latroit",]

l_rus_list_17 = [
"Lliam Taylor & Deflo",
"Lloyd Banks Feat. Styles P",
"Lloyd Charmers & Sir Collins",
"Lloyd Griffiths",
"Lloyd Jones",
"Lloyd Lawrence & Tony T",
"LLP",
"Lly Ocean",
"LMFAO",
"Lndkid",
"LNKAY",
"LNY TNZ feat. Jantine",
"Lo Air & Pure Poison",
"Lo Blanquito",
"LO feat. Aimee",
"Lo feat. B.Sykes",
"Lo Tide",
"Lo-Fi Electronic",
"Lo-Fi-Fnk",
"LO'99",
"Loaded Lux",
"Loadstar",
"Locco Lovers ft. Adrian Rodriguez",
"Loco Escrito",
"Loco Sunshine feat. David Rush & Honorebel",
"LocoDJ",
"Locura",
"Lodato & Pollyanna",
"Lodoss",
"Lodovica Comello",
"Loft",
"Logan Chapman",
"Logan Henderson",
"Logic",
"Logistics",
"Logovibes feat. Shaharah",
"Loic B feat. Mir",
"Loic Nottet",
"Loic Penillo & Matthias Ka & Audrey Valorzi",
"Loick Essien",
"LoKa Up feat. Anthony El Mejor",
"Lokee feat. Pearl Andersson",
"Lokii feat. REMMI",
"LOKO",
"LoL Deejays vs. Minelli & FYI",
"Lola & DJ Piligrim",
"Lola Blanc",
"Lola Coca",
"Lola feat. Ruby",
"Lola Indigo",]

l_rus_list_18 = [
"Lola Marsh",
"LoLa Monroe",
"Lolita Hunters",
"Lolita Jolie",
"Lolita Kox",
"Lollipop",
"Lolo Zouai",
"Lomaticc",
"Lonczinski & Andy Wild feat. Matthew Steeper",
"London 32",
"London Boys",
"London Elektricity",
"London Grammar",
"London On Da Track x G-Eazy feat. City Girls & Juvenile",
"London Philharmonic Orchestra And Andrew Skeet",
"London Topaz feat. Emma Whines",
"London32",
"LOne",
"Lonely Boy",
"Lonely The Brave",
"LoneMoon",
"Long & Harris",
"Long & Harris feat. Envy Monroe",
"Long Lost Sun",
"Longview",
"Lonnie Broocks",
"Lonnie Brooks",
"Lonny Bereal feat. Kelly Rowland",
"Lonya",
"Loojan feat. Brosste Moor",
"Look Blue Go Purple",
"Lookas",
"Lookinich",
"Loona",
"LOOP",
"Loopers",
"Loosid",
"Loote",
"Lora Lea",
"Lora Superfin",
"Lord Kossity",
"Lord Siva & Vera",
"Lord Swan3x",
"Lorde",
"Lordi",
"Lore",
"Lorean feat. Uncle Po",
"Loredana & Deepcentral",
"Loredana & Mozzik",
"Loredana Berte",]

l_rus_list_19 = [
"Loreen & Elliphant",
"Lorejay vs. DJ Stress feat. Fargo",
"Loren feat. The Limba",
"Loren Gray",
"Loren North",
"Lorena Simpson",
"Lorenz Koin feat. Norah B.",
"Lorenzo Al Dino",
"Lorenzo Asher",
"Lorenzo feat. Shy'm",
"Lorenzo Fragola",
"Lorenzo Rossi",
"Lorenzo Spano feat. Liz Hill",
"Loretta Kohl",
"Lori! Lori!",
"Lorina",
"Loris Pionieri feat. Raisa",
"Lorna feat. Shorty & Cuban Deejays",
"Lorri. B",
"Los Angeles",
"Los Canos",
"Los Chicos",
"Los Del Rio",
"Los feat. Diddy & Ludacris",
"Los Gitanos",
"Los Lobos",
"Los Mag",
"Los Orishas",
"Los Padres",
"Los Paraguayos",
"Loskin feat. Sevenever",
"Lossgo",
"Lost Capital & Pillows",
"Lost Frequencies",
"Lost In Separation",
"Lost Island feat. Laivin",
"Lost Kings",
"Lost Knights feat. Kiki",
"Lost Sky feat. JEX",
"Lost Stories",
"Lost Witness",
"Lostboycrow",
"Lostly",
"Lotic",
"Lotus",
"Lou Bega",
"Lou Reed",
"Lou Stone",
"Lou Van, Vijay & Sofia Zlatko",
"Louane",]

l_rus_list_20 = [
"Loud Bit",
"Loud Control",
"Loud Luxury",
"Loud Project feat. Phelipe",
"Louder",
"Louis Armstrong",
"Louis B feat. DJ Luke Nasty",
"Louis Bailar",
"Louis Futon feat. ROZES",
"Louis Hayes",
"Louis La Roche",
"Louis Richardet",
"Louis The Child",
"Louis Tomlinson",
"Louis Vivet feat. Mister Blonde",
"Louisa Baileche",
"Louisa Johnson",
"Louisa Johnson feat. 2 Chainz",
"Louise",
"Louise Hoffner",
"Louise Lula",
"Louka",
"Loukas Giorkas feat. Stereo Mike",
"Louna",
"Lounge Café, Chillout Lounge, Bossa Nova",
"Loungeotic",
"Louw feat. Mun",
"Love & The Outcome",
"Love 4 Sale",
"Love Dominique",
"Love Fame Tragedy",
"Love Generation",
"Love Harder feat. Amber Van Day",
"Love Injection",
"Love Is Colder Than Death",
"Love Message",
"LOVE SICK",
"Love Stallion",
"Love System",
"Love Unit feat. Carlprit",
"Lovebugs",
"Lovecards",
"Lovely",
"Lovely Girl",
"Loverush",
"Lovespeed",
"Lovestarrs",
"Lovewoodmusic",
"Lovex",
"Lovey James",]

l_rus_list_21 = [
"Loveyourself Gang feat. Anna Lesiv",
"Loviloveis & T1One",
"Loving Arms",
"LOVRA",
"Low Noise",
"Low Pros feat. Que",
"Low Steppa",
"Low Voltage",
"Lowcash",
"Lowell feat. Icona Pop",
"LowKey & Kardinal",
"LowKicks",
"LowLeX",
"Lowlife",
"LOYAL",
"Loyz",
"LP feat. Chris Loco",
"LRIST",
"Ls.Den и Bahh Tee",
"LS2",
"LSB",
"LSB feat. Sophia Wardman",
"LSD (Labrinth, Sia, Diplo)",
"LSpeed Deejay feat. Andrea Morph",
"LT United",
"LTN",
"Lu Guessa feat. Filipe Guerra",
"Lu.Re",
"LU2VYK",
"Lu40",
"Luana Vjollca feat. Faydee",
"Luc Meyer feat. Alex Gewehr",
"Luca Benni",
"Luca Bertoni",
"Luca Carboni",
"Luca Dayz feat. DJ SQ, West Crav & EOS",
"Luca De Angelis",
"Luca De Maas",
"Luca Debonaire",
"Luca Donzelli",
"Luca Fioretti",
"Luca Guerrieri",
"Luca Haenni & Christopher S",
"Luca Hanni",
"Luca Marchese",
"Luca Noise feat. Luca Zeta",
"Luca Perra",
"Luca Pirazzi",
"Luca Schreiner",
"Luca Tarantino",]

l_rus_list_22 = [
"Luca Zeta & Sander",
"Lucas & Steve",
"Lucas Blades",
"Lucas Estrada",
"Lucas Grabeel",
"Lucas Maverick feat. MNEK & Sinead Harnett",
"Lucas Nord",
"Lucaveros",
"Lucenzo",
"Luchian Cris",
"Lucia Micarelli",
"Lucia Nadal",
"Lucia Perez",
"Lucian Base",
"Lucian Colareza",
"Lucian Elgi feat. Dezy",
"Lucian feat. Jordan Corey",
"Lucian feat. Remmi",
"Lucian Walker ft. Jeffree Star",
"Luciana ft. Will Sparks",
"Luciano Pavarotti",
"Luciano Supervielle",
"Luciano Vargas feat. Viktor",
"Lucid Blue",
"Lucid Green",
"Lucie Azard feat. Nick O",
"Lucie Jones",
"Lucien & A.R.D.I.",
"Lucio and Nicky",
"Lucio and Niky",
"Lucio Dalla",
"Lucius Blue",
"Lucky Charmes",
"Lucky Date",
"Lucky Daye feat. Ty Dolla Sign & Wale",
"Lucky Garcia feat. Jany Mc Honey",
"Lucky Luke",
"Lucky Man Project",
"Lucky Peterson",
"Lucky Rose",
"Lucky4",
"LuckyDee",
"Lucq & The Durands feat. Noubya",
"Lucy Hale",
"Lucy In Disguise feat. Laura Claire",
"Lucy Iris",
"Lucy Love",
"Lucy Lu",
"Lucy Rose",
"Ludacris",]

l_rus_list_23 = [
"Ludomir feat. Josef Johansson",
"Ludovic Beier",
"Ludovico Einaudi",
"Ludovika feat. Camille Jones",
"Ludvigsson & Jorm",
"Ludwig London",
"Ludwig Van Beethoven",
"Luel Project",
"Luengo & Diaz",
"Luh Kel",
"Lui Mкme",
"Luigi 21 Plus & J Balvin",
"Luigi Lusini",
"Luigi Masi",
"Luigi Peretti",
"Luigi Pilo",
"Luigi Rocca",
"Luigi Tozzi",
"Luiku",
"Luina",
"Luina feat. Mito",
"Luis A. Moreno",
"Luis Fonsi",
"Luis Hermandez",
"Luis Lopez feat. Adena",
"Luis Quezada",
"Luis Rodriguez",
"Luis Vazquez feat. Adrian Milena",
"Luis Villegas",
"Luisa",
"Luix Spectrum",
"Luixmi",
"Luiz Ejlli",
"Lujipeka",
"Luka Caro pres. Midnight",
"Luka Caro x Rave & Crave",
"Luka J Master feat. Giulia I & Shark",
"Lukas Graham",
"Lukas Leon",
"Lukas Mayer",
"Lukas Termena",
"Lukas Wieteszka",
"Luke Anders feat. Liel Kolet",
"Luke Bingham feat. Sway",
"Luke Bond",
"Luke Bryan",
"Luke Chable",
"Luke Combs",
"Luke Cusato",
"Luke Evans",]

l_rus_list_24 = [
"Luke Friend",
"Luke Hassan",
"Luke Howard",
"Luke James",
"Luke K feat. Tony T & Acero MC",
"Luke Million & Asta",
"Luke Shayer",
"Luke Silver",
"Luke Sital-Singh",
"Luke ST feat. Murke",
"Luke Terry",
"Luke Warner & Dreamy",
"Lukino Simjay feat. Joy Jackson",
"LuKone & deMoga feat. Liviu Teodorescu",
"Lulleaux",
"Lulu James",
"Lulu Rouge feat. Fanney Osk",
"LUM!X & Gabry Ponte",
"Lumberjack",
"Lume",
"Lumen",
"Lumi",
"Lumia Brothers",
"Lumidee",
"Luminate",
"Luminita Anghel",
"Luminize",
"Lumira",
"Lumisade",
"Luna",
"Luna Moor & Blayze",
"Luna Shadows",
"Lunar",
"Lunar 3",
"Lunar Girl",
"Lunay",
"LUNAZ feat. Frankie Balou",
"LunchBoxxx & TheFilthyBarKid",
"LunchMoney",
"Luniz",
"Luny Tunes feat. Don Omar, Sharlene & Maluma",
"Lupa J",
"Lupe Fiasco",
"Luperz feat. BeeAnn",
"Lups Digga",
"Lura & Ruggiero",
"Lure",
"Lush & Simon",
"Lushington",
"Lusine",]

l_rus_list_25 = [
"Lustral",
"Lute",
"Luther Allison",
"Lutricia McNeal",
"Luttrell",
"Lutz Kirchhof",
"Lutzenkirchen",
"Luv Unit",
"Luvabstract",
"LuvBug",
"Luxor",
"Luxx",
"Luyanna",
"LVD feat. Alma Rogers",
"Lvly",
"Lvndscape",
"LVSN feat. Oz",
"LVTHER",
"Lvx",
"LX feat. Baby Jay",
"Lx24",
"Lxandra",
"LXE",
"Lyan feat. Serel",
"LYAR",
"Lyck",
"Lydia",
"Lyel",
"Lyfe Jennings",
"Lyinheart",
"Lykashin (Win Ney)",
"Lykke Li",
"Lykov",
"Lylloo & Lorinda",
"Lylloo feat. Egas",
"Lynch & Aacher",
"Lynda Craft",
"Lynn Chircop",
"Lynn Hayek",
"Lynn Larouge",
"Lynx & Jeremy Carr",
"LYRA",
"Lyrica Anderson",
"Lyrics Family feat. Винт & Max (Da BOMB)",
"Lyrix",
"Lys feat. J. Yolo",
"Lyuba Almann",
"LYUBIMOV",
"Lyus feat. Michael Shynes",
"Lyves",
"LZRD feat. Jake Miller",
]

litera = SoundSymbol.objects.get(name="L")

count = 0

for tag in l_rus_list_25:
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
