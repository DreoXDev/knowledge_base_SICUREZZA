# Firewall e Architetture

## Packet filter

Un firewall packet filter decide se permettere o bloccare pacchetti usando campi di header: indirizzi IP, porte TCP/UDP, protocollo e talvolta informazioni di livello 2.

Per contrastare IP spoofing esterno verso una sottorete, il filtro deve bloccare pacchetti in ingresso dall'esterno che dichiarano come sorgente un indirizzo appartenente alla rete interna.

## Application gateway

Un application gateway lavora come proxy applicativo. Comprende il protocollo applicativo e puo' applicare controlli piu' semantici rispetto a un packet filter, ma e' piu' costoso e specifico.

## Screened subnet

Una screened subnet usa filtri e segmentazione per isolare servizi esposti dalla rete interna. E' una forma architetturale per ridurre l'impatto di compromissioni.

## DMZ

La DMZ e' una rete separata che ospita servizi pubblici, come web server o mail gateway. La rete interna resta dietro ulteriori controlli.

## Collegamenti

- [[Packet_Filtering]]
- [[Application_Gateway_DMZ]]
- [[Difese_Rete_Firewall]]

## Fonti

- SRC-006
- SRC-009
- SRC-011

