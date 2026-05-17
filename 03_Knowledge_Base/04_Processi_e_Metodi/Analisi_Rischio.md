# Analisi e gestione del rischio

> [!Info]
> L'analisi del rischio serve a capire quali valori proteggere, da quali minacce difendersi e quali vulnerabilità ridurre. È il collegamento tra teoria della sicurezza e decisioni operative.

## Perché serve l'analisi del rischio

L'implementazione della sicurezza incontra diversi ostacoli:

- conflitto tra usabilità e sicurezza;
- progettazione tardiva della sicurezza;
- necessità di compromesso tra benefici e costi.

> [!Important]
> Una corretta analisi dei rischi è fondamentale perché permette di decidere dove investire risorse di sicurezza in modo proporzionato.

## Definizione di rischio

Il rischio può essere inteso come possibilità di perdita o danno.

In ambito sicurezza informatica:

$$
Rischio = Vulnerabilità \times Minacce \times Valori
$$

Dove:

- **valori sensibili**: elementi importanti, critici o sensibili da proteggere;
- **vulnerabilità**: debolezze che possono essere sfruttate;
- **minacce**: circostanze o agenti che possono arrecare danno.

## Valori sensibili

I valori sensibili rispondono alla domanda:

> Quali parti del sistema informativo sono importanti, sensibili o critiche?

Sono gli elementi da proteggere, considerando anche la loro importanza relativa.

## Vulnerabilità

Le vulnerabilità rispondono alla domanda:

> In cosa siamo vulnerabili?

Sono debolezze o possibilità di attacco che possono compromettere confidenzialità, integrità o disponibilità.

Una vulnerabilità può essere vista come una **via alternativa** non prevista dal progettista.

## Minacce

Le minacce rispondono alla domanda:

> Quali sono i pericoli a cui siamo esposti?

Sono circostanze, eventi o agenti che possono causare danni.

## Gestione dei rischi

La gestione del rischio dipende da due dimensioni principali:

- probabilità, legata a vulnerabilità e minacce;
- impatto, legato ai valori sensibili coinvolti.

In base alla combinazione tra probabilità e impatto si possono adottare strategie diverse:

| Probabilità / Impatto | Strategia |
|---|---|
| rischio basso | rischio ignorabile |
| rischio medio | controllo e contenimento |
| rischio alto | prevenzione e protezione |
| rischio trasferibile o mitigabile con piani esterni | assicurazione, piano di backup, eliminazione di single point of failure o multiple point of failure |

## Quando è rilevante all'esame

L'analisi del rischio è un tema trasversale: aiuta a motivare perché alcune misure di sicurezza sono necessarie, perché altre sono eccessive e perché ogni decisione tecnica deve essere valutata in relazione a probabilità, impatto e valore degli asset coinvolti.

## Collegamenti

- [[CIA_Triad_DAD]]
- [[Safety_vs_Security]]
- [[Glossario]]

## Fonti

- SRC-001

