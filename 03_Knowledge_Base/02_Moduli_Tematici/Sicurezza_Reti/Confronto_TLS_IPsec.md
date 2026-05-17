# Confronto tra TLS e IPsec

## TLS

TLS protegge la comunicazione tra applicazioni sopra TCP/IP.

Caratteristiche:

- lavora sopra il trasporto;
- protegge dati applicativi;
- è usato da HTTPS;
- usa handshake, certificati, key exchange e cifratura simmetrica per i dati;
- lascia in chiaro informazioni di rete e trasporto.

## IPsec

IPsec protegge a livello IP.

Caratteristiche:

- trasparente alle applicazioni;
- protegge traffico host-to-host o gateway-to-gateway;
- può essere usato per VPN;
- protegge anche informazioni dei protocolli superiori;
- può mascherare meglio lo scopo applicativo del traffico.

## Tabella di confronto

| Aspetto | TLS | IPsec |
|---|---|---|
| Livello | sopra TCP | livello IP |
| Protezione | applicazione-applicazione | host-host o gateway-gateway |
| Uso tipico | HTTPS, email sicura | VPN |
| Visibilità header IP/TCP | restano visibili | più informazioni vengono incapsulate/cifrate |
| Trasparenza per applicazioni | richiede supporto applicativo/librerie | trasparente alle applicazioni |
| Protezione da traffic analysis | limitata | maggiore, ma non totale |
| Protezione da IP spoofing | limitata | maggiore, perché l'origine viene autenticata |

## Uso combinato

TLS e IPsec possono essere usati insieme.

```text
Applicazione protetta da TLS
dentro
tunnel IPsec/VPN
```

> [!Summary]
> TLS protegge bene dati applicativi specifici. IPsec protegge traffico tra endpoint di rete. La scelta dipende dal livello a cui si vuole applicare la sicurezza.

## Collegamenti

- [[TLS_HTTPS]]
- [[IPsec_VPN]]
- [[Crittografia_Introduzione]]

## Fonti

- SRC-006

