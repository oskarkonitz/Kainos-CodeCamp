import math
import random
import time
import pygame
import os

##########  USTAWIENIA  ##########

ILOSC_KOSMITOW = 20
MAX_PUNKTY = 200
WYMIAR_KOSMITY = 60
POLE_RADIOAKTYWNE_KOSMITY = 20


def kolizja(x1, y1, x2, y2):
    srodek_kosmity_x = x1 + WYMIAR_KOSMITY / 2
    srodek_kosmity_y = y1 + WYMIAR_KOSMITY / 2
    odleglosc = math.sqrt(math.pow(srodek_kosmity_x - x2, 2) + math.pow(srodek_kosmity_y - y2, 2))
    if odleglosc < WYMIAR_KOSMITY / 2:
        return True
    else:
        return False


def kolizja2(x1, y1, x2, y2):
    dotyk = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if dotyk < POLE_RADIOAKTYWNE_KOSMITY:
        return True
    else:
        return False


def wygrano():
    # print("wygrana")
    screen.blit(ekran_wygranej, (0, 0))
    pygame.display.flip()
    os.system('clear')
    print("Udało ci się zabić aż", punkty, "kosmitów!")
    print("Twoja planeta jak i statek zostały ocalone a ty wybierasz się w dalszą podróż.")
    print(" ")
    x = input("Wpisz exit aby zamknąć: ")
    if x == 'exit':
        pygame.quit()


def przegrana():
    # print("przegrana")
    screen.blit(ekran_przegranej, (0, 0))
    pygame.display.flip()
    os.system('clear')

    if punkty == 0:
        print("Niestety nie udało ci się zabić żadnego kosmity.")
    elif punkty == 1:
        print("Udało ci się zabić tylko jednego kosmite.")
    else:
        print("Udało ci się zabić aż", punkty, "kosmitów!")

    print("Niestety twoja planeta została przejęta a cała ludzkość została niewolnikami wyżej rozwiniętej cywilizacji.")
    print(" ")
    x = input("Wpisz exit aby zamknąć: ")
    if x == 'exit':
        pygame.quit()
    elif x == 'restart':
        return True


pygame.init()

# ustawienie wielkości okna
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# ustawienie tytułu okna
pygame.display.set_caption(' Space Invaders ')

punkty = 0
kosmita_trafiony = []
kosmita_x = []
kosmita_y = []
kosmita_kierunek = []

os.system('clear')
print('########## USTAWIENIA ##########')
time.sleep(.200)
print("ILOŚĆ KOSMITÓW: ", ILOSC_KOSMITOW)
time.sleep(.200)
print("POTRZEBNE PUNKTY: ", MAX_PUNKTY)
time.sleep(.200)
print(" ")
print("Aby zmienić ustawienia musisz zajrzeć na sam początek kodu.")
print(" ")
time.sleep(.500)
print("########## ZASADY GRY ##########")
time.sleep(.200)
print("Aby wygrać musisz zdobyć odpowiednią ilość punktów ( aktualnie ustawione: ", MAX_PUNKTY, ")")
time.sleep(.200)
print("Aby sie przemiszczać używaj strzałek a aby strzelać spacji")
time.sleep(.200)
print("Jeśli statek przeciwnika cię dotknie - przegrywasz")
time.sleep(.200)
print("Jeśli statek przeciwnika dotrze do dołu ekranu - przegrywasz")
time.sleep(.200)
print("Nie jestem artystą więc jest zakaz oceniania mojego statku!")
time.sleep(.200)
print("Aby rozpocząć musisz kliknąć w okienko gry")
time.sleep(.200)
print("POWODZENIA!")
time.sleep(1)
print(" ")
print("########## START ##########")
time.sleep(.200)
x4 = input("Aby kontunuować wpisz: Rozumiem -> ")

x3 = True

while x3 == True:
    if x4 == 'Rozumiem' or x4 == 'rozumiem':
        os.system('clear')
        print("ILOŚĆ PUNKTÓW: ", punkty, "/", MAX_PUNKTY)
        x3 = False
    else:
        print("spróbuj ponownie: ")
        x4 = input("Aby kontunuować wpisz: Rozumiem -> ")

