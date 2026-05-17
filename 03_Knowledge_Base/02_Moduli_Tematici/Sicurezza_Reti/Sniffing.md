# Sniffing

> [!Info]
> Lo sniffing intercetta traffico di rete. Compromette soprattutto la confidenzialità quando dati o metadati sono osservabili.

## Definizione

Lo **sniffing** è l'intercettazione del traffico di rete tramite software capace di acquisire pacchetti a livello data-link.

Uno sniffer può mostrare informazioni in chiaro relative a header di livello 2, 3 e 4, e protocolli applicativi come FTP o HTTP se non cifrati.

## Promiscuous mode

Una scheda di rete in **promiscuous mode** legge tutti i pacchetti in transito sul mezzo, non solo quelli destinati al proprio MAC address.

## Usi offensivi e difensivi

Lo sniffing può essere usato per:

- ricerca di password e username in chiaro;
- analisi di anomalie;
- analisi delle prestazioni;
- monitoraggio difensivo;
- analisi post-mortem del traffico.

> [!Warning]
> Lo stesso strumento può essere usato per amministrazione legittima o per attacco. Il contesto e le autorizzazioni sono fondamentali.

## LAN switched e non-switched

In una LAN non switched, tutti i nodi condividono il mezzo e una scheda in promiscuous mode può leggere molto traffico.

In una rete switched, lo switch inoltra il traffico in base a:

```text
MAC address + porta dello switch
```

Quindi uno sniffer vede normalmente solo il traffico destinato al proprio host.

## Sniffing su rete switched

Possibilità concettuali:

- port mirroring;
- repeater;
- TAP hardware;
- deviazione del traffico tramite attacchi come [[ARP_Poisoning_Spoofing]].

## Collegamenti

- [[ARP_Poisoning_Spoofing]]
- [[Wiretap_Attivo_Passivo]]
- [[TLS_HTTPS]]
- [[IPsec_VPN]]

## Fonti

- SRC-006

