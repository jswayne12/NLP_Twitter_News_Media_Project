import numpy as np
conservative_news = [
    {'entity':'OANN','twitter':'OANN'},
    {'entity':'Fox', 'twitter':'FoxNews'},
    {'entity':'NewsmaxTV','twitter':'newsmax'},
    {'entity':'Washington Examiner','twitter':'dcexaminer'},
    {'entity':'Washington Times','twitter':'WashTimes'},
    {'entity':np.array([3,5,3,1,1,0]),'twitter':''}
]

conservative_alt = [
    {'entity':'Sean Hannity','twitter':'seanhannity'},
    {'entity':'GOP', 'twitter':'GOP'},
    {'entity':'Tucker Carlson', 'twitter':'TuckerCarlson'},
    {'entity':'Breitbart', 'twitter':'BreitbartNews'},
    {'entity':'Laura Ingraham', 'twitter':'IngrahamAngle'},
    {'entity':'Glenn Beck','twitter':'glennbeck'},
    {'entity':'The Daily Wire', 'twitter':'realDailyWire'},
    {'entity':"Bill O'Reilly", 'twitter':'BillOReilly'},
    {'entity':'Ben Shapiro', 'twitter':'benshapiro'},
    {'entity':'Dave Rubin', 'twitter':'RubinReport'},
    {'entity':np.array([3,2,3,1,3,2,1,2,2,1,0]), 'twitter':''}
]

conservative_politicians = [
    {'entity':'Ted Cruz','twitter': 'tedcruz'},
    {'entity':'Rand Paul', 'twitter':'RandPaul'},
    {'entity':'Lindsey Graham','twitter':'LindseyGrahamSC'},
    {'entity':'Jim Jordan','twitter':'Jim_Jordan'},
    {'entity':'Louie Gohmert', 'twitter':'replouiegohmert'},
    {'entity':'Mitch McConnell', 'twitter':'LeaderMcConnell'},
    {'entity':'Tom Cotton','twitter':'SenTomCotton'},
    {'entity':'Kevin McCarthy', 'twitter':'GOPLeader'},
    {'entity':'Lauren Boebert','twitter':'laurenboebert'},
    {'entity':'Mitt Romney', 'twitter':'MittRomney'},
    {'entity':np.array([4,1,2,2,1,2,1,2,1,2,0]), 'twitter':''}
]
moderate_news = [
    {'entity':'ABC News','twitter':'ABC'},
    {'entity':'CNN','twitter':'CNN'},
    {'entity':'NBC News', 'twitter':'NBCNews'},
    {'entity':'Wall Street Journal', 'twitter':'WSJ'},
    {'entity':'CBS News', 'twitter':'CBSNews'},
    {'entity':np.array([3,5,2,4,1,0]), 'twitter':''}
]
moderate_politicians = [
    {'entity':'Nancy Pelosi', 'twitter':'SpeakerPelosi'},
    {'entity':'Kamala Harris', 'twitter':'VP'},
    {'entity':'Chuck Schumer', 'twitter':'SenSchumer'},
    {'entity':'Dick Durbin', 'twitter':'SenatorDurbin'},
    {'entity':'Joe Manchin', 'twitter':'Sen_JoeManchin'},
    {'entity':'Adam Schiff', 'twitter':'RepAdamSchiff'},
    {'entity':'Senate Democrats', 'twitter':'SenateDems'},
    {'entity':'House Democrats', 'twitter':'HouseDemocrats'},
    {'entity':'Joe Biden', 'twitter':'POTUS'},
    {'entity':'Joe Neguse', 'twitter':'RepJoeNeguse'},
    {'entity':np.array([3,4,3,2,1,3,2,2,3,1,0]), 'twitter':''},
]

liberal_news = [
    {'entity':'MSNBC', 'twitter':'MSNBC'},
    {'entity':'New York Times', 'twitter':'nytimes'},
    {'entity':'NPR','twitter':'NPR'},
    {'entity':'The Washington Post','twitter':'washingtonpost'},
    {'entity':'Huffpost', 'twitter':'HuffPost'},
    {'entity':np.array([1,5,2,3,2,0]),'twitter':''}
]

liberal_alt = [
    {'entity':'The Young Turks', 'twitter':'TheYoungTurks'},
    {'entity':'Secular Talk', 'twitter':'KyleKulinski'},
    {'entity':'The David Pakman Show', 'twitter':'davidpakmanshow'},
    {'entity':'The Majority Report', 'twitter':'majorityfm'},
    {'entity':'Democracy Now', 'twitter':'democracynow'},
    {'entity':'Daily Kos', 'twitter':'dailykos'},
    {'entity':'Thom Hartmann', 'twitter':'Thom_Hartmann'},
    {'entity':'The Humanist Report', 'twitter':'HumanistReport'},
    {'entity':'Current Affairs', 'twitter':'curaffairs'},
    {'entity':'AlterNet', 'twitter':'AlterNet'},
    {'entity':np.array([3,2,1,1,4,2,1,1,1,1,0]), 'twitter':''},
]

liberal_politicians = [
    {'entity':'Bernie Sanders','twitter':'BernieSanders'},
    {'entity':'Elizabeth Warren', 'twitter':'ewarren'},
    {'entity':'AOC', 'twitter':'AOC'},
    {'entity':'Cory Booker', 'twitter':'CoryBooker'},
    {'entity':'Pete Buttigieg', 'twitter':'PeteButtigieg'},
    {'entity':'Rashida Tlaib', 'twitter':'RashidaTlaib'},
    {'entity':'Ilhan Omar', 'twitter':'IlhanMN'},
    {'entity':'Ayanna Pressley', 'twitter':'AyannaPressley'},
    {'entity':'Jamaal Bowman', 'twitter':'JamaalBowmanNY'},
    {'entity':'Cori Bush', 'twitter':'CoriBush'},
    {'entity':np.array([4,3,4,3,2,2,2,2,1,1,0]), 'twitter':''},
]