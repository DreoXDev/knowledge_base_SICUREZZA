# Piano Codex — Aggiornamento KB con `00.Intro.pdf`

> Repo target: Knowledge Base per **Sicurezza e Affidabilità — secondo parziale**  
> Asset analizzato: `00.Intro.pdf`  
> Tipo asset: slide introduttive / overview concettuale  
> Obiettivo: integrare i concetti introduttivi nella KB senza creare ridondanza, preparando una base leggibile in Obsidian e utile come contesto per AI, flashcard e NotebookLM.

---

## 1. Scopo dell'aggiornamento

Questo file non introduce ancora dettagli tecnici profondi, ma definisce il perimetro concettuale della seconda parte del corso:

- differenza tra **Safety Engineering** e **Security Engineering**;
- idea base di vulnerabilità come **via alternativa**;
- relazione tra requisiti di safety e conseguenze di security;
- triade **CIA**: Confidentiality, Integrity, Availability;
- modello opposto **DAD**: Disclosure, Alteration, Destruction;
- ostacoli pratici all'implementazione della sicurezza;
- introduzione all'**analisi e gestione del rischio**.

Codex deve trattare questo asset come materiale fondativo: le note create ora dovranno essere linkate dai futuri argomenti su crittografia, reti, sistemi operativi, applicazioni, password cracking, traffico di rete, OSINT, DevSecOps e Cybersecurity & AI.

---

## 2. Struttura da creare o aggiornare

Se la repo è appena inizializzata, creare questa struttura minima. Se esiste già, aggiornare senza duplicare.

```text
knowledge_base_sicurezza_affidabilita/
├── README.md
├── index.md
├── 00_Meta/
│   ├── Roadmap_Esame.md
│   ├── Fonti.md
│   ├── Glossario.md
│   └── Stato_Avanzamento.md
├── 01_Fondamenti/
│   ├── Introduzione_Sicurezza.md
│   ├── Safety_vs_Security.md
│   ├── CIA_Triad_DAD.md
│   └── Analisi_Rischio.md
├── 02_Crittografia/
├── 03_Sicurezza_Reti/
├── 04_Sicurezza_Sistemi_Operativi/
├── 05_Sicurezza_Applicazioni/
├── 06_Laboratori/
├── 07_Domande_Esame/
│   ├── Domande_Note.md
│   └── Flashcards_Esame.md
└── 99_Raw/
    └── 00.Intro.pdf
```

---

## 3. Operazioni preliminari

1. Copiare il file sorgente in:

```text
99_Raw/00.Intro.pdf
```

2. Aggiornare `00_Meta/Fonti.md` con una voce simile:

```markdown
## 00.Intro.pdf

- Tipo: slide introduttive del secondo parziale
- Stato: analizzato
- Argomenti principali:
  - programma della seconda parte del corso
  - safety vs security
  - vulnerabilità come via alternativa
  - CIA Triad
  - DAD
  - ostacoli alla sicurezza
  - analisi e gestione del rischio
- Note generate:
  - [[Introduzione_Sicurezza]]
  - [[Safety_vs_Security]]
  - [[CIA_Triad_DAD]]
  - [[Analisi_Rischio]]
```

3. Aggiornare `00_Meta/Stato_Avanzamento.md`:

```markdown
| Fonte | Stato | Note create/aggiornate | Flashcard | Da rivedere |
|---|---|---|---|---|
| 00.Intro.pdf | Analizzato | Introduzione, Safety vs Security, CIA/DAD, Analisi rischio | Sì | No |
```

---

## 4. Aggiornare `index.md`

Aggiungere una sezione iniziale per i fondamenti:

```markdown
# Knowledge Base — Sicurezza e Affidabilità, secondo parziale

## Fondamenti

- [[Introduzione_Sicurezza]]
- [[Safety_vs_Security]]
- [[CIA_Triad_DAD]]
- [[Analisi_Rischio]]

## Macro-argomenti del corso

- [[Crittografia]]
- [[Sicurezza nelle reti]]
- [[Sicurezza nei sistemi operativi]]
- [[Sicurezza nelle applicazioni]]

## Studio per l'esame

- [[Domande_Note]]
- [[Flashcards_Esame]]
- [[Glossario]]
```

---

## 5. Creare o aggiornare `00_Meta/Roadmap_Esame.md`

Inserire una roadmap basata sull'agenda della seconda parte del corso.

Contenuto consigliato:

