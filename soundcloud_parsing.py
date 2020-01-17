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

w_rus_list_1 = [
"W. Darling",
"W.A.S.P.",
"W.C. Clark",
"W.E.T.",
"W&W",
"W33 & Music Hayk",
"Wafande",
"Wafia",
"Wahlbeck",
"Wahlstedt",
"Waka Flocka",
"Wake Of Humanity",
"Wake Owl",
"Wal Vi",
"Walden",
"Waldos People",
"Wale",
"Wali Finkbeiner",
"Walk Off The Earth",
"Walk The Moon",
"Walkboy",
"Walker & Daniels",
"Walki Bass & Dany Aznar",
"Walki-Bass",
"Walking Def",
"Walking On Cars",
"Wall S",
"Wallaby & Neimy",
"Wallaby feat. Andie Nora",
"Wallace Band",
"Wallenski Feat. Kaya Laft & Dj Manolito",
"Wallmers & Katy Art",
"Wally Lopez",
"Walter Beasley",
"Walter Martin feat. Karen O",
"Walter Parks & Swamp Cabbage",
"Walter Trout",
"Walters & Kazha",
"Wanda Jackson",
"Wanessa feat. Soulja Boy",
"Wang Chung",
"Wang Feng",
"Wang Wei",
"Wankelmut",
"Wann & Leon Sherman",
"Wapea & Feid",
"Waplan feat. Myah Marie",
"Waqas feat. Medina",
"Warmarshal",
"Warrant",]

w_rus_list_2 = [
"Warrborn",
"Warren Parnell",
"Warren Zevon",
"WasaBee",
"Wasback",
"Waseem Stark feat. Samad",
"WASER feat. Robbie Rosen",
"Wash feat. Trey Songz",
"Washington",
"Wasp",
"Waste Management",
"WasteLand",
"WatchTheDuck",
"Waterbone",
"Waterfall feat. Akon & Play N' Skillz",
"Watermat",
"Wateva",
"Watkins Family Hour",
"Watsky feat. Wax",
"Watt feat. Post Malone",
"WAV Project",
"Wav-E",
"Wave Kid",
"Wave Projects",
"Wave Racer feat. Kwame",
"Wave Wave feat. Hilla",
"Wavejackers",
"Waverokr",
"Waves feat. Command Sisters",
"Waveshock",
"Wawa",
"Wax Motif",
"Way D feat. Никита Горюк",
"Way Out West",
"Waylon",
"Wayne Hector",
"Wayne Marshall",
"Waysons & R3hab",
"Waysons feat. Charlie Ray & Nathan Brumley",
"WayV",
"WDL feat. Elliphant",
"WDL feat. Mawe",
"WDSTCK",
"WDX",
"We & Us",
"We Architects & Abi F Jones",
"We Are Are We",
"We Are Augustines",
"We Are Fury",
"We Are Legends",]

w_rus_list_3 = [
"We Are Loud",
"We Are Me",
"We Are Scientists",
"We Are The Ocean",
"We Are Twin",
"We As Human",
"We Love Machines",
"We R Saints feat. Fya Tune & Indiiana",
"We The Kings",
"We Were Evergreen",
"Wealstarr & Ji Nilsson",
"Weared",
"WeareD feat. Maria Milewska",
"WeArtists",
"Weatherstar",
"Wee-o feat. Morgan Karr",
"Weekend",
"Weekend Heroes",
"Weekend Riots",
"Weekend Vibes",
"Weel",
"Weezer",
"Weiss",
"Wekho feat. Sunday Rose",
"Weldeck",
"Wellenrausch",
"Wellenreiter feat. Natalia",
"Wells",
"Wellvizy & Визави",
"Welshly Arms",
"Wendel Kos feat. Andrea Holley",
"Wendell feat. Andia",
"Wengie feat. Minnie",
"Wentus Blues Band",
"Werewolf",
"Werrason feat. Mohombi",
"Wes Montgomery",
"Wesley Brown",
"Wesley Verstegen",
"WeSmile",
"Wess & Aleksandar Galoski",
"West Of October",
"West Side Stories",
"West.K feat. Danijel Kostic & Weldon",
"Western",
"Westfunk",
"Westlife",
"Westphal & Whyman feat. Sophie Zeller",
"Wet Bed Gang",
"Wet Fingers",]

w_rus_list_4 = [
"Wet Wet Wet",
"Weval",
"Wezz Devall",
"Wh0 feat. Byron Stingily",
"Wham!",
"What So Not",
"What's Up",
"Whatz Up",
"Whelan",
"Whethan",
"Whigfield",
"Whiiite",
"While She Sleeps",
"Whinnie Williams",
"Whiskey Pete & Ralvero",
"Whiskey River Gun Club",
"Whisky Lights",
"Whispervoice",
"Whissell",
"White Balance",
"White Chocolate",
"White Collar Funk",
"White Denim",
"White Guys",
"White House",
"White Kola",
"White Lies",
"White Lion",
"White Lynx",
"White N3rd",
"White Nights",
"White Noise",
"White Project",
"White Sea",
"White Snake",
"White Whale feat. Playingtheangel & Ray-D",
"White Zoo feat. Maram",
"White-Akre",
"WhiteBlack & DJ KreCer",
"Whiteout",
"Whiteout feat. Kate Miles",
"Whiteside",
"Whitesnake",
"Whitesound feat. Alexandra Stan",
"Whitesquare",
"Whitney Houston",
"Whitney Woerz",
"Whizzkids",
"Who Is Fancy",
"Who.am.i",]

