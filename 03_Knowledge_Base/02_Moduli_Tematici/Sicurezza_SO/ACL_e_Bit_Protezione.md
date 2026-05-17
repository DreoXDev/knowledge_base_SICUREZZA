# Access Control List e bit di protezione

> [!Info]
> ACL e bit Unix/Linux sono meccanismi concreti per rappresentare chi può accedere a una risorsa e con quali diritti.

## Access Control List

Una **Access Control List** associa a una risorsa una lista di soggetti o gruppi e i rispettivi diritti.

Esempio concettuale:

```text
utente/gruppo          risorsa       diritti
ROSSI.VENDITE          File1         ORW
*.VENDITE              File2         RX
BIANCHI.MARKETING      *.*           X
```

Dove:

| Simbolo | Significato |
|---|---|
| `O` | ownership |
| `R` | read |
| `W` | write |
| `X` | execute |

## Benefici delle ACL

Le ACL permettono:

- risparmio di spazio rispetto a una tabella completa soggetto-oggetto;
- facile determinazione degli utenti che hanno un diritto su una risorsa;
- facile revoca o modifica dell'accesso di un utente a una risorsa.

## Bit di protezione Unix/Linux

I bit di protezione sono una versione semplificata di ACL.

In Unix/Linux, per ogni file si usano permessi distinti per:

- owner;
- group;
- world.

Per ciascuno si definiscono i diritti:

```text
R W X
```

Quindi la struttura tipica è:

```text
OWNER  GROUP  WORLD
R W X  R W X  R W X
```

## Benefici dei bit di protezione

- bassa occupazione di memoria;
- bastano user ID, group ID e 9 bit per file;
- gestione semplice;
- il proprietario può assegnare o modificare i diritti della risorsa.

## Limite

I bit di protezione sono più semplici ma meno espressivi di ACL più generali.

> [!Summary]
> Le ACL sono più flessibili; i bit Unix/Linux sono più semplici e compatti.

## Collegamenti

- [[Controllo_Accessi_SO]]
- [[DAC_MAC]]

## Fonti

- SRC-005

