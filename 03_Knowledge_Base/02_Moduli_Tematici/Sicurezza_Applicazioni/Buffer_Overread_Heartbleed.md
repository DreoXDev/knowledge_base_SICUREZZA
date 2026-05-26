# Buffer Overread e Heartbleed

Un buffer overread e' una lettura oltre i limiti di un buffer. A differenza del buffer overflow, non scrive memoria adiacente: la legge e puo' esporre informazioni sensibili.

## Heartbleed

Heartbleed, CVE-2014-0160, e' una vulnerabilita' legata al meccanismo heartbeat TLS. Il client invia un payload e dichiara una lunghezza. Il server copia in risposta un numero di byte pari alla lunghezza dichiarata.

Se la lunghezza dichiarata e' maggiore del payload reale, una `memcpy` con lunghezza non verificata puo' copiare anche memoria oltre il payload.

## Weakness collegata

Il problema e' un caso di CWE-130: improper handling of length parameter inconsistency. Il parametro di lunghezza non e' coerente con la dimensione effettiva dei dati.

## Conseguenze

- Esposizione di memoria del processo.
- Possibile leak di chiavi, credenziali, cookie o altri dati sensibili.
- Violazione della confidenzialita' senza necessariamente causare crash.

## Collegamenti

- [[Buffer_Manipulation]]
- [[Buffer_Overflow_vs_Buffer_Overread]]

## Fonti

- SRC-008

