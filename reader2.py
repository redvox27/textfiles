with open("textfile_python.txt") as f:
    test = f.read()
    lijst = []
    iban = ""
    ibanList = []
    startWaarde = 0
    pointer = 0
    index = 0

    iban = test.split("NL")
    ibanList = ["NL" + line for line in iban]
    ibanList.pop(0)
    print(ibanList)