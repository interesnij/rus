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

k_rus_list_1 = [
"K CAMP",
"K Crystal",
"K Drew",
"K JiT",
"K Koke feat. Maverick Sabre",
"K Kutta feat. Flo Rida",
"K Maro",
"K Naan",
"K S Project",
"K Theory",
"K Theory X Wizard",
"K W S",
"K-391",
"K-Chante & Кот Балу",
"K-Dee",
"K-Flow feat. Severiano",
"K-Klass feat. Bobbi Depasois",
"K-Maro",
"K-Narias",
"K-One & John L",
"K-Real",
"K-Rim",
"K-Tree feat. Flo Rida & Shawn",
"K-Zone",
"K. Michelle",
"K. Roosevelt feat. Hit-Boy",
"K.B. Caps",
"K.Blank feat. Elaine Winter",
"K.D.M feat. Artu",
"K.E.FEAR",
"K.EM.D",
"K.Flay",
"K.ICE feat. RAMI",
"K.Melody",
"K.S. Project",
"K.T.A.",
"K'Naan feat. Nas",
"K14a",
"K1lled & Денис Лирик",
"k1RG",
"K2",
"K3N",
"K7 & Exit 59 feat. Tanto Metro, Devonte & Mad Stuntman",
"Ka-Re",
"KA!NE",
"Kaady feat. Lovisa",
"Kaan Pars",
"Kaarl feat. Mathilde Hoslet",
"Kaaze",
"Kabana",]

k_rus_list_2 = [
"Kabat",
"Kacey Musgraves",
"Kaci",
"Kacy Hill",
"Kacy Rese",
"Kadebostany",
"Kadi",
"Kadie Elder",
"Kadmir",
"Kadnay",
"Kadoc",
"Kados feat. Mickey Boy",
"KADRA",
"Kady Z",
"Kaef",
"Kaffe",
"Kaffein",
"Kago Pengchi",
"Kagramanov & Karina Evn",
"Kahikko & Jespr",
"Kai & Shami",
"Kai Dza-Wa feat. Igor Kmeto Ml.",
"Kai Kahana feat. Cec Lopez",
"Kai Sheen",
"Kai Tracid",
"Kai Wachi",
"Kaidro & Spce CadeX feat. Veronica Bravo",
"Kaii Dreams",
"Kaiia vs. Manilla Maniacs",
"Kaiko & Calo",
"Kail & Джиос",
"Kailee Morgue",
"Kaimo K",
"Kain feat. Sweet Insane",
"Kain Rivers",
"Kaira",
"Kairiv & Кравц",
"Kairo Kingdom",
"Kairos Augur",
"Kaiser Chiefs",
"Kaiser Souzai",
"Kaiserdisco",
"Kaistal.A.O",
"KAIZ",
"Kaizer Panda & Kayali",
"KAJ feat. The Ready Set",
"Kaka",
"KaktuZ & Freaky DJ's",
"Kaleef",
"Kaleida",]

k_rus_list_3 = [
"Kaleidoscope",
"Kalenna",
"Kaleo",
"KALI",
"Kalia",
"Kalibwoy",
"Kalide & Deakin XD feat. Bianca",
"Kalif feat. Roxanna",
"Kalin & Myles",
"Kaliopi",
"Kallau & Bitas",
"Kallau & Cuddly Cactus",
"Kallay Saunders",
"Kalle Mattson",
"Kallina",
"Kallitechnis",
"Kallula",
"Kalma",
"Kalomira",
"Kalomoira",
"Kalpee",
"Kaltrina Selimi",
"Kaluma feat. Fabienne Rothe",
"Kalwi & Remi",
"Kam Parker",
"Kama",
"Kamaiyah feat. Quavo & Tyga",
"Kamakaze & Massappeals feat. Morgan Munroe",
"Kamal",
"Kamaleon",
"Kamaliya",
"Kamasya",
"Kamaura",
"Kamazz (3NT)",
"Kamelia",
"Kami",
"Kamik",
"Kamil Brandt",
"Kamil Ghaouti feat. Inaes",
"Kamil Mikulcik & Nela Pociskova",
"Kamil Pankowski & Khaeem feat. Alexa Lusader",
"Kamila Amelie feat. Lazee",
"Kamille",
"Kaminski",
"Kamo",
"KAN",
"Kan R. Gao, Feat. Laura Shigih",
"Kanary Diamonds",
"Kandia Kora",
"Kando feat. Alicia",]

