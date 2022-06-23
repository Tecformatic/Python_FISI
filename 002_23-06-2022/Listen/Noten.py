from colorama import Fore
noten = [["Noah", 2.0], ["Hanna", 1.2], ["Ben", 1.7], ["Emma", 2.1],
["Paul", 1.3], ["Mia", 1.9]]

def noten_avg(noten: list):
    avg = 0
    for item in noten:
        avg = avg + item[1]
    avg = avg / len(noten)
    return avg

print(f"Notendurchschnitt: {Fore.CYAN}{noten_avg(noten):0.2f}{Fore.WHITE}")