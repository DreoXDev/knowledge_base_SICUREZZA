# Sicurezza Applicazioni - Parte 2

La seconda parte riguarda weakness legate alla memoria, vulnerabilita' kernel basate su null pointer dereference e linee guida Java per prevenire difetti ricorrenti tramite secure coding e analisi statica.

## Percorso di studio

1. [[Buffer_Manipulation]]
2. [[Buffer_Overflow]]
3. [[Buffer_Overread_Heartbleed]]
4. [[Null_Pointer_Dereference]]
5. [[CVE_2009_2692]]
6. [[CVE_2009_1897]]
7. [[Java_Secure_Coding_Guidelines]]

## Idee guida

- Buffer overflow e buffer overread sono entrambi accessi fuori limite, ma uno scrive e l'altro legge.
- Un overflow sullo stack puo' alterare variabili, base pointer o return address.
- Heartbleed e' un esempio di overread causato da inconsistenza tra lunghezza dichiarata e payload reale.
- Una null pointer dereference nel kernel puo' diventare privilege escalation se indirizzi bassi sono controllabili.
- Le linee guida Java riducono weakness prima che diventino vulnerabilita'.

## Fonti

- SRC-008

