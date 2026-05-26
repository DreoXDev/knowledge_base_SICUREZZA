# Sicurezza Applicazioni - Introduzione

Le applicazioni eseguono funzionalita' per categorie di utenti usando risorse messe a disposizione dal sistema. Per questo sono target naturali: chi attacca puo' voler negare funzionalita', farle eseguire da utenti non autorizzati o accedere a risorse per cui non ha diritti.

## Perche' le applicazioni sono esposte

Le applicazioni moderne sono spesso connesse alla rete globale. Questo aumenta la superficie di attacco: un errore applicativo non resta confinato al singolo host, ma puo' essere raggiunto da molti attaccanti remoti.

## Funzionalita', utenti e risorse

Una applicazione corretta deve rispettare la [[Glossario_Sicurezza_Applicazioni|security policy]]: chi puo' eseguire quale funzione, su quali dati, con quali vincoli.

Gli attacchi applicativi puntano spesso a:

- negare una funzionalita' agli utenti autorizzati;
- eseguire una funzionalita' come utente non autorizzato;
- leggere, modificare o cancellare risorse non autorizzate;
- aggirare controlli di autenticazione o autorizzazione.

## Collegamento con CIA Triad

Gli attacchi applicativi si leggono bene tramite [[CIA_Triad_DAD]]:

- confidenzialita': esposizione di dati tramite XSS, SQL injection o buffer overread;
- integrita': modifica di dati, comandi o query;
- disponibilita': crash, consumo di risorse o negazione di funzioni.

## Fonti

- SRC-007

