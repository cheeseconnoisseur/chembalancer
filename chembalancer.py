import numpy as np
from chempy import balance_stoichiometry
import urllib.request
import urllib.parse
#import re
#import bs4
from bs4 import BeautifulSoup as soup
import pandas as pd



def balancer():
    print("#######################################")
    print("superbeta")
    print("enter")
    print("#######################################")
    lol = input(":")
    lol = lol.replace(" ","")
    print(lol)
    loll = []
    lolff = []
    lolss = []
    loll = lol.split("=")
    print(loll)
    lolf = loll[0]
    print(lolf)
    lols = loll[1]
    print(lols)
    lolff = lolf.split("+")
    lolss = lols.split("+")
    print(lolff)

    if len(lolff) == 2 and len(lolss) == 1:
        reac, prod = balance_stoichiometry({lolff[0], lolff[1]}, {lolss[0]})
    elif len(lolff) == 2 and len(lolss) == 2:
        reac, prod = balance_stoichiometry({lolff[0], lolff[1]}, {lolss[0], lolss[1]})
    elif len(lolff) == 2 and len(lolss) == 3:
        reac, prod = balance_stoichiometry({lolff[0], lolff[1]}, {lolss[0], lolss[1], lolss[2]})
    elif len(lolff) == 2 and len(lolss) == 4:
        reac, prod = balance_stoichiometry({lolff[0], lolff[1]}, {lolss[0], lolss[1], lolss[2], lolss[3]})    
    elif len(lolff) == 3 and len(lolss) == 1:
        reac, prod = balance_stoichiometry({lolff[0], lolff[1], lolff[2]}, {lolss[0]})
    elif len(lolff) == 3 and len(lolss) == 1:
        reac, prod = balance_stoichiometry({lolff[0], lolff[1], lolff[2]}, {lolss[0]})
    else:
        print("error occured with equation: ",lol)
    print("reactants = ",reac)
    print("products = ", prod)
    print("overall : ",reac, " = ", prod)
    main()

def allels():
    link = "https://en.wikipedia.org/wiki/List_of_chemical_elements"
    #link = "https://www.google.com"
    f = urllib.request.urlopen(link)
    myfile = f.read()
    f.close()
    #page_soup = soup(myfile, "html.parser")
    #table = page_soup.findAll("div",{"class":"mw-parser-output"})
    #paragraphs = re.findall(r'<td>(.*?)</td>',str(myfile))
    table = pd.read_html(link)
    #print(table[1][1])
    n=0
    for el in table[1][1][1:]:
        n=n+1
        try:
            print(n-1,el," ", table[1][2][n])
        except:

            continue
    main()

def main():
    inp = input("look at symbols (ls) or balance equating (bq)")
    if inp in("ls","LS","look at symbols","LOOK AT SYMBOLS"):
        allels()
    elif inp in("bq","BQ","balance equations","BALANCE EQUATIONS"):
        balancer()

main()
