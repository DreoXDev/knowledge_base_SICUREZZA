# Challenge Response e Attacchi

Un protocollo challenge/response permette di dimostrare il possesso di un segreto senza trasmetterlo direttamente.

## Schema base

1. Il verificatore invia una challenge, spesso un nonce.
2. Il reclamante calcola una response crittografica.
3. Il verificatore controlla che la response sia corretta.

Con chiave asimmetrica, la response puo' dimostrare il possesso della chiave privata corrispondente a una chiave pubblica nota.

## Nonce

Il nonce deve cambiare a ogni esecuzione. Questo impedisce a un attaccante di riutilizzare una response valida in un replay attack.

## Reflection e relay

Nei protocolli bidirezionali bisogna includere identita' e contesto nei messaggi. Se mancano, un attaccante puo' riflettere una challenge in un'altra sessione e ottenere una response valida.

## Needham-Schroeder

Needham-Schroeder asimmetrico mostra perche' gli identificativi sono importanti: senza identita' corrette nei messaggi, un attaccante puo' inserirsi tra due sessioni e convincere una parte di stare autenticando il soggetto sbagliato.

## Collegamenti

- [[Challenge_Response_Nonce]]
- [[Replay_Reflection_Attack]]
- [[Needham_Schroeder]]

## Fonti

- SRC-004
- SRC-009

