# Modelli di sicurezza multilivello

> [!Info]
> I modelli multilivello definiscono regole formali per decidere quali soggetti possono accedere a quali oggetti in base a livelli di sicurezza o integrità.

## Definizione

I modelli di sicurezza MAC definiscono in modo preciso la relazione di accessibilità tra soggetti e oggetti del sistema.

La relazione dipende dagli obiettivi e dai requisiti di sicurezza del dominio applicativo.

## Sicurezza multilivello

La sicurezza multilivello nasce in ambienti militari.

In questi contesti, la confidenzialità dei dati è spesso il requisito principale.

Il sistema classifica:

- soggetti;
- oggetti.

Esempi di livelli:

```text
top-secret
secret
riservato / limitato
unclassified
```

## Regola base per la confidenzialità

L'accesso è consentito solo se:

```text
livello soggetto >= livello oggetto
```

Quindi un soggetto può leggere dati del proprio livello o di livello inferiore, ma non dati di livello superiore.

## Adattamento ad ambienti commerciali

In ambienti commerciali la confidenzialità resta importante, ma in alcuni casi l'integrità dei dati può essere ancora più importante.

Per questo esistono modelli orientati alla confidenzialità e modelli orientati all'integrità.

## Problemi noti

I modelli multilivello presentano alcuni problemi:

- complessità di amministrazione;
- necessità di applicazioni dedicate;
- tendenza alla over-classification;
- problema del blind write-up;
- difficoltà di definire molti livelli di classificazione.

> [!Summary]
> È importante conoscere gli obiettivi e il funzionamento dei modelli multilivello per progettare e valutare meglio politiche di sicurezza, anche se nella pratica possono essere complessi da amministrare.

## Collegamenti

- [[DAC_MAC]]
- [[Bell_LaPadula]]
- [[Biba]]
- [[Compartimenti_Muraglia_Cinese]]

## Fonti

- SRC-005

