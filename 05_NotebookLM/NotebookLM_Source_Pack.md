# NotebookLM Source Pack

Questo file raccogliera' progressivamente una versione compatta dei contenuti piu' importanti della knowledge base.

> [!Warning]
> Non aggiungere contenuti non supportati dalle fonti. Ogni sezione deve indicare da quali note o source ID deriva.

## Stato

Il source pack contiene il primo nucleo fondativo derivato da `SRC-001 - 00.Intro.pdf`.

## Contenuti principali

- La seconda parte del corso riguarda sicurezza informatica, con focus su crittografia, sicurezza nelle reti, sicurezza nei sistemi operativi e sicurezza nelle applicazioni.
- La distinzione tra safety engineering e security engineering è fondativa: la safety previene danni catastrofici dovuti a malfunzionamenti, mentre la security previene, difende e recupera da attacchi intenzionali.
- Una vulnerabilità può essere vista come una via alternativa non prevista dal progettista.
- La CIA Triad descrive gli obiettivi principali della sicurezza: confidenzialità, integrità e disponibilità.
- Il modello DAD descrive attacchi che compromettono la CIA Triad: Disclosure, Alteration e Destruction.
- L'analisi del rischio collega vulnerabilità, minacce e valori sensibili per decidere dove investire risorse di sicurezza.
- La crittografia protegge messaggi e dati tramite schemi di cifratura, ma non risolve da sola tutti i problemi di sicurezza: implementazione, gestione delle chiavi e contesto operativo restano decisivi.
- Gli schemi di cifratura trasformano plaintext in ciphertext tramite una chiave e devono permettere la decifratura corretta del messaggio da parte del destinatario autorizzato.
- La crittografia simmetrica usa la stessa chiave per cifrare e decifrare. È efficiente e molto utile per la confidenzialità, ma ha limiti su scambio delle chiavi, non-ripudio e attribuzione verso terze parti.
- DES è uno standard storico oggi debole per la dimensione della chiave; Triple DES aumenta la sicurezza ripetendo DES; AES è lo standard simmetrico moderno con blocchi da 128 bit e chiavi da 128, 192 o 256 bit.

## Definizioni importanti

- Safety engineering: prevenzione di danni catastrofici causati dal cattivo funzionamento di un sistema informatico.
- Security engineering: prevenzione, difesa e recupero rispetto ad attacchi che possono compromettere i valori rappresentati da un sistema informatico.
- Confidenzialità: protezione dell'accesso alle informazioni da parte di soggetti non autorizzati.
- Integrità: protezione da modifiche, cancellazioni, creazioni o manomissioni non autorizzate.
- Disponibilità: garanzia che utenti autorizzati possano usare risorse e servizi quando necessario.
- Rischio: possibilità di perdita o danno, modellabile come combinazione di vulnerabilità, minacce e valori.
- Plaintext: messaggio in chiaro prima della cifratura.
- Ciphertext: messaggio cifrato prodotto da un algoritmo crittografico.
- Forza bruta: attacco che prova tutte le chiavi o configurazioni possibili.
- Crittoanalisi: studio degli attacchi contro sistemi crittografici.
- Algoritmo simmetrico: algoritmo che usa la stessa chiave per cifrare e decifrare.

## Confronti importanti

- Safety vs security: la safety si concentra su danni accidentali o malfunzionamenti, la security su attacchi intenzionali e abusi.
- CIA vs DAD: la CIA Triad descrive cosa proteggere; DAD descrive famiglie di attacco contro quegli obiettivi.
- Crittografia simmetrica vs firma digitale: la simmetrica consente confidenzialità efficiente, ma non prova a terzi quale partecipante abbia generato un messaggio.
- DES vs AES: DES usa chiavi effettive da 56 bit ed è vulnerabile a forza bruta moderna; AES usa blocchi da 128 bit e chiavi più lunghe, ed è lo standard moderno.

## Domande utili per il ripasso

- Spiega la differenza tra safety engineering e security engineering.
- Definisci CIA Triad e modello DAD.
- Che cosa significa considerare una vulnerabilità come via alternativa?
- Perché l'analisi del rischio è necessaria nell'implementazione della sicurezza?
- Perché la crittografia non è una soluzione universale?
- Quali sono le componenti di uno schema di cifratura?
- Perché la crittografia simmetrica non garantisce non-ripudio verso terze parti?
- Confronta DES, Triple DES e AES.
