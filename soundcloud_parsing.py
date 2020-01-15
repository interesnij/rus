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

h_rus_list_1 = [
"H a N D",
"H Magnum",
"H. Alahard",
"H.a.N.D.",
"H.A.P.P.Y Tunez Project",
"H.E.R.",
"H1GH",
"H2O",
"Haart",
"Habbo Foxx",
"Hacktivist",
"Haddaway",
"Hades",
"Hadise",
"Hadouken!",
"Haezer feat. Born I Music",
"Hafdis Huld",
"Hafex & Alena Novak",
"Hagen Feetly",
"Hahlweg",
"Hail The Villain",
"Hailee Steinfeld",
"Haipa",
"Haise",
"Haitian Fresh feat. B.o.B & Wyclef Jean",
"Hakan Akkus",
"Hakan Ismen",
"Haketa Takefumi",
"Hakim",
"Hala feat. Julian",
"Halas Daniel feat. Sarah",
"Haldor L?greid",
"Halem",
"Halestorm",
"Haley Reinhairt",
"Haley Reinhart",
"Half An Orange",
"Halflife feat. Aruba Red",
"Halford",
"Hallman",
"Hallucination Realized",
"Hallux & Nuno Fernandez feat. Marcus",
"Halsey",
"HameLeON MC",
"Hamishe Bahar",
"Hamlet",
"HammAli & Navai",
"Hammerfall",
"Hamp & Yeps feat. Neya",
"Hampenberg",]

h_rus_list_2 = [
"Hamster feat. Becktoria",
"Hamza",
"Hamzaa",
"Hamzeh",
"Hana",
"Hande Yener",
"Handel",
"Handell feat. Vera Ostrova",
"Hang Massive",
"Hani",
"Hani Dabit feat. Joelle Sahar",
"Hank Ballard",
"Hank Williams",
"Hankesz",
"Hann",
"Hann feat. Ksenia",
"Hanna Ferm",
"Hanna Pakarinen",
"Hanna Turi",
"Hannah Diamond",
"Hannah Jacques",
"Hannah Jane Lewis",
"Hannah Jo",
"Hannah Lucia",
"Hannah Wants & Chris Lorenzo feat. Janai",
"Hanne Mjoen",
"Hannie",
"Hannis",
"Hannov",
"Hanover",
"Hans Justin",
"Hans Seo feat. Anna Toth",
"Hans Van Even",
"Hans Zimmer",
"Hansel D",
"Hanski feat. Ren",
"Hanson",
"Hanz and Gruber",
"Hanz Zimmer",
"Hapnik feat. Xavi Bosch",
"Happy J",
"Happy People",
"Happy Sovok",
"Hara feat. Nosfe",
"Hard Candy",
"Hard Rock Sofa",
"Hard-Fi",
"HardBoy feat. JackyJack & Shamik",
"Hardcore Superstar",
"Harddope",]

h_rus_list_3 = [
"Harddope & Faxonat",
"Hardened feat. Griso",
"Hardnoise",
"Hardrox feat. Saby",
"Hardsoul",
"Hardwell",
"Harel Skaat",
"Hari Mata Hari",
"Haris",
"Hariz",
"Harlee",
"Harlem River Drive",
"Harlin James & Clav",
"Harloe",
"Harmi",
"Harmo & Vibes",
"Harmonik",
"Harmonique feat. Victoria RAY",
"Harmony",
"Haro & Karoll",
"Harold Van Lennep",
"Harper",
"Harpoon feat. Stef Domazet",
"Harre",
"Harri Georgio feat. Sofia",
"Harris & Ford",
"Harrison & Juicy M",
"Harrison feat. Melody Thornton",
"HARRS & Anakyn feat. Jytte",
"Harry Belafonte",
"Harry Hudson",
"Harry Leon",
"Harry Nilsson",
"Harry Phillips",
"Harry Romero",
"Harry Styles",
"Harry Verbeke",
"Harryson",
"Harshman",
"Hart",
"Hartebees",
"Hartley",
"Hartman feat. Ralph Larenzo",
"HARU",
"Harvey Stripes feat. Lloyd",
"Has Bola & Magas",
"Hash",
"HashTag",
"Hassaan Mackey",
"Hasse De Moor",]

