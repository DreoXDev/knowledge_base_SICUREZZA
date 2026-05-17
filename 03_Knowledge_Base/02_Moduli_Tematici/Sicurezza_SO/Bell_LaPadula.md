# Modello di Bell-LaPadula

> [!Info]
> Bell-LaPadula è un modello MAC orientato alla confidenzialità. Impedisce che informazioni sensibili fluiscano verso soggetti con autorizzazione insufficiente.

## Obiettivo

Il modello di **Bell-LaPadula** è orientato alla **confidenzialità**.

Il suo obiettivo è impedire che informazioni sensibili fluiscano verso soggetti con livello di autorizzazione insufficiente.

## Contesto

Nasce da policy di sicurezza militare e usa livelli di classificazione per soggetti e oggetti.

Esempi:

- top-secret;
- secret;
- riservato;
- unclassified.

## Proprietà principali

Il sistema operativo usa uno schema MAC che garantisce due proprietà.

### Simple security property - no-read-up

Un soggetto non può leggere oggetti di classificazione più alta.

```text
No Read Up
```

Esempio: un utente `secret` non può leggere oggetti `top-secret`.

### Confinement property - no-write-down

Un soggetto non può scrivere oggetti di classificazione più bassa.

```text
No Write Down
```

Esempio: un utente `secret` non può scrivere dati in un oggetto `unclassified`.

## Perché no-write-down

La regola serve a impedire che informazioni di livello alto vengano copiate o propagate verso livelli più bassi.

> [!Important]
> Bell-LaPadula protegge la confidenzialità controllando i flussi di informazione dall'alto verso il basso.

## Collegamenti

- [[Modelli_Multilivello]]
- [[Biba]]
- [[Compartimenti_Muraglia_Cinese]]
- [[Covert_Channels]]
- [[CIA_Triad_DAD]]

## Fonti

- SRC-005

