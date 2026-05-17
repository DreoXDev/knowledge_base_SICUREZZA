# Safety vs Security

> [!Info]
> Safety e security sono concetti collegati ma non equivalenti. La safety riguarda i danni causati dal cattivo funzionamento di un sistema; la security riguarda attacchi, abusi e compromissioni intenzionali.

## Safety engineering

La **safety engineering** riguarda la prevenzione di danni catastrofici causati dal cattivo funzionamento di un sistema informatico.

Esempi:

- sistemi life-critical;
- sistemi avionici;
- controllori di centrali nucleari.

## Security engineering

La **security engineering** riguarda la prevenzione, difesa e recupero rispetto ad attacchi che possono compromettere i valori rappresentati da un sistema informatico.

## Differenza fondamentale

> [!Important]
> Tutte le misure di safety sono anche misure di sicurezza, ma non tutte le misure di sicurezza sono misure di safety.

La safety si concentra principalmente sui danni causati da malfunzionamenti o condizioni accidentali.

La security si concentra invece sulla presenza di attaccanti, abusi, accessi non autorizzati e comportamenti intenzionali.

## Esempio: apertura porte automobile

Un requisito di safety può imporre che le porte di un'automobile si aprano quando l'auto è capovolta.

Una possibile soluzione è installare un sensore di pressione sul tetto dell'auto.

Tuttavia, questa soluzione può introdurre una conseguenza di security: un attaccante potrebbe tentare di aprire l'auto saltando sul tetto.

> [!Warning]
> Una soluzione che migliora la safety può introdurre nuove vulnerabilità di security se non viene progettata considerando anche possibili abusi intenzionali.

## Sintesi rapida

| Aspetto | Safety engineering | Security engineering |
|---|---|---|
| Problema centrale | Malfunzionamenti e danni accidentali | Attacchi e abusi intenzionali |
| Obiettivo | Prevenire danni catastrofici | Proteggere valori e risorse del sistema |
| Esempi | Sistemi avionici, life-critical, centrali nucleari | Accessi non autorizzati, manomissioni, DoS |
| Rischio tipico | Guasto del sistema | Sfruttamento di vulnerabilità |

## Collegamenti

- [[Introduzione_Sicurezza]]
- [[Analisi_Rischio]]
- [[Glossario]]

## Domande d'esame correlate

> [!Question]
> Spiega la differenza tra safety engineering e security engineering.

> [!Question]
> Perché security is not safety?

## Fonti

- SRC-001

