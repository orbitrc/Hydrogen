#!/usr/bin/env python3

import os

LINKS = (
    ('arrow', 'default'),
    ('arrow', 'left_ptr'),
    # ('closedhand', 'dnd-move'),
    # ('closedhand', 'dnd-none'),
    # ('closedhand', 'grabbing'),
    # ('closedhand', 'move'),
    # ('closedhand', 'fcf21c00b30f7e3f83fe0dfd12e71cff'),
    # ('copy', 'dnd-copy'),
    # ('copy', '1081e37283d90000800003c07f3ef6bf'),
    # ('copy', '6407b0e94181790501fd1e167b474872'),
    # ('copy', 'b66166c04f8c3109214a4fbd64a50fc8'),
    # ('cross', 'crosshair'),
    # ('cross', 'tcross'),
    # ('crossed_circle', 'circle'),
    # ('crossed_circle', 'not-allowed'),
    # ('crossed_circle', '03b6e0fcb3499374a867c041f52298f0'),
    ('split_hor', 'split_h'),
    ('split_ver', 'split_v'),
)

if __name__ == '__main__':
    for l in LINKS:
        src = l[0]
        dst = l[1]
        os.system(f'ln -sf {src} Hydrogen/cursors/{dst}')

