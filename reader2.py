with open("textfile_python.txt") as f:
    test = f.read()
    lijst = []
    iban = ""
    startWaarde = 0
    pointer = 0
    index = 0

while index < 5 :
    for pointer in range(0,len(test)):
        if pointer < startWaarde + 18:
           iban += test[pointer]

        if pointer >= 18:
            startWaarde = pointer
            index += 1

    



#wewe
