# Canary vs ASLR vs Executable Space Protection

| Difesa | Idea | Limite |
|---|---|---|
| Canary | Rilevare sovrascrittura prima del return | Se il canary e' noto o letto, puo' essere ricostruito |
| ASLR | Randomizzare indirizzi | Leak di indirizzi puo' ridurne l'efficacia |
| Executable space protection | Non eseguire codice da pagine dati | JIT spraying e ROP possono aggirare l'assunzione semplice |

## Da ricordare

Sono difese complementari. Nessuna elimina il bug: riducono la probabilita' o l'impatto dello sfruttamento.

## Collegamenti

- [[Buffer_Overflow]]
- [[Contromisure_Buffer_Overflow]]

## Fonti

- SRC-008

