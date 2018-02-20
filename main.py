# Gumby theft detection program
# Created Feb 8, 2018
# Copyright (c) Sambhav Saggi 2018
# All rights reserved
# Created for Gregory Calvetti
# Output may be wrong

#Set some constants
DENSITY_THRESH=0.7

#Get ready to compare numbers
def takeClosest(list, derp):
    meme = []
    for i in list:
        meme.append(abs(derp-i))
    return meme.index(min(meme))

#Material info
baking_soda = {
    "fire":    1,
    "vinegar": 2,
    "iodine":  1,
    "bromo":   2
}
drywall_compound = {
    "fire":    2,
    "vinegar": 0,
    "iodine":  1,
    "bromo":   0
}
corn_starch = {
    "fire":    2,
    "vinegar": 0,
    "iodine":  2,
    "bromo":   1
}
salt = {
    "fire":    1,
    "vinegar": 0,
    "iodine":  1,
    "bromo":   1
}
flour = {
    "fire":    2,
    "vinegar": 0,
    "iodine":  2,
    "bromo":   1
}
sugar = {
    "fire":    2,
    "vinegar": 0,
    "iodine":  0,
    "bromo":   1
}

#Density
density={
    "copper"   :  8.96,
    "steel"    :  7.85,
    "brass"    :  8.73,
    "aluminum" :  2.7,
    "none"     :  0
}

#Evidence
evidence = {
    "num":{"footprint":247,"density":8.9},
    "chroma":["blue","red"],
    "react":{"fire":2,"vinegar":2,"bromo":2,"iodine":2}
#0 is no reaction, 1 is some reaction, 2 is violent reaction. Iodine: 0 is none
# 1 is yellow, 2 is brown. Bromo: 0 is green, 1 is yellow, 2 is blue
}

#Suspects
suspect_list=["cafe_worker","janitor","handyman","administrator","ccac"]
cafe_worker = {
    "name":"cafe_worker",
    "powder1":baking_soda,
    "powder2":flour,
    "metal1":density["copper"],
    "metal2":density["steel"],
    "footprint":244,
    "chroma":["yellow","blue"]
}
janitor = {
    "name":"janitor",
    "powder1":salt,
    "powder2":baking_soda,
    "metal1":density["steel"],
    "metal2":density["none"],
    "footprint":286,
    "chroma":["blue","red"]
}
handyman = {
    "name":"handyman",
    "powder1":drywall_compound,
    "powder2":sugar,
    "metal1":density["aluminum"],
    "metal2":density["steel"],
    "footprint":265,
    "chroma":["black",""]
}
administrator = {
    "name":"administrator",
    "powder1":sugar,
    "powder2":salt,
    "metal1":density["copper"],
    "metal2":density["brass"],
    "footprint":330,
    "chroma":["blue","orange"]
}
ccac = {
    "name":"ccac",
    "powder1":baking_soda,
    "powder2":corn_starch,
    "metal1":density["copper"],
    "metal2":density["aluminum"],
    "footprint":265,
    "chroma":["red","blue"]
}

#BEGIN THE SEARCH!!!!

