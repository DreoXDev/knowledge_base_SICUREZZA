# Protocollo Needham-Schroeder

> [!Info]
> Needham-Schroeder è un protocollo di autenticazione reciproca a chiave pubblica. È importante perché mostra che anche protocolli basati su crittografia forte possono fallire se i messaggi non includono identità e contesto corretti.

## Obiettivo

Needham-Schroeder è un protocollo di autenticazione reciproca basato su crittografia a chiave pubblica.

L'obiettivo è permettere ad Alice e al server di autenticarsi reciprocamente usando nonce e cifratura asimmetrica.

## Versione nelle slide

La versione mostrata è:

```text
A -> S: encrPK-S(A, NA)
S -> A: encrPK-A(NA, NS)
A -> S: encrPK-S(NS)
```

Dove:

- `A` è Alice;
- `S` è il server;
- `NA` è il nonce generato da Alice;
- `NS` è il nonce generato dal server;
- `PK-S` è la chiave pubblica del server;
- `PK-A` è la chiave pubblica di Alice.

## Requisiti desiderati

Il protocollo dovrebbe soddisfare tre requisiti:

1. usare crittografia insieme a challenge/response;
2. cambiare il challenge di volta in volta tramite nonce;
3. inserire identificativi nei messaggi criptati.

## Vulnerabilità

La versione originale è vulnerabile perché il secondo e il terzo messaggio non includono l'identità del mittente.

Questo bug è stato identificato 17 anni dopo l'ideazione del protocollo.

## Parallel sessions attack

Nel **parallel sessions attack**, Charlie apre sessioni parallele e usa Alice come oracolo per ottenere messaggi validi da inoltrare al server.

L'attacco sfrutta il fatto che i messaggi non sono sufficientemente legati all'identità e al contesto della sessione.

## Versione corretta

La versione corretta aggiunge l'identità del server nel secondo messaggio e l'identità di Alice nel terzo:

```text
A -> S: encrPK-S(A, NA)
S -> A: encrPK-A(S, NA, NS)
A -> S: encrPK-S(A, NS)
```

## Idea chiave

> [!Important]
> I protocolli crittografici possono essere vulnerabili anche se usano algoritmi crittografici forti. La correttezza dipende dalla struttura dei messaggi e dalle assunzioni sul contesto.

## Collegamenti

- [[Challenge_Response_Nonce]]
- [[Replay_Reflection_Attack]]
- [[Crittografia_Asimmetrica]]
- [[Limiti_Crittografia_e_Threat_Model]]

## Fonti

- SRC-004

