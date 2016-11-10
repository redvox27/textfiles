with open("textfile_python.txt") as f:
    test = f.read()



    eersteDeel = ""
    tweedeDeel = ""
    derdeDeel = ""
    lijst = []

    startwaarde = 0
    eindwaarde = -1
    index =0

    while index < 5 :

        for pointer in range(startwaarde,len(test)):
            if pointer < startwaarde + 4 :
                eersteDeel += test[pointer]
                print(eersteDeel)
            if pointer > startwaarde +4 and pointer < startwaarde + 9:
                tweedeDeel += test[pointer]

            if pointer > startwaarde + 9 and pointer < eindwaarde:
                derdeDeel += test[pointer]

        startwaarde = eindwaarde
        eindwaarde += 20
        index = index +1


    lijst.append(eersteDeel)
