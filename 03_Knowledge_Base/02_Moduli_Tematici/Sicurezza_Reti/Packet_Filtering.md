# Packet filtering

## Definizione

Il **packet filtering** è uno dei modi più semplici per implementare policy di sicurezza.

Router, switch e firewall possono supportare liste di regole di filtraggio o access control rules.

## Regole di filtraggio

Le regole vengono controllate in sequenza su ogni pacchetto. La prima regola che corrisponde viene applicata.

Ogni regola può definire:

- `permit`, cioè allow;
- `deny`, cioè drop.

Una regola può includere protocollo, indirizzo sorgente, porta sorgente, indirizzo destinazione, porta destinazione e azione.

## Filtri anti-spoofing

Un uso importante è bloccare traffico con indirizzi sorgente non ammissibili rispetto al lato da cui arriva.

### Traffico interno verso esterno

Un border router dovrebbe inoltrare verso l'esterno solo pacchetti con sorgenti interne legittime.

### Traffico esterno verso interno

Il router dovrebbe bloccare traffico proveniente da Internet che dichiara indirizzi sorgente interni.

> [!Summary]
> Il packet filtering può ridurre attacchi come IP spoofing, ma lavora soprattutto su header e regole statiche, non sulla semantica applicativa.

## Collegamenti

- [[Difese_Rete_Firewall]]
- [[Spoofing_Phishing_Pharming]]
- [[Application_Gateway_DMZ]]

## Fonti

- SRC-006

