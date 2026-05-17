# Password, hashing e salt

> [!Info]
> Le password non dovrebbero essere memorizzate in chiaro. Un sistema più sicuro conserva valori derivati tramite hashing e salt, così la compromissione del file password non rivela immediatamente i segreti degli utenti.

## Uso delle password

Nel caso più semplice, l'utente inserisce una password e il sistema verifica che sia corretta.

Tuttavia il sistema non dovrebbe memorizzare direttamente le password in chiaro.

Una soluzione tipica è memorizzare nel password file un valore derivato dalla password tramite una funzione di hash.

Esempio concettuale:

```text
password = wonderland
hash(wonderland) = exrygb
```

Il file delle password contiene quindi:

```text
User   hash(pw)
Bob    kdnsmi
Alice  exrygb
Jack   hsbdjv
```

> [!Info]
> Le funzioni di hash sono considerate non invertibili per ipotesi: dato l'hash, non dovrebbe essere possibile risalire facilmente alla password.

## Password file protetti

Le password vengono protette tramite hashing crittografico, spesso usando funzioni ad hoc volutamente più lente di SHA-2.

La lentezza intenzionale serve a rendere più costosi gli attacchi offline basati su molti tentativi.

## Salt

Il **salt** è un numero casuale associato alla password.

Nelle slide viene indicato come numero random da 12 bit.

Il salt viene memorizzato nel file delle password e la password viene memorizzata come:

```text
hash(pw + salt)
```

## Perché usare il salt

Il salt serve a ridurre problemi come:

- utenti diversi che scelgono la stessa password;
- uso di tabelle password-hash precompilate;
- riconoscimento immediato di password uguali.

## Multiple point of failure

Il sistema operativo protegge il file delle password e, allo stesso tempo, mantiene le password in forma hashata.

> [!Important]
> La sicurezza non deve dipendere da una sola barriera. Anche se il file password viene protetto, le password devono comunque essere memorizzate in forma non direttamente leggibile.

## Collegamenti

- [[Attacchi_alle_Password]]
- [[Hashing_Message_Digest]]
- [[Processo_Autenticazione_Sicuro]]

## Fonti

- SRC-004

