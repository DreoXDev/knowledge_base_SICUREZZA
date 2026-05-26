# Bell-LaPadula con Compartimenti

Bell-LaPadula e' un modello MAC orientato alla confidenzialita'. La versione estesa con compartimenti combina classificazione multilivello e need-to-know.

## Regola di lettura

Un soggetto puo' leggere un oggetto solo se:

- il livello del soggetto domina il livello dell'oggetto;
- i compartimenti dell'oggetto sono sottoinsieme dei compartimenti del soggetto.

In forma compatta:

```text
livello_soggetto >= livello_oggetto
AND
compartimenti_oggetto ⊆ compartimenti_soggetto
```

## Regole principali

- No read up: non si leggono oggetti a livello superiore.
- No write down: non si scrive verso livelli inferiori.
- Compartimenti: limitano l'accesso anche tra soggetti con livello sufficiente.

## MAC o DAC

E' una politica MAC, non DAC, perche' le regole sono imposte dal sistema e non dalla discrezione del proprietario della risorsa.

## Collegamenti

- [[Bell_LaPadula]]
- [[Compartimenti_Muraglia_Cinese]]
- [[DAC_MAC]]

## Fonti

- SRC-005
- SRC-009
- SRC-010

