# Cifratura ibrida

> [!Info]
> La cifratura ibrida combina la velocità degli algoritmi simmetrici con la flessibilità della crittografia asimmetrica per proteggere lo scambio della chiave di sessione.

## Perché combinare algoritmi diversi

Gli algoritmi simmetrici come DES o AES sono molto più veloci di RSA.

RSA, però, è più flessibile per la gestione delle chiavi e permette di usare chiavi pubbliche su canali insicuri.

Per questo, nella pratica si combinano le due classi.

## Prestazioni

| Algoritmi | Prestazioni tipiche |
|---|---|
| DES / MD5 in hardware | gigabit al secondo |
| RSA | kilobit al secondo |

> [!Important]
> RSA viene usato tipicamente per cifrare piccole quantità di dati, non grandi messaggi.

## Confidenzialità: RSA + AES/DES

Schema pratico:

### Lato mittente

1. genera una chiave segreta casuale `k`;
2. usa AES o DES con `k` per cifrare il messaggio;
3. cifra `k` con la chiave pubblica del destinatario usando RSA;
4. invia il messaggio cifrato con AES e la chiave segreta cifrata con RSA.

### Lato destinatario

1. decifra la chiave `k` usando RSA con la propria chiave privata;
2. usa `k` per decifrare il messaggio con AES o DES.

## Vantaggio

Questo schema sfrutta:

- l'efficienza degli algoritmi simmetrici per cifrare il messaggio;
- la flessibilità degli algoritmi asimmetrici per proteggere lo scambio della chiave di sessione.

## Integrità e autenticità: RSA + Message Digest

Per firme digitali efficienti si usa:

- hashing/message digest per riassumere il messaggio;
- RSA per firmare il digest.

## Uso in TLS

TLS usa una logica ibrida: durante l'handshake si stabiliscono chiavi condivise e poi i dati applicativi vengono cifrati con crittografia simmetrica.

Vedi: [[TLS_HTTPS]]

## Collegamenti

- [[RSA]]
- [[Crittografia_Simmetrica]]
- [[Crittografia_Asimmetrica]]
- [[Firme_Digitali]]
- [[Hashing_Message_Digest]]

## Fonti

- SRC-003
- SRC-006
