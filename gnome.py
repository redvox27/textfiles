with open("gen.txt") as f :
    file = f.read()

    #begin door ATG weg te halen in de string dan in lijst gen zetten
    gen = file.split("ATG")
    print("hele string: ",gen)

    #als TAG in de string voorkomt in de lijst: print die string
    matchingTAG = [s for s in gen if "TAG" in s]
    #als TAA in de string voorkomt in de lijst: print die string
    matchingTAA = [s for s in gen if "TAA" in s]
    # als TGA in de string voorkomt in de lijst: print die string
    matchingTGA = [s for s in gen if "TGA" in s]

    #laat de strign in matchingTAG,TAA,TGA eindigen voor deze tags
    testTAG =[i.split("TAG")[1] for i in matchingTAG]
    testTAA = [i.split("TAA")[1] for i in matchingTAA]
    testTGA = [i.split("TGA")[1] for i in matchingTGA]


    print(matchingTAG)
    print("TAG: ",testTAG)
    print("TAA: ",testTAA)
    print("TGA: ",testTGA)
