# Schemi di cifratura

> [!Info]
> Uno schema di cifratura trasforma un messaggio leggibile in un messaggio cifrato. La sicurezza dipende dall'algoritmo, dalla chiave e dal modo in cui entrambi sono usati.

## Idea generale

Uno schema di cifratura permette di trasformare un messaggio leggibile, detto **plaintext**, in un messaggio non comprensibile, detto **ciphertext**.

Solo chi conosce la chiave corretta può risalire dal messaggio cifrato al messaggio originale.

## Componenti di un sistema crittografico

Un sistema crittografico consiste in generale di cinque parti:

| Componente | Significato |
|---|---|
| `P` | insieme dei messaggi in chiaro, cioè plaintext |
| `K` | insieme delle chiavi per codifica e decodifica |
| `C` | insieme dei messaggi cifrati, cioè ciphertext |
| `encrypt` | funzione di codifica: $K \times P \to C$ |
| `decrypt` | funzione di decodifica: $K \times C \to P$ |

## Obiettivo

Vogliamo cifrare un messaggio per proteggerlo da accessi non autorizzati, ma anche poterlo decifrare correttamente affinché il destinatario autorizzato possa leggerlo.

In forma generale:

```text
decrypt(k, encrypt(k, p)) = p
```

dove:

- `p` è il plaintext;
- `k` è la chiave;
- `encrypt(k, p)` produce il ciphertext;
- `decrypt(k, c)` ricostruisce il plaintext.

## Esempio: cifrario di Cesare

Il **cifrario di Cesare** è un esempio semplice di schema di cifratura.

Funziona tramite spostamento delle lettere usando aritmetica modulo `n`, dove `n` è il numero di caratteri dell'alfabeto.

Esempio con chiave `k = 2`:

```text
encrypt(2, COMPUTERZ) = EQORWVGTB
decrypt(2, EQORWVGTB) = COMPUTERZ
```

## Limite principale

Il cifrario di Cesare ha poche chiavi disponibili.

Con un alfabeto di 26 lettere, le chiavi utili sono solo da 1 a 25. Questo lo rende facilmente attaccabile con un attacco di [[Forza_Bruta_e_Crittoanalisi|forza bruta]].

## Collegamenti

- [[Forza_Bruta_e_Crittoanalisi]]
- [[Crittografia_Simmetrica]]
- [[Crittografia_Introduzione]]

## Fonti

- SRC-002

