# Glossario

## Safety engineering

Prevenzione di danni catastrofici causati dal cattivo funzionamento di un sistema informatico.

## Security engineering

Prevenzione, difesa e recupero rispetto ad attacchi che possono compromettere i valori rappresentati da un sistema informatico.

## Vulnerabilità

Debolezza o via alternativa che può essere sfruttata per compromettere confidenzialità, integrità o disponibilità.

## Minaccia

Circostanza, evento o agente che può arrecare danno a un sistema.

## Valore sensibile

Elemento importante, critico o sensibile di un sistema informativo che deve essere protetto.

## Confidenzialità

Capacità di assicurare che le informazioni siano accessibili solo a soggetti autorizzati.

## Integrità

Capacità di assicurare che le informazioni non siano modificate, cancellate, create o manomesse da soggetti non autorizzati.

## Disponibilità

Capacità di assicurare l'accesso a risorse e servizi agli utenti autorizzati quando necessario.

## Autenticità

Capacità di garantire l'identità del mittente di informazioni trasmesse o archiviate.

## Non-ripudio

Capacità di assicurare che il mittente non possa negare la paternità delle informazioni trasmesse o archiviate.

## CIA Triad

Modello che descrive i tre obiettivi fondamentali della sicurezza: confidenzialità, integrità e disponibilità.

## DAD

Modello che descrive tre famiglie di attacchi alla CIA Triad: Disclosure, Alteration e Destruction.

## DoS

Denial of Service: attacco che mira a impedire o rallentare l'accesso legittimo a un servizio.

## Crittografia

Disciplina che studia tecniche per proteggere messaggi e dati, garantendo proprietà come confidenzialità, integrità e autenticità.

## Plaintext

Messaggio in chiaro, leggibile prima della cifratura.

## Ciphertext

Messaggio cifrato, prodotto dall'applicazione di un algoritmo crittografico a un plaintext.

## Chiave crittografica

Parametro usato da un algoritmo crittografico per cifrare o decifrare un messaggio.

## Encrypt

Funzione di codifica che trasforma un plaintext in ciphertext usando una chiave.

## Decrypt

Funzione di decodifica che trasforma un ciphertext nel plaintext corrispondente usando una chiave.

## Cifrario di Cesare

Schema di cifratura basato sullo spostamento delle lettere dell'alfabeto tramite aritmetica modulare.

## Forza bruta

Attacco che prova tutte le chiavi o configurazioni possibili di uno spazio finito.

## Crittoanalisi

Studio delle tecniche per violare o indebolire sistemi crittografici.

## Algoritmo simmetrico

Algoritmo crittografico che usa la stessa chiave per cifrare e decifrare.

## Algoritmo asimmetrico

Algoritmo crittografico che usa una coppia di chiavi, una pubblica e una privata.

## Hashing

Classe di algoritmi che producono un'impronta o digest di un messaggio.

## DES

Data Encryption Standard: algoritmo simmetrico storico basato su blocchi da 64 bit e chiave effettiva da 56 bit.

## Triple DES

Variante di DES che cifra tre volte con chiavi diverse per aumentare la sicurezza.

## AES

Advanced Encryption Standard: algoritmo simmetrico moderno basato su blocchi da 128 bit e chiavi da 128, 192 o 256 bit.

## Scambio delle chiavi

Processo con cui due o più soggetti ottengono una chiave condivisa senza renderla nota ad attaccanti.

## Crittografia asimmetrica

Classe di algoritmi crittografici che usa una coppia di chiavi: una pubblica e una privata.

## Chiave pubblica

Chiave distribuibile pubblicamente, usata per cifrare messaggi verso il proprietario o per verificare firme prodotte dalla sua chiave privata.

## Chiave privata

Chiave nota solo al proprietario, usata per decifrare messaggi destinati a lui o per produrre firme digitali.

## RSA

Algoritmo crittografico asimmetrico basato sulla difficoltà di fattorizzare numeri molto grandi.

## One-way function

Funzione facile da calcolare in una direzione ma computazionalmente difficile da invertire.

## Message digest

Riassunto crittografico di un messaggio, usato soprattutto per verificare l'integrità.

## Hashing crittografico

Classe di algoritmi che producono un digest del messaggio e devono essere non invertibili e resistenti alle collisioni.

## Collision resistance

Proprietà per cui è computazionalmente improbabile trovare due messaggi diversi con lo stesso digest.

## Firma digitale

Meccanismo basato su crittografia a chiave pubblica e hashing che garantisce integrità, autenticità e non-ripudio.

## Chiave di sessione

Chiave segreta casuale generata per cifrare una specifica comunicazione o sessione.

## Cifratura ibrida

Schema che combina crittografia simmetrica per cifrare i dati e crittografia asimmetrica per proteggere lo scambio della chiave segreta.

