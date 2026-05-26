# Buffer Overflow vs Null Pointer Dereference

| Aspetto | Buffer overflow | Null pointer dereference |
|---|---|---|
| Errore | Scrittura oltre buffer | Uso di NULL come puntatore valido |
| Effetto comune | Corruzione memoria | Crash |
| Exploit tipico | Sovrascrivere return address o puntatori | Controllare pagina NULL/indirizzi bassi |
| Caso critico | C e codice nativo | Kernel mode |

## Da ricordare

Entrambi possono diventare controllo del flusso, ma per strade diverse: overflow corrompe memoria adiacente, null dereference sfrutta un accesso a indirizzi nulli o bassi.

## Collegamenti

- [[Buffer_Overflow]]
- [[Null_Pointer_Dereference]]

## Fonti

- SRC-008

