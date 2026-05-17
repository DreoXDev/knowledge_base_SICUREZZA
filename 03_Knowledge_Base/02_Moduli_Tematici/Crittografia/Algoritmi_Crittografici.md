# Algoritmi crittografici

> [!Info]
> La fiducia in un algoritmo crittografico non nasce solo dalla sua formula: dipende anche da analisi pubblica, prova del tempo, implementazione e usabilità del processo.

## Quando un algoritmo è degno di fiducia

Un algoritmo crittografico affidabile dovrebbe:

- basarsi su matematica consolidata;
- essere stato analizzato da esperti;
- aver superato la prova del tempo;
- avere complessità temporale proporzionata al livello di sicurezza richiesto;
- non imporre requisiti inutilmente complessi su chiavi e input;
- essere inserito in un processo semplice e usabile per l'utente.

> [!Important]
> La sicurezza non dipende solo dalla teoria matematica dell'algoritmo, ma anche da implementazione, usabilità e corretto processo operativo.

## Principali classi di algoritmi

Le tre principali classi sono:

1. **algoritmi simmetrici**, detti anche a chiave segreta;
2. **algoritmi asimmetrici**, detti anche a chiave pubblica;
3. **algoritmi di hashing**, detti anche message digest.

## Confronto tra classi di algoritmi

| Classe | Esempi | Uso principale | Punti forti | Limiti |
|---|---|---|---|---|
| Simmetrici | DES, AES | confidenzialità efficiente | molto veloci | problema dello scambio chiavi, non-ripudio non comprovabile a terzi |
| Asimmetrici | RSA | confidenzialità, firma digitale, gestione chiavi | chiavi pubbliche distribuibili, supporto a non-ripudio | molto più lenti |
| Hashing | MD5, SHA1, SHA2 | integrità | digest compatto del messaggio | non garantiscono confidenzialità né autenticità da soli |

## Collegamenti

- [[Crittografia_Simmetrica]]
- [[Crittografia_Asimmetrica]]
- [[Hashing_Message_Digest]]
- [[Firme_Digitali]]
- [[Cifratura_Ibrida]]
- [[DES_TripleDES_AES]]
- [[Forza_Bruta_e_Crittoanalisi]]
- [[Crittografia_Introduzione]]

## Domande d'esame correlate

> [!Question]
> Quali caratteristiche deve avere un algoritmo crittografico degno di fiducia?

> [!Question]
> Quali sono le tre principali classi di algoritmi crittografici?

## Fonti

- SRC-002
- SRC-003