k_rus_list_4 = [
"Kandy",
"Kane Brown",
"Kanero",
"Kangaroo",
"Kanguru",
"Kanita",
"Kannamix feat. Veela",
"Kansas",
"Kant",
"Kantango",
"Kantare feat. Patricia Edwards & Syntheticsax",
"Kantika",
"Kantinent & Алексей Сулима",
"Kanute",
"Kany West feat. Jay-Z ft. & Frank Ocean",
"Kanye Wes",
"Kanye West",
"Kanza",
"Kaoma",
"Kap G feat. Chris Brown",
"Kap Slap",
"Kapara",
"Kapera",
"Kaplin feat. Vertuga & Rodion pres. Vita",
"Kapre & J. Esho",
"Kaptan",
"Kara Kross",
"Kara One",
"Karabass",
"Karakuli",
"Karami",
"Karanda",
"Karapuzikee",
"Karat",
"Kardinal Offishall",
"Karen",
"Karen B.",
"Karen Harding",
"Karen Harding feat. Wh0",
"Karen Lovely",
"Karen O",
"Karen Overton",
"Karen Souza",
"Karen Туз",
"Karena",
"Karetus",
"Kari Kimmel",
"Karie feat. George Hora",
"Karim",
"Karim Maas",]

k_rus_list_5 = [
"Karim Mika",
"Karin Nagi",
"Karin Park",
"Karina (Вартанян Карина)",
"Karina Evn",
"Karina feat. Rayski",
"Karina feat. Romanof",
"Karina Pasian",
"Kario Y Yaret",
"Karise Eden",
"Karizma",
"Karkaz feat. Joe Jury",
"Karl Jenkins",
"Karl Maddison",
"Karl Wine",
"Karl Wolf",
"Karlen",
"Karliene",
"Karma",
"Karma Fields",
"Karmah",
"Karmen DJ",
"Karmen feat. Achi",
"Karmen feat. Krishane",
"Karmen feat. Stylo G",
"Karmen Stavec",
"Karmic",
"Karmin",
"Karmin & Watsky",
"Karmin Shiff",
"Karnaval Blues",
"Karnazh & Kate Hall",
"Karnivool",
"Karo",
"Karol G",
"Karolina Goceva",
"Karolina Westberg",
"Karosa feat. Kledia",
"KARTASHOW",
"Kartellen Feat. Alex",
"Kartvelli",
"Karuan",
"Karunesh",
"Karusel & EFGI",
"Karybde & Scylla",
"Karym",
"Karyna feat. Andrei Leonte",
"Kasabian",
"Kasbo",
"Kash Doll",]

k_rus_list_6 = [
"Kashif",
"Kashmir",
"Kasia Mos",
"Kaskade",
"Kaskeiyp",
"Kass",
"Kassandra",
"Kassia",
"Kasta и Гуф",
"Kastilla",
"Kastle feat. Lotti",
"KastomariN",
"Kastra",
"Kasum",
"Kat Dahlia",
"Kat De Luna",
"Kat Deluna",
"Kat Galamay",
"Kat Graham",
"Kat Krazy",
"Kat Perkins",
"Kat Stephie",
"Kataleya",
"Katana",
"Katanah",
"Kataphraktoi",
"Katarina",
"Katastrofe feat. Александр Рыбак",
"Katatonia",
"Kataztrofee feat. French Montana, The Game & Young Dro",
"Katdrop",
"Kate & Or feat. Nitan Ben Ari",
"Kate Boy",
"Kate Havnevik",
"Kate Lesing feat. Cj Slava",
"Kate Linn",
"Kate Lomas",
"Kate Melody",
"Kate Micucci",
"Kate Miller",
"Kate Miller-Heidke",
"Kate Rin",
"Kate Ryan",
"Kate Stewart",
"Kate Voegele",
"Kate's Project",
"KateKey",
"Katelyn Tarver",
"Katerina Lioliou",
"Katerina Stikoudi",]

