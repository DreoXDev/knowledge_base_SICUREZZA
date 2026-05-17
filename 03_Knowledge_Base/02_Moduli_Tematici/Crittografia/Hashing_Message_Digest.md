# Hashing e message digest

> [!Info]
> Un message digest è un riassunto crittografico del messaggio. È utile per verificare l'integrità, ma da solo non garantisce confidenzialità, autenticità o non-ripudio.

## Definizione

Un **message digest** è un riassunto del messaggio: una sorta di checksum crittografico caratterizzante del messaggio.

Idealmente, ogni digest dovrebbe corrispondere a uno e un solo messaggio.

Nella pratica, questo non è matematicamente possibile per tutti i messaggi, perché lo spazio dei messaggi può essere molto più grande dello spazio dei digest.

> [!Important]
> Un buon algoritmo di hashing deve approssimare il più possibile l'idea che messaggi diversi producano digest diversi.

## Proprietà richieste

### Non invertibile

Dato il digest di un messaggio, deve essere impossibile o estremamente difficile ricostruire un messaggio che produca quel digest.

### Collision resistant

Deve essere improbabile trovare due messaggi diversi che producano lo stesso digest.

## Uso per integrità

Per verificare l'integrità di un messaggio:

1. si conosce il digest `MD` del messaggio originale;
2. si calcola il digest del messaggio ricevuto;
3. si confrontano i due digest;
4. se coincidono, si può assumere che il messaggio non sia stato modificato.

> [!Warning]
> Il controllo funziona solo se il digest noto non è stato a sua volta manomesso.

## Esempi di algoritmi

| Algoritmo | Dimensione digest | Note |
|---|---:|---|
| MD5 | 128 bit | storico, oggi non adatto a sicurezza forte |
| SHA1 | 160 bit | storico, oggi debole per collisioni |
| SHA2 | 256, 384, 512 bit | famiglia più robusta |

## MD5

MD5 applica trasformazioni complesse a blocchi di 512 bit del messaggio e produce un digest di 128 bit.

L'idea originaria era rendere computazionalmente infattibile:

- produrre due messaggi con lo stesso digest;
- produrre un messaggio con un digest target prestabilito.

## Supporto ai requisiti di sicurezza

| Requisito | Supporto | Motivo |
|---|---|---|
| Confidenzialità | No | il digest non è un messaggio cifrato e non serve a trasmettere segreti |
| Integrità | Sì | la coppia messaggio + digest permette di verificare modifiche |
| Autenticità | No | chiunque può calcolare il digest di un messaggio |
| Non-ripudio | No | il digest da solo non prova l'identità del mittente |

## Uso per password

Gli hash sono usati anche per memorizzare password in modo non direttamente leggibile.

Vedi: [[Password_Hashing_Salt]]

## Collegamenti

- [[Firme_Digitali]]
- [[Algoritmi_Crittografici]]
- [[CIA_Triad_DAD]]

## Fonti

- SRC-003
- SRC-004
