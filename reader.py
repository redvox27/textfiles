with open("textfile_python.txt") as f:
    test = f.read()



    eersteDeel = ""
    tweedeDeel = ""
    derdeDeel = ""
    lijst = []

    lengte = ""
    startwaarde = 0
    eindwaarde = -1
    index =0




    for pointer in range(startwaarde,len(test)):
        if pointer < startwaarde + 4 :
                eersteDeel += test[pointer]

        if pointer > startwaarde +3 and pointer < startwaarde + 8:
                tweedeDeel += test[pointer]


        if pointer > startwaarde + 7 and pointer < eindwaarde + startwaarde + 19:
                derdeDeel += test[pointer]
                #print(derdeDeel)

        if "NL" in pointer :


