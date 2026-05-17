# Trasmissione dati in rete

## Livelli e unità trasmesse

| Livello | Protocollo/esempio | Unità dati |
|---|---|---|
| Applicazione | HTTP, SMTP, POP | application data |
| Trasporto | TCP | segment |
| Rete | IP | packet |
| Data Link | Ethernet | frame |
| Fisico | segnali | signals |

## Incapsulamento

I dati applicativi vengono incapsulati aggiungendo header dei livelli inferiori.

```text
Dati applicativi
+ header TCP
+ header IP
+ MAC address / header livello 2
```

## Implicazione per la sicurezza

Ogni livello può esporre informazioni diverse:

- i dati applicativi possono contenere credenziali o contenuti sensibili;
- gli header TCP/IP espongono metadati;
- gli indirizzi MAC sono visibili nel dominio locale;
- il traffico può essere analizzato anche quando il contenuto è cifrato.

## Collegamenti

- [[Sniffing]]
- [[TLS_HTTPS]]
- [[IPsec_VPN]]

## Fonti

- SRC-006

