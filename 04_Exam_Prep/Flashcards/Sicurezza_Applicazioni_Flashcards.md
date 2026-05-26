# Flashcards - Sicurezza Applicazioni

## Fonte

- SRC-007
- SRC-008

## Flashcard 1

**Domanda:** Che cos'e' una weakness?

**Risposta:**  
E' un tipo di errore nel progetto, implementazione o operazione di un sistema software che, in condizioni appropriate, puo' portare all'introduzione di vulnerabilita'.

## Flashcard 2

**Domanda:** Differenza tra weakness e vulnerabilita'?

**Risposta:**  
La weakness e' la categoria o tipo di difetto; la vulnerabilita' e' una sua occorrenza concreta in un sistema sfruttabile per violare la security policy.

## Flashcard 3

**Domanda:** Differenza tra CWE, CAPEC e CVE?

**Risposta:**  
CWE cataloga weakness, CAPEC cataloga schemi d'attacco, CVE cataloga vulnerabilita' concrete in software noti.

## Flashcard 4

**Domanda:** Che cos'e' XSS?

**Risposta:**  
E' uno schema d'attacco in cui input malevolo viene interpretato come codice dal browser della vittima.

## Flashcard 5

**Domanda:** Differenza tra persistent, reflected e DOM-based XSS?

**Risposta:**  
Persistent: payload salvato lato server e servito a piu' utenti. Reflected: payload incluso nella richiesta e riflesso nella risposta. DOM-based: manipolazione avviene lato client nel DOM.

## Flashcard 6

**Domanda:** Contromisura principale contro SQL injection?

**Risposta:**  
Prepared statement/query parametrizzate, cosi' codice SQL e dati utente restano separati.

## Flashcard 7

**Domanda:** Che cos'e' un buffer overflow?

**Risposta:**  
E' una scrittura fuori dai limiti di un buffer, che puo' sovrascrivere memoria adiacente.

## Flashcard 8

**Domanda:** Perche' un buffer overflow sullo stack e' pericoloso?

**Risposta:**  
Puo' sovrascrivere variabili locali, base pointer o return address, alterando il flusso di esecuzione.

## Flashcard 9

**Domanda:** Qual e' l'idea di Heartbleed?

**Risposta:**  
Una lunghezza dichiarata maggiore del payload reale induce la copia in risposta di memoria oltre il payload inviato.

## Flashcard 10

**Domanda:** Perche' una NULL pointer dereference nel kernel puo' diventare privilege escalation?

**Risposta:**  
Se l'attaccante controlla la pagina NULL o indirizzi bassi, il kernel puo' eseguire o usare dati controllati dall'attaccante con privilegi kernel.

## Flashcard 11

**Domanda:** Lezione principale di CVE-2009-2692?

**Risposta:**  
Un puntatore a funzione NULL non controllato in una struttura del kernel puo' essere sfruttato per redirigere l'esecuzione.

## Flashcard 12

**Domanda:** Differenza tra Java secure coding guideline domain dependent e domain independent?

**Risposta:**  
Le domain dependent dipendono dal dominio applicativo e sono difficili da controllare automaticamente; le domain independent riguardano struttura del codice e sono piu' automatizzabili.

