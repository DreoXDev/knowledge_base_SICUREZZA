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

## Fonti

- SRC-001
- SRC-002
- SRC-003
