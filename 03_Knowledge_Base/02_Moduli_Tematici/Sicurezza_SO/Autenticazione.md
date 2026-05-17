# Autenticazione

> [!Info]
> L'autenticazione verifica che un soggetto sia davvero chi dichiara di essere. È una precondizione per applicare correttamente controllo accessi e protezione delle risorse.

## Definizione

L'autenticazione è il processo con cui un sistema verifica che un soggetto sia davvero chi dichiara di essere.

Nelle slide il soggetto che dichiara una certa identità è chiamato **reclamante**.

Esempio:

```text
Sono Alice!
```

Il sistema deve decidere se accettare o rifiutare questa identità reclamata.

## Obiettivo

L'obiettivo dell'autenticazione è evitare l'accesso di soggetti non autorizzati alle risorse del sistema.

## Dopo l'autenticazione

L'autenticazione stabilisce chi è il soggetto.

Il controllo degli accessi stabilisce cosa quel soggetto può fare.

Vedi: [[Controllo_Accessi_SO]]

## Metodi per l'autenticazione

I metodi principali possono essere raggruppati in tre categorie.

### Dimostrazione di conoscenza

Il soggetto dimostra di conoscere un segreto.

Esempi:

- PIN;
- password;
- challenge/response.

### Dimostrazione di possesso

Il soggetto dimostra di possedere un oggetto.

Esempi:

- chiavi fisiche;
- smartcard di identificazione;
- token hardware.

### Caratteristiche personali uniche

Il soggetto viene riconosciuto tramite caratteristiche biometriche.

Esempi:

- impronte digitali;
- riconoscimento del viso;
- riconoscimento vocale.

## Collegamenti

- [[Password_Hashing_Salt]]
- [[Challenge_Response_Nonce]]
- [[Processo_Autenticazione_Sicuro]]
- [[Sicurezza_SO_Introduzione]]

## Fonti

- SRC-004
- SRC-005
