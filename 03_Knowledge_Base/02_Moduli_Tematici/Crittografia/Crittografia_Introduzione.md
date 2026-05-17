# Introduzione alla crittografia

> [!Info]
> La crittografia è uno strumento fondamentale della sicurezza informatica, ma funziona solo se è implementata correttamente, usata nel contesto giusto e accompagnata da una gestione sicura delle chiavi.

## Definizione

La **crittografia** è la disciplina che studia tecniche per proteggere messaggi e dati, con lo scopo di garantire proprietà di sicurezza nella comunicazione tra due o più soggetti.

Le proprietà principali coinvolte sono:

- riservatezza o confidenzialità;
- integrità;
- autenticità.

Il termine deriva dal greco *kryptos*, cioè "nascosto".

## Ruolo nella sicurezza

La crittografia non è una soluzione universale a tutti i problemi di sicurezza.

È però uno strumento molto importante quando:

- viene implementata correttamente;
- viene usata in modo appropriato;
- è inserita in un processo di sicurezza coerente.

> [!Warning]
> Un algoritmo crittografico forte può diventare inutile se usato male, se le chiavi sono gestite male o se il sistema circostante è vulnerabile.

## Collegamento con la CIA Triad

La crittografia può contribuire a:

- **confidenzialità**, proteggendo il contenuto dei messaggi;
- **integrità**, tramite codici o meccanismi di verifica;
- **autenticità**, tramite meccanismi che permettono di identificare il mittente.

Questa prima parte riguarda soprattutto la [[Crittografia_Simmetrica]], che supporta bene la confidenzialità ma non risolve da sola non-ripudio e prova verso terze parti.

La disponibilità, invece, non è risolta direttamente dalla crittografia introdotta in questa sezione: un sistema cifrato può comunque subire attacchi alla disponibilità, come saturazione di risorse o negazione del servizio.

## Collegamenti

- [[CIA_Triad_DAD]]
- [[Schemi_di_Cifratura]]
- [[Algoritmi_Crittografici]]
- [[Analisi_Rischio]]

## Domande d'esame correlate

> [!Question]
> Che cos'è la crittografia e perché non risolve da sola tutti i problemi di sicurezza?

## Fonti

- SRC-002

