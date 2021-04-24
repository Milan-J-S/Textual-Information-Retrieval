#Assignment 3
import os
import re
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.tree import Tree
import nltk

info = {}

specs = ["Manufacturer","Model","Camera Resolution","Lens Aperture","Front Camera Resolution","Video Recording","Screen Resolution","Screen Size","Battery Capacity","OS","RAM","Storage","Processor","Price" ]

text = []
cleaned_text = []
for _,_,f in os.walk('corpus'):
    for f1 in f:
        fil = open('corpus/'+f1,"r",encoding='latin1')
        text.append(re.findall('[^\<].+[^\>]',fil.read()))




for i in range(len(text)):
    info = {}
    ne_in_sent = {}
    for item in text[i]:
        ne_tree = ne_chunk(pos_tag(word_tokenize(item)))
        for subtree in ne_tree:
            if type(subtree) == Tree: 
                ne_label = subtree.label()
                ne_string = " ".join([token for token, pos in subtree.leaves()])
                #print(ne_string,ne_label)
                if(ne_string not in ne_in_sent):
                    ne_in_sent[ne_string] = 0
                ne_in_sent[ne_string]+=1

    #print(ne_in_sent)
    #print(sorted(ne_in_sent,reverse = True,key = ne_in_sent.get))
    features = sorted(ne_in_sent,reverse = True,key = ne_in_sent.get)

    info['Manufacturer'] = features[0]
    info['Model'] = features[1]
    if(re.match('[0-9]|\ ',features[0])):
         pass
    elif(re.search('[0-9]|\ ',features[0])):
         info['Model'] = features[0]
         info['Manufacturer'] = features[1]
    if((len(features[1]) > len(features[0])) and not re.search('[0-9]|\ ',features[1])):
         #print(features[1])
         info['Model'] = features[0]
         info['Manufacturer'] = features[1]

    t = text[i]
    for item in t:
        ram = re.findall(r'[0-9][A-Za-z0-9]+\ of\ ram',item.lower())
        if(ram != []):
            info['RAM'] = ram[0].split()[0]
        storage = re.findall(r'[A-Za-z0-9]+\ of\ storage',item.lower())
        if(storage != []):
            info['Strorage'] = storage[0].split()[0]
        aperture = re.findall(r'f[\/0-9\.]+\ lens',item.lower())
        if(aperture != []):
            info['Lens Aperture'] = aperture[0].split()[0]
        cam = re.findall(r'[0-9\.]+.?mp|[0-9\.]+.?megapixel',item.lower())
        if(cam != []):
            info['Camera Resolution'] = cam[0].split()[0]
        front = re.findall(r'[0-9]+mp.*front|[0-9]+.?megapixel.*front',item.lower())
        if(front != []):
            info['Front Camera Resolution'] = front[0].split()[0]
        screen = re.findall(r'[0-9][0-9\.]+.?in[^\.]*display|[0-9][0-9\.]+.?inch.*screen',item.lower())
        if(screen != []):
            info['Screen Size'] = screen[0].split()[0]
        screenres = re.findall(r'[0-9]+p[^\.]*display|[0-9]+p[^\.]*screen',item.lower())
        if(screenres == []):
            screenres = re.findall(r'[FQW][A-Z]+[^\.]*display|[FQW][A-Z]+[^\.]*screen',item)
        if(screenres != []):
            info['Screen Resolution'] = screenres[0].split()[0]
        battery = re.findall(r'[0-9][0-9,]+mah.*battery',item.lower())
        if(battery != []):
            info['Battery Capacity'] = battery[0].split()[0]
        proc = re.findall(r'[a-z][a-z]+\ [0-9][0-9]+[^m^\.]*processor',item.lower())
        if(proc != []):
            info['Processor'] = ""
            info['Processor'] = " ".join(proc[0].split()[0:2])
        price = re.findall(r'\$[0-9]+|[0-9]+\$',item.lower())
        if(price != []):
            info['Price'] = price[0].split()[0]
        video = re.findall(r'[0-9]+[kp].*video',item.lower())
        if(video == []):
            video = re.findall(r'video.*[0-9]+[kp]',item.lower())
            if(video != []):     
                info['Video Recording'] = video[0].split()[-1]
        elif(video != []):
            info['Video Recording'] = video[0].split()[0]
        OS = re.findall(r'android [0-9]\.?[0-9]?|ios [0-9][0-9]?',item.lower())
        if(OS != []):
            info['OS'] = OS[0]

        

        #info['Features'] = features

    #print(info)

    for sp in specs:
        if(sp in info):
            print(f'{sp:30} : ',info[sp])
    print()
    print()


