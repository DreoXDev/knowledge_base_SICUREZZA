# ARP poisoning e address spoofing

> [!Info]
> ARP poisoning mostra come un protocollo locale semplice e stateless possa permettere deviazione del traffico e man-in-the-middle.

## Ethernet e MAC address

Ethernet è un protocollo di livello 2 che trasmette dati sotto forma di frame.

I frame usano indirizzi **MAC**:

- lunghi 48 bit;
- associati alle interfacce di rete;
- usati per identificare sorgente e destinazione nel dominio locale.

## ARP

**ARP**, Address Resolution Protocol, mappa indirizzi IPv4 da 32 bit in indirizzi MAC da 48 bit.

Usa messaggi ARP request e ARP reply. Le risposte vengono memorizzate nella **ARP cache**.

## ARP poisoning

L'ARP poisoning sfrutta il comportamento stateless di ARP:

- le ARP reply possono essere salvate anche se non sollecitate;
- l'attaccante invia risposte ARP falsificate;
- la vittima aggiorna la cache con associazioni IP-MAC false;
- il traffico può essere deviato verso l'attaccante.

## Network address spoofing

| Tipo | Descrizione |
|---|---|
| ARP/MAC spoofing | falsificazione del MAC address nel livello 2 |
| IP spoofing | falsificazione dell'indirizzo IP sorgente nel livello 3 |

## Difese concettuali

Possibili difese:

- ARP statiche in sola lettura;
- detection/prevention;
- rilevamento di più IP associati allo stesso MAC;
- ignorare reply non sollecitate;
- accettare aggiornamenti solo dopo timeout.

## Collegamenti

- [[Sniffing]]
- [[Wiretap_Attivo_Passivo]]
- [[Spoofing_Phishing_Pharming]]
- [[IPsec_VPN]]

## Fonti

- SRC-006

