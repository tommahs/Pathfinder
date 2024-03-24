#/usr/bin/python
def addToDB(input):
    import csv
    with open('weapons.json', 'a') as file:
        # file.append(input)
        file.write('test\n')
    return 0

addToDB('test')


