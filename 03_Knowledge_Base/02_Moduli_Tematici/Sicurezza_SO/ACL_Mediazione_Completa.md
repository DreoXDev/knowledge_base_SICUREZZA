# ACL e Mediazione Completa

Una Access Control List associa a ogni oggetto protetto l'elenco dei soggetti autorizzati e dei diritti concessi.

## Funzionamento ACL

Per ogni risorsa, la ACL specifica quali utenti o gruppi possono leggere, scrivere, eseguire o svolgere altre operazioni. E' quindi una vista per oggetto della matrice di controllo degli accessi.

## Bit Unix/Linux

Nei sistemi Unix/Linux classici, i permessi sono rappresentati con 9 bit:

- 3 bit per owner: read, write, execute;
- 3 bit per group: read, write, execute;
- 3 bit per others/world: read, write, execute.

E' una forma compatta ma meno espressiva di una ACL arbitraria.

## Mediazione completa

La mediazione completa e' il principio secondo cui ogni accesso a ogni oggetto protetto deve essere controllato.

Nella pratica puo' esserci tensione con efficienza, cache, file descriptor o handle gia' aperti: controllare ogni singola operazione e' piu' sicuro, ma puo' avere costo maggiore.

## Collegamenti

- [[ACL_e_Bit_Protezione]]
- [[Obiettivi_Controllo_Accessi]]
- [[DAC_MAC]]

## Fonti

- SRC-005
- SRC-009
- SRC-011