for i in range(0,5):
    test_suspect = suspect_list[i]

    #Cafe Worker
    if test_suspect == "cafe_worker":
        cafe_worker_evidence=0
        #Powder 1
        powder1=cafe_worker["powder1"]
        if powder1["fire"] == evidence["react"]['fire']:
            cafe_worker_evidence+=1
        if powder1["vinegar"] == evidence["react"]['vinegar']:
            cafe_worker_evidence+=1
        if powder1["iodine"] == evidence["react"]['iodine']:
            cafe_worker_evidence+=1
        if powder1["bromo"] == evidence["react"]['bromo']:
            cafe_worker_evidence+=1
        #Powder 2
        powder2=cafe_worker["powder2"]
        if powder2["fire"] == evidence["react"]['fire']:
            cafe_worker_evidence+=1
        if powder2["vinegar"] == evidence["react"]['vinegar']:
            cafe_worker_evidence+=1
        if powder2["iodine"] == evidence["react"]['iodine']:
            cafe_worker_evidence+=1
        if powder2["bromo"] == evidence["react"]['bromo']:
            cafe_worker_evidence+=1

    #Janitor
    elif test_suspect == "janitor":
        janitor_evidence=0
        #Powder 1
        powder1=janitor["powder1"]
        if powder1["fire"] == evidence["react"]['fire']:
            janitor_evidence+=1
        if powder1["vinegar"] == evidence["react"]['vinegar']:
            janitor_evidence+=1
        if powder1["iodine"] == evidence["react"]['iodine']:
            janitor_evidence+=1
        if powder1["bromo"] == evidence["react"]['bromo']:
            janitor_evidence+=1
        #Powder 2
        powder2=janitor["powder2"]
        if powder2["fire"] == evidence["react"]['fire']:
            janitor_evidence+=1
        if powder2["vinegar"] == evidence["react"]['vinegar']:
            janitor_evidence+=1
        if powder2["iodine"] == evidence["react"]['iodine']:
            janitor_evidence+=1
        if powder2["bromo"] == evidence["react"]['bromo']:
            janitor_evidence+=1

    #Handyman
    elif test_suspect == "handyman":
        handyman_evidence=0
        #Powder 1
        powder1=handyman["powder1"]
        if powder1["fire"] == evidence["react"]['fire']:
            handyman_evidence+=1
        if powder1["vinegar"] == evidence["react"]['vinegar']:
            handyman_evidence+=1
        if powder1["iodine"] == evidence["react"]['iodine']:
            handyman_evidence+=1
        if powder1["bromo"] == evidence["react"]['bromo']:
            handyman_evidence+=1
        #Powder 2
        powder2=handyman["powder2"]
        if powder2["fire"] == evidence["react"]['fire']:
            handyman_evidence+=1
        if powder2["vinegar"] == evidence["react"]['vinegar']:
            handyman_evidence+=1
        if powder2["iodine"] == evidence["react"]['iodine']:
            handyman_evidence+=1
        if powder2["bromo"] == evidence["react"]['bromo']:
            handyman_evidence+=1

    #Administrator
    elif test_suspect == "administrator":
        administrator_evidence=0
        #Powder 1
        powder1=administrator["powder1"]
        if powder1["fire"] == evidence["react"]['fire']:
            administrator_evidence+=1
        if powder1["vinegar"] == evidence["react"]['vinegar']:
            administrator_evidence+=1
        if powder1["iodine"] == evidence["react"]['iodine']:
            administrator_evidence+=1
        if powder1["bromo"] == evidence["react"]['bromo']:
            administrator_evidence+=1
        #Powder 2
        powder2=administrator["powder2"]
        if powder2["fire"] == evidence["react"]['fire']:
            administrator_evidence+=1
        if powder2["vinegar"] == evidence["react"]['vinegar']:
            administrator_evidence+=1
        if powder2["iodine"] == evidence["react"]['iodine']:
            administrator_evidence+=1
        if powder2["bromo"] == evidence["react"]['bromo']:
            administrator_evidence+=1

    #CCAC
    elif test_suspect == "ccac":
        ccac_evidence=0
        #Powder 1
        powder1=ccac["powder1"]
        if powder1["fire"] == evidence["react"]['fire']:
            ccac_evidence+=1
        if powder1["vinegar"] == evidence["react"]['vinegar']:
            ccac_evidence+=1
        if powder1["iodine"] == evidence["react"]['iodine']:
            ccac_evidence+=1
        if powder1["bromo"] == evidence["react"]['bromo']:
            ccac_evidence+=1
        #Powder 2
        powder2=ccac["powder2"]
        if powder2["fire"] == evidence["react"]['fire']:
            ccac_evidence+=1
        if powder2["vinegar"] == evidence["react"]['vinegar']:
            ccac_evidence+=1
        if powder2["iodine"] == evidence["react"]['iodine']:
            ccac_evidence+=1
        if powder2["bromo"] == evidence["react"]['bromo']:
            ccac_evidence+=1

# ------Done w/ powders -------
#Begin metals
for i in range(0,5):
    test_suspect = suspect_list[i]

    #Cafe Worker
    if test_suspect == "cafe_worker":
        #Metal 1
        metal1=cafe_worker["metal1"]
        if abs(metal1 - evidence["num"]["density"]) < DENSITY_THRESH:
            cafe_worker_evidence+=1
        #Metal 2
        metal2=cafe_worker["metal2"]
        if abs(metal2 - evidence["num"]["density"]) < DENSITY_THRESH:
            cafe_worker_evidence+=1

    #Janitor
    elif test_suspect == "janitor":
        #Metal 1
        metal1=janitor["metal1"]
        if abs(metal1 - evidence["num"]["density"]) < DENSITY_THRESH:
            janitor_evidence+=1
        #Metal 2
        metal2=janitor["metal2"]
        if abs(metal2 - evidence["num"]["density"]) < DENSITY_THRESH:
            janitor_evidence+=1

    #Handyman
    elif test_suspect == "handyman":
        #Metal 1
        metal1=handyman["metal1"]
        if abs(metal1 - evidence["num"]["density"]) < DENSITY_THRESH:
            janitor_evidence+=1
        #Metal 2
        metal2=handyman["metal2"]
        if abs(metal2 - evidence["num"]["density"]) < DENSITY_THRESH:
            handyman_evidence+=1

    #Administrator
    elif test_suspect == "administrator":
        #Metal 1
        metal1=administrator["metal1"]
        if abs(metal1 - evidence["num"]["density"]) < DENSITY_THRESH:
            administrator_evidence+=1
        #Metal 2
        metal2=administrator["metal2"]
        if abs(metal2 - evidence["num"]["density"]) < DENSITY_THRESH:
            administrator_evidence+=1

    #CCAC
    elif test_suspect == "ccac":
        #Metal 1
        metal1=ccac["metal1"]
        if abs(metal1 - evidence["num"]["density"]) < DENSITY_THRESH:
            ccac_evidence+=1
        #Metal 2
        metal2=ccac["metal2"]
        if abs(metal2 - evidence["num"]["density"]) < DENSITY_THRESH:
            ccac_evidence+=1

