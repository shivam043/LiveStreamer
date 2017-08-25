import webbrowser
import argparse
import sys


"""Storing data"""
list_channel=["Barca TV(SPA)","BBC 1(UK)","BBC 2(UK)","BBC 3(UK)","BBC 4(UK)","BOXNATION(UK)","BRAVO TV(UK)","BRITISH EURO SPORTS 1(UK)","BRITISH EURO SPORTS 2(UK)","BT SPORT 1(UK)","BT SPORT 2(UK)","BT SPORT 3(UK)","BT SPORT ESPN(UK)",
"CANAL+SPORT(FR)","CHANNEL 4(UK)","CHANNEL 5(UK)","CHELSEA TV(UK)","DIRECT TV SPORTS(SPAIN)","ESPN(USA)","ESPN VIVO 2(SPA)","EUROSPORT 1(RUS)","EUROSPORT 2(RUS)","FOX SPORTS 1(US)","FOX SPORTS 1(NL)","FOX SPORTS 1(SPA)","FOX SPORTS 2(US)",
"FOX SPORTS 2(SPA)","FOX SPORTS 2(NL)","GEO SUPER(ASIA)","GOL(SPA)","ITV 1(UK)","ITV 2(UK)","ITV 3(UK)","ITV 4(UK)","LALIGA TV(SPA)","MOVISTAR DEPORTES 1(SPA)","MOVISTAR DEPORTES 2(SPA)","MOVISTAR FORMULA 1(SPA)","MOVISTAR FUTBOL(SPA)","MOVISTAR GOLF(SPA)",
"MOVISTAR MOTOGP(SPA)","MUTV","NBA TV(USA)","NBCSN","NFL NETWORK(USA)","PREMIER SPORTS(UK)","PTV SPORTS(PAK)","RACING(UK)","REAL MADRID TV(SPA)","SKY SPORTS 1(UK)","SKY SPORTS 2(UK)","SKY SPORTS 3(UK)","SKY SPORTS 4(UK)","SKY SPORTS 5(UK)","SKY SPORTS F1(UK)","SKY SPORTS MIX(UK)",
"SKY SPORTS NEWS(UK)","SKY SPORTS NEWS(UK)","SONY SIX(ASIA)","SPORTSNET ONE(CAN)","SPORTSNET ONTARIO(CAN)","SPORTSNET WORLD(CAN)","STAR SPORTS 1(ASIA)","STAR SPORTS 2(ASIA)","STAR SPORTS 3(ASIA)","STAR SPORTS 4(ASIA)","SUPERSPORT 1(ALB)","SUPERSPORT 2(ALB)","SUPERSPORT 3(ALB)","SUPERSPORT 4(ALB)",
"SUPERSPORT 5(ALB)","TELEDEPORTE(SPA)","TEN 2(ASIA)","TEN CRICKET(ASIA)","TEN SPORTS(ASIA)","TRT SPOR(TUR)","TSN 1(CAN)","TSN 3(CAN)","TYC SPORTS(ARG)","WWE NETWORK(USA)","ZIGGO SPORT SELECT(NETH)"]
list_channel_url=["http://cinestrenostv.tv/canales/envivo/barcatv.html","http://cricfree.sx/update/bbc1.php","http://cricfree.sx/update/bbc2.php","http://www.filmon.tv/tv/channel/export?channel_id=113&affid=50442Nm","http://www.filmon.com/tv/channel/export?channel_id=103","http://cricfree.tv/update/boxnation.phphttp://v2.ustreamix.com/stream.php?id=bravo-tv",
"http://cricfree.sx/update/euro.php","http://cricfree.sx/update/euro2.php","http://cricfree.cc/update/bt1.php","http://cricfree.cc/update/bt2.php","http://www.cricfree.cc/bt-sport-3live-streaming","http://cricfree.sx/update/espn.php","http://cinestrenostv.tv/canales/envivo/sport1.html","http://www.filmon.com/tv/channel/export?channel_id=65","http://www.filmon.com/tv/channel/export?channel_id=22",
"http://cricfree.tv/update/chelsea.php","http://cinestrenostv.tv/canales/envivo/directv.html","http://cricfree.sx/update/espnusa.php","http://cinestrenostv.tv/canales/envivo/espn2.html","http://www.tv-sport-hd.com/channel/eurosport.html","http://www.tv-sport-hd.com/channel/eurosport2.html","http://cricfree.sx/update/fox1.php","http://freecalcio.eu/player.php?id=fox1-2&width=700&height=400","http://cinestrenostv.tv/canales/envivo/foxsports1.html",
"http://cricfree.sx/update/fox2.php","http://cinestrenostv.tv/canales/envivo/foxsports2.html","http://freecalcio.eu/player.php?id=fox2-2&width=700&height=400","http://c247.tv/live.php?ch=Geo_Super&vw=620&vh=490&domain=embed.crichd.com","http://cinestrenostv.tv/canales/envivo/goltv.html","http://www.filmon.tv/tv/channel/export?channel_id=11&autoPlay=1","http://www.filmon.com/tv/channel/export?channel_id=67&affid=44505232","http://www.filmon.tv/tv/channel/export?channel_id=26&autoPlay=1",
"http://www.filmon.tv/tv/channel/export?channel_id=101&autoPlay=1","http://cinestrenostv.tv/canales/envivo/laliga123multi1.html","http://sportstvstream.me/frames/lfctvinner.php","http://cinestrenostv.tv/canales/deportes/plusdeportes.php","http://cinestrenostv.tv/canales/envivo/deportes2.html","http://cinestrenostv.tv/canales/envivo/formula1.html","http://cinestrenostv.tv/canales/envivo/plusfutbol.html","http://cinestrenostv.tv/canales/envivo/plusgolf.html","http://cinestrenostv.tv/canales/envivo/motogp.html",
"http://cricfree.sx/update/mutv.php","http://www.liveonlinetv247.net/embed/nbatv.php?width=650&height=480","http://cricfree.sc/update/nbcsn.php","http://cricfree.sx/update/nflnetwork.php","http://cricfree.sx/update/premiersports.php","http://cricfree.sc/update/ptvsports.php","http://cricfree.sc/update/ukrace.php","http://cinestrenostv.tv/canales/envivo/realmadrid.html","http://cricfree.cc/update/sky1.php","http://cricfree.cc/update/sky2.php","http://www.cricfree.cc/update/sky3.php","http://cricfree.cc/update/sky4.php",
"http://cricfree.cc/update/sky5.php","http://cricfree.sx/update/skysf1.php","http://crichd.tv/update/skysmix.php","http://cricfree.sx/update/news.php","http://c247.to/live.php?ch=Sony_Six&vw=650&vh=450&domain=desistream.in","http://cricfree.sx/update/snone.php","http://cricfree.sx/update/snontario.php","http://cricfree.sx/update/setcafl.php","http://c247.tv/live.php?ch=Star_Sports1&vw=650&vh=480&domain=desistream.in","http://cricfree.sx/update/starsports2.php","http://embed247.com/live.php?ch=Star_Sports3&vw=600&vh=400&domain=desistream.in",
"http://cricfree.sx/update/starsports4.php","http://sportstvstream.me/frames/supersport1inner.php","http://sportstvstream.me/frames/supersport2inner.php","http://sportstvstream.me/frames/supersport3inner.php","http://sportstvstream.me/frames/supersport4inner.php","http://sportstvstream.me/frames/supersport5inner.php","http://cinestrenostv.tv/canales/envivo/teledeporte.html","http://c247.tv/live.php?ch=Ten_Action&vw=620&vh=490&domain=embed.crichd.com","http://embed247.com/live.php?ch=Ten_Cricket&vw=600&vh=400&domain=desistream.in",
"http://c247.to/live.php?ch=Ten_Sports&vw=650&vh=450&domain=desistream.in","http://tv-live.in/wp-content/uploads/tv-online/Channel/Turkey/Channel/TRT%203%20Sport%20live.html","http://cricfree.sx/update/tsn1.php","http://cricfree.sx/update/tsn2.php","http://sportstvstream.me/frames/tsn3inner.php","http://cinestrenostv.tv/canales/envivo/tycsports.html","http://crichd.tv/update/wwe.php","http://sportstvstream.me/frames/ziggosportselectinner.php"]