w_rus_list_5 = [
"WhoisFiyah & MishCatt",
"Whole-Z feat. Julia Guerra",
"WhoMadeWho",
"Whoshafee",
"Why Don't We",
"Why Don't We & Macklemore",
"Why Mona",
"Why We Run",
"Whyt Noyz",
"Wicowico & Marc Cyrus feat. Nicki Pierre",
"Wide Awake",
"Wideboys",
"WIDY",
"Wig Wam",
"Wiinston",
"Wiktoria",
"Wild Beasts",
"Wild Boyz & Not Sorry",
"Wild Cards feat. Veronica Bravo",
"Wild Cherry",
"Wild Culture",
"Wild Moreno",
"Wild Pistols & Yana Fortep",
"Wild Strawberries",
"Wild Wind",
"Wild Youth",
"Wildboyz",
"Wilde Project feat. Matt Blue",
"Wilder Woods",
"Wildes",
"WildOnes",
"Wildstylez",
"Wildvibes",
"Wiley",
"Wilhelm Richard Wagner",
"Wilhelmina",
"Wilhelmsson",
"Wilkinson",
"Will Armex",
"Will Atkinson & Rowetta",
"Will Fast",
"Will G.",
"Will Grands feat. Aimee",
"Will Holland feat. Jeza",
"Will I Am",
"Will K & FaderX feat. Scarlett Quinn",
"Will K feat. AMY MIYU",
"Will Matla",
"Will Not Fear & Sutt",
"Will Rees",]

w_rus_list_6 = [
"Will Schuester feat. Finn Hudson",
"Will See",
"Will Simms",
"Will Smith",
"Will Sparks",
"Will Tang",
"Will Wilde",
"Will Young",
"Will.i.Am",
"Willamette Stone",
"Willem De Roo",
"William Basinski",
"William Bell feat. Snoop Dogg",
"William Black feat. Rico & Miella",
"William Clarke",
"William Ekh & Martell",
"William feat. SKYLR",
"William Fitzsimmons",
"William Harrison",
"William Hawk",
"William Joseph",
"William Naraine",
"William Singe",
"Willie And The Poor Boys",
"Willie Gomez",
"Willie May",
"Willie Nelson",
"Willow Smith",
"Willy Beaman",
"Willy Joy & Proper Villains feat. Metric Man",
"Willy Saul feat. Loyan & May",
"Willy The Dee Jay",
"Willy Williаm",
"Wilmie",
"Wilson Phillips",
"Wilson Pickett",
"Win & Woo feat. Kaleena Zanders",
"WindRaisers feat. Nathan Brumley",
"Winger",
"Wingtip feat. Delacey",
"Winona Oak",
"Winston Francis",
"Winston Jarrett",
"Winston Surfshirt",
"Winston Williams & Pat Kelly",
"Winta",
"Winter",
"Winter Leaves",
"WiseNoize feat. Yvee",
"Wish I Was feat. Luna",]

w_rus_list_7 = [
"Wit Blu",
"Witchcraft",
"Witchwood",
"Within Temptation",
"Without Face",
"Without Limits",
"Without Words",
"Witi & Артур Тринёв",
"Witloof Bay",
"Witt Lowry feat. Ava Max",
"Wiwek",
"Wiz Khalifa",
"Wizard feat. Riev",
"WizG feat. Mechi Pieretti",
"Wizkid",
"WK2",
"Wlack",
"Wlady",
"WNDR feat. Samuel Eli",
"Woak & Kiko Franco & Sylvain Armand feat. Nick Kingswell",
"Woak & Make U Sweat",
"Woe feat. Flo Rida",
"Wolf Alice",
"Wolf Box",
"Wolf Colony",
"Wolf Gang",
"Wolffe",
"Wolffox",
"Wolfgang Amadeus Mozart",
"Wolfgang Gartner",
"Wolfie",
"Wolfie feat. Nadia Rose",
"Wolfire",
"Wolfmother",
"Wolfpack",
"Wolkenlos",
"Wolkoff",
"Wolvo feat. Reign",
"Woman's Hour",
"Won-G feat. Rick Ross",
"Wonder Girls",
"Wonderland",
"Wonderland Avenue",
"Wongo feat. Blak Trash",
"Woo2tech & Sensekraft",
"Woodes",
"Woodkid",
"Woody Van Eyden",
"Woofax",
"Wookie feat. Eliza Doolittle",]

w_rus_list_8 = [
"Wooli & AFK feat. Jay Fresh",
"Worakls",
"Work Drugs",
"Work Friends",
"Work Of Art",
"World In Motion",
"World Of Girls",
"World Sketch feat. Jonathan Mendelsohn",
"World Sound",
"Worry",
"Worry Blast",
"Worst Brown",
"Wot",
"Woti Trela",
"Wound Man",
"WOW",
"Wow-Fi",
"Wow! Wow! feat. Toby",
"Wpx",
"Wrabel",
"Wrathschild",
"Wray",
"Wrechiski",
"Wretch 32",
"Wrexter",
"Written On The Sky",
"WRLD",
"Wrongonyou",
"WSTRN",
"WTF!",
"WTRFALL",
"Wu-Tang Clan",
"Wuillermo Tuff",
"Wusa feat. IIVES",
"Wuuha feat. Ali",
"Wyclef Jean",
"Wye Oak",
"Wylde",
"Wynonie Harris",
"Wynter Gordon",
]

litera = SoundSymbol.objects.get(name="W")

count = 0

for tag in w_rus_list_6:
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
