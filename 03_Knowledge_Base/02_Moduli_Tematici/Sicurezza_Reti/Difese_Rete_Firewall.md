# Difese contro attacchi dalla rete e firewall

> [!Info]
> Le difese di rete combinano gestione organizzativa, hardening tecnico, controllo perimetrale, intrusion detection e protocolli crittografici.

## Difese generali

Misure importanti:

- applicazione tempestiva di security patch;
- riconfigurazione attenta di software, servizi e topologia;
- uso di network scanner per cercare vulnerabilità;
- security policy aziendali;
- formazione dello staff;
- filtering e firewalling;
- intrusion detection;
- protocolli di rete con crittografia.

## Security enforcement devices

Una tipica architettura di sicurezza implementa policy tramite dispositivi di controllo perimetrale, come border router e firewall.

> [!Info]
> Router e firewall sono dispositivi diversi, ma molte funzionalità di firewall possono essere implementate anche in un border router.

## Firewall

Un firewall è una barriera di isolamento e una difesa perimetrale passiva.

Compiti principali:

- consentire solo ciò che è autorizzato dalla security policy;
- rilevare e riportare tentativi di violazione;
- svolgere auditing e accounting;
- collegare segmenti di rete a livello data-link o network.

## Tipi di firewall

| Tipo | Livello | Caratteristiche |
|---|---|---|
| Packet filter | livello 2/3, spesso stateless | controlla header IP/TCP, indirizzi e porte |
| Application gateway | livello applicazione, spesso stateful | controlla semanticamente dati applicativi su più pacchetti |

## Collegamenti

- [[Packet_Filtering]]
- [[Application_Gateway_DMZ]]
- [[Auditing_Intrusion_Detection]]
- [[TLS_HTTPS]]

## Fonti

- SRC-006

