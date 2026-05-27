# Errori o Risposte Dubbie

| Asset | Domanda | Problema | Correzione proposta |
|---|---|---|---|
| SRC-009 | TLS/SSL | La risposta puo' mescolare SSL e TLS senza distinguere bene lo stack. | Usare TLS come protocollo moderno: IP header e TCP header visibili, record TLS sopra TCP, dati applicativi protetti. |
| SRC-009 | IPsec tunnel | Formulazioni come "IPsec sotto IP" possono essere ambigue. | Spiegare incapsulamento: nuovo header IP esterno + ESP + pacchetto IP originale protetto. |
| SRC-010 | IPsec transport | La domanda richiede transport mode, non tunnel mode. | Usare risposta dedicata: header IP originale visibile, payload IP protetto. |
| SRC-009 | Hash | "Univocamente rappresentativo" e' troppo forte. | Dire che collisioni esistono teoricamente, ma devono essere computazionalmente impraticabili. |
| SRC-009 | Firme digitali | "Criptare con privata" puo' essere formulato in modo impreciso. | Parlare di firma del digest con chiave privata e verifica con chiave pubblica. |
| SRC-009 | XSS/SQL injection | Alcune risposte sono troppo operative o sintetiche. | Collegare a improper neutralization, contesto di interpretazione e contromisure principali. |

## Stato

Le correzioni sono gia' applicate in [[Risposte_Esame_Media_Lunghezza]].

