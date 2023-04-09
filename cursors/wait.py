#!/usr/bin/env python3

import os

POSITIONS = [
    (0, 0, 24, 24),
    (24, 0, 48, 24),
    (48, 0, 72, 24),
    (72, 0, 96, 24),
    (96, 0, 120, 24),
    (120, 0, 144, 24),
    (144, 0, 168, 24),
    (168, 0, 192, 24),
    (192, 0, 216, 24),
    (216, 0, 240, 24),
    (240, 0, 264, 24),
    (264, 0, 288, 24),
    (288, 0, 312, 24),
    (312, 0, 336, 24),
]

if __name__ == '__main__':
    os.system('mkdir -p png/x1')
    os.system('mkdir -p png/x1.5')
    os.system('mkdir -p png/x2')

    for idx, pos in enumerate(POSITIONS):
        num = str(idx + 1)
        if len(num) == 1:
            num = '0' + num
        x1 = pos[0]
        y1 = pos[1]
        x2 = pos[2]
        y2 = pos[3]

        os.system(f'inkscape --export-filename=png/x1/wait-{num}.png --export-area={x1}:{y1}:{x2}:{y2} --export-width=24 --export-height=24 src/wait-src-resample.svg')
        os.system(f'inkscape --export-filename=png/x1.5/wait-{num}.png --export-area={x1}:{y1}:{x2}:{y2} --export-width=36 --export-height=36 src/wait-src-resample.svg')
        os.system(f'inkscape --export-filename=png/x2/wait-{num}.png --export-area={x1}:{y1}:{x2}:{y2} --export-width=48 --export-height=48 src/wait-src-resample.svg')

