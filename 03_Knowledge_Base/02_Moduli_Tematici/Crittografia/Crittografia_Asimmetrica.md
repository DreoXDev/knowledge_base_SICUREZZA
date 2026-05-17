# Crittografia asimmetrica

> [!Info]
> La crittografia asimmetrica usa una coppia di chiavi per ogni soggetto. Risolve meglio il problema della distribuzione delle chiavi e permette firme digitali verificabili anche da terze parti.

## Definizione

Gli algoritmi asimmetrici, o **a chiave pubblica**, usano una coppia di chiavi per ogni soggetto:

- `k_pub`: chiave pubblica, conosciuta da tutti;
- `k_priv`: chiave privata, conosciuta solo dal proprietario.

La relazione tra le chiavi è tale che un messaggio codificato con una chiave può essere decodificato solo con la chiave corrispondente.

```text
decrypt(k_priv, encrypt(k_pub, p)) = p
decrypt(k_pub, encrypt(k_priv, p)) = p
```

## Uso per confidenzialità

Per inviare un messaggio confidenziale ad A:

1. il mittente cifra il messaggio con la chiave pubblica di A;
2. solo A può decifrarlo con la propria chiave privata.

> [!Info]
> La chiave pubblica può essere distribuita su canali insicuri, perché non è segreta. La chiave privata invece non deve mai essere condivisa.

## Numero di chiavi

Con crittografia simmetrica, `n` utenti che comunicano a coppie richiedono:

$$
\frac{n(n-1)}{2}
$$

chiavi condivise.

Con crittografia asimmetrica, invece, servono solo `n` coppie di chiavi, una per utente.

> [!Important]
> La crittografia asimmetrica risolve meglio il problema della scalabilità nella gestione delle chiavi.

## Supporto ai requisiti di sicurezza

| Requisito | Supporto | Motivo |
|---|---|---|
| Confidenzialità | Sì | solo chi conosce la chiave privata può decifrare ciò che è stato cifrato con la chiave pubblica corrispondente |
| Integrità | Sì | si può verificare la validità del messaggio tramite firma digitale |
| Autenticità | Sì | solo il possessore della chiave privata può produrre un messaggio verificabile con la chiave pubblica corrispondente |
| Non-ripudio | Sì | la verifica può essere fatta anche da terze parti, quindi è adatta a firme digitali |

## Differenza rispetto alla crittografia simmetrica

Nella crittografia simmetrica autenticità e integrità valgono solo tra i partecipanti che condividono la chiave.

Nella crittografia asimmetrica, invece, la verifica può essere fatta anche da terze parti, perché la chiave pubblica può essere usata per controllare una firma prodotta con la chiave privata.

## Collegamenti

- [[Crittografia_Simmetrica]]
- [[RSA]]
- [[Firme_Digitali]]
- [[Certificati_X509_PKI]]
- [[CIA_Triad_DAD]]

## Fonti

- SRC-003

