#!/usr/bin/python3

from assets.prefixes import webfarm_prefix, invalid_input_prefix
from assets.shortcuts import Exit
from assets.headers import modules_header


class Modules:
    def __init__(self):
        try:
            modules_header()
            print('Modules:')
            print('\n\t1): Scripts')
            print('\n\tX): Exit\n')
            while True:
                modules_select = input(webfarm_prefix).lower()
                if modules_select == '1':
                    from modules.scripts.scripts import Scripts
                    Scripts()
                elif modules_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
        except KeyboardInterrupt:
            Exit()
