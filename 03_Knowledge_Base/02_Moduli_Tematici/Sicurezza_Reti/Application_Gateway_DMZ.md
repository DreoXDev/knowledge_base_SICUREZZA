# Application gateway, screened subnet e DMZ

## Application gateway

Un **application gateway** è un proxy che controlla traffico a livello applicativo.

Caratteristiche:

- monitora traffico specifico per una certa applicazione;
- riceve il traffico destinato all'applicazione;
- inoltra dati tra client e applicazione;
- può esistere un gateway diverso per ogni applicazione.

Esempi:

- firewall FTP configurato per accettare download ma non upload;
- filtro email anti-spam.

## Vantaggio

Rispetto al packet filtering, l'application gateway può controllare il significato dei dati applicativi, anche su più pacchetti.

## Screened subnet

In una soluzione mista:

1. il firewall accetta connessioni su porte note per servizi esposti;
2. esegue destination NAT verso l'application gateway;
3. l'application gateway controlla il traffico come proxy del servizio reale.

## DMZ

La **DMZ**, demilitarized zone, separa:

- utenti e host interni;
- servizi esposti pubblicamente.

Schema concettuale:

```text
Internet
-> Firewall
-> DMZ con servizi esposti
-> Firewall
-> rete privata interna
```

## Architettura base

Una architettura di sicurezza può includere:

- border router;
- firewall;
- rete esterna;
- DMZ;
- rete protetta interna;
- sniffer/IDS;
- port mirroring verso sistemi di analisi.

> [!Important]
> La DMZ limita l'impatto della compromissione di un servizio esposto, separandolo dalla rete interna.

## Collegamenti

- [[Difese_Rete_Firewall]]
- [[Packet_Filtering]]
- [[Auditing_Intrusion_Detection]]

## Fonti

- SRC-006

