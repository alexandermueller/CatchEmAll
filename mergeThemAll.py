#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont

# Pokemon Count is at most 152.
pokemonCount = 9
stdW, stdH = (240, 240)
W, H = (300, 300)
finalW, finalH = (W * (pokemonCount + 1), H * (pokemonCount + 1))
deltaX = 15
deltaY = 10
fontSize = 30
pokemon = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran(f)","Nidorina","Nidoqueen","Nidoran(m)","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetchd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew","Missingno."]
prefixes = ["Bulb","Ivy","Venu","Char","Char","Char","Squirt","War","Blast","Cater","Meta","Butter","Wee","Kak","Bee","Pid","Pidg","Pidg","Rat","Rat","Spear","Fear","Ek","Arb","Pika","Rai","Sand","Sand","Nido","Nido","Nido","Nido","Nido","Nido","Clef","Clef","Vul","Nine","Jiggly","Wiggly","Zu","Gol","Odd","Gloo","Vile","Pa","Para","Veno","Veno","Dig","Dug","Meow","Per","Psy","Gol","Man","Prime","Grow","Arca","Poli","Poli","Poli","Ab","Kada","Ala","Ma","Ma","Ma","Bell","Weepin","Victree","Tenta","Tenta","Geo","Grav","Gol","Pony","Rapi","Slow","Slow","Magne","Magne","Far","Do","Do","See","Dew","Gri","Mu","Shell","Cloy","Gas","Haunt","Gen","On","Drow","Hyp","Krab","King","Volt","Electr","Exegg","Exegg","Cu","Maro","Hitmon","Hitmon","Licki","Koff","Wee","Rhy","Rhy","Chan","Tang","Kangas","Hors","Sea","Gold","Sea","Star","Star","Mr.","Scy","Jyn","Electa","Mag","Pin","Tau","Magi","Gyara","Lap","Dit","Ee","Vapor","Jolt","Flare","Pory","Oma","Oma","Kabu","Kabu","Aero","Snor","Artic","Zap","Molt","Dra","Dragon","Dragon","Mew","Mew","Miss"]
postfixes = ["basaur","ysaur","usaur","mander","meleon","izard","tle","tortle","toise","pie","pod","free","dle","una","drill","gey","eotto","eot","tata","icate","row","row","kans","bok","chu","chu","shrew","slash","oran","rina","queen","ran","rino","king","fairy","fable","pix","tales","puff","tuff","bat","bat","ish","oom","plume","ras","sect","nat","moth","lett","trio","th","sian","duck","duck","key","ape","lithe","nine","wag","whirl","wrath","ra","bra","kazam","chop","choke","champ","sprout","bell","bell","cool","cruel","dude","eler","em","ta","dash","poke","bro","mite","ton","fetchd","duo","drio","eel","gong","mer","uk","der","ster","tly","ter","gar","ix","zee","no","by","ler","orb","ode","cute","utor","bone","wak","lee","chan","tung","fing","zing","horn","don","sey","gela","khan","sea","dra","deen","king","yu","mie","mime","ther","nx","buzz","mar","sir","ros","karp","dos","ras","to","vee","eon","eon","eon","gon","nyte","star","to","tops","dactyl","lax","cuno","dos","tres","tini","nair","nite","two","ew","ssingno."]
font = ImageFont.truetype("arial.ttf", fontSize)

background = Image.open("./Assets/background.png").convert("RGBA")
final = Image.new("RGBA", (finalW, finalH))
draw = ImageDraw.Draw(final)

pokemonCount = 152 if pokemonCount > 152 or pokemonCount < 0 else pokemonCount

for i in xrange(0, pokemonCount + 1):
    for j in xrange(0, pokemonCount + 1):
        if not (i == j == 0):
            pokeName = ""
            fileName = ""
            body = 0
            face = 0
            red = 0
            if i == 0 or j == 0:
                red = 255
                index = j + i
                pokeName = pokemon[index - 1]
                text = "%03d. %s" % (index, pokeName)
                body = index
                face = index
            elif i == j:
                red = 255
                text = pokeName = pokemon[i - 1]
                body = face = i
            else:
                body = i
                face = j
                text = pokeName = "%s%s" % (prefixes[j - 1], postfixes[i - 1])

            print "Adding: (%03d,%03d)[%s].png" % (body, face, pokeName)
            filename = "./pokemon/(%03d,%03d)[%s].png" % (body, face, pokeName)
            current = Image.open(filename).convert("RGBA")

            x, y = (W * i, H * j)
            final.paste(background, (x, y, x + 300, y + 300))
            final.paste(current, (x + deltaX, y + deltaY, x + deltaX + stdW, y + deltaY + stdH), current)
                               
            w, h = draw.textsize(text, font=font)
            draw.text((x + (W - w)/2, y + (H - 33)), text, fill=(red,0,0,255), font=font)

origin = Image.open("./Assets/origin.png").convert("RGBA")
final.paste(origin, (0, 0, 340, 340))
print "Saving..."
final.save('Merged Poster/PokeFusionsPoster.png')
print "Finished!"
# final.show()