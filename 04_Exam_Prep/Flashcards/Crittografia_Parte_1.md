# Flashcards - Crittografia Parte 1

## Fonte

- SRC-002

## Flashcard 1

**Domanda:** Che cos'è la crittografia?

**Risposta:**  
La crittografia è la disciplina che studia tecniche per proteggere messaggi e dati, con l'obiettivo di garantire riservatezza, integrità e autenticità nella comunicazione tra due o più soggetti.

## Flashcard 2

**Domanda:** Perché la crittografia non risolve tutti i problemi di sicurezza?

**Risposta:**  
Perché la sicurezza dipende anche da implementazione, gestione delle chiavi, usabilità, processo operativo e vulnerabilità del sistema circostante. Un algoritmo forte può essere inefficace se usato male.

## Flashcard 3

**Domanda:** Quali sono le cinque parti di un sistema crittografico?

**Risposta:**  
Sono l'insieme dei messaggi in chiaro `P`, l'insieme delle chiavi `K`, l'insieme dei messaggi cifrati `C`, la funzione di codifica `encrypt: K x P -> C` e la funzione di decodifica `decrypt: K x C -> P`.

## Flashcard 4

**Domanda:** Che cos'è il cifrario di Cesare?

**Risposta:**  
È uno schema di cifratura che sposta le lettere dell'alfabeto di un numero fisso di posizioni usando aritmetica modulo il numero di lettere. È debole perché ha poche chiavi ed è facilmente violabile con forza bruta.

## Flashcard 5

**Domanda:** Che cos'è un attacco di forza bruta?

**Risposta:**  
È un attacco che prova tutte le chiavi o configurazioni possibili di uno spazio finito finché trova quella corretta.

## Flashcard 6

**Domanda:** Che cos'è la crittoanalisi?

**Risposta:**  
È lo studio degli attacchi che cercano di violare la crittografia analizzando messaggi cifrati, algoritmi, chiavi o informazioni indirette come frequenza e lunghezza dei messaggi.

## Flashcard 7

**Domanda:** Quali sono le tre principali classi di algoritmi crittografici?

**Risposta:**  
Algoritmi simmetrici o a chiave segreta, algoritmi asimmetrici o a chiave pubblica e algoritmi di hashing o message digest.

## Flashcard 8

**Domanda:** Come funzionano gli algoritmi simmetrici?

**Risposta:**  
Usano la stessa chiave segreta sia per cifrare sia per decifrare. Due soggetti possono comunicare in modo confidenziale solo se condividono una chiave non nota ad altri.

## Flashcard 9

**Domanda:** Quale requisito è supportato meglio dalla crittografia simmetrica?

**Risposta:**  
La confidenzialità, perché solo chi conosce la chiave segreta può decifrare il messaggio.

## Flashcard 10

**Domanda:** Perché la crittografia simmetrica non garantisce non-ripudio verso terze parti?

**Risposta:**  
Perché la chiave è condivisa tra i partecipanti: ciascuno di loro potrebbe aver prodotto un messaggio valido, quindi un terzo non può attribuire con certezza il messaggio a uno specifico mittente.

## Flashcard 11

**Domanda:** Quante chiavi servono per far comunicare `n` utenti a coppie con crittografia simmetrica?

**Risposta:**  
Servono `n(n-1)/2` chiavi, cioè una chiave per ogni coppia di utenti.

## Flashcard 12

**Domanda:** Che cos'è DES?

**Risposta:**  
DES, Data Encryption Standard, è un algoritmo simmetrico storico che cifra blocchi da 64 bit usando una chiave effettiva da 56 bit e 16 round basati su confusione e diffusione.

## Flashcard 13

**Domanda:** Perché DES non è più considerato sicuro?

**Risposta:**  
Perché lo spazio delle chiavi da 56 bit è diventato attaccabile con forza bruta grazie all'aumento della potenza computazionale e alla parallelizzazione.

## Flashcard 14

**Domanda:** Che cos'è Triple DES?

**Risposta:**  
È una variante di DES che cifra tre volte usando chiavi diverse, ottenendo una sicurezza paragonabile a una chiave da 112 bit.

## Flashcard 15

**Domanda:** Che cos'è AES?

**Risposta:**  
AES, Advanced Encryption Standard, è un algoritmo simmetrico moderno adottato dal NIST nel 2001. Usa blocchi da 128 bit e chiavi da 128, 192 o 256 bit.

## Flashcard 16

**Domanda:** Quali sono i principali pro e contro della crittografia simmetrica?

**Risposta:**  
I pro sono efficienza, velocità e ottimo supporto alla confidenzialità. I contro sono gestione complessa delle chiavi, supporto limitato a integrità/autenticità/non-ripudio e impossibilità di provare il mittente a terze parti.