k_rus_list_7 = [
"Katerine Duska",
"KATFYR",
"Katharine McPhee",
"Katherine Ellis, Hugo Kalfon, Rio Dela Duna",
"Katherine Tanner",
"Kathy Read",
"Kati Gazela feat. Ray Kuba",
"Kati Wolf",
"Katia",
"Katia feat. Wildboyz",
"Katie Armiger",
"Katie Bell feat. Claydee",
"Katie feat. Ty Dolla Sign",
"Katie Keller",
"Katie Kern",
"Katie Melua",
"Katie Webster",
"Kato",
"Kato Jimenez",
"Katrella",
"Katrin & DJ Cross feat. Max'C",
"Katrin Mokko",
"Katrin Moro",
"Katrina",
"Katrina And The Waves",
"Katrina Parker",
"Katrine",
"Katrisha",
"KATS",
"Katty B.",
"Katty Heath",
"Katu",
"Katy B",
"Katy feat. The Elders & Rihanna",
"Katy Perry",
"Katy Rain",
"Katy Tindemark ft. Miks Dukurs",
"Katy Tiz",
"Katya Che",
"Katya Disney",
"Katya Lee",
"Katya Steff",
"Katya Sun",
"Katya Tu",
"KATZ",
"Katzenjammer",
"Kaum feat. Tasha",
"Kav Verhouzer",
"Kavabanga",
"Kavi Jezzie Hockaday",]

k_rus_list_8 = [
"Kavinsky feat. The Weeknd",
"KAWALA",
"Kawilo feat. Valentina J Woods",
"Kay Caldwell",
"Kay Cola",
"Kay feat. Kurtis Blow",
"Kay One",
"Kay Starr",
"KAYA",
"Kaya feat. Craig David",
"Kaya Jones",
"Kaya Stewart",
"Kaydy Cain feat. Yassir & Los Del Control",
"KAYEF",
"KAYEX",
"Kayla",
"Kayliox",
"Kaymbo Shines feat. Lukay",
"Kayna Samet feat. Francisco",
"Kayosa & Tolland feat. Matt Noland",
"Kayper",
"Kayra",
"Kaysha Lee",
"Kaytranada",
"Kayzo",
"Kaz James",
"Kazaky (Казаки)",
"Kazantip",
"Kazlo feat. Alexa Lusader",
"KaZoO",
"KBDM",
"Kc & The Sunshine Band",
"KC Lights feat. Laronge",
"Kcink",
"KD Division",
"KDA",
"KDDK feat. Arilena Ara",
"Kdk",
"KDrew",
"Keam",
"Kean Dysso",
"Keane",
"Keanu Silva",
"Keasha Torry feat. LaZ (Tа Сторона) & СКРО",
"Keat",
"Keb' Mo'",
"Kebana",
"Kedrone",
"KeeKee R.O.C. feat. Chi T",
"Keelo",]

k_rus_list_9 = [
"Keelyn Ellis",
"Keen'V",
"Keenly",
"Keeno",
"Keep Shelly In Athens",
"Keepflow feat. Ruana",
"Keepsake feat. Slyleaf",
"Kehlani",
"Keif",
"Keiino",
"Keiko Matsui",
"Keisha Buchanan",
"Keith Ape feat. Bryan Chase",
"Keith James",
"Keith Jarrett",
"Keith Kenniff",
"Keith Scott",
"Keith Thompson's Strange Brew",
"Keith Urban",
"Keithian",
"Kejsi Tola",
"Keke Palmer",
"KeKe Wyatt",
"Keke",
"Keko Salata feat. Ivone Cerdan",
"Kekra feat. Niska",
"Keky",
"Kel",
"Kelde",
"Keldian",
"Kele Okereke",
"Kele vs Sander Van Doorn feat. Lucy Taylor",
"Kelela",
"Kelin Elise",
"Kelis",
"Kelita",
"Keljet",
"Kella",
"Kelli-Leigh",
"Kellie Pickler",
"Kelly Carvin",
"Kelly Clarkson",
"Kelly Joyce",
"Kelly Pepper",
"Kelly Pfaff feat. DJ Wes D & Ros",
"Kelly Price",
"Kelly Rowland",
"Kelly Sheehan",
"Kelly Simonz's Blind Faith",
"Kelly Sweet",]

