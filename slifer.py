#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import system
from lib.utils import *
from argparse import ArgumentParser
from lib.mycolors import *

NAME = "Slifer"

HEADER = """
  .--.--.     ,--,                                        
 /  /    '. ,--.'|     ,--,     .--.,                     
|  :  /`. / |  | :   ,--.'|   ,--.'  \            __  ,-. 
;  |  |--`  :  : '   |  |,    |  | /\/          ,' ,'/ /| 
|  :  ;_    |  ' |   `--'_    :  : :     ,---.  '  | |' | 
 \  \    `. '  | |   ,' ,'|   :  | |-,  /     \ |  |   ,' 
  `----.   \|  | :   '  | |   |  : :/| /    /  |'  :  /   
  __ \  \  |'  : |__ |  | :   |  |  .'.    ' / ||  | '    
 /  /`--'  /|  | '.'|'  : |__ '  : '  '   ;   /|;  : |    
'--'.     / ;  :    ;|  | '.'||  | |  '   |  / ||  , ;    
  `--'---'  |  ,   / ;  :    ;|  : \  |   :    | ---'     
             ---`-'  |  ,   / |  |,'   \   \  /           
                      ---`-'  `--'      `----'"""

print(HEADER + '\n')


parser = ArgumentParser(
    description="The LFI exploitation tool by th3f0r31gn3r")
parser.add_argument('mode', metavar='MODE', choices=[
                    'fuzz', 'interactive'], help="The Brute-Force or Interactive mode")
parser.add_argument('--url', metavar='', type=str,
                    help='Target Url Page with parameter', required=True)
parser.add_argument('--wordlist', metavar='', type=str,
                    help='Wordlist file')
parser.add_argument('--version', help='Show version', action='version')
parser.version = NAME + " v1.0"
args = parser.parse_args()


def __construct():
    pass


def main():
    system('clear')

    print(HEADER)
    print("\n" + NAME + yellow + " LFI" + reset +
          " exploitation tool by " + blue + "th3f0r31gn3r" + reset +
          " - ✨ Let's dance and hack together ✨" + '\n')

    __construct()


if __name__ == "__main__":
    main()
