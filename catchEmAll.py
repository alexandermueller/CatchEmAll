#!/usr/bin/python

#######################
#                     #
# Gotta Catch 'Em All #
#     Pokefusion      #
#    Alex Mueller     #
#                     #
#######################

from lxml import html
import requests
import urllib

pokemon = ["Missingno.","Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran(f)","Nidorina","Nidoqueen","Nidoran(m)","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetchd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
prefixes = ["Miss","Bulb","Ivy","Venu","Char","Char","Char","Squirt","War","Blast","Cater","Meta","Butter","Wee","Kak","Bee","Pid","Pidg","Pidg","Rat","Rat","Spear","Fear","Ek","Arb","Pika","Rai","Sand","Sand","Nido","Nido","Nido","Nido","Nido","Nido","Clef","Clef","Vul","Nine","Jiggly","Wiggly","Zu","Gol","Odd","Gloo","Vile","Pa","Para","Veno","Veno","Dig","Dug","Meow","Per","Psy","Gol","Man","Prime","Grow","Arca","Poli","Poli","Poli","Ab","Kada","Ala","Ma","Ma","Ma","Bell","Weepin","Victree","Tenta","Tenta","Geo","Grav","Gol","Pony","Rapi","Slow","Slow","Magne","Magne","Far","Do","Do","See","Dew","Gri","Mu","Shell","Cloy","Gas","Haunt","Gen","On","Drow","Hyp","Krab","King","Volt","Electr","Exegg","Exegg","Cu","Maro","Hitmon","Hitmon","Licki","Koff","Wee","Rhy","Rhy","Chan","Tang","Kangas","Hors","Sea","Gold","Sea","Star","Star","Mr.","Scy","Jyn","Electa","Mag","Pin","Tau","Magi","Gyara","Lap","Dit","Ee","Vapor","Jolt","Flare","Pory","Oma","Oma","Kabu","Kabu","Aero","Snor","Artic","Zap","Molt","Dra","Dragon","Dragon","Mew","Mew"]
postfixes = ["ssingno.","basaur","ysaur","usaur","mander","meleon","izard","tle","tortle","toise","pie","pod","free","dle","una","drill","gey","eotto","eot","tata","icate","row","row","kans","bok","chu","chu","shrew","slash","oran","rina","queen","ran","rino","king","fairy","fable","pix","tales","puff","tuff","bat","bat","ish","oom","plume","ras","sect","nat","moth","lett","trio","th","sian","duck","duck","key","ape","lithe","nine","wag","whirl","wrath","ra","bra","kazam","chop","choke","champ","sprout","bell","bell","cool","cruel","dude","eler","em","ta","dash","poke","bro","mite","ton","fetchd","duo","drio","eel","gong","mer","uk","der","ster","tly","ter","gar","ix","zee","no","by","ler","orb","ode","cute","utor","bone","wak","lee","chan","tung","fing","zing","horn","don","sey","gela","khan","sea","dra","deen","king","yu","mie","mime","ther","nx","buzz","mar","sir","ros","karp","dos","ras","to","vee","eon","eon","eon","gon","nyte","star","to","tops","dactyl","lax","cuno","dos","tres","tini","nair","nite","two","ew"]

getter = urllib.URLopener()
for i in range(152):
    for j in range(152):
        name = ""
        url = "http://images.alexonsager.net/pokemon/fused/%d/%d.%d.png" % (i, i, j)
        
        if i == j:
            name = pokemon[i]
        else:
            name = "%s%s" % (prefixes[j], postfixes[i]) # The link is backwards from the way the names are made, including how the fusion works

        print "(%03d,%03d) %s" % (i, j, name)

        if i == 0:
            i = 152
        if j == 0:
            j = 152

        filename = "./pokemon/(%03d,%03d)[%s].png" % (i, j, name)

        if i == 152:
            i = 0
        if j == 152:
            j = 0

        getter.retrieve(url, filename)