k_rus_list_10 = [
"KELM",
"Kelsea Ballerini",
"Kelsy Karter",
"Kelton Wade",
"Kem",
"Kemistrie",
"KEMPEL",
"KEMPEL & SHPILEVOY",
"Ken Carlter feat. Tommy Driker",
"Ken Hensley",
"Ken Laszlo",
"Ken Loi",
"Ken Martina",
"Ken Navarro",
"Ken Wilbard",
"Kenai",
"Kenan Dogulu",
"Kendall K",
"Kende",
"Kendi",
"Kendji Girac",
"Kendra & Capitan Kidd",
"Kendra Erika",
"Kendrick Lamar",
"Kenichi Tamura",
"Kenio Fuke",
"Kenn Colt & Hiisak",
"Kenn Colt feat. Brenton Mattheus",
"Kenn Colt feat. Jaimes",
"Kenn Colt feat. Nari & Milani",
"Kenneth G & Maurice West",
"Kenneth G & Sheezan",
"Kenneth G feat. Ilang",
"Kenneth Potempa",
"Kenny ´Dope´ Presents The Bucketheads",
"Kenny Bern",
"Kenny Burrell",
"Kenny Chesney",
"Kenny Dsk",
"Kenny G",
"Kenny Kruger",
"Kenny Neal",
"Kenny Wayne Shepherd",
"Kent Jones feat. Pitbull & Lil Wayne",
"Kentera",
"Kenty",
"Kenzie",
"Kenzie May",
"Keo",
"Keramina",]

k_rus_list_11 = [
"Keremina",
"Keri Hilson",
"Kerli",
"Kernell",
"Kerria",
"Kerry Force",
"Kerry Leva",
"Kerry Reeve feat. Demi McMahon",
"Kerser",
"Kerstin Ott",
"Kery Fay",
"Kery Scandal feat. Akeem Worldwide",
"Kes",
"Kesh",
"Kesha",
"Keshi",
"Keshia",
"Keshia Chante",
"Kesi",
"KESMAR",
"Kess Ross feat. John Gibbons vs. Phats & Small",
"KET-U",
"Ketelens' Brukke",
"KEV",
"Kev Spencer",
"Keven & Ery feat. Franco El Gorila",
"Kevin 2k feat. D.Masta",
"Kevin Blanc",
"Kevin Borg",
"Kevin Carvallo",
"Kevin Cossom feat. French Montana",
"Kevin Courtois & Lexy Panterra",
"Kevin Crowley",
"Kevin David vs. Quantum Beatz",
"Kevin Drew feat. Taryn Manning",
"Kevin Forbes",
"Kevin Gates",
"Kevin Hammond",
"Kevin Hunter",
"Kevin Hussein",
"Kevin Karla & La Banda feat. Domac",
"Kevin Keapon",
"Kevin Kendle",
"Kevin Kern",
"Kevin Lyttle",
"Kevin McCall",
"Kevin Michael",
"Kevin Miller",
"Kevin Morby",
"Kevin Roldan",]

k_rus_list_12 = [
"Kevin Rudolf",
"Kevin Sunray & Arrow feat. Charley",
"Kevin Walker",
"Kevin Wild feat. Kelly Sweet",
"Kevin Zack",
"Kevlar feat. Lisa Jane",
"Kexxy Pardo & Trapical",
"Key Lean feat. Tiff Lacey",
"Key Notez feat. Yesi",
"KeyC",
"Keymass & Bonche",
"Keypro & Kiss",
"Keyptown",
"Keys N Krates",
"KeySax",
"Keyshia Cole",
"Keyzer",
"KG Man & Yungg Trip",
"KGproject",
"Kh33n feat. David Edward",
"Khainz, Alok",
"Khaled",
"Khalid",
"Khalif",
"Khalifa feat. Wayne Wonder",
"Khalil",
"Khamsin feat. Layna",
"Khan Twinz feat. 6ixlo",
"Kharfi & Jade Million",
"Kharfi feat. Mike Gomes",
"Kharmelo",
"Khikko",
"Khlorinn feat. Lindsay Nourse",
"KhoMha",
"Khon",
"Khrebto feat. NeonHeart",
"Kiah Victoria",
"Kiana",
"Kiana Lede",
"Kiara Nelson",
"Kiasmos & Hogni",
"Kick Clap Kick",
"Kickbombo feat. Ebby",
"Kicking Daisies",
"KickRaux & Beenie Man & Tommy Lee Sparta feat. Nyla",
"Kicks N Licks feat. Nicole Millar",
"Kid Arkade",
"Kid Astray",
"Kid Coconutz",
"Kid Cudi",]