# ------Done w/ metals -------
#Begin shoe size

shoes=[0,0,0,0,0]
for i in range(0,5):
    test_suspect = suspect_list[i]
    if test_suspect == "cafe_worker":
        shoes[i]=cafe_worker["footprint"]
    elif test_suspect == "janitor":
        shoes[i]=janitor["footprint"]
    elif test_suspect == "handyman":
        shoes[i]=handyman["footprint"]
    elif test_suspect == "administrator":
        shoes[i]=administrator["footprint"]
    elif test_suspect == "ccac":
        shoes[i]=ccac["footprint"]

smallestID=takeClosest(shoes,evidence["num"]["footprint"])


if smallestID == 0:
    cafe_worker_evidence+=1
elif smallestID == 1:
    janitor_evidence+=1
elif smallestID == 2:
    handyman_evidence+=1
elif smallestID == 3:
    administrator_evidence+=1
elif smallestID == 4:
    ccac_evidence += 1

# ------Done w/ shoe size -------
#Begin chromotography

for i in range(0,5):
    test_suspect = suspect_list[i]
    if test_suspect == "cafe_worker":
        if cafe_worker["chroma"][0] == evidence["chroma"][0]:
            cafe_worker_evidence+=1
        elif cafe_worker["chroma"][1] == evidence["chroma"][0]:
            cafe_worker_evidence+=1
        elif cafe_worker["chroma"][0] == evidence["chroma"][1]:
            cafe_worker_evidence+=1
        elif cafe_worker["chroma"][1] == evidence["chroma"][1]:
            cafe_worker_evidence+=1
    elif test_suspect == "janitor":
        if janitor["chroma"][0] == evidence["chroma"][0]:
            janitor_evidence+=1
        elif janitor["chroma"][1] == evidence["chroma"][0]:
            janitor_evidence+=1
        elif janitor["chroma"][0] == evidence["chroma"][1]:
            janitor_evidence+=1
        elif janitor["chroma"][1] == evidence["chroma"][1]:
            janitor_evidence+=1
    elif test_suspect == "handyman":
        if handyman["chroma"][0] == evidence["chroma"][0]:
            handyman_evidence+=1
        elif handyman["chroma"][1] == evidence["chroma"][0]:
            handyman_evidence+=1
        elif handyman["chroma"][0] == evidence["chroma"][1]:
            handyman_evidence+=1
        elif handyman["chroma"][1] == evidence["chroma"][1]:
            handyman_evidence+=1
    elif test_suspect == "administrator":
        if administrator["chroma"][0] == evidence["chroma"][0]:
            administrator_evidence+=1
        elif administrator["chroma"][1] == evidence["chroma"][0]:
            administrator_evidence+=1
        elif administrator["chroma"][0] == evidence["chroma"][1]:
            administrator_evidence+=1
        elif administrator["chroma"][1] == evidence["chroma"][1]:
            administrator_evidence+=1
    elif test_suspect == "ccac":
        if ccac["chroma"][0] == evidence["chroma"][0]:
            ccac_evidence+=1
        elif ccac["chroma"][1] == evidence["chroma"][0]:
            ccac_evidence+=1
        elif ccac["chroma"][0] == evidence["chroma"][1]:
            ccac_evidence+=1
        elif ccac["chroma"][1] == evidence["chroma"][1]:
            ccac_evidence+=1

################################################################################

#Display results
total=10
results=[cafe_worker_evidence,janitor_evidence,handyman_evidence,
administrator_evidence,ccac_evidence]
suspect_list_proper=["cafe worker","janitor","handyman","administrator",
"CCAC teacher"]

unranked={
    "Cafe worker":cafe_worker_evidence/total*100,
    "Janitor":janitor_evidence/total*100,
    "Handyman":handyman_evidence/total*100,
    "Administrator":administrator_evidence/total*100,
    "CCAC teacher":ccac_evidence/total*100
}

unrankedxy={
    "Cafe worker":(str(cafe_worker_evidence/total*100)+"\t%"),
    "Janitor":(str(janitor_evidence/total*100)+"\t%"),
    "Handyman":(str(handyman_evidence/total*100)+"\t%"),
    "Administrator":(str(administrator_evidence/total*100)+"\t%"),
    "CCAC teacher":(str(ccac_evidence/total*100)+"\t%")
}

ranked=sorted(unranked, key=unranked.get, reverse=True)

ordered_out=["","","","",""]
for i in range(0,len(ranked)):
    ordered_out[i] = ranked[i]+" \t"+unrankedxy[ranked[i]]

maxNum = max(results)
guilty=suspect_list_proper[results.index(maxNum)]

print("It was the "+guilty+"!\n")
print("GASP!\n")

for i in ordered_out:
    print(i)
#Done