h_rus_list_4 = [
"HAT1 & Влад Зорин",
"Hatari",
"Hateful Trio",
"Hatikvah",
"Haula feat. VRS.US",
"Haute",
"Hava Izmailova feat. Adelina Izmailova",
"Havana",
"Have You Seen This Boy",
"Havoc",
"Havok Jones feat. Young Thug",
"Hawk Nelson",
"HAWK4 feat. Natasha Che",
"Hawksburn",
"Haxim",
"Haxon & Rush feat. Matthew Steeper",
"Hayam",
"Haydee",
"Hayden James",
"Hayes feat. Nico & Vinz",
"Hayko",
"Hayla",
"Hayley Kiyoko",
"Hayley Kiyoko feat. Kehlani",
"Hayley Orrantia",
"Hayley Scott",
"Hayley Westenra",
"Hayz",
"HAZE, Breeze & Bengston",
"Hazel & Adrima",
"Hazel feat. Lunar",
"Hazel feat. MC Sherlock",
"Hazem Beltagui",
"Hazers",
"Hb Monte",
"Hcue feat. Kida",
"HD feat. Jason Derulo feat. Smokey",
"Head & Phone",
"Head & The Heart",
"Headcharger",
"Headhunterz",
"Headie One",
"Headline Blues Band",
"Headliners",
"Headstrong",
"Healing Energy Music",
"Heart FX",
"Heart Of Steel",
"Heartist",
"Hearts & Colors",]

h_rus_list_5 = [
"Heartskin",
"Heatbeat",
"Heath Hunter & The Pleasure Co",
"Heather Bright",
"Heaven",
"Heaven's Cry",
"Heavens DJ",
"Heavy D & The Boyz",
"Heavy feat. Jubilee",
"Heavy Kind",
"Heavy Pulse feat. Nathan Brumley",
"Heavy Rain",
"HeavyFeet & Nate James",
"Heavyweight",
"Hector Delfosse",
"Hector feat. Elena Leon",
"Hector feat. Yalena",
"Hector Lopez",
"Hed Kandi",
"Hedegaard",
"Hedley",
"HeeJun feat. Pusha T",
"Hego feat. Yaya",
"Heidi Montag",
"Heilsarmee",
"Heimlich",
"Hein Cooper",
"Heizo & Sans",
"Hekler",
"Helen feat. Dorian",
"Helen Shapiro",
"HELEN YES",
"Helena & David Puentez",
"Helena & Vassy",
"Helena feat. Mr. Wilson",
"Helena feat. Shawnee Taylor",
"Helena feat. Steve Owner",
"Helena Legend",
"Helena Paparizou",
"Helena-Shadia",
"Helene Fischer",
"Heleni Isis",
"Helgon feat. Ben Lacy & Jade Norris",
"Helgon feat. Tom Hex",
"Helin Bird",
"Helios",
"Helix",
"Hell In The Club",
"Hellberg",
"Hellbilly Boys",]

h_rus_list_6 = [
"Helldog",
"Hellens",
"HELLO",
"Hello Mellow",
"Hellos",
"Helloween",
"Helly Luv",
"Helmut Fritz",
"Helmut Kraft",
"Helmut Zacharias",
"Helucze",
"Hemka",
"Hennessy",
"Henny-M",
"Henree feat. Nikka & Maya Simantov",
"Henri (BR)",
"Henri Josh, Funkyou2 feat. Maria Sampaio",
"Henri PFR",
"Henri Purnell",
"Henrik B",
"Henrik Freischlader Band",
"Henrik Lundholm",
"Henrik Wikstrom",
"Henrix & Bream feat. Zashanelli",
"Henrix Borg",
"Henrix feat. Celeda",
"Henry",
"Henry D & Alexander Orue feat. Dayson",
"Henry Dark",
"Henry Deep",
"Henry Derr feat. Alesya Kay",
"Henry Fong",
"Henry Hacking",
"Henry Himself & JALLZ",
"Henry John Morgan",
"Henry Land feat. Kim",
"Henry Mancini",
"Henry Mendez",
"Her",
"Her Majesty & The Wolves",
"Her Songs",
"Hera Bjork",
"Herbie Hancock",
"Hercules & Love Affair feat. Gustaph",
"Heren feat. Bearoid",
"Herizen",
"Herman feat. CeeLo Green",
"Herman Langschwert & Michael Roselieb",
"Hermetic",
"Herobust & LAXX",]

