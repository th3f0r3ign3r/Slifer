from lib.mycolors import *
from os import path as os_path
from re import search
from requests import get


def warnings(message):
    return print(red + "Warning: " + reset + message)


def info(message):
    return print(green + "Info: " + reset + message)


def validateUrl(url):
    address = ("^((http|https)://)(www.)?" +
               "[a-zA-Z0-9@:%._\\+~#?&//=]" +
               "{2,256}\\.[a-z]" +
               "{2,6}\\b([-a-zA-Z0-9@:%" +
               "._\\+~#?&//=]*)")
    ip = ("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])" +
          "\\b([-a-zA-Z0-9@: %" +
          "._\\+~#?&//=]*)" + "$")

    address = compile(address)
    ip = compile(ip)

    if search(address, url):
        return True
    elif search(ip, url):
        return True
    else:
        return False


def checkTarget(url):
    try:
        r = get(url)
        return r.ok
    except:
        return warnings("Something went wrong with the target")


def getWordlist(wordlist):
    try:
        if os_path.isfile(wordlist):
            with open(wordlist, 'r') as file:
                WORDLIST = [line for line in file.readlines()]
                WORDLIST_COUNT = len(WORDLIST)
                return (WORDLIST, WORDLIST_COUNT)
    except:
        warnings("Something went wrong with the wordlist")
