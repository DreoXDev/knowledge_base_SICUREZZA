# Covert channels

> [!Info]
> Un covert channel è un canale non previsto per trasferire informazioni. È pericoloso perché può aggirare politiche di accesso apparentemente corrette.

## Definizione

Un **covert channel** è un canale alternativo attraverso cui dati sensibili vengono trasmessi a un soggetto non autorizzato.

Il canale può essere condiviso anche legalmente, ma viene usato in modo non previsto per trasferire informazioni.

## Attaccanti possibili

Esempi:

- utente interno malevolo;
- Trojan installato in un programma di servizio.

## Meccanismi possibili

I dati possono essere comunicati:

- scrivendo su file con diversa protezione;
- codificando informazioni nei nomi dei file;
- usando codifiche segrete in file apparentemente legali;
- variando il numero di spazi dopo un carattere;
- usando l'ultima cifra non significativa di un campo;
- segnalando eventi monitorabili;
- sfruttando presenza o assenza di oggetti in memoria;
- bloccando o sbloccando un file in intervalli temporali concordati.

## Perché sono pericolosi

I covert channels sono difficili da eliminare perché non sempre violano direttamente le regole di accesso.

Possono sfruttare effetti collaterali, tempi, nomi, metadati o stati osservabili.

> [!Important]
> Un controllo degli accessi corretto deve considerare anche i flussi indiretti di informazione, non solo gli accessi diretti ai file.

## Collegamenti

- [[Obiettivi_Controllo_Accessi]]
- [[Bell_LaPadula]]
- [[Limiti_Crittografia_e_Threat_Model]]

## Fonti

- SRC-005

