# Flashcards - Sicurezza SO Parte 1

## Fonte

- SRC-004

## Flashcard 1

**Domanda:** Quali sono due problemi centrali della sicurezza nei sistemi operativi?

**Risposta:**  
Autenticazione e controllo degli accessi. L'autenticazione stabilisce e verifica l'identità del richiedente; il controllo degli accessi decide se un soggetto autenticato può accedere a oggetti protetti.

## Flashcard 2

**Domanda:** Che cos'è l'autenticazione?

**Risposta:**  
È il processo con cui un sistema verifica che un soggetto sia davvero chi dichiara di essere, con l'obiettivo di impedire l'accesso a soggetti non autorizzati.

## Flashcard 3

**Domanda:** Quali sono le tre categorie principali di metodi di autenticazione?

**Risposta:**  
Dimostrazione di conoscenza, come password o PIN; dimostrazione di possesso, come smartcard o chiavi fisiche; caratteristiche personali uniche, come biometria.

## Flashcard 4

**Domanda:** Perché le password non devono essere memorizzate in chiaro?

**Risposta:**  
Perché se il file delle password viene letto da un attaccante, le password sarebbero immediatamente compromesse. Si memorizza invece un hash della password.

## Flashcard 5

**Domanda:** Che cos'è il salt?

**Risposta:**  
È un valore casuale memorizzato insieme alla password hashata. La password viene salvata come `hash(pw + salt)`, così password uguali producono hash diversi e si ostacolano tabelle precomputate.

## Flashcard 6

**Domanda:** Perché gli hash per password possono essere volutamente lenti?

**Risposta:**  
Per rendere più costosi gli attacchi offline: se ogni tentativo richiede più tempo, provare grandi quantità di password diventa meno praticabile.

## Flashcard 7

**Domanda:** Quali sono strategie comuni di attacco alle password?

**Risposta:**  
Provare password assenti, password derivate dallo user ID, informazioni note dell'utente, dizionari, sostituzioni comuni, forza bruta su lettere/numeri e infine forza bruta su set completo di caratteri.

## Flashcard 8

**Domanda:** Perché usare solo lettere minuscole indebolisce una password?

**Risposta:**  
Perché riduce lo spazio delle possibilità. Una password di 6 caratteri con 95 caratteri possibili ha circa `95^6` combinazioni, mentre con sole lettere minuscole ha solo `26^6` combinazioni.

## Flashcard 9

**Domanda:** Quali proprietà deve avere un processo di autenticazione sicuro?

**Risposta:**  
Non deve rivelare dettagli prima del successo, deve usare errori generici, può rallentare i tentativi, può bloccare utenti dopo fallimenti, può usare più fattori e deve resistere ad attacchi basati sul tempo.

## Flashcard 10

**Domanda:** Perché i messaggi di errore di login devono essere generici?

**Risposta:**  
Per non rivelare se un utente esiste, se la password è sbagliata o se l'account è disabilitato. Queste informazioni aiuterebbero l'attaccante.

## Flashcard 11

**Domanda:** Che cos'è challenge/response?

**Risposta:**  
È uno schema in cui il sistema invia una challenge e l'utente risponde calcolando una funzione del valore ricevuto, dimostrando di conoscere un segreto senza trasmetterlo direttamente.

## Flashcard 12

**Domanda:** Perché trasmettere direttamente una password è pericoloso?

**Risposta:**  
Perché un attaccante che intercetta la comunicazione può riutilizzare la password e impersonare l'utente.

## Flashcard 13

**Domanda:** Che cos'è un nonce?

**Risposta:**  
È un valore usato una sola volta in un protocollo. Non deve essere segreto, ma deve cambiare a ogni sessione per impedire il riuso di vecchi messaggi validi.

## Flashcard 14

**Domanda:** Che cos'è un replay attack?

**Risposta:**  
È un attacco in cui un messaggio valido intercettato viene reinviato in seguito per ottenere accesso o autenticarsi come un altro utente.

## Flashcard 15

**Domanda:** Come si difende un protocollo da replay attack?

**Risposta:**  
Usando nonce o challenge diverse a ogni sessione, così una risposta vecchia non è più valida.

## Flashcard 16

**Domanda:** Che cos'è un reflection attack?

**Risposta:**  
È un attacco che sfrutta la simmetria di un protocollo bidirezionale, facendo calcolare a una parte una risposta che poi viene riflessa in un'altra sessione.

## Flashcard 17

**Domanda:** Come si può mitigare un reflection attack?

**Risposta:**  
Inserendo identificativi nei messaggi cifrati, così ogni risposta è legata al ruolo e al contesto corretto.

## Flashcard 18

**Domanda:** Che cos'è Needham-Schroeder?

**Risposta:**  
È un protocollo di autenticazione reciproca basato su crittografia a chiave pubblica, nonce e challenge/response.

## Flashcard 19

**Domanda:** Perché la versione originale di Needham-Schroeder è vulnerabile?

**Risposta:**  
Perché alcuni messaggi non includono l'identità del mittente, permettendo un parallel sessions attack in cui l'attaccante riusa messaggi validi tra sessioni diverse.

## Flashcard 20

**Domanda:** Come viene corretto Needham-Schroeder?

**Risposta:**  
Aggiungendo gli identificativi corretti nei messaggi cifrati, ad esempio includendo `S` nel secondo messaggio e `A` nel terzo, per legare messaggio, identità e contesto.

