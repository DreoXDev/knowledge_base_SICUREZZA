# Certificati X.509 e PKI

> [!Info]
> Certificati X.509 e PKI rispondono al problema centrale della crittografia a chiave pubblica: sapere se una chiave pubblica appartiene davvero all'entità dichiarata.

## Problema della distribuzione delle chiavi pubbliche

In un sistema a chiave pubblica, la chiave pubblica di un utente `U` serve per:

- mandare messaggi confidenziali a `U`;
- autenticare provenienza e integrità di un messaggio firmato da `U`.

Ma c'è un'assunzione fondamentale:

> La chiave pubblica deve corrispondere davvero all'entità che vogliamo autenticare o a cui vogliamo inviare messaggi confidenziali.

Il problema diventa quindi:

> Come stabilire con sicurezza chi è il proprietario di una chiave pubblica?

## Certificati X.509

Un certificato garantisce la veridicità di una chiave pubblica rispetto a una certa entità, per esempio una persona o un'azienda.

Un certificato è emesso da un'autorità di certificazione fidata e autorizzata.

X.509 è uno standard per emettere certificati che associano un'identità a una chiave pubblica.

## Contenuto di un certificato X.509

Un certificato X.509 contiene:

- nome dell'entità certificata;
- chiave pubblica dell'entità;
- nome dell'autorità di certificazione che rilascia il certificato;
- firma digitale dell'autorità di certificazione.

## Verifica di un certificato

Se si dispone della chiave pubblica dell'autorità di certificazione, si può verificare:

- la veridicità del certificato;
- l'integrità del certificato.

Se ci si fida dell'autorità di certificazione, ci si può fidare dell'associazione tra entità e chiave pubblica riportata nel certificato.

## Catene di certificati

Una catena di certificati permette di estendere la fiducia.

Esempio:

- A possiede la chiave pubblica di X e si fida di X;
- X ha rilasciato un certificato a Y;
- Y ha rilasciato un certificato a Z.

A può fidarsi di Z se:

1. verifica il certificato di Y tramite la chiave pubblica di X;
2. ottiene con fiducia la chiave pubblica di Y;
3. usa la chiave pubblica di Y per verificare il certificato di Z;
4. ottiene con fiducia la chiave pubblica di Z.

## PKI - Public Key Infrastructure

Una **PKI** è l'infrastruttura organizzativa e tecnica che gestisce certificati e autorità di certificazione.

La struttura vista nelle slide è gerarchica:

```text
IPRA
└── PCA
    └── CA
        └── User
```

Dove:

- `IPRA`: Internet Policy Registration Authority;
- `PCA`: Policy Certification Authority;
- `CA`: Certification Authority;
- `User`: utente o entità finale certificata.

## Collegamenti

- [[Crittografia_Asimmetrica]]
- [[Firme_Digitali]]
- [[RSA]]
- [[Limiti_Crittografia_e_Threat_Model]]

## Fonti

- SRC-003

