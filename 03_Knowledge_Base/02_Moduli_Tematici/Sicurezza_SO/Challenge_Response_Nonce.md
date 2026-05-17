# Challenge/response e nonce

> [!Info]
> Challenge/response permette di dimostrare la conoscenza di un segreto senza trasmettere direttamente il segreto. Il nonce impedisce il riuso di vecchie risposte valide.

## Challenge/response

Nel meccanismo **challenge/response**, la password non è semplicemente una stringa trasmessa al server.

La password può essere vista come una funzione matematica `F(x)` che l'utente sa calcolare.

Per autenticarsi:

1. il sistema propone un valore casuale `X`;
2. il richiedente risponde con il valore corretto `F(X)`;
3. il sistema verifica la risposta.

## Obiettivo

L'obiettivo è dimostrare la conoscenza del segreto senza trasmettere direttamente il segreto.

## Rischio della trasmissione diretta

Se Alice trasmette direttamente:

```text
User: alice
Pw: wonderland
```

un attaccante che intercetta la comunicazione può riutilizzare la password e fingere di essere Alice.

Questo è collegato agli attacchi basati sull'intercettazione dei dati in rete, come il man-in-the-middle.

## Challenge/response con crittografia

Un protocollo più sicuro usa la crittografia per dimostrare la conoscenza del segreto senza trasmetterlo.

Esempio con chiave segreta condivisa `K`:

1. il server invia una challenge;
2. Alice cifra la challenge con `K`;
3. il server decifra e verifica;
4. la chiave `K` non viene mai inviata sulla rete.

## Nonce

Un **nonce** è un messaggio usato una sola volta.

Caratteristiche:

- cambia a ogni autenticazione;
- non deve essere segreto;
- impedisce il riuso di vecchie risposte valide.

> [!Important]
> Il nonce serve soprattutto a difendere dai replay attack.

## Requisiti per challenge/response sicuri

Un protocollo challenge/response sicuro deve:

1. usare crittografia insieme a challenge/response;
2. cambiare il challenge ogni volta tramite nonce;
3. inserire identificativi nei messaggi cifrati.

## Autenticazione bidirezionale

Spesso non basta autenticare il client verso il server: anche il server deve autenticarsi verso il client.

In questo caso si parla di autenticazione reciproca o bidirezionale.

## Collegamenti

- [[Replay_Reflection_Attack]]
- [[Needham_Schroeder]]
- [[Crittografia_Simmetrica]]
- [[Crittografia_Asimmetrica]]

## Fonti

- SRC-004

