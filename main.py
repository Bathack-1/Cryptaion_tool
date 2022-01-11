import time

fil = open("krypteringsinstillinger")
innstillinger = fil.read()

alfabet = innstillinger
alfabet_lengde = len(alfabet)

def enkod(bokstav, nøkkel):
    bokstav_posisjon = alfabet.find(bokstav)
    ny_posisjon = (bokstav_posisjon + nøkkel) % alfabet_lengde
    return alfabet[ny_posisjon]

def dekod(bokstav, nøkkel):
    bokstav_posisjon = alfabet.find(bokstav)

    ny_posisjon = (bokstav_posisjon - nøkkel) % alfabet_lengde

    return alfabet[ny_posisjon]

def enkod_ord(beskje, nøkkel):
    kryptert_beskje = ""

    for bokstav in beskje:
        if bokstav in alfabet:
            kryptert_beskje += enkod(bokstav, nøkkel)
        else:
            kryptert_beskje += bokstav

    return kryptert_beskje

def dekod_ord(kryptert_beskje, nøkkel):
    dekryptert_beskje = ""

    for bokstav in kryptert_beskje:
        if bokstav in alfabet:
            dekryptert_beskje += dekod(bokstav, nøkkel)
        else:
            dekryptert_beskje += bokstav

    return dekryptert_beskje

def brute_force(kryptert_beskje):
    for nøkkel in range(1, alfabet_lengde):
        dekryptert_beskje = ""

        for bokstav in kryptert_beskje:
            if bokstav in alfabet:
                dekryptert_beskje += dekod(bokstav, nøkkel)
            else:
                dekryptert_beskje += bokstav

        print(dekryptert_beskje)
#c
def main():
    while True:
        svar = input("enkode, dekode, brute force eller avslutte? ").lower()
        if "avslutte" in svar:
            exit()

        elif "enkode" in svar:
            beskje = input("hva er beskjeen? \n").lower()
            nøkkel = int(input("Hva er nøkkelen? \n"))
            print(enkod_ord(beskje, nøkkel))

        elif "dekode" in svar:
            beskje = input("hva er beskjeen? \n").lower()
            nøkkel = int(input("Hva er nøkkelen? \n"))
            print(dekod_ord(beskje, nøkkel))

        elif "brute force" in svar:
            beskje = input("hva er beskjeen? \n").lower()
            brute_force(beskje)

        time.sleep(3)

if __name__ == '__main__':
    main()
