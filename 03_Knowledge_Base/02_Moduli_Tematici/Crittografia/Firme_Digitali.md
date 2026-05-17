# Firme digitali

> [!Info]
> La firma digitale combina crittografia a chiave pubblica e hashing per garantire autenticità del mittente, integrità del messaggio e non-ripudio.

## Obiettivo

La firma digitale serve a garantire:

- autenticazione del mittente;
- integrità del messaggio;
- non-ripudio.

La crittografia a chiave pubblica soddisfa i requisiti necessari per realizzare un meccanismo di firma digitale.

## Uso "al contrario" della chiave pubblica

Per firmare digitalmente si usa la crittografia a chiave pubblica in modo inverso rispetto alla confidenzialità:

1. il mittente cifra con la propria chiave privata;
2. chiunque può verificare decifrando con la chiave pubblica del mittente.

```text
decrypt(k_pub, encrypt(k_priv, p)) = p
```

Questo funziona perché solo il possessore della chiave privata può aver prodotto un contenuto verificabile con la chiave pubblica corrispondente.

## Firme digitali efficienti

Cifrare direttamente un messaggio molto grande con RSA può essere inefficiente.

La soluzione standard è firmare il **message digest** del messaggio.

Siano:

```text
M = messaggio
F = MessageDigest(M)
F' = encrypt(F, k_priv)
```

Il mittente invia:

```text
M + F'
```

dove `F'` è il digest firmato.

## Verifica lato destinatario

Il destinatario:

1. riceve il messaggio `M` e la firma `F'`;
2. decifra `F'` con la chiave pubblica del mittente, ottenendo `F`;
3. calcola `MessageDigest(M)` sul messaggio ricevuto;
4. confronta il digest calcolato con quello ottenuto dalla firma;
5. se coincidono, integrità e identità del mittente sono confermate.

> [!Summary]
> In pratica non si firma l'intero messaggio: si firma il digest del messaggio.

## Proprietà ottenute

| Proprietà | Come viene ottenuta |
|---|---|
| Integrità | se il messaggio cambia, cambia anche il digest |
| Autenticità | solo la chiave privata del mittente può produrre la firma |
| Non-ripudio | la verifica può essere fatta da terze parti usando la chiave pubblica |

## Collegamenti

- [[Crittografia_Asimmetrica]]
- [[RSA]]
- [[Hashing_Message_Digest]]
- [[Certificati_X509_PKI]]

## Fonti

- SRC-003