```markdown
# Roadmap Esame — Secondo Parziale

> [!Info]
> Il secondo parziale è completamente teorico: l'obiettivo della KB è trasformare slide, appunti e domande note in materiale studiabile direttamente da Obsidian e utilizzabile come contesto per AI/NotebookLM.

## Programma principale

1. Crittografia
2. Sicurezza nelle reti
3. Sicurezza nei sistemi operativi
4. Sicurezza nelle applicazioni

## Laboratori rilevanti

- Selenium
- Crittografia e firme digitali
- Password cracking
- Analisi del traffico di rete

## Interventi esterni

- OSINT
- DevSecOps
- Cybersecurity & AI

## Strategia di studio

- Leggere prima le note sintetiche della KB.
- Ripassare con flashcard.
- Usare le domande note come simulazione orale/scritta.
- Usare NotebookLM o altri strumenti AI solo dopo aver consolidato la struttura della KB.
```

---

## 6. Creare `01_Fondamenti/Introduzione_Sicurezza.md`

Questa nota deve spiegare il ruolo introduttivo del file.

Contenuto consigliato:

```markdown
# Introduzione alla seconda parte del corso

> [!Info]
> Questa sezione introduce la parte di corso dedicata alla sicurezza informatica. Il focus non è sugli esercizi, ma sulla comprensione teorica dei concetti e sulla capacità di collegarli tra loro.

## Programma

La seconda parte del corso copre quattro aree principali:

- crittografia;
- sicurezza nelle reti;
- sicurezza nei sistemi operativi;
- sicurezza nelle applicazioni.

## Laboratori

I laboratori collegati agli argomenti teorici includono:

- Selenium;
- crittografia e firme digitali;
- password cracking;
- analisi del traffico di rete.

## Interventi esterni

Gli interventi esterni previsti riguardano:

- OSINT;
- DevSecOps;
- Cybersecurity & AI.

## Idea chiave

La sicurezza deve essere vista come un insieme di tecniche, principi e processi per prevenire, difendere e recuperare da attacchi che possono compromettere i valori rappresentati da un sistema informatico.

## Collegamenti

- [[Safety_vs_Security]]
- [[CIA_Triad_DAD]]
- [[Analisi_Rischio]]
```

---

## 7. Creare `01_Fondamenti/Safety_vs_Security.md`

Questa nota deve essere breve ma molto chiara, perché la distinzione è fondativa.

Contenuto consigliato:

```markdown
# Safety vs Security

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

## Collegamenti

- [[Introduzione_Sicurezza]]
- [[Analisi_Rischio]]
```

---

## 8. Creare `01_Fondamenti/CIA_Triad_DAD.md`

Questa nota deve diventare uno dei riferimenti principali della KB.

Contenuto consigliato:

```markdown
# CIA Triad e modello DAD

## CIA Triad

La sicurezza informatica viene spesso descritta attraverso tre obiettivi fondamentali:

1. **Confidenzialità** (*Confidentiality*)
2. **Integrità** (*Integrity*)
3. **Disponibilità** (*Availability*)

---

## Confidenzialità

La **confidenzialità** è la capacità di controllare e assicurare la riservatezza delle informazioni archiviate o trasmesse rispetto a soggetti non autorizzati.

Possibili compromissioni:

- accesso a dati che non dovrebbero essere noti;
- visibilità dell'esistenza di oggetti che dovrebbero rimanere nascosti;
- analisi del traffico di rete.

---

## Integrità

L'**integrità** è la capacità di controllare e assicurare che le informazioni memorizzate o trasmesse non vengano modificate, cancellate, create o manomesse da soggetti non autorizzati.

Possibili compromissioni:

- modifica non autorizzata di un oggetto;
- cancellazione non autorizzata;
- creazione non autorizzata;
- manomissione di informazioni sensibili;
- manomissione di software o hardware.

### Firma digitale, autenticità e non-ripudio

Nel contesto della comunicazione, l'integrità è collegata anche a:

- **autenticità del mittente**: garanzia dell'identità del mittente;
- **non-ripudio**: garanzia che il mittente non possa negare la paternità delle informazioni trasmesse o archiviate.

---

## Disponibilità

La **disponibilità** è la capacità di assicurare l'uso di risorse e servizi agli utenti autorizzati quando ne hanno bisogno.

Possibili compromissioni:

- causare un crash di sistema;
- manomettere gli algoritmi di scheduling;
- saturare la banda di rete per impedire o rallentare l'accesso a un servizio;
- compromettere un file di password per impedire l'accesso a utenti autorizzati;
- distruggere fisicamente un computer.

---

## DAD

Gli attacchi alla CIA Triad possono essere descritti tramite il modello **DAD**:

| Attacco | Requisito compromesso |
|---|---|
| Disclosure | Confidentiality |
| Alteration | Integrity |
| Destruction | Availability |

> [!Summary]
> La CIA Triad descrive ciò che bisogna proteggere.  
> Il modello DAD descrive le principali famiglie di attacchi contro questi obiettivi.

## Collegamenti

- [[Introduzione_Sicurezza]]
- [[Analisi_Rischio]]
- [[Glossario]]
```

---

