# Controllo degli accessi nei sistemi operativi

> [!Info]
> Il controllo degli accessi decide quali soggetti possono usare quali oggetti protetti e con quali diritti. Arriva dopo l'autenticazione: prima si stabilisce chi è il soggetto, poi si decide cosa può fare.

## Idea generale

Il controllo degli accessi serve a stabilire quali soggetti possono usare quali oggetti protetti e con quali diritti.

Gli utenti autorizzati all'accesso al sistema non hanno necessariamente gli stessi diritti su tutte le risorse.

Esempi di diritti:

- lettura;
- scrittura;
- esecuzione;
- uso di periferiche;
- accesso a file, dischi o stampanti.

## Soggetti, oggetti e diritti

| Concetto | Significato |
|---|---|
| Soggetto | entità attiva che richiede accesso, ad esempio utente o processo |
| Oggetto | risorsa protetta, ad esempio file, memoria, periferica |
| Diritto | operazione consentita, ad esempio read, write, execute |

## Password per risorse specifiche

Un possibile meccanismo di controllo accessi è assegnare password a specifiche risorse.

Questo però è un approccio debole.

### Svantaggi

- è poco raffinato;
- distingue solo tra possibilità e divieto di accesso;
- è poco usabile;
- richiede molte password diverse;
- rende difficile tracciare chi ha accesso a quali risorse;
- è scomodo per programmi che devono accedere a molte risorse;
- rende difficile revocare i diritti.

> [!Important]
> Il controllo degli accessi richiede meccanismi più strutturati delle semplici password per risorsa.

## Collegamenti

- [[Autenticazione]]
- [[ACL_e_Bit_Protezione]]
- [[Obiettivi_Controllo_Accessi]]
- [[DAC_MAC]]

## Fonti

- SRC-005

