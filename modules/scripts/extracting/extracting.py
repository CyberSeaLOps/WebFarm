#!/usr/bin/python3

from assets.shortcuts import Exit
from assets.prefixes import webfarm_prefix, invalid_input_prefix
from assets.headers import extracting_header


class Extracting:
    def __init__(self):
        try:
            extracting_header()
            print('Scripts:')
            print('\n\t1): Link Extractor')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                scripts_select = input(webfarm_prefix).lower()
                if scripts_select == '1':
                    from modules.scripts.extracting.link_extractor import LinkExtractor
                    LinkExtractor()
                elif scripts_select == 'z':
                    from modules.modules import Modules
                    Modules()
                elif scripts_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
        except KeyboardInterrupt:
            Exit()
