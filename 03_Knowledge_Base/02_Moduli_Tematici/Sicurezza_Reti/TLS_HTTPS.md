# TLS e HTTPS

> [!Info]
> TLS protegge privacy e integrità dei dati applicativi sopra TCP/IP. HTTPS è HTTP su TLS.

## TLS

**TLS**, Transport Layer Security, è il successore di SSL.

Fornisce privacy e integrità dei dati applicativi sopra TCP/IP.

Esempi di protocolli applicativi che possono usare TLS:

- HTTP;
- SMTP;
- POP;
- altri protocolli applicativi.

## Posizione nello stack

TLS si colloca tra applicazione e TCP.

```text
HTTP / SMTP / POP
TLS
TCP
IP
```

## Incapsulamento TLS

TLS incapsula i dati applicativi in formato cifrato. Gli header TCP/IP restano esterni e osservabili.

## Sottoprotocolli principali

| Sottoprotocollo | Scopo |
|---|---|
| Handshake Protocol | stabilire una connessione autenticata e concordare parametri crittografici |
| Application Data Protocol | trasportare dati applicativi protetti |

## TLS handshake

Il TLS handshake serve a negoziare cipher suite, autenticare il server tramite certificato, scambiare o derivare chiavi e preparare la cifratura simmetrica dei dati.

> [!Important]
> TLS usa una logica ibrida: meccanismi asimmetrici e certificati per stabilire fiducia e chiavi, poi crittografia simmetrica per proteggere i dati applicativi.

## HTTPS

**HTTPS** è HTTP su SSL/TLS.

| Protocollo | Porta |
|---|---:|
| HTTP | 80 |
| HTTPS | 443 |

## Limiti

TLS protegge i dati applicativi, ma lascia visibili metadati di rete e trasporto. Restano quindi possibili alcune forme di spoofing e traffic analysis.

## Collegamenti

- [[Certificati_X509_PKI]]
- [[Cifratura_Ibrida]]
- [[Confronto_TLS_IPsec]]

## Fonti

- SRC-006

