# IPsec Modalita Trasporto e Tunnel

IPsec lavora a livello IP e puo' proteggere traffico tra host o tra gateway. Le due modalita' principali da distinguere all'esame sono transport mode e tunnel mode.

## Transport mode

In modalita' trasporto non viene incapsulato l'intero pacchetto IP originale.

Struttura concettuale con ESP:

```text
Header IP originale | Header ESP | Payload IP protetto | Trailer/Auth ESP
```

L'header IP originale resta visibile ed e' usato per l'instradamento. IPsec protegge il payload del pacchetto IP, quindi tipicamente segmento TCP/UDP e dati applicativi. Con ESP si puo' ottenere confidenzialita' del payload e integrita'/autenticazione secondo configurazione.

> [!Warning]
> In transport mode gli indirizzi IP sorgente e destinazione originali non sono nascosti, perche' restano nell'header IP visibile.

## Tunnel mode

In modalita' tunnel l'intero pacchetto IP originale viene incapsulato dentro un nuovo pacchetto IP.

```text
Nuovo header IP | Header ESP | Header IP originale protetto | Payload originale protetto | Trailer/Auth ESP
```

Il nuovo header esterno serve per instradare il traffico tra endpoint del tunnel, ad esempio due gateway VPN. L'header IP originale e il payload originale sono protetti all'interno.

## Confronto rapido

| Aspetto | Transport mode | Tunnel mode |
|---|---|---|
| Cosa protegge | Payload IP | Intero pacchetto IP originale |
| Header IP originale | Visibile | Protetto/incapsulato |
| Uso tipico | Host-to-host | VPN gateway-to-gateway o host-to-gateway |
| Privacy metadati | Minore | Maggiore |

## Collegamenti

- [[IPsec_VPN]]
- [[Confronto_TLS_IPsec]]
- [[TLS_Struttura_Pacchetto]]

## Fonti

- SRC-006
- SRC-009
- SRC-010

