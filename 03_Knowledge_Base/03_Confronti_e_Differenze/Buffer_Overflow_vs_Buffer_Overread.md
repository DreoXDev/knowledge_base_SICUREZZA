# Buffer Overflow vs Buffer Overread

| Aspetto | Buffer overflow | Buffer overread |
|---|---|---|
| Operazione | Scrittura fuori limite | Lettura fuori limite |
| Rischio principale | Corruzione memoria e controllo flusso | Esposizione informazioni |
| Esempio | Sovrascrittura return address | Heartbleed |
| CIA | Integrita'/disponibilita', talvolta confidenzialita' | Confidenzialita' |

## Da ricordare

Overflow non significa solo crash: puo' alterare l'esecuzione. Overread non altera direttamente la memoria, ma puo' rivelare segreti utili per altri exploit.

## Collegamenti

- [[Buffer_Overflow]]
- [[Buffer_Overread_Heartbleed]]

## Fonti

- SRC-008