h_rus_list_7 = [
"Herosblack",
"Hersi",
"Hersi Matmuja",
"Herve Pagez & Diplo feat. Charli XCX",
"Heso",
"Hess",
"Hever Jara & Da Jostick",
"Hevi Levi feat. Viva",
"Hevia",
"Hevito",
"Hey Violet",
"Heyder",
"Heymen",
"HH Soulsurvivors",
"Hi Basic",
"Hi Fi",
"Hi Motive",
"Hi Tack",
"Hi-Fi",
"HI-LO",
"Hi-Mode",
"Hi-Q",
"Hi-Tack",
"Hiclass Weapon",
"Hidden Charms",
"HIDDN",
"Hide & Dream",
"Hien",
"HIFI & John Lakke feat. Bright Lights",
"High Contrast",
"HIGH feat. Эмкиро & Пепел",
"High Heelerz feat. DJ Kim",
"High Highs",
"High Maintenance",
"High N Wild",
"High Noon At Salinas",
"High Rolla",
"High Rollers & Keylas",
"High Valley feat. Ricky Skaggs",
"High15",
"Highasakite",
"Higheffect",
"Higher Brothers & DJ Snake",
"Higher Self",
"Highestpoint",
"Highland",
"Highly Sedated",
"Highly Suspect feat. Young Thug & Terrible Johnny",
"Highness",
"Highpro",]

h_rus_list_8 = [
"Hight feat. Hannah Jane Lewis",
"Highway",
"Highway Ryders",
"Hihatjack feat. Dino Mileta",
"Hiiata",
"HIIO",
"Hiio vs. Deorro",
"Hijackers",
"Hijos De La Playa",
"Hikaru Utada & Skrillex",
"Hilary Duff",
"Hilary Stagg",
"Hilda x Don Diablo",
"Hill & Gordon",
"Hillman",
"HIM",
"Hinata",
"Hind",
"Hinder",
"Hinojosa feat. Mr Chris",
"Hinol",
"Hip (В Основе)",
"Hippo Dukly",
"Hipster feat. Two Fingerz",
"HIRO",
"Hiromori Aso",
"Hirschwell",
"Hirshee",
"Hiss Band",
"History Of Fail",
"Hit-Boy feat. Nipsey Hussle",
"Hitarda",
"Hitfinders & Molla feat. Felipe Romero & Be1",
"Hitmaka feat. Meek Mill, 2 Chainz, YBN Nahmir, A Boogie Wit Da Hoodie & Tyga",
"HITS 'O' GOOD",
"Hittar Cuesta",
"Hjalmer & Medina",
"Hkeem & Unge Ferrari",
"HMC (Hannah & Miami Calling)",
"Hobo",
"Hockey",
"Hocus Pocus",
"Hodges",
"Hogland",
"Hokima",
"Hokkaido",
"Hokkaido feat. Debbie Digital",
"Hold Up",
"Holl & Rush",
"Holland",]

h_rus_list_9 = [
"Holland Park",
"Hollaphonic",
"Hollen & Raffaele Rizzi",
"Hollerado",
"Hollidayrain",
"Hollow Coves",
"Hollowed By The Sun",
"Hollowgram And Stillill",
"Hollowpoint",
"Holly & CMRN",
"Holly & Dirty Ducks",
"Holly Cole",
"Holly Drummond",
"Holly Henry",
"Holly Rose",
"Holly Valance",
"Hollyn",
"Hollywood",
"Holmes & Watson",
"Holod",
"Holseek",
"Holy Molly",
"Holychild",
"Homens Da Luta",
"HOMIE",
"HON",
"Honey",
"Honey Cocaine",
"Honey Cone",
"Honka",
"Honne",
"Honor",
"Honorata Skarbek",
"Honorebel",
"Honors",
"Hoobastank",
"Hooch",
"Hoodboi feat. TZAR",
"Hoodie Allen",
"Hoodoo Gurus",
"Hoody",
"Hoodys",
"Hooha",
"Hook N Sling",
"Hooray For Earth",
"Hooss",
"Hooters",
"Hope",
"Hope Tala",
"Hopes Hollow",]

