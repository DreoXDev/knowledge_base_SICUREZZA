# Sistemi operativi trusted: principi di progettazione

> [!Info]
> Un sistema operativo trusted deve applicare politiche di sicurezza in modo affidabile, ma anche restare gestibile e usabile. Meccanismi troppo complessi tendono a essere aggirati o configurati male.

## Principi principali

Un sistema operativo trusted dovrebbe applicare diversi principi di progettazione.

### Minimi privilegi

Ogni soggetto deve avere solo i privilegi necessari per svolgere il proprio compito.

### Mediazione completa

Ogni accesso a ogni oggetto protetto deve essere controllato.

### Autorizzazione negata per default

Se una richiesta non è esplicitamente autorizzata, deve essere negata.

### Multiple point of failure

La sicurezza non deve dipendere da un unico punto di protezione.

### Separazione fra utenti e minima condivisione

Gli utenti devono essere separati quanto possibile e la condivisione deve essere ridotta al minimo necessario.

### Protezione rispetto al riutilizzo delle risorse

Quando una risorsa viene riutilizzata, il sistema deve evitare che dati residui siano visibili al nuovo utilizzatore.

### Accounting and audit

Il sistema deve registrare e rendere analizzabili le azioni rilevanti per la sicurezza.

## Requisiti di usabilità e semplicità

La sicurezza deve essere considerata insieme all'usabilità.

Principi collegati:

### Economia del meccanismo

I meccanismi devono essere semplici, comprensibili e gestibili.

### Struttura aperta

La sicurezza deve basarsi sulla segretezza di pochi elementi critici, non sulla segretezza dell'intero progetto.

### Facilità d'uso

Un sistema difficile da usare tende a essere aggirato o configurato male dagli utenti.

> [!Summary]
> Un sistema operativo trusted deve combinare principi rigorosi di sicurezza con meccanismi semplici, gestibili e usabili.

## Collegamenti

- [[Obiettivi_Controllo_Accessi]]
- [[Auditing_Intrusion_Detection]]
- [[Password_Hashing_Salt]]
- [[Analisi_Rischio]]

## Fonti

- SRC-005