"""making command parsers"""
url_dict=dict() 
l=len(list_channel)
for i in range(l):
	url_dict[i]=list_channel_url[i]
def stream(code):
	print("Streaming in a web page...")
	webbrowser.open(url_dict[code])
def showchannels():
	print(("Total available channels {0} ").format(l))
	print("Codes to stream channel")
	for i in range(len(list_channel)):
		print("[",i,"] ",list_channel[i])
def RepresentsInt(s):
    try: 
        int(s)>=0 and int(s)<=l
        return True
    except ValueError:
        return False


"""python dict to store channel urls according to codes"""
def parser_error(errmsg):
	print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
	print("Error: " + errmsg)
	sys.exit()        
def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -stream 32")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-stream ChannelCode','-STREAM ChannelCode',help="Runs the channel in a webpage", required=True)
    parser.add_argument('-show','-SHOW',help='Shows all the channel codes', nargs='?', default=False)
    return parser.parse_args()


if __name__ == '__main__':
	argument_string=' '.join(sys.argv[1:])
	
	
	if argument_string.lower()=='-show':
		showchannels()
	elif argument_string[0:7].lower()=="-stream" and RepresentsInt(argument_string[8:]):
		c=int(argument_string[8:])
		stream(c)
	else:  
		parse_args()  
	