k_rus_list_13 = [
"Kid Cupid",
"Kid Drama",
"Kid Hastings",
"Kid Ink",
"Kid Kern",
"Kid Massive",
"Kid RED feat. Chris Brown",
"Kid Rock",
"Kid Sister",
"Kid Sole feat. IROH",
"Kid Williams",
"Kiddo",
"Kideko",
"Kidro",
"Kids By Nature",
"Kidz Bop Kids",
"Kiefer Sutherland",
"Kiera Weathers",
"Kieran Alleyne",
"Kieran Johnson feat. Cookzee",
"Kierra Sheard",
"Kiesza",
"Kiesza, Chris Malinchak & Malinkiesza",
"Kiholm feat. Josh Money",
"Kiiara",
"KIIDA feat. Marc Wulf",
"Kiido",
"KIIRA",
"Kika feat. Andreas Wijk",
"Kike Puentes",
"Kike Rodriguez & McMesie",
"Kiker feat. Паша Каин & RoMa RASST",
"Kiki C feat. Daffy",
"Kiki Doll",
"Kiki Rowe",
"Kiko & Olivier Giacomotto",
"Kiko Franco & WOAK feat. Samantha Machado",
"Kiko Rivera",
"Kilate Tesla & Puri",
"Kilbourne",
"KilFil",
"Kilgore",
"Kilhom",
"Kilian",
"Kiligin",
"Kill FM",
"Kill J",
"Kill Paris",
"Kill Sniffers",
"Kill The Buzz",]

k_rus_list_14 = [
"Kike Rodriguez & McMesie",
"Kiker feat. Паша Каин & RoMa RASST",
"Kiki C feat. Daffy",
"Kiki Doll",
"Kiki Rowe",
"Kiko & Olivier Giacomotto",
"Kiko Franco & WOAK feat. Samantha Machado",
"Kiko Rivera",
"Kilate Tesla & Puri",
"Kilbourne",
"KilFil",
"Kilgore",
"Kilhom",
"Kilian & Jo",
"Kilian Dominguez feat. Alvaro Guerra & Silvia Roman",
"Kilian Taras feat. Ya-Ya & Neon El Emperador",
"Kiligin",
"Kill F",
"Kill J",
"Kill Paris",
"Kill Sniffers",
"Kill The Buzz",
"Kill The Noise",
"Kill Them With Colour feat. David Spekter",
"Killa Fonic & Carla's Dreams",
"Killa Kyleon feat. Jack Freeman",
"Killa Squad",
"Killa Voice feat. Арина Перчик",
"Killabyte feat. Danyka Nadeau",
"Killah Priest",
"Killer Bee",
"Killer Hertz feat. Raphaella",
"Killercats",
"Killogy & Matthew White feat. Angelika Vee",
"KillSonik",
"Killswitch Engage",
"Kilohertz",
"Kilswitch Engage",
"Kilter",
"Kilu & Adam Tas",
"Kim Angeles",
"Kim Burrell & Pharell Williams",
"Kim Cesarion",
"Kim Churchill",
"Kim Dotcom",
"Kim Kaey",
"Kim Kwang Min",
"Kim Lee & Lil Debbie",
"Kim Leoni",
"Kim Lucas",]

k_rus_list_15 = [
"Kim Lukas",
"Kim Morgan",
"Kim Petras",
"Kim Robertson",
"Kim Russell",
"Kim Simmonds",
"Kim Sozzi",
"Kim Viera",
"Kim Waters",
"Kim Wilde feat. Laurent Voulzy",
"Kim-Lian",
"Kimak",
"Kimara",
"KimBack",
"Kimberley Locke",
"Kimberley Walsh",
"Kimberly Anne",
"Kimberly Cole",
"Kimberly Fransens",
"Kimberly Wyatt",
"Kimbra",
"Kimishkez",
"Kimotion feat. Adrian McKinnon",
"Kimoto Boy",
"Kimura & Tube Tonic",
"KINA",
"Kinbell feat. Brenton Mattheus",
"Kind Of Blue",
"Kindervater",
"Kindness feat. Robyn",
"Kinetica",
"King & White",
"King Arthur",
"King Company",
"King Deco",
"King Horror",
"King Kazi, Brown Girl, Viruss & Ullumanati",
"King Khan & His Shrines",
"King Kobra",
"King Nine",
"King Of Bass",
"King Of Woolworths",
"King Princess",
"King Todli & Real Purple Deep feat. Dj Biggy B",
"KINGDM",
"Kingdom 7 feat. Lauren Laimant",
"Kingdom Come",
"Kings & Michael Tsaousopoulos",
"Kings & Themis Adamantidis",
"Kings feat. Alexandra",]

