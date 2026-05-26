# Domande Note - Context AI

## Scopo

Questo file orienta NotebookLM sulle domande note integrate da SRC-009, SRC-010 e SRC-011. La fonte primaria per rispondere deve essere [[Risposte_Esame_Media_Lunghezza]], supportata dalla KB teorica.

## Domande ricorrenti

- Q-CRYPTO-001: simmetrica vs asimmetrica e numero di chiavi.
- Q-CRYPTO-002: crittografia a chiave pubblica e firme digitali.
- Q-SO-002: ACL e mediazione completa.
- Q-SO-004: Bell-LaPadula con compartimenti.
- Q-NET-001: packet filter e IP spoofing.
- Q-NET-007: IPsec transport mode.
- Q-APP-002: SQL injection.
- Q-APP-003: buffer overflow.

## Correzioni importanti

- TLS protegge dati applicativi sopra TCP; header IP e TCP restano visibili.
- IPsec tunnel mode incapsula l'intero pacchetto IP originale.
- IPsec transport mode protegge il payload IP e lascia visibile l'header IP originale.
- Un hash non e' un identificatore univoco assoluto: collisioni teoriche esistono, ma devono essere impraticabili.
- Per firme digitali dire "firma del digest con chiave privata", non genericamente "cifratura del messaggio".

## File da usare

- [[Matrice_Domande_Argomenti]]
- [[Risposte_Esame_Media_Lunghezza]]
- [[Flashcards_Domande_Note]]
- [[Simulazioni_Appelli]]
- [[Errori_o_Risposte_Dubbie]]

## Fonti

- SRC-009
- SRC-010
- SRC-011

