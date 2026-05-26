# TLS Struttura del Pacchetto

TLS sta sopra TCP e sotto il protocollo applicativo. Protegge i dati applicativi, ma non nasconde gli header IP e TCP.

## Struttura concettuale

```text
Header IP | Header TCP | Record TLS | Dati applicativi protetti
```

Il record TLS contiene un header TLS e dati applicativi cifrati e autenticati secondo la cipher suite negoziata. Gli header IP e TCP restano visibili perche' servono a instradare e consegnare la comunicazione.

## Protezione ottenuta

TLS fornisce confidenzialita' e integrita' dei dati applicativi, oltre ad autenticazione del server tramite certificato durante l'handshake. Non nasconde indirizzi IP, porte TCP e altri metadati di trasporto.

## Da non confondere

TLS non e' IPsec: TLS protegge sopra TCP, IPsec protegge a livello IP. HTTPS e' HTTP su TLS.

## Collegamenti

- [[TLS_HTTPS]]
- [[Confronto_TLS_IPsec]]
- [[IPsec_Modalita_Trasporto_Tunnel]]

## Fonti

- SRC-006
- SRC-009

