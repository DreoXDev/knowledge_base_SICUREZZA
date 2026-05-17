# Compartimenti e modello della Muraglia Cinese

> [!Info]
> I compartimenti introducono il principio del need-to-know. La Muraglia Cinese, invece, controlla i conflitti di interesse e non va confusa con un modello multilivello classico.

## Multi-level vs multi-lateral

I modelli **multi-level** controllano i flussi di informazione in base al livello di criticità dei dati e degli utenti.

I modelli **multi-lateral** controllano i flussi in base a raggruppamenti semantici dei dati e degli utenti.

Esempi di raggruppamenti:

- compartimenti;
- progetti;
- gruppi;
- ruoli.

## Bell-LaPadula esteso con compartimenti

Nel modello esteso, oltre ai livelli di sicurezza, si associano soggetti e oggetti a compartimenti.

Un compartimento può rappresentare:

- progetto;
- missione;
- gruppo operativo.

## Regola della necessità di conoscere

L'accesso è consentito solo se:

```text
livello soggetto >= livello oggetto
AND
compartimenti oggetto subset-of compartimenti soggetto
```

Questo esprime la regola del **need-to-know**: non basta avere un livello alto, bisogna anche appartenere al compartimento corretto.

> [!Important]
> Avere un livello di sicurezza sufficiente non implica automaticamente accesso a tutti i dati di quel livello.

## Muraglia Cinese

Il modello della **Muraglia Cinese** di Brewer e Nash gestisce i conflitti di interesse.

## Obiettivo

Controllare il flusso di dati critici tra aziende concorrenti, limitando l'accesso alle informazioni riservate da parte di consulenti.

## Organizzazione dei dati

I dati sono organizzati su tre livelli:

1. oggetti singoli;
2. dataset aziendali;
3. classi di conflitto di interesse, o COI.

Relazioni:

```text
oggetti singoli subset-of dataset aziendali subset-of classi di COI
```

Ogni oggetto appartiene a un solo dataset e ogni dataset appartiene a una sola classe COI.

## Regola di accesso

Un soggetto `S` può accedere a un oggetto `O` se, rispetto a ogni oggetto `O'` già acceduto da `S`:

```text
dataset(O) = dataset(O')
OR
dataset(O) non appartiene alla COI di dataset(O')
```

In parole semplici:

- si può continuare ad accedere allo stesso dataset aziendale;
- non si può accedere a dataset di aziende concorrenti nella stessa classe di conflitto di interesse.

## Collegamenti

- [[Bell_LaPadula]]
- [[Modelli_Multilivello]]
- [[DAC_MAC]]

## Fonti

- SRC-005

