# CIA Triad e modello DAD

> [!Info]
> La CIA Triad descrive i tre obiettivi fondamentali della sicurezza informatica: confidenzialità, integrità e disponibilità. Il modello DAD descrive tre famiglie di attacchi che compromettono tali obiettivi.

## CIA Triad

La sicurezza informatica viene spesso descritta attraverso tre obiettivi fondamentali:

1. **Confidenzialità** (*Confidentiality*)
2. **Integrità** (*Integrity*)
3. **Disponibilità** (*Availability*)

## Confidenzialità

La **confidenzialità** è la capacità di controllare e assicurare la riservatezza delle informazioni archiviate o trasmesse rispetto a soggetti non autorizzati.

Possibili compromissioni:

- accesso a dati che non dovrebbero essere noti;
- visibilità dell'esistenza di oggetti che dovrebbero rimanere nascosti;
- analisi del traffico di rete.

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

## Disponibilità

La **disponibilità** è la capacità di assicurare l'uso di risorse e servizi agli utenti autorizzati quando ne hanno bisogno.

Possibili compromissioni:

- causare un crash di sistema;
- manomettere gli algoritmi di scheduling;
- saturare la banda di rete per impedire o rallentare l'accesso a un servizio;
- compromettere un file di password per impedire l'accesso a utenti autorizzati;
- distruggere fisicamente un computer.

## DAD

Gli attacchi alla CIA Triad possono essere descritti tramite il modello **DAD**:

| Attacco | Requisito compromesso |
|---|---|
| Disclosure | Confidentiality |
| Alteration | Integrity |
| Destruction | Availability |

> [!Summary]
> La CIA Triad descrive ciò che bisogna proteggere. Il modello DAD descrive le principali famiglie di attacchi contro questi obiettivi.

## Collegamenti

- [[Introduzione_Sicurezza]]
- [[Analisi_Rischio]]
- [[Glossario]]

## Domande d'esame correlate

> [!Question]
> Definisci la CIA Triad e spiega il modello DAD.

> [!Question]
> Fai esempi di compromissione di confidenzialità, integrità e disponibilità.

## Fonti

- SRC-001

