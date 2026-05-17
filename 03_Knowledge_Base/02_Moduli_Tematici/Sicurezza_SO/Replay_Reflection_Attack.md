# Replay attack e reflection attack

> [!Info]
> Replay e reflection attack mostrano che cifrare un messaggio non basta: un protocollo deve impedire riuso, ambiguità di ruolo e trasferimento di risposte tra sessioni diverse.

## Replay attack

Un **replay attack** avviene quando un attaccante intercetta un messaggio valido e lo riutilizza in seguito per autenticarsi.

Esempio:

1. Alice si autentica inviando una risposta cifrata valida;
2. Charlie intercetta quella risposta;
3. Charlie reinvia la stessa risposta;
4. il server accetta Charlie come se fosse Alice.

## Difesa tramite nonce

La difesa principale è usare un nonce, cioè una challenge valida una sola volta.

Se Charlie reinvia una vecchia risposta, il server la rifiuta perché la challenge attuale è diversa.

> [!Summary]
> Il nonce non deve essere segreto: deve solo essere nuovo a ogni sessione.

## Reflection attack

Un **reflection attack** sfrutta protocolli di autenticazione bidirezionale simmetrici.

Scenario:

- il client e il server usano lo stesso protocollo in entrambe le direzioni;
- Charlie non conosce la chiave e non sa calcolare `encrK(N)`;
- Charlie apre una sessione parallela e fa calcolare alla vittima la risposta corretta;
- poi riflette quella risposta verso il server.

## Perché è possibile

Il problema nasce dalla simmetria del protocollo: se i messaggi nelle due direzioni hanno la stessa forma, un attaccante può riutilizzare una risposta prodotta per un contesto in un altro contesto.

## Soluzione

Eliminare la simmetria inserendo l'identità del mittente nei messaggi cifrati.

Esempio:

```text
encrK(server, N)
```

In questo modo, quando il messaggio viene decifrato, il destinatario può verificare non solo il nonce, ma anche l'identità associata al messaggio.

> [!Important]
> Nei protocolli di autenticazione non basta cifrare: bisogna anche legare crittograficamente messaggi, identità e contesto.

## Collegamenti

- [[Challenge_Response_Nonce]]
- [[Needham_Schroeder]]
- [[Limiti_Crittografia_e_Threat_Model]]

## Fonti

- SRC-004

