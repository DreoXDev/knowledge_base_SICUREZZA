# Modello Biba

> [!Info]
> Biba è un modello MAC orientato all'integrità. Impedisce che dati o soggetti meno affidabili contaminino oggetti a integrità più alta.

## Obiettivo

Il modello **Biba** è orientato all'**integrità**.

Il suo obiettivo è impedire che dati o soggetti meno affidabili compromettano oggetti di maggiore integrità.

## Proprietà principali

Il sistema operativo usa uno schema MAC che garantisce due proprietà.

### Simple integrity axiom - no-write-up

Un soggetto non può modificare oggetti di classificazione più alta.

```text
No Write Up
```

Esempio: un soggetto a integrità media non può scrivere su oggetti a integrità alta.

### Integrity confinement axiom - no-read-down

Un soggetto non legge oggetti di classificazione più bassa.

```text
No Read Down
```

Questa regola evita che dati meno affidabili influenzino soggetti o processi di livello più alto.

## Differenza rispetto a Bell-LaPadula

| Modello | Obiettivo | Regole sintetiche |
|---|---|---|
| Bell-LaPadula | confidenzialità | no-read-up, no-write-down |
| Biba | integrità | no-write-up, no-read-down |

> [!Summary]
> Bell-LaPadula evita la fuga di informazioni verso il basso; Biba evita la contaminazione dell'integrità verso l'alto.

## Collegamenti

- [[Bell_LaPadula]]
- [[Modelli_Multilivello]]
- [[CIA_Triad_DAD]]

## Fonti

- SRC-005

