# Obiettivi generali del controllo degli accessi

> [!Info]
> Il controllo accessi deve mediare ogni accesso, applicare i minimi privilegi e prevenire usi impropri o indiretti degli oggetti protetti.

## Mediazione completa

La **mediazione completa** richiede di controllare ogni accesso a ogni oggetto protetto.

Il sistema non deve controllare solo il primo accesso o solo alcuni passaggi: ogni operazione rilevante deve passare dal controllo.

## TOC/TOU

Gli attacchi **TOC/TOU** (*time-of-check/time-of-use*) sfruttano la differenza temporale tra:

- momento in cui un accesso viene controllato;
- momento in cui la risorsa viene effettivamente usata.

Se la risorsa cambia tra controllo e uso, l'attaccante può aggirare il controllo.

> [!Warning]
> La mediazione completa aiuta a prevenire attacchi TOC/TOU perché evita che il controllo sia separato in modo insicuro dall'uso effettivo.

## Principio dei privilegi minimi

Il controllo accessi deve permettere di implementare il principio dei **minimi privilegi**.

Ogni soggetto deve avere solo i privilegi strettamente necessari per svolgere il proprio compito.

## Uso appropriato degli oggetti protetti

Il sistema deve controllare che gli oggetti protetti vengano usati in modo appropriato.

Questo include anche la prevenzione di leak indiretti verso soggetti non autorizzati.

## Collegamenti

- [[Covert_Channels]]
- [[SO_Trusted_Principi]]
- [[Controllo_Accessi_SO]]

## Fonti

- SRC-005