## Certificato X.509

Certificato digitale che associa un'identità a una chiave pubblica, firmato da un'autorità di certificazione.

## Autorità di certificazione

Entità fidata che emette certificati digitali e garantisce l'associazione tra identità e chiavi pubbliche.

## Catena di certificati

Sequenza di certificati in cui la fiducia viene propagata da un'autorità fidata verso entità successive.

## PKI

Public Key Infrastructure: infrastruttura per gestire chiavi pubbliche, certificati e autorità di certificazione.

## Threat model

Descrizione delle minacce, degli attaccanti, delle capacità e delle assunzioni considerate nella progettazione della sicurezza.

## Sistema operativo

Software di base che gestisce risorse hardware, processi, memoria, file system, dispositivi e comunicazioni.

## Autenticazione

Processo con cui un sistema verifica che un soggetto sia davvero chi dichiara di essere.

## Reclamante

Soggetto che dichiara una certa identità durante un processo di autenticazione.

## Controllo degli accessi

Meccanismo che decide se un soggetto autenticato può accedere a una risorsa o oggetto protetto.

## Password file

File che contiene informazioni usate per verificare le password degli utenti, tipicamente hash e salt invece delle password in chiaro.

## Salt

Valore casuale associato a una password prima del calcolo dell'hash, usato per contrastare password uguali e tabelle precomputate.

## Challenge/response

Schema di autenticazione in cui il sistema invia una challenge e l'utente deve calcolare una risposta corretta senza trasmettere direttamente il segreto.

## Nonce

Valore usato una sola volta in un protocollo, utile per impedire il riuso di messaggi validi.

## Man-in-the-middle attack

Attacco in cui un aggressore intercetta o manipola la comunicazione tra due parti.

## Replay attack

Attacco in cui un messaggio valido intercettato viene riutilizzato successivamente per autenticarsi o ottenere accesso.

## Reflection attack

Attacco in cui un messaggio o una challenge viene riflessa in una sessione parallela per ottenere una risposta valida.

## Needham-Schroeder

Protocollo di autenticazione reciproca a chiave pubblica, noto anche per una vulnerabilità scoperta anni dopo la sua proposta originale.

## Parallel sessions attack

Attacco che sfrutta sessioni parallele per riutilizzare messaggi validi in un contesto diverso da quello previsto.

## Oggetto protetto

Risorsa del sistema soggetta a controllo accessi, ad esempio file, memoria, periferica o oggetto generico.

## Soggetto

Entità attiva che richiede accesso a una risorsa, ad esempio utente o processo.

## Access Control List

Lista associata a una risorsa che specifica quali utenti o gruppi hanno quali diritti su quella risorsa.

## Ownership

Diritto o ruolo di proprietario di una risorsa.

## Bit di protezione

Permessi compatti associati a file, tipicamente distinti per owner, group e world.

## Mediazione completa

Principio secondo cui ogni accesso a ogni oggetto protetto deve essere controllato.

## TOC/TOU

Time-of-check/time-of-use: vulnerabilità che nasce quando una risorsa cambia tra il momento del controllo e quello dell'uso.

## Principio dei minimi privilegi

Principio secondo cui ogni soggetto deve avere solo i privilegi strettamente necessari.

## Covert channel

Canale alternativo o non ovvio usato per trasmettere informazioni a soggetti non autorizzati.

## DAC

Discretionary Access Control: modello in cui il proprietario di una risorsa può concedere o modificare accessi a propria discrezione.

## MAC

Mandatory Access Control: modello in cui il sistema impone politiche di accesso non modificabili liberamente dagli utenti.

## Sicurezza multilivello

Modello in cui soggetti e oggetti sono classificati su livelli di sicurezza.

## Bell-LaPadula

Modello MAC orientato alla confidenzialità basato su no-read-up e no-write-down.

## Biba

Modello MAC orientato all'integrità basato su no-write-up e no-read-down.

## Compartimento

Raggruppamento semantico di dati o soggetti, ad esempio progetto, missione o ruolo.

## Need-to-know

Regola secondo cui un soggetto può accedere solo alle informazioni necessarie al proprio ruolo o compartimento.

## Muraglia Cinese

Modello di controllo accessi orientato alla gestione dei conflitti di interesse.

## COI

Conflict of Interest: classe di conflitto di interesse tra dataset.

## Auditing

Registrazione e analisi di eventi rilevanti per la sicurezza.

## IDS

Intrusion Detection System: sistema che analizza dati di audit per rilevare compromissioni o usi non autorizzati.

## Sistema operativo trusted

Sistema operativo progettato per applicare in modo affidabile politiche e meccanismi di sicurezza.

## Fonti

- SRC-001
- SRC-002
- SRC-003
- SRC-004
- SRC-005