k_rus_list_16 = [
"Kings feat. Haris Mos",
"Kings Krew Feat Boom",
"Kings Of Convenience",
"Kings Of Leon",
"Kings Of Tomorrow feat. Elzi Hall",
"Kingsley",
"Kingston",
"KingStyle",
"Kinko Acid",
"Kinski & Dakuka",
"Kinspin",
"Kinza",
"Kip Moore",
"Kir Angels & Gosh Crash feat. Max Pride",
"Kir Tender",
"Kira Puru",
"Kira Shine",
"Kiran M Sajeev",
"Kirill Slepuha feat. Ани Лорак",
"Kirillfasco & Дарья Кумпаньенко",
"KirillOnly",
"Kirin feat. Myah Marie",
"Kirk Fletcher",
"Kirk Norcross & Zack Knight",
"Kirk Whalum",
"Kirko Bangz",
"Kirsten Arian",
"Kirsty",
"Kisch feat. Syon",
"Kishe",
"Kiso & Vanillaz feat. Malcolm Anthony",
"Kiso feat. Jillea",
"Kiso feat. Kayla Diamond",
"Kiss",
"Kiss 'N Ride",
"Kiss Audio",
"Kiss The Burner",
"Kissa",
"Kissadilla",
"Kissie Lee",
"Kissin' Dynamite",
"Kissy",
"Kissлород",
"Kit Fysto feat. Cody Longo",
"Kita Alexander",
"Kitaro",
"Kitberg feat. Ярослав",
"Kito",
"Kitoboy & Кравц & Пицца",
"Kitsch 2.0",]

k_rus_list_17 = [
"Kitten The Hip",
"Kiva",
"Kiyoi & Eki",
"Kize",
"KJ Sawka & Stratus",
"Kjust",
"KKO",
"Klaas",
"Klangfeld feat. Tillmann Uhrmacher",
"Klangkarussell",
"KlangKuenstler feat. Linda Muriel",
"Klangquelle",
"Klangspieler & Xona",
"Klapa S Mora",
"Klara & Jag",
"Klass",
"Klassify feat. Sensus & Devonne",
"Klaudia Gawlas",
"Klaudya feat. Felipe Romero",
"Klaus Doldinger",
"Klauss & Turino, Jakko feat. Paul Aiden",
"Klauss Goulart",
"Klava & Korry",
"Klave",
"Klaxons",
"KLAY feat. НЕвесьЯ",
"Klaypex",
"Klein George",
"Klelight",
"Kler",
"Klf",
"Klia",
"Klim",
"Klimentyev",
"Klingande",
"Klinika",
"Klipsа",
"Klissmoon",
"KLIZMA",
"Kllo",
"Kloe",
"Klok and Dager",
"Klosman",
"Kloter",
"Kloud",
"KLP",
"KLP feat. Dena Amy",
"Klubbheads",
"Klubbingman",
"Klune feat. IVYE",]

k_rus_list_18 = [
"Klunsh",
"Klute",
"Klyde",
"Klymvx",
"Klypex",
"KMG's",
"KMK Live Show feat. Tony T",
"Knez",
"Knife Party",
"Knob",
"Knoxa feat. Georgia Ko",
"KNOXA feat. Georgia Ku",
"Knut Anders Sorum",
"KO (Настя Кочеткова)",
"KO & The Xi",
"Ko Ray",
"Ko-Dan",
"Ko4a feat. Зомб",
"Koala feat. Filatov & Karas",
"Kobe Bourne",
"Kobi Marimi",
"Kobko",
"Kobra And The Lotus",
"Koda Kumi",
"Kodak Black",
"Kodaline",
"KODI",
"Kodie",
"Koehne & Kruegel feat. Janine Delon",
"Koen Groeneveld",
"koF",
"Kofa & Lisitsyn",
"Koffee feat. Gunna",
"KOGAN",
"Kogan & Fierce",
"Koit Toome & Laura",
"Kokab & Beatchild",
"Kokaholla feat. Quinn Bates",
"Kokenn",
"Kokiri",
"Koko Taylor",
"Kola Project",
"Kolaj",
"KOLAJ & Eric Nam",
"Kolak & Taylder feat. Emma",
"Kolibri",
"Kolidescopes",
"Kolir, St1ff & MC Pasha",
"Koliukas",
"Koloah & Olya Dibrova (Gorchitza)",]

