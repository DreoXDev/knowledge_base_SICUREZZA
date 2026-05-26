# Null Pointer Dereference

Un puntatore contiene un indirizzo di memoria. NULL e' un valore speciale che indica assenza di oggetto valido. Una null pointer dereference avviene quando il programma usa NULL come se puntasse a un oggetto.

## Da crash a exploit

In molti programmi una dereferenziazione di NULL causa crash. In alcuni contesti, soprattutto kernel, puo' diventare sfruttabile se l'attaccante riesce a controllare la pagina 0 o indirizzi bassi.

## Mapping

La weakness e' collegata a CWE-476: NULL Pointer Dereference.

## Pagina 0, mmap e kernel

Con `mmap` un processo puo' richiedere mapping di memoria. Se la pagina 0 o indirizzi bassi sono mappabili, l'attaccante puo' predisporre dati o codice dove il kernel si aspetta di trovare una struttura valida.

Il rischio aumenta perche' il kernel puo' essere mappato nello spazio di memoria del processo e opera con privilegi superiori. Se dereferenzia un puntatore a funzione NULL, puo' saltare verso un indirizzo controllato.

## Contromisure

- Non mappare pagina 0.
- Controllare puntatori prima dell'uso.
- Evitare check tardivi.
- Usare warning del compilatore e static analysis.
- Impostare difese kernel come `mmap_min_addr`.

## Collegamenti

- [[CVE_2009_2692]]
- [[CVE_2009_1897]]
- [[Buffer_Overflow_vs_Null_Pointer_Dereference]]
- [[Contromisure_Null_Pointer_Dereference]]

## Fonti

- SRC-008

