#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from Constants import *
from PIL import Image, ImageDraw, ImageFont

def clamp(minVal, val, maxVal):
    return max(minVal, min(val, maxVal))

def main(argc, argv):
    font = ImageFont.truetype(FONT_TYPE, FONT_SIZE)
    rows = MAX_POKEMON_COUNT
    columns = MAX_POKEMON_COUNT

    startRow = 0
    startColumn = 0

    if argc == 2:
        columns, rows = [clamp(1, int(i), MAX_POKEMON_COUNT) if i.isnumeric() else MAX_POKEMON_COUNT for i in argv]

    if argc == 4:
        startColumn, startRow = [clamp(0, int(argv[i * 2]) - 1, MAX_POKEMON_COUNT) if argv[i * 2] else MAX_POKEMON_COUNT for i in range(2)]
        columns, rows = [clamp(1, int(argv[i * 2 + 1]), MAX_POKEMON_COUNT) if argv[i * 2 + 1] else MAX_POKEMON_COUNT for i in range(2)]

    background = Image.open("./Assets/background.png").convert("RGBA")
    finalW, finalH = (SPRITE_WIDTH * (columns + 1), SPRITE_HEIGHT * (rows + 1) + BOTTOM_DELTA)
    final = Image.new("RGBA", (finalW, finalH))
    draw = ImageDraw.Draw(final)
    
    if not os.path.exists(MERGED_DIR):
        os.makedirs(MERGED_DIR)

    origin = Image.open("./Assets/origin.png").convert("RGBA")
    final.paste(origin, (0, 0, 340, 340))

    # Draw background first

    for i in range(columns + 1):
        for j in range(rows + 1):
            x, y = (i * SPRITE_WIDTH, j * SPRITE_HEIGHT)
            final.paste(background, (x, y, x + SPRITE_WIDTH, y + SPRITE_HEIGHT))

    cellWidth = background.size[0]
    croppedCell = background.crop((0, 0, cellWidth, BOTTOM_DELTA))
    
    for i in range(columns + 1):
        x, y = (SPRITE_WIDTH * i, SPRITE_HEIGHT * (rows + 1))
        final.paste(croppedCell, (x, y, x + cellWidth, y + BOTTOM_DELTA))

    # Plop origin cell down

    origin = Image.open("./Assets/origin.png").convert("RGBA")
    final.paste(origin, (0, 0, 340, 340))
    
    # Draw sprites and text

    for i in reversed(range(startColumn, min(startColumn + columns, MAX_POKEMON_COUNT) + 1)):
        for j in reversed(range(startRow, min(startRow + rows, MAX_POKEMON_COUNT) + 1)):
            if not (i == j == 0 or (i == startColumn and j == startRow)):
                pokeName = ""
                fileName = ""
                body = 0
                face = 0
                red = 0

                if i == startColumn or j == startRow:
                    red = 255
                    index = j if i == startColumn else i
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

                x, y = (SPRITE_WIDTH * (i - startColumn), SPRITE_HEIGHT * (j - startRow))
                width, height = current.size
                deltaX, deltaY = (round((SPRITE_WIDTH - width) / 2), round((SPRITE_HEIGHT - height) / 2))
      
                final.paste(current, (x + deltaX, y + deltaY, x + deltaX + width, y + deltaY + height), current)
                                   
                w, h = draw.textsize(text, font=font)
                draw.text((x + (SPRITE_WIDTH - w) / 2, y + (SPRITE_HEIGHT - 33)), text, fill=(red,0,0,255), font=font)

    # Finally, draw credits

    credits = "「PokeFusion 2015 | Poster Generator: Alex Mueller | Sprites & Website: Alex Onsager @ https://pokemon.alexonsager.net」"
    f = ImageFont.truetype(FONT_TYPE, int(FONT_SIZE * 2 / 5))
    w, h = draw.textsize(credits, font=f)
    delta = (BOTTOM_DELTA - h) / 2
    x, y = ((finalW - w) / 2, finalH - h - delta)
    draw.text((x, y), credits, fill=(150, 150, 150, 255), font=f)

    print("Saving...")
    final.save('%s/PokeFusionsPoster(%ix%i)[rowStart=%s, columnStart=%s].png' % (MERGED_DIR, columns, rows, POKEMON[startRow], POKEMON[startColumn]))
    print("Finished!")

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])