# Contromisure Null Pointer Dereference

## Problema

Il programma usa un puntatore NULL come se puntasse a un oggetto valido. Nel kernel puo' portare a privilege escalation.

## Cause tipiche

- Controllo NULL assente.
- Controllo NULL dopo l'uso.
- Puntatori a funzione non verificati.
- Ottimizzazioni del compilatore che eliminano check tardivi.

## Contromisure

- Controllare puntatori prima di ogni dereferenziazione critica.
- Evitare check tardivi.
- Non mappare pagina 0.
- Configurare `mmap_min_addr`.
- Usare static analysis e warning del compilatore.

## Limiti delle contromisure

Un controllo scritto nel sorgente puo' non bastare se viene dopo l'uso. La sicurezza dipende anche da configurazione kernel e privilegi di mapping.

## Collegamenti

- [[Null_Pointer_Dereference]]
- [[CVE_2009_2692]]
- [[CVE_2009_1897]]

