# Style Guide

## Stile generale

Le note devono avere tono universitario, chiaro e orientato all'esame. Evitare frasi vaghe, contenuti non verificati e spiegazioni troppo colloquiali.

Preferire note modulari, collegate tra loro, invece di file lunghi e monolitici.

## Markdown e Obsidian

Usare Markdown pulito e compatibile con Obsidian.

Linkare solo concetti realmente utili:

```md
[[Nome della nota]]
```

## Callout

Usare callout quando migliorano la leggibilita':

```md
> [!Info]
> Contesto generale o sintesi del concetto.
```

```md
> [!Question]
> Domanda tipica d'esame.
```

```md
> [!Warning]
> Errore comune o confusione frequente.
```

```md
> [!Example]
> Esempio concettuale o scenario.
```

## Note teoriche

Struttura consigliata:

```md
# Titolo Concetto

> [!Info]
> Sintesi breve in 2-4 righe.

## Definizione

## Spiegazione

## Dettagli importanti

## Collegamenti con altri concetti

## Possibili domande d'esame

## Errori comuni

## Fonti
```

## Definizioni

Le definizioni devono essere brevi ma precise. Se serve, aggiungere una spiegazione intuitiva separata dalla definizione formale.

## Domande d'esame

Le domande devono avere un ID progressivo nel formato `Q-001`, `Q-002`, `Q-003`.

Le risposte devono essere complete ma non enciclopediche: abbastanza dettagliate per un esame teorico, ma facili da ripassare.

## Flashcard

Preferire flashcard atomiche:

```md
Che cos'e' X?:: X e' ...
```

Per risposte piu' articolate:

```md
**Domanda:** ...

**Risposta:** ...
```

Ogni flashcard deve testare un solo concetto.

