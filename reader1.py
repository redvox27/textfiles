som = 0
max = 0
min = 0
avg = 0
testString = ""
with open("textfile_python1.txt") as f:
    test = f.readlines()

    for line in test:
        testString += line.split()[1]

    for line in test:
        som += int(line.split()[3])



    avg = som / 5
    print(som)
    print(float(avg))
    print("games:", testString)


