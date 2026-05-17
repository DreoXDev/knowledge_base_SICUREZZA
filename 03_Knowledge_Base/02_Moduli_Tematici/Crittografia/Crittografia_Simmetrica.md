# Crittografia simmetrica

> [!Info]
> La crittografia simmetrica usa una chiave segreta condivisa per cifrare e decifrare. È molto efficiente, ma introduce problemi importanti di distribuzione delle chiavi e non-ripudio.

## Definizione

Gli algoritmi simmetrici, o **a chiave segreta**, usano la stessa chiave `k` sia per cifrare sia per decifrare.

```text
decrypt(k, encrypt(k, p)) = p
```

Per instaurare una comunicazione confidenziale, due soggetti devono conoscere una chiave condivisa che non deve essere nota a nessun altro.

## Funzionamento

1. Il mittente prende il testo in chiaro.
2. Lo cifra con la chiave segreta.
3. Ottiene un testo cifrato.
4. Il destinatario decifra il testo cifrato usando la stessa chiave segreta.
5. Recupera il testo in chiaro.

## Requisiti di sicurezza supportati

| Requisito | Supporto | Motivo |
|---|---|---|
| Confidenzialità | Sì | solo chi conosce la chiave segreta può decodificare il messaggio |
| Integrità | Sì, ma con ulteriori assunzioni | serve aggiungere un codice verificabile con chiave condivisa per controllare la validità del messaggio |
| Autenticità | Sì, ma solo nel canale condiviso | solo chi conosce la chiave può essere mittente, ma non si distingue quale partner specifico |
| Non-ripudio | No, rispetto a terze parti | non si può dimostrare a terzi chi tra i partecipanti abbia generato il messaggio |

> [!Warning]
> La crittografia simmetrica non è adatta alle firme digitali, perché autenticità e non-ripudio valgono solo internamente al canale protetto dalla chiave condivisa e non sono comprovabili a terze parti.

## Problema del numero di chiavi

Se `n` individui vogliono comunicare in modo sicuro a coppie, serve una chiave per ogni coppia.

Il numero totale di chiavi è:

$$
\frac{n(n-1)}{2}
$$

Questa crescita quadratica rende difficile la gestione delle chiavi quando il numero di utenti aumenta.

## Collegamento con rischio e vulnerabilità

Una chiave scambiata o conservata male diventa una vulnerabilità. Anche se l'algoritmo è forte, la sicurezza complessiva dipende dal processo di gestione delle chiavi e dal contesto operativo.

## Collegamenti

- [[DES_TripleDES_AES]]
- [[Limiti_Crittografia_Simmetrica]]
- [[CIA_Triad_DAD]]
- [[Analisi_Rischio]]

## Fonti

- SRC-002

