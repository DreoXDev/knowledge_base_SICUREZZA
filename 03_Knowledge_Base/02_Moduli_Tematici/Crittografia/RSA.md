# RSA

> [!Info]
> RSA è un algoritmo a chiave pubblica basato sulla difficoltà di fattorizzare numeri molto grandi. Supporta confidenzialità e firme digitali, ma è molto più lento degli algoritmi simmetrici.

## Contesto storico

RSA è un algoritmo a chiave pubblica inventato da Rivest, Shamir e Adleman.

Si inserisce nel contesto della crittografia a chiave pubblica, resa famosa dal lavoro di Diffie e Hellman sulle nuove direzioni della crittografia.

## Idea di base

Gli algoritmi asimmetrici si basano su problemi computazionalmente difficili da invertire, detti **one-way functions**.

Nel caso di RSA, la funzione difficile da invertire è legata alla fattorizzazione di numeri molto grandi.

> [!Important]
> È computazionalmente difficile calcolare la chiave privata conoscendo solo la chiave pubblica.

## Generazione delle chiavi

RSA usa due numeri primi molto grandi `p` e `q`.

Procedura:

1. scegliere `p` e `q`, numeri primi molto grandi;
2. calcolare:

$$
n = p \cdot q
$$

$$
\varphi = (p-1)(q-1)
$$

3. scegliere `e` e `d` tali che:

$$
e \cdot d \equiv 1 \pmod{\varphi}
$$

4. eliminare `p`, `q` e `\varphi`;
5. usare:

$$
k_{pub} = (e,n)
$$

$$
k_{priv} = (d,n)
$$

## Cifratura e decifratura

Dato un messaggio `M`, la cifratura è:

$$
C = M^e \mod n
$$

La decifratura è:

$$
D = C^d \mod n = M
$$

La correttezza si basa sul teorema di Eulero, che estende il piccolo teorema di Fermat.

## Esempio con numeri piccoli

Scelta:

```text
p = 3
q = 5
n = 15
phi = 8
k_pub = (e = 11, 15)
k_priv = (d = 3, 15)
M = 2
```

Cifratura:

$$
C = M^e \mod n = 2^{11} \mod 15 = 8
$$

Decifratura:

$$
D = C^d \mod n = 8^3 \mod 15 = 2
$$

## Sicurezza di RSA

La sicurezza dipende dal fatto che, conoscendo solo `e` e `n`, per scoprire `d` bisognerebbe fattorizzare `n`, cioè trovare i fattori primi `p` e `q`.

Quando `n` ha molte cifre, questa operazione diventa computazionalmente impraticabile con mezzi ordinari.

## Recap

### Pro

- buon supporto a confidenzialità;
- buon supporto a integrità;
- buon supporto ad autenticità e non-ripudio;
- proprietà verificabili anche da terze parti;
- numero di chiavi lineare nel numero di utenti;
- chiavi pubbliche scambiabili su canali insicuri.

### Limiti

- non si presta a implementazioni efficienti come gli algoritmi simmetrici;
- velocità tipicamente dell'ordine dei kilobit al secondo;
- non conviene usarlo per cifrare direttamente grandi quantità di dati.

## Collegamenti

- [[Crittografia_Asimmetrica]]
- [[Firme_Digitali]]
- [[Cifratura_Ibrida]]
- [[Forza_Bruta_e_Crittoanalisi]]

## Fonti

- SRC-003

