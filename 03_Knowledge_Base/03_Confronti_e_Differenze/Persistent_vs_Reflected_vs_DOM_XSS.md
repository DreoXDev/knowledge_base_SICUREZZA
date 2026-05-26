# Persistent vs Reflected vs DOM XSS

| Variante | Dove sta il payload | Dove avviene l'errore |
|---|---|---|
| Persistent | Salvato lato server | Output server verso piu' utenti |
| Reflected | Nella richiesta | Risposta server che riflette input |
| DOM-based | Nel client/DOM/URL | JavaScript lato client |

## Da ricordare

Persistent e reflected coinvolgono tipicamente output prodotto dal server. DOM-based nasce quando il codice client legge input non fidato e lo inserisce in sink pericolosi.

## Collegamenti

- [[Cross_Site_Scripting_XSS]]

## Fonti

- SRC-007

