# IPsec e VPN

> [!Info]
> IPsec protegge traffico a livello IP ed è spesso usato per VPN. È più trasparente alle applicazioni rispetto a TLS.

## IPsec

**IPsec** è un meccanismo di sicurezza a livello IP.

Caratteristiche:

- funziona in configurazione host-to-host;
- è trasparente alle applicazioni;
- protegge traffico tra host, non direttamente tra applicazioni;
- è usato per stabilire comunicazioni VPN.

## Posizione nello stack

IPsec opera sotto TCP/UDP e sopra o insieme al livello IP, proteggendo il traffico dei livelli superiori.

## Incapsulamento IPsec

Schema concettuale:

```text
Header IPsec
Header IP originale
Header TCP
Application data
```

La parte originale può essere cifrata e mascherata.

## Tunnel IPsec

Gli header IPsec specificano gli indirizzi dei due endpoint del tunnel.

Gli endpoint possono essere router, gateway di reti locali, computer utente o gateway di una rete remota.

## VPN

Le **VPN**, Virtual Private Networks, sono spesso usate tra un dipendente remoto e l'azienda oppure tra reti locali diverse della stessa azienda.

Tutto il traffico tra endpoint VPN è cifrato.

## Difese offerte da IPsec

IPsec offre:

- maggiore resistenza a sniffing;
- maggiore resistenza a modifica dei dati;
- protezione dei protocolli superiori;
- maggiore protezione contro traffic analysis;
- maggiore protezione contro IP spoofing, perché anche l'indirizzo sorgente viene autenticato.

## IPsec e traffic analysis

Poiché IPsec cifra a livello di rete, lo scopo applicativo di una comunicazione diventa meno distinguibile.

Tuttavia alcune analisi statistiche restano possibili.

## Collegamenti

- [[Confronto_TLS_IPsec]]
- [[Sniffing]]
- [[Spoofing_Phishing_Pharming]]
- [[TLS_HTTPS]]

## Fonti

- SRC-006

