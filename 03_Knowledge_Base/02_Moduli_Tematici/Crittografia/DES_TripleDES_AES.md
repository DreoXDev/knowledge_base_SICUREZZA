# DES, Triple DES e AES

> [!Info]
> DES, Triple DES e AES sono esempi importanti di crittografia simmetrica. Mostrano anche come la sicurezza pratica dipenda dalla dimensione delle chiavi e dalla potenza computazionale disponibile nel tempo.

## DES - Data Encryption Standard

DES è un algoritmo di cifratura simmetrica basato su:

- confusione dell'informazione;
- diffusione dell'informazione.

Codifica messaggi in blocchi da 64 bit e applica 16 volte una funzione combinatoria a ogni blocco usando la chiave come parametro.

## Struttura generale di DES

Il blocco da 64 bit viene diviso in:

- metà sinistra;
- metà destra.

La funzione interna combina dati e chiave, applica permutazioni e somme, poi ripete il processo per 16 round.

Obiettivi:

- evitare relazioni ovvie tra bit di input e bit di output;
- diffondere l'effetto delle modifiche dell'input su più bit dell'output.

## Chiave DES

La versione originale usa:

- 56 bit di chiave effettiva;
- 8 bit aggiuntivi per correzione d'errore.

Le operazioni sono logiche e implementabili efficientemente sia in hardware sia in software.

## Sicurezza di DES

Non esiste una prova matematica della sicurezza di DES.

DES può essere violato tramite forza bruta:

- lo spazio delle chiavi è pari a `2^56`;
- in media si provano `2^55` chiavi.

Storicamente:

- nel 1977 il tempo stimato nel caso medio era superiore a 700 anni;
- nel 1997 un attacco parallelo su circa 3500 PC richiese circa 4 mesi;
- nel 1998 una macchina specializzata da circa 100.000 dollari riuscì a risolvere il problema in circa 4 giorni.

> [!Important]
> La sicurezza pratica di un algoritmo può cambiare nel tempo a causa dell'aumento della potenza computazionale e della possibilità di parallelizzare gli attacchi.

## Triple DES

Triple DES nasce come alternativa a DES.

L'idea è cifrare tre volte usando tre chiavi diverse.

La sicurezza risultante è paragonabile all'uso di una chiave da 112 bit e aumenta enormemente il tempo stimato per un attacco di forza bruta.

## AES - Advanced Encryption Standard

AES è basato su trasformazioni efficienti applicate a blocchi da 128 bit.

Le trasformazioni includono:

- sostituzione;
- scorrimento;
- mescolamento dei bit.

Caratteristiche:

- blocchi da 128 bit;
- chiavi da 128, 192 o 256 bit;
- numero di cicli tra 10 e 14, estendibile;
- adottato dal NIST nel 2001.

## Confronto sintetico

| Algoritmo | Tipo | Blocco | Chiave | Note |
|---|---|---:|---:|---|
| DES | simmetrico | 64 bit | 56 bit effettivi | oggi debole contro forza bruta |
| Triple DES | simmetrico | basato su DES | sicurezza circa 112 bit | più sicuro di DES, ma più pesante |
| AES | simmetrico | 128 bit | 128/192/256 bit | standard moderno ed efficiente |

## Collegamenti

- [[Crittografia_Simmetrica]]
- [[Forza_Bruta_e_Crittoanalisi]]
- [[Limiti_Crittografia_Simmetrica]]

## Fonti

- SRC-002

