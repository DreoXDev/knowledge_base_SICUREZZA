# Source Note - 01.Crittografia-p2.pdf

## Metadata

| Campo | Valore |
|---|---|
| Source ID | SRC-003 |
| Tipo fonte | slide teoriche - crittografia, parte 2 |
| Stato | integrato nella KB |
| Collegamento raw asset | `../../01_Raw_Assets/slides/01.Crittografia-p2.pdf` |

## Riassunto della fonte

`01.Crittografia-p2.pdf` completa il blocco introduttivo di crittografia. La fonte estende la parte simmetrica con crittografia asimmetrica, RSA, hashing, message digest, firme digitali, cifratura ibrida, certificati X.509, catene di certificati, PKI e limiti della crittografia quando il threat model è incompleto.

## Concetti principali estratti

- Crittografia asimmetrica a chiave pubblica e privata.
- Scalabilità del numero di chiavi rispetto alla crittografia simmetrica.
- Supporto ad autenticità, integrità e non-ripudio.
- RSA e problema della fattorizzazione.
- Message digest e hashing crittografico.
- MD5, SHA1 e SHA2 come algoritmi di digest.
- Firme digitali efficienti tramite firma del digest.
- Cifratura ibrida RSA + AES/DES.
- Distribuzione delle chiavi pubbliche.
- Certificati X.509, catene di certificati e PKI.
- Limiti pratici della crittografia rispetto al threat model.

## Dettagli teorici rilevanti

La crittografia asimmetrica risolve alcuni limiti della crittografia simmetrica: riduce il problema del numero di chiavi e consente firme digitali verificabili anche da terze parti. Introduce però costi computazionali più elevati e richiede fiducia nell'associazione tra identità e chiave pubblica.

RSA è basato sulla difficoltà di fattorizzare numeri molto grandi. Per ragioni di efficienza, nella pratica RSA viene combinato con algoritmi simmetrici e funzioni di hashing.

I certificati X.509 e la PKI affrontano il problema della distribuzione affidabile delle chiavi pubbliche. La crittografia, tuttavia, non sostituisce un threat model completo: bug, utenti, protocolli, dispositivi e social engineering possono rimanere vulnerabili.

## Domande potenziali d'esame

> [!Question]
> Come funziona la crittografia asimmetrica e in che cosa differisce da quella simmetrica?

> [!Question]
> Spiega RSA e il problema computazionale su cui si basa.

> [!Question]
> Perché si firma il message digest invece dell'intero messaggio?

> [!Question]
> Che problema risolvono certificati X.509 e PKI?

> [!Question]
> Perché la crittografia non è sufficiente se il threat model è incompleto?

## Collegamenti suggeriti alla KB

- [[Crittografia_Asimmetrica]]
- [[RSA]]
- [[Hashing_Message_Digest]]
- [[Firme_Digitali]]
- [[Cifratura_Ibrida]]
- [[Certificati_X509_PKI]]
- [[Limiti_Crittografia_e_Threat_Model]]
- [[Crittografia_Simmetrica]]
- [[Limiti_Crittografia_Simmetrica]]

## Ambiguità o punti da verificare

- Le slide citano MD5 e SHA1 come contenuto storico del corso; per usi moderni vanno trattati con cautela e non presentati come scelte sicure.

