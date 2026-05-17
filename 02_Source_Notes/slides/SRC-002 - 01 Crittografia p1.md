# Source Note - 01.Crittografia-p1.pdf

## Metadata

| Campo | Valore |
|---|---|
| Source ID | SRC-002 |
| Tipo fonte | slide teoriche - crittografia, parte 1 |
| Stato | integrato nella KB |
| Collegamento raw asset | `../../01_Raw_Assets/slides/01.Crittografia-p1.pdf` |

## Riassunto della fonte

`01.Crittografia-p1.pdf` introduce il blocco di crittografia del secondo parziale. La fonte definisce la crittografia, presenta il modello generale di cifratura, mostra il cifrario di Cesare come esempio semplice, introduce forza bruta e crittoanalisi, classifica gli algoritmi crittografici e approfondisce la crittografia simmetrica tramite DES, Triple DES e AES.

## Concetti principali estratti

- Crittografia come disciplina per proteggere messaggi e dati.
- Schema generale con plaintext, ciphertext, chiavi, `encrypt` e `decrypt`.
- Cifrario di Cesare e limite dello spazio delle chiavi.
- Attacchi di forza bruta e fattori di fattibilità.
- Crittoanalisi e possibili obiettivi.
- Requisiti di affidabilità di un algoritmo crittografico.
- Classi principali: algoritmi simmetrici, asimmetrici e hashing.
- Crittografia simmetrica e chiave segreta condivisa.
- DES, Triple DES e AES.
- Limiti della crittografia simmetrica: scambio chiavi, numero di chiavi, non-ripudio.

## Dettagli teorici rilevanti

La crittografia è fondamentale per la sicurezza, ma non è autosufficiente. Un algoritmo robusto può fallire se implementato male, usato nel contesto sbagliato o associato a una gestione debole delle chiavi.

La crittografia simmetrica è efficiente e adatta alla confidenzialità, ma non risolve completamente autenticità, integrità e non-ripudio verso terze parti.

DES mostra come la sicurezza pratica cambi nel tempo: una chiave ritenuta sufficiente può diventare vulnerabile con l'aumento della potenza computazionale e con la parallelizzazione degli attacchi.

## Domande potenziali d'esame

> [!Question]
> Che cos'è la crittografia e quali requisiti di sicurezza può supportare?

> [!Question]
> Descrivi il modello generale di uno schema di cifratura.

> [!Question]
> Che cos'è un attacco di forza bruta e da quali fattori dipende la sua fattibilità?

> [!Question]
> Spiega vantaggi e limiti della crittografia simmetrica.

> [!Question]
> Confronta DES, Triple DES e AES.

## Collegamenti suggeriti alla KB

- [[Crittografia_Introduzione]]
- [[Schemi_di_Cifratura]]
- [[Forza_Bruta_e_Crittoanalisi]]
- [[Algoritmi_Crittografici]]
- [[Crittografia_Simmetrica]]
- [[DES_TripleDES_AES]]
- [[Limiti_Crittografia_Simmetrica]]
- [[CIA_Triad_DAD]]
- [[Analisi_Rischio]]

## Ambiguità o punti da verificare

- Gli algoritmi asimmetrici, hashing, firma digitale e gestione avanzata delle chiavi devono essere integrati dagli asset successivi.