h_rus_list_10 = [
"HOPI",
"Hopium feat. Phoebe Lou",
"Hopsin",
"Horia Brenciu",
"Horizon feat. Bianca & Sammy Arriaga",
"Hornet La Frappe feat. Leto & RK",
"Hornyshakerz feat. Devision",
"Horrorshow feat. I.E.",
"Horus",
"HOSH & 1979 feat. Jalja",
"Hot & Nasty",
"Hot Bananas",
"Hot Banditoz",
"Hot Butter",
"Hot Challenge",
"Hot Chelle Rae",
"Hot Cherry",
"Hot Colors feat. Lexter",
"Hot Hotels & DJ Kapuzen",
"Hot Mouth & Nezzo",
"Hot Rod",
"Hot Shade & Mike Perry",
"Hot Shade feat. Cal",
"Hot Shade feat. Nomi Bontegard",
"Hot Since 82 feat. Alex Mills",
"Hot Source feat. Ayak Thiik",
"Hotel 17",
"Hotel Fm",
"Hotel Garuda",
"Hotel Stereo",
"Hothouse Flowers",
"Hotlife, Tomo Hirata & Derek Hake feat. Anna Yvette",
"Hottub & Badrapper",
"Hounded feat. Bamiyah",
"Hours feat. Alexandra Rotan",
"House Massive",
"House Of Goobata",
"House Of Prayers",
"House Of Virus & Marshall Jefferson feat. Soliaris",
"House Rockerz",
"House South Brothers",
"Housechilling",
"Housedelicious feat. Teja",
"Housefly",
"Housegeist",
"Housemaxx",
"Housenick",
"Housephonics",
"Housequake",
"Houses",]

h_rus_list_11 = [
"Houseshaker",
"Housetec",
"HouseTwins",
"Houseways",
"Hovannii & Haro",
"Hovannii & Jenche",
"Hoved",
"Hovi Star",
"Hovig",
"How To Dress Well",
"Howard Shore",
"Howie B",
"Howie Day",
"Howie Dorough (Of Backstreet Boys) feat. U",
"Howlow",
"Hoxton Whores",
"Hoxtones",
"Hoxygen",
"Hoyaa",
"HOZIAS",
"Hozier",
"HPark",
"Hreez",
"HRRTZ & Light Army",
"HRVY",
"Hubert Kah",
"Hubo Bosss",
"Hudson Mohawke",
"Hudson Taylor",
"Hudson Thames",
"Huem",
"Huey Mack feat. Afrojack & Twista",
"Hugel",
"Hugh",
"Hugh Hardie",
"Hugh Hendricks & The Buccaneers",
"Hugh Laurie",
"Hugh Malcolm",
"Hugo Cantarra",
"Hugo Lopez",
"Hugo Rizzo & Stego",
"Hugo Sanchez feat. Anabella",
"Human Nature",
"Human Resource",
"Humo feat. Nel",
"Hunger",
"Huntar",
"Hunter Hayes",
"Hunter Siegel",
"Hurricane Love",]

h_rus_list_12 = [
"Hurts",
"Hush",
"Husky feat. Shyam P",
"Husman",
"Husp",
"Hybrasil",
"Hybrid",
"Hybrid Minds",
"Hydra",
"Hydro",
"Hymner feat. Alessandra",
"Hymner feat. Bast",
"HYOYEON feat. San E",
"Hypanda & IA",
"Hype Intro",
"Hype Jones feat. Terri B",
"Hyper Crush",
"Hyper Potions feat. Danyka Nadeau",
"Hyperclap & Lovespeake",
"Hypercolor",
"HyperPhysics",
"Hyperstar",
"Hyphee feat. Lil Coop",
"Hyphen Hyphen",
"Hypnotics",
"Hypnotune",
"Hypocrisy",
"Hypoxia feat. Mr.M (Та Сторона)",
"Hypster feat. Bethany Brown",
"Hysteria!",
"Hysterica",
"Hyuna (4Minute)",
]

litera = SoundSymbol.objects.get(name="H")

count = 0

for tag in h_rus_list_10:
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