## 9. Creare `01_Fondamenti/Analisi_Rischio.md`

Contenuto consigliato:

```markdown
# Analisi e gestione del rischio

## Perché serve l'analisi del rischio

L'implementazione della sicurezza incontra diversi ostacoli:

- conflitto tra usabilità e sicurezza;
- progettazione tardiva della sicurezza;
- necessità di compromesso tra benefici e costi.

> [!Important]
> Una corretta analisi dei rischi è fondamentale perché permette di decidere dove investire risorse di sicurezza in modo proporzionato.

---

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

---

## Valori sensibili

I valori sensibili rispondono alla domanda:

> Quali parti del sistema informativo sono importanti, sensibili o critiche?

Sono gli elementi da proteggere, considerando anche la loro importanza relativa.

---

## Vulnerabilità

Le vulnerabilità rispondono alla domanda:

> In cosa siamo vulnerabili?

Sono debolezze o possibilità di attacco che possono compromettere confidenzialità, integrità o disponibilità.

Una vulnerabilità può essere vista come una **via alternativa** non prevista dal progettista.

---

## Minacce

Le minacce rispondono alla domanda:

> Quali sono i pericoli a cui siamo esposti?

Sono circostanze, eventi o agenti che possono causare danni.

---

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
| rischio trasferibile o mitigabile con piani esterni | assicurazione, piano di backup, eliminazione di single/multiple point of failure |

## Collegamenti

- [[CIA_Triad_DAD]]
- [[Safety_vs_Security]]
- [[Glossario]]
```

---

## 10. Aggiornare `00_Meta/Glossario.md`

Aggiungere o aggiornare queste voci:

```markdown
# Glossario

## Safety engineering

Prevenzione di danni catastrofici causati dal cattivo funzionamento di un sistema informatico.

## Security engineering

Prevenzione, difesa e recupero rispetto ad attacchi che possono compromettere i valori rappresentati da un sistema informatico.

## Vulnerabilità

Debolezza o via alternativa che può essere sfruttata per compromettere confidenzialità, integrità o disponibilità.

## Minaccia

Circostanza, evento o agente che può arrecare danno a un sistema.

## Valore sensibile

Elemento importante, critico o sensibile di un sistema informativo che deve essere protetto.

## Confidenzialità

Capacità di assicurare che le informazioni siano accessibili solo a soggetti autorizzati.

## Integrità

Capacità di assicurare che le informazioni non siano modificate, cancellate, create o manomesse da soggetti non autorizzati.

## Disponibilità

Capacità di assicurare l'accesso a risorse e servizi agli utenti autorizzati quando necessario.

## Autenticità

Capacità di garantire l'identità del mittente di informazioni trasmesse o archiviate.

## Non-ripudio

Capacità di assicurare che il mittente non possa negare la paternità delle informazioni trasmesse o archiviate.

## CIA Triad

Modello che descrive i tre obiettivi fondamentali della sicurezza: confidenzialità, integrità e disponibilità.

## DAD

Modello che descrive tre famiglie di attacchi alla CIA Triad: Disclosure, Alteration e Destruction.

## DoS

Denial of Service: attacco che mira a impedire o rallentare l'accesso legittimo a un servizio.
```

---

## 11. Aggiornare `07_Domande_Esame/Flashcards_Esame.md`

Aggiungere una sezione specifica per l'introduzione.

Usare un formato stabile e facile da importare/convertire in futuro.

