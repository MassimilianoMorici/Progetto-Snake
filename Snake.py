import curses
from copy import copy
from random import randint
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

curses.initscr() # inizializzazione schermo
finestra = curses.newwin(30,60,0,0) # creazione finestra 30x60
finestra.keypad(True) # abilita la possibilità di premere i tasti con le 4 frecce 
finestra.border(0) # bordo esterno al campo
finestra.timeout(10) # il serpente si muove nella direzione puntata oppure è "statico"
snake = [[15,13], [15,12], [15,11]] # creazione serpente
cibo = [5,35] # creazione primo cibo, colonna indicata ma nono lo aggiungo ancora
doveGuardo = KEY_DOWN # il serpente parte verso il basso
punti = 0 # punti di partenza
finestra.addch(cibo[0], cibo[1], 'O') # la funzione addch aggiunge "O" riga,colonna

while True:
    # mostriamo costantemente il punteggio del giocatore al centro
    finestra.addstr(0,14," Punteggio: " + str(punti) + ' ')
    # aggiorna lo schermo automaticamente ad ogni frame di gioco e ottiene il tasto preso dall'utente
    tasto = finestra.getch()
    if tasto != -1:
        doveGuardo = tasto
    
    # in base al tasto premuto dall'utente si fanno diverse azioni.
    # si genera la nuova testa a partire dalla posizione della vecchia
    # e si aggiunge o sottrae 1 in base al tasto premuto dall'utente e la coordinata richiesta
    nuovaTesta = copy(snake[0])
    if doveGuardo == KEY_DOWN:
        nuovaTesta[0] += 1
    elif doveGuardo == KEY_UP:
        nuovaTesta[0] -= 1
    elif doveGuardo == KEY_RIGHT:
        nuovaTesta[1] += 1
    elif doveGuardo == KEY_LEFT:
        nuovaTesta[1] -= 1    

    # si inserisce la nuova testa
    snake.insert(0, nuovaTesta)
    
    # se il serpente esce dallo schermo break
    if snake[0][0] == 0 or snake[0][0] == 29 or snake[0][1] == 0 or snake[0][1] == 59:
        break
    
    # se il serpente si cammina sopra break
    if snake[0] in snake[1:]:
        break

    # se finisco sul cibo 
    if snake[0] == cibo:
        cibo = []
        punti += 1
        while cibo == [] :
            # generiamo il prossimo cibo
            cibo = [randint(1,28), randint(1,58)]
            if cibo in snake:
                cibo = []
        finestra.addch(cibo[0], cibo[1], 'O') # aggiunge il nuovo cibo alla finestra

    # se il serpente finisce su qualsiasi casella
    else:
        ultimoPezzo = snake.pop() # estrai l'ultimo pezzo del serpente e metti ' '
        finestra.addch(ultimoPezzo[0], ultimoPezzo[1], ' ')    

    # se non ho
    finestra.addch(snake[0][0], snake[0][1], 'X') # si aggiunge  

curses.endwin() # GAME OVER
print('\n GAME OVER! Punteggio finale: ' + str(punti))            