k_rus_list_19 = [
"Kolombo",
"Kolonie feat. Al Morris",
"KolRus feat. T1One",
"Koly Kolgate feat. Eminem",
"Kolyas",
"Komiko",
"Kommo",
"Komo",
"Komodo",
"Kompany & G-REX",
"Kompulsor",
"Konac",
"KOne",
"Kongsted",
"Konig & Kromer feat. Cataleya",
"Konnie Metaxa",
"KONO",
"Konoplev",
"Konshens",
"Konstantah",
"Konstantin E. feat. MainstreaM One",
"Konstantin feat. Ayla Shatz",
"Konstantin feat. Ayla Shatz & Cleo",
"Konstantin Ozeroff",
"Kontra K",
"Kontrabanda",
"Koo",
"Koobra",
"Kool & The Gang",
"Kool and The Gang",
"Kool John",
"Koop",
"Kopo feat. Alexandra Stan & Drei Ros",
"Koppers",
"Korde",
"Kori Cosby",
"Korn",
"Korol'OK",
"Koru",
"Kosca feat. Colleen Kelly",
"kosH",
"Kosheen",
"Kosikk",
"Kosinus & The Dual Personality feat. Demirra",
"Kosling",
"Kosmin feat. Beatrice",
"Kosmonova",
"Kosmos",
"Kosta",
"Kostas Haritodiplomenos",]

k_rus_list_20 = [
"Kosteo & Byubeat",
"Kotaro Oshio",
"kOtmOs",
"Koto",
"Kotuno",
"Kotuno feat. Зомб & Skzk",
"Kourosh Tazmini",
"Kova feat. HAIZ",
"Kovacs",
"Kovacs feat. Gnash",
"Kovalenco Gennadi, Vlad Gorban feat. IK",
"Kovalev",
"Kovary",
"Kove",
"Koven",
"Kovia feat. Bibi",
"Kowa",
"KOYU feat. Example",
"Koza Nostra",
"Kozah feat. Anuka",
"Kozmix",
"Kpo2LL",
"KRA",
"Kraak & Smaak",
"Kraantje Pappie",
"Kraft",
"Kraftwerk",
"Krait",
"Krajno",
"KRAK'N",
"Krakota",
"Kraljevi Ulice & 75 Cents",
"Kram",
"Kranium feat. Tory Lanez",
"Krasavina",
"Krash Loud Control",
"Kraski",
"Krasotin feat. Dasha Luks",
"Krassimir Avramov",
"Kraulis",
"Krava",
"Krazy Sandi",
"Kream",
"Kreayshawn",
"Krec",
"Kredo feat. Songdreamer",
"KReeD",
"Kreesha Turner",
"Kreida",
"Kreisiraadio",]

k_rus_list_21 = [
"Krem feat. Adina",
"Krempal",
"Krept & Konan",
"Krestall feat. Courier & Aqualiquid, Jubilee, Rickey F",
"Krewella",
"Kriess Guyte",
"Kriga & Gryma",
"Krimsonn",
"Krinitsyn & Pravda",
"KripMus",
"Kris Allen",
"Kris Baha",
"Kris Baptiste",
"Kris Kristofferson",
"Kris Kross Amsterdam",
"Kris Maydak",
"Kris Monico feat. Profreshnill",
"Kris Wu feat. Jhene Aiko",
"Krishane feat. Shaggy",
"Kriso Lindberg",
"Kriss Gomez",
"Kriss Norman",
"Kriss Soul feat. Penny Well",
"Krissy",
"Krist Van D feat. Niles Mason",
"Krista Siegfrids",
"Kristal A",
"Kristelle feat. Влад Топалов",
"Kristen Williams feat. Vinny Venditto",
"Kristian Bush",
"Kristian Kostov",
"Kristian Leontiou",
"Kristian Tuska",
"Kristin Chenoweth",
"Kristina & The Dolls",
"Kristina Casolani & Pizza Brothers",
"Kristina Dolce feat. B.R.Y.C.E.",
"Kristina Dux",
"Kristina Jolly",
"Kristina Korvin feat. Andrey Fan",
"Kristina Maria",
"Kristina Si",
"Kristina Sky & Randy Boyer feat. Shyboy",
"Kristina Train",
"Kristine Elezaj",
"Kristine W",
"Kristinia DeBarge",
"Kristoffer Rahbek",
"KristyAnne",
"Krizia",]

