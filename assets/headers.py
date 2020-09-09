#!/usr/bin/python3

from assets.properties import clear_screen
from assets.desgins import logo, author
import os


def modules_header():
    from assets.banners import modules_banner
    os.system(clear_screen)
    print(logo)
    print(modules_banner)
    print(author)


def scripts_header():
    from assets.banners import scripts_banner
    os.system(clear_screen)
    print(logo)
    print(scripts_banner)
    print(author)


def extracting_header():
    from assets.banners import extracting_banner
    os.system(clear_screen)
    print(logo)
    print(extracting_banner)
    print(author)


def link_extractor_header():
    from assets.banners import link_extractor_banner
    os.system(clear_screen)
    print(logo)
    print(link_extractor_banner)
    print(author)
