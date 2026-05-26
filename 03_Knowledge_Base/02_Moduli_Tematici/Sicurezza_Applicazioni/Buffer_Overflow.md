# Buffer Overflow

Un buffer overflow e' una scrittura fuori dai limiti di un buffer.

> [!Warning]
> Il buffer overflow non e' solo "crash del programma": in C puo' diventare controllo del flusso di esecuzione, perche' la memoria adiacente al buffer puo' contenere variabili locali, base pointer o return address.

## Stack frame

Quando una funzione e' chiamata, lo stack frame contiene informazioni come:

- variabili locali;
- base pointer;
- return address;
- eventuali argomenti e dati temporanei.

Se un buffer locale viene scritto oltre i suoi limiti, la scrittura puo' raggiungere altri elementi dello stack frame.

## Effetti possibili

- Sovrascrittura di variabili locali.
- Sovrascrittura del base pointer.
- Sovrascrittura del return address.
- Salto verso codice controllato dall'attaccante.

## Shellcode e NOP sled

Lo shellcode e' codice preparato dall'attaccante per essere eseguito dalla vittima. Un NOP sled e' una sequenza di istruzioni NOP che aumenta la probabilita' che un salto impreciso arrivi comunque allo shellcode.

Un exploit file puo' contenere padding, indirizzi, NOP sled e shellcode per provocare l'overflow e pilotare l'esecuzione.

## Heap buffer overflow

Sul heap l'obiettivo non e' necessariamente il return address. La corruzione puo' riguardare metadati, strutture dati o puntatori a funzione.

## Contromisure

- Canary values: valori sentinella controllati prima del ritorno da funzione.
- GCC `-fstack-protector`, `-fstack-protector-all`, `-fstack-protector-strong`.
- ASLR: randomizzazione degli indirizzi.
- Executable space protection: separazione tra pagine dati e pagine eseguibili.
- NX, XD, XN, DEP: meccanismi hardware/software per impedire esecuzione da pagine dati.

## Limiti

- Un buffer overread puo' rivelare canary o indirizzi utili.
- JIT spraying puo' abusare di codice generato just-in-time.
- I linguaggi managed riducono il rischio, ma non lo eliminano quando interagiscono con codice nativo.

## Collegamenti

- [[Buffer_Manipulation]]
- [[Buffer_Overflow_vs_Buffer_Overread]]
- [[Canary_vs_ASLR_vs_Executable_Space_Protection]]
- [[Contromisure_Buffer_Overflow]]

## Fonti

- SRC-008

