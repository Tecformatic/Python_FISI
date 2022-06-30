# My Name


from msilib.schema import tables


def main():
    guests = []
    # Aufgabe 2(1):
    addGroup(guests, ['James1', 'David1', 'Amy1'])
    addGroup(guests, ['Pamela2', 'Janet2', 'Carl2'])
    addGroup(guests, ['Christine3'])
    addGroup(guests, ['Stephen4', 'Stephanie4'])
    addGroup(guests, ['Martha5'])
    addGroup(guests,     ['Virginia6', 'Gregory6', 'Ryan6', 'Debra6'])

    
    # Aufgabe 2(2):
    #printTable(guests)
    # Aufgabe 2(3):
    plan = placeGuest(guests, 4)
    printTable(plan)

def addGroup(base: list, appendix: list):
    base.append(appendix)

def printTable(data: list):
    for i in range(len(data)):
        print(f"Tischnr.: {i + 1}")
        for person in data[i]:
            print(f"\t{person}")
        print("")

def placeGuest(data: list, Tables:  int):
    base = data.copy()
    plan = []
    
    for tb in range(Tables):
        people = []
        for i in range(len(base)):
            try:
                people.append(base[i][0])
                base[i].pop(0)
            except:
                continue
        plan.append(people)
    return(plan)

    
    

    




if __name__ == '__main__':
    main()
