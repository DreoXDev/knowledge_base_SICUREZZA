# Processo di autenticazione sicuro

> [!Info]
> Un processo di autenticazione sicuro deve proteggere il segreto, ma anche evitare di rivelare informazioni indirette tramite errori, tempi di risposta o procedure di recupero.

## Proprietà di un sistema ben progettato

Un sistema di autenticazione ben progettato dovrebbe:

- non fornire dettagli su nomi utente o sistema prima dell'autenticazione;
- usare risposte di errore generiche;
- poter essere intenzionalmente lento per scoraggiare forza bruta;
- disabilitare utenti dopo alcuni tentativi falliti;
- supportare autenticazione a più fattori;
- essere resistente ad attacchi basati sul tempo di risposta.

## Messaggi di errore

Un sistema non dovrebbe dire:

```text
password errata per utente esistente
utente inesistente
account disabilitato
```

perché queste risposte rivelano informazioni utili all'attaccante.

Meglio rispondere con messaggi generici, ad esempio:

```text
Login failed: invalid user ID or password.
```

## Recupero password

Anche il recupero password non dovrebbe rivelare se un indirizzo email è registrato.

Messaggio corretto:

```text
If that email address is in our database, we will send you a password reset link.
```

## Autenticazione a più fattori

Un sistema può usare più meccanismi insieme, per esempio:

```text
password + one-time password
```

Questo riduce il rischio che la compromissione di un singolo fattore basti per accedere.

## Timing attack

Un attacco basato sul tempo di risposta sfrutta differenze misurabili nei tempi del sistema per dedurre informazioni, ad esempio se un utente esiste o se una parte della password è corretta.

> [!Important]
> La sicurezza del processo di autenticazione dipende anche da ciò che il sistema rivela indirettamente.

## Collegamento con autorizzazione

Un login corretto non implica accesso illimitato: dopo l'autenticazione entrano in gioco politiche di controllo accessi, ACL, DAC/MAC e modelli di sicurezza.

Vedi: [[ACL_e_Bit_Protezione]], [[DAC_MAC]]

## Collegamenti

- [[Autenticazione]]
- [[Attacchi_alle_Password]]
- [[Challenge_Response_Nonce]]

## Fonti

- SRC-004
- SRC-005
