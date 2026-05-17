# Limiti della crittografia simmetrica

> [!Info]
> La crittografia simmetrica è molto efficiente per cifrare dati, ma non basta per risolvere problemi di firma digitale, prova verso terzi e distribuzione sicura delle chiavi.

## Punti di forza

DES, Triple DES e AES mostrano i vantaggi tipici della crittografia simmetrica:

- implementazioni efficienti anche su hardware dedicato;
- velocità molto elevate, anche dell'ordine dei gigabit al secondo;
- ottimo supporto alla confidenzialità.

## Limiti

La crittografia simmetrica ha però limiti importanti:

- supporto sub-ottimo per integrità, autenticità e non-ripudio;
- autenticità e integrità valgono solo tra i partecipanti del canale protetto;
- non permette di dimostrare a terzi chi abbia inviato un messaggio;
- richiede una chiave diversa per ogni coppia di utenti;
- rende critico il problema dello scambio sicuro delle chiavi.

## Perché il non-ripudio non è garantito

Se due utenti condividono la stessa chiave, entrambi possono generare un messaggio valido.

Quindi un terzo non può stabilire con certezza quale dei due abbia prodotto il messaggio.

> [!Summary]
> La crittografia simmetrica è ottima per cifrare dati in modo efficiente, ma non basta per risolvere il problema della firma digitale e della prova verso terze parti.

## Soluzione parziale: crittografia asimmetrica

La [[Crittografia_Asimmetrica]] riduce il problema dello scambio delle chiavi, perché le chiavi pubbliche possono essere distribuite su canali insicuri.

Tuttavia introduce un nuovo problema: bisogna verificare che una chiave pubblica appartenga davvero all'entità dichiarata.

Questo porta al tema dei [[Certificati_X509_PKI]].

## Collegamenti

- [[Crittografia_Simmetrica]]
- [[DES_TripleDES_AES]]
- [[Algoritmi_Crittografici]]
- [[CIA_Triad_DAD]]

## Fonti

- SRC-002
- SRC-003