```markdown
# Flashcards Esame

## Fondamenti — Introduzione

### Flashcard 1

**Domanda:** Qual è la differenza tra safety engineering e security engineering?

**Risposta:**  
La safety engineering mira a prevenire danni catastrofici causati dal cattivo funzionamento di un sistema, soprattutto in sistemi life-critical. La security engineering mira invece a prevenire, difendere e recuperare da attacchi intenzionali che possono compromettere i valori di un sistema informatico.

---

### Flashcard 2

**Domanda:** Perché una misura di safety può creare problemi di security?

**Risposta:**  
Una misura di safety può introdurre nuove modalità di abuso. Ad esempio, un meccanismo che apre le porte di un'auto capovolta tramite sensore sul tetto può essere sfruttato da un attaccante saltando sul tetto per ottenere accesso non autorizzato.

---

### Flashcard 3

**Domanda:** Che cosa si intende per vulnerabilità come “via alternativa”?

**Risposta:**  
Una vulnerabilità può essere vista come un modo non previsto o non desiderato per accedere a una risorsa, modificare un comportamento o aggirare i controlli. Nei sistemi complessi queste vie alternative possono essere molte.

---

### Flashcard 4

**Domanda:** Quali sono i tre obiettivi della CIA Triad?

**Risposta:**  
I tre obiettivi sono confidenzialità, integrità e disponibilità. La confidenzialità limita l'accesso alle informazioni ai soli autorizzati, l'integrità protegge da modifiche o manomissioni non autorizzate, la disponibilità assicura che utenti autorizzati possano accedere a risorse e servizi quando necessario.

---

### Flashcard 5

**Domanda:** Che cosa rappresenta il modello DAD?

**Risposta:**  
Il modello DAD rappresenta tre famiglie di attacchi alla CIA Triad: Disclosure contro la confidenzialità, Alteration contro l'integrità e Destruction contro la disponibilità.

---

### Flashcard 6

**Domanda:** Quali sono alcuni esempi di compromissione della confidenzialità?

**Risposta:**  
Esempi sono l'accesso non autorizzato a dati riservati, la visibilità dell'esistenza di oggetti che dovrebbero rimanere nascosti e l'analisi del traffico di rete.

---

### Flashcard 7

**Domanda:** Quali sono alcuni esempi di compromissione dell'integrità?

**Risposta:**  
Esempi sono modifica, cancellazione o creazione non autorizzata di oggetti, manomissione di informazioni sensibili e manomissione di software o hardware.

---

### Flashcard 8

**Domanda:** Quali sono alcuni esempi di compromissione della disponibilità?

**Risposta:**  
Esempi sono crash di sistema, saturazione della banda tramite DoS, manomissione dello scheduling, compromissione di file di password e distruzione fisica di un computer.

---

### Flashcard 9

**Domanda:** Quali sono i principali ostacoli all'implementazione della sicurezza?

**Risposta:**  
I principali ostacoli sono il conflitto tra usabilità e sicurezza, il fatto che spesso la sicurezza venga progettata troppo tardi e la necessità di bilanciare benefici e costi.

---

### Flashcard 10

**Domanda:** Come si può modellare il rischio in sicurezza informatica?

**Risposta:**  
Il rischio può essere modellato come prodotto tra vulnerabilità, minacce e valori sensibili: maggiore è la debolezza del sistema, maggiore è l'esposizione alle minacce e maggiore è il valore degli asset coinvolti, più alto sarà il rischio.

---
```

---

## 12. Aggiornare `07_Domande_Esame/Domande_Note.md`

Aggiungere una sezione di possibili domande teoriche derivate dall'introduzione.

```markdown
# Domande note e possibili domande d'esame

## Fondamenti — Introduzione

1. Spiega la differenza tra safety engineering e security engineering.
2. Perché security is not safety?
3. Che cosa significa descrivere una vulnerabilità come una via alternativa?
4. Spiega l'esempio del meccanismo di apertura delle porte dell'automobile e il conflitto tra safety e security.
5. Definisci la CIA Triad.
6. Spiega la confidenzialità e fai esempi di compromissione.
7. Spiega l'integrità e fai esempi di compromissione.
8. Qual è il ruolo della firma digitale rispetto a integrità, autenticità e non-ripudio?
9. Spiega la disponibilità e fai esempi di compromissione.
10. Che cosa rappresenta il modello DAD?
11. Quali sono gli ostacoli principali all'implementazione della sicurezza?
12. Che cos'è l'analisi del rischio?
13. Spiega la formula: Rischio = Vulnerabilità × Minacce × Valori.
14. Quali strategie si possono adottare nella gestione del rischio?
```

---

## 13. Controlli di qualità richiesti a Codex

Dopo aver aggiornato la repo, Codex deve controllare:

1. Nessun file duplicato nei fondamenti.
2. Tutte le note devono avere link Obsidian coerenti.
3. Il glossario deve contenere solo voci atomiche e riutilizzabili.
4. Le flashcard devono essere autosufficienti.
5. Le domande d'esame devono essere collegate ai contenuti della KB.
6. Le note non devono copiare passivamente le slide, ma riorganizzarle in forma studiabile.
7. Lo stile deve rimanere coerente con Obsidian:
   - titoli chiari;
   - sezioni brevi;
   - box `[!Info]`, `[!Important]`, `[!Warning]`, `[!Summary]`;
   - tabelle solo quando aiutano davvero.
8. Non inserire emoji.
9. Usare accenti corretti in italiano.
10. Mantenere i termini tecnici inglesi quando sono rilevanti per l'esame, ma sempre con spiegazione italiana.

---

## 14. Commit consigliato

Dopo l'aggiornamento, usare un commit simile:

```bash
git add .
git commit -m "Add introductory security fundamentals from 00.Intro"
```

---

## 15. Stato atteso dopo l'applicazione

Alla fine di questo piano la repo deve avere:

- una roadmap del secondo parziale;
- una prima sezione fondativa studiabile;
- un glossario iniziale;
- flashcard introduttive;
- possibili domande d'esame;
- tracciamento della fonte `00.Intro.pdf`;
- struttura pronta per integrare i prossimi asset uno alla volta.
