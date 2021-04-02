#!/usr/bin/env python3

import os
import sys
from Constants import *
from PIL import Image, ImageDraw, ImageFont

def main(argc, argv):
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    rows = MAX_POKEMON_COUNT
    columns = MAX_POKEMON_COUNT

    if argc == 2:
        columns, rows = [max(1, min(int(i), MAX_POKEMON_COUNT)) if i.isnumeric() else MAX_POKEMON_COUNT for i in argv]

    background = Image.open("./Assets/background.png").convert("RGBA")
    finalW, finalH = (SPRITE_WIDTH * (columns + 1), SPRITE_HEIGHT * (rows + 1) + BOTTOM_DELTA)
    final = Image.new("RGBA", (finalW, finalH))
    draw = ImageDraw.Draw(final)
    
    if not os.path.exists(MERGED_DIR):
        os.makedirs(MERGED_DIR)

    for i in range(columns + 1):
        for j in range(rows + 1):
            if not (i == j == 0):
                pokeName = ""
                fileName = ""
                body = 0
                face = 0
                red = 0
                if i == 0 or j == 0:
                    red = 255
                    index = j + i
                    pokeName = POKEMON[index - 1]
                    text = "%03d. %s" % (index, pokeName)
                    body = index
                    face = index
                elif i == j:
                    red = 255
                    text = pokeName = POKEMON[i - 1]
                    body = face = i
                else:
                    body = i
                    face = j
                    text = pokeName = "%s%s" % (PREFIXES[j - 1], SUFFIXES[i - 1])

                print("Adding: (%03d,%03d)[%s].png" % (body, face, pokeName))
                filename = "./Assets/Sprites/(%03d,%03d)[%s].png" % (body, face, pokeName)
                current = Image.open(filename).convert("RGBA")

                x, y = (SPRITE_WIDTH * i, SPRITE_HEIGHT * j)
                width, height = current.size
                deltaX, deltaY = (round((SPRITE_WIDTH - width) / 2), round((SPRITE_HEIGHT - height) / 2))
                
                final.paste(background, (x, y, x + SPRITE_WIDTH, y + SPRITE_HEIGHT))
                final.paste(current, (x + deltaX, y + deltaY, x + deltaX + width, y + deltaY + height), current)
                                   
                w, h = draw.textsize(text, font=font)
                draw.text((x + (SPRITE_WIDTH - w) / 2, y + (SPRITE_HEIGHT - 33)), text, fill=(red,0,0,255), font=font)

    width = background.size[0]
    cropped = background.crop((0, 0, width, BOTTOM_DELTA))
    
    for i in range(columns + 1):
        x, y = (SPRITE_WIDTH * i, SPRITE_HEIGHT * (rows + 1))
        final.paste(cropped, (x, y, x + width, y + BOTTOM_DELTA))

    origin = Image.open("./Assets/origin.png").convert("RGBA")
    final.paste(origin, (0, 0, 340, 340))

    attribution = "Poster: Alex Mueller | Sprites: Alex Onsager"
    f = ImageFont.truetype("arial.ttf", int(FONT_SIZE * 2 / 5))
    w, h = draw.textsize(attribution, font=f)
    delta = (BOTTOM_DELTA - h) / 2
    x, y = ((finalW - w) / 2, finalH - h - delta)
    draw.text((x, y), attribution, fill=(100, 100, 100, 255), font=f)

    print("Saving...")
    final.save('%s/PokeFusionsPoster(%ix%i).png' % (MERGED_DIR, rows, columns))
    print("Finished!")

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])