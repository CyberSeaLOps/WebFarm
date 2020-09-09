#!/usr/bin/python3

from assets.properties import clear_screen
from assets.desgins import logo, author
from assets.banners import scripts_banner
import os


def modules_header():
    os.system(clear_screen)
    print(logo)
    print(author)


def scripts_header():
    os.system(clear_screen)
    print(logo)
    print(scripts_banner)
    print(author)