for i in range(ILOSC_KOSMITOW):
    kosmita_x.append(random.randint(0, 460))
    kosmita_y.append(random.randint(0, 300))
    kosmita_trafiony.append(False)

for i in range(ILOSC_KOSMITOW):
    if random.randint(0, 1) == 1:
        kosmita_kierunek.append('r')
    else:
        kosmita_kierunek.append('l')

# załaduj obrazek statku
statek = pygame.image.load('data/statek2.png')
ekran_wygranej = pygame.image.load('data/wygrana.png')
kosmita = pygame.image.load('data/kosmita.png')
pocisk = pygame.image.load('data/pocisk.png')
ekran_przegranej = pygame.image.load('data/przegrana_o.png')
x = 220
y = 340
screen.blit(statek, (x, y))

# pętla gry
running = True
pocisk1 = False
dzialanie = False

while running:
    # zdarzenia zewnętrzne np. kliknięcie na klawiaturze
    for event in pygame.event.get():
        # zdarzenie zamknięcia programu
        if event.type == pygame.QUIT:
            running = False

        # dodaj obsługę zdarzenia na kliknięcie klawisza
        # obsługa strzałek jako poruszanie się statku
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            screen.fill('black')
            if y == 0:
                y = y
            else:
                y -= 20

            screen.blit(statek, (x, y))
            # print("up", x, " ", y)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            screen.fill('black')
            if y == 360:
                y = y
            else:
                y += 20

            screen.blit(statek, (x, y))
            # print("down", x, " ", y)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            screen.fill('black')
            if x == 0:
                x = x
            else:
                x -= 20

            screen.blit(statek, (x, y))
            # print("left", x, " ", y)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            screen.fill('black')
            if x == 540:
                x = x
            else:
                x += 20

            screen.blit(statek, (x, y))
            # print("right", x, " ", y)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            x_pocisk = x
            y_pocisk = y
            pocisk1 = True
            # kosmita_trafiony[1] = True

    # narysuj statek w odpowieniej pozycji
    #     KOSMICI

    for i in range(ILOSC_KOSMITOW):
        if kosmita_kierunek[i] == "r":
            if kosmita_x[i] == 460:
                kosmita_y[i] += 5
                kosmita_kierunek[i] = "l"
            else:
                kosmita_x[i] += 1
        else:
            if kosmita_x[i] == 0:
                kosmita_y[i] += 5
                kosmita_kierunek[i] = "r"
            else:
                kosmita_x[i] -= 1

        if kosmita_y[i] == 360:
            przegrana()

        screen.fill('black')
        screen.blit(statek, (x, y))
        if pocisk1 == True:
            dzialanie = True
            if y_pocisk > 0:
                y_pocisk -= 2
            else:
                pocisk1 = False

            screen.blit(pocisk, (x_pocisk, y_pocisk))

            if kolizja(kosmita_x[i], kosmita_y[i], x_pocisk, y_pocisk) == True:
                kosmita_trafiony[i] = True

        if kolizja2(kosmita_x[i], kosmita_y[i], x, y) == True:
            przegrana()

        for j in range(ILOSC_KOSMITOW):
            if kosmita_trafiony[j] == False:
                screen.blit(kosmita, (kosmita_x[j], kosmita_y[j]))
            else:
                punkty += 1
                os.system('clear')
                print("ILOŚĆ PUNKTÓW: ", punkty, "/", MAX_PUNKTY)
                kosmita_x[j] = random.randint(0, 460)
                kosmita_y[j] = random.randint(0, 300)
                screen.blit(kosmita, (kosmita_x[j], kosmita_y[j]))
                kosmita_trafiony[j] = False

                if punkty >= MAX_PUNKTY:
                    wygrano()

    # aktualizuje cały ekran
    pygame.display.flip()
    # ogranicza FPS do 60
    clock.tick(60)

# zamknięcie programu
pygame.quit()