k_rus_list_22 = [
"KRNE feat. Jupe",
"Krokus",
"Kron feat. F1GhT",
"Kronic",
"Krono",
"Kros",
"Krosses",
"Krowly feat. Nikita Ravel",
"Krugers",
"Krum & Andrea",
"Krumbsnatcha",
"Krunk! & Miljay feat. iDo",
"Krup_E",
"Kruse & Nuernberg feat. Isis Salam",
"Krusty",
"Kruv feat. Ремо & Санчес",
"Kryan, Fabyan, Yoandri, Micke Moreno",
"Kryder",
"KRYGA",
"Kryga feat. Rhea Raj",
"Kryoman",
"Kryptomedic & Disphonia",
"Kryptomedic & Fragz",
"Krystl",
"Ksandra",
"Ksanti",
"Ksela feat. DJ-Sirious",
"Ksenia & Black Rose Beatz",
"Ksenia AnikinA",
"Kseniya Anikina",
"Ksenona",
"KseroN",
"KSHMR",
"Kson",
"Kson & Ditro",
"KStewart",
"KT Tunstall",
"Ktree",
"Ku De Ta",
"Kubi",
"Kubikk feat. Selecta",
"Kubilay Aydin & Aytac Ozalp",
"Kuchenmann",
"Kudrina",
"Kudu Blue",
"Kukuzenko",
"Kulture Shock",
"Kulwinder Billa feat. Yuvika Choudhary",
"Kuma",
"Kumi Koda",]

k_rus_list_23 = [
"Kumo feat. City Island",
"Kungs",
"Kunteynir",
"Kuoga feat. Ivy",
"Kuolemanlaakso",
"Kuptsova",
"KURA",
"Kurbat",
"Kurd Maverick & Plastik Funk feat. Ashlee Williss",
"Kurt & Luis Fonsi",
"Kurt Calleja",
"Kurt Elling",
"Kurtis Blow",
"Kush Kush",
"Kut & Run",
"Kut feat. Grom",
"Kutless",
"Kuunkuiskaajat",
"KUURO",
"Kuzheleva",
"Kuzmin Project",
"Kuznetsov",
"Kvazar",
"KVBeats feat. Rashad & DJ Rob Swift",
"Kvinn",
"Kvlibra",
"Kvmo",
"KVPV",
"KVR feat. Twan Ray",
"KVSH & Beowulf & Flakke",
"KVSH & Malifoo",
"KVSH & The Otherz & Froede",
"Kwabs",
"Kwaku Asante",
"Kwame feat. LayLay",
"Kwamie Liv feat. Angel Haze",
"Kwan Hendry feat. SoulCream",
"Kwassa",
"KWAYE",
"Kyan Palmer feat. Nicopop. & Ryen",
"Kyau & Albert",
"Kyboe!",
"Kyd The Band",
"Kydus",
"Kye Sones",
"Kyfra & Eche Palante feat. Brandon Lehti",
"Kygo",
"Kyiki",
"KYKO",
"Kyla Fava, Wooshay & Skylark",]

k_rus_list_24 = [
"Kyla La Grange",
"Kyle Alessandro",
"Kyle Brylin",
"Kyle Christopher",
"Kyle Dion",
"Kyle Evans",
"Kyle Lettman",
"Kyle Meehan",
"Kyle Tree",
"Kyle Walker",
"Kyle Watson",
"Kyler England",
"Kylian Mash and Glasses Malone feat. Jay Sean",
"Kylie Clan",
"Kylie Minogue",
"Kymai feat. Aynell",
"Kyndall",
"Kynt",
"Kyo",
"Kyraa",
]

litera = SoundSymbol.objects.get(name="K")

count = 0

for tag in k_rus_list_12:
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
