# Denial of Service, DDoS e SYN flood

> [!Info]
> DoS e DDoS compromettono la disponibilità: l'obiettivo è impedire o rallentare l'accesso legittimo a risorse e servizi.

## Denial of Service

Un attacco **Denial of Service** mira a compromettere la disponibilità di un servizio.

Esempi:

- attacchi fisici ad apparati;
- flooding;
- SYN flooding;
- flooding ICMP;
- smurf attack;
- DDoS;
- attacchi DNS con reindirizzamento del traffico.

## SYN flood

Il SYN flood sfrutta l'instaurazione di connessioni TCP.

Connessione normale:

```text
Client -> Server: SYN, SEQNUM = X
Server -> Client: SYN-ACK, X+1, SEQNUM = Y
Client -> Server: ACK, Y+1
```

Nell'attacco il server mantiene stato per molte connessioni incomplete, fino a esaurire risorse e degradare il servizio.

## DDoS

Un **Distributed Denial of Service** usa molte macchine compromesse per generare traffico coordinato verso la vittima.

## Smurf

Lo smurf combina ping broadcast e IP spoofing per amplificare traffico verso la vittima.

## Collegamenti

- [[CIA_Triad_DAD]]
- [[Difese_Rete_Firewall]]
- [[Packet_Filtering]]

## Fonti

- SRC-006

