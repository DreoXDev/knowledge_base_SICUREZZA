# SRC-008 - Sicurezza applicazioni p2

> [!Info]
> Fonte originale: `01_Raw_Assets/slides/Sicurezza applicazioni parte 2.pdf`
> Stato: integrato nella KB
> Tipo: slide teoriche
> Modulo: Sicurezza nelle applicazioni

## Argomenti principali

- Buffer manipulation: buffer overflow e buffer overread.
- Vulnerability pattern in C: `gets`, `fgets` con lunghezza errata, input utente come parametro di lunghezza, magic numbers.
- Buffer overflow su stack e heap, shellcode, NOP sled e puntatori a funzione.
- Contromisure: canary values, stack protector GCC, ASLR, executable space protection, NX/XD/XN/DEP.
- Buffer overread e Heartbleed / CVE-2014-0160.
- Null pointer dereference nel kernel e CVE-2009-2692 / CVE-2009-1897.
- Java secure coding guidelines e strumenti static analysis.

## Concetti chiave estratti

Un buffer e' uno spazio di memoria usato per conservare dati; in C letture e scritture possono uscire dai limiti se il programma non controlla indici e lunghezze. L'overflow scrive fuori limite, l'overread legge fuori limite.

La null pointer dereference spesso produce crash, ma nel kernel puo' diventare privilege escalation se l'attaccante controlla la pagina NULL o indirizzi bassi usati dal codice privilegiato.

## Dettaglio per sezioni

### Buffer overflow

Lo stack contiene variabili locali, base pointer e return address. Una scrittura oltre il buffer puo' sovrascrivere dati adiacenti o il return address, portando l'esecuzione verso shellcode. Su heap, la corruzione puo' coinvolgere puntatori a funzione.

### Contromisure

Canary values rilevano sovrascritture prima del ritorno da funzione. ASLR rende meno prevedibili gli indirizzi. Executable space protection impedisce esecuzione da pagine dati. Le difese non sono assolute: overread, JIT spraying e codice nativo in ambienti managed possono aggirare alcune assunzioni.

### Heartbleed

Heartbleed nasce da una inconsistenza tra lunghezza dichiarata e payload reale nel heartbeat TLS: `memcpy` copia piu' dati di quelli inviati e restituisce memoria adiacente.

### CVE kernel e Java

CVE-2009-2692 e CVE-2009-1897 mostrano che null pointer dereference nel kernel puo' essere sfruttata con mapping della pagina 0 e manipolazione di puntatori. Le linee guida Java riducono weakness tramite regole di coding e static analysis.

## Collegamenti alla KB

- [[Buffer_Manipulation]]
- [[Buffer_Overflow]]
- [[Buffer_Overread_Heartbleed]]
- [[Null_Pointer_Dereference]]
- [[CVE_2009_2692]]
- [[CVE_2009_1897]]
- [[Java_Secure_Coding_Guidelines]]

## Possibili domande d'esame

- Come puo' un buffer overflow alterare il flusso di controllo?
- Spiega canary values, ASLR ed executable space protection.
- Che cos'e' Heartbleed e perche' e' un buffer overread?
- Come puo' una null pointer dereference diventare privilege escalation?
- Quali warning SpotBugs sono citati dalle slide?

## Flashcard derivate

- Buffer overflow: scrittura fuori limite.
- Buffer overread: lettura fuori limite.
- NOP sled: sequenza di NOP che aumenta la probabilita' di raggiungere shellcode.
- ASLR: randomizzazione degli indirizzi.
- Heartbleed: lunghezza dichiarata maggiore del payload reale.
- Null pointer dereference kernel: possibile uso di dati controllati con privilegi kernel.

## Note di integrazione

Le note distinguono pattern generale, weakness, vulnerabilita' concreta e contromisura, per evitare di confondere buffer overflow, Heartbleed e CVE kernel.

