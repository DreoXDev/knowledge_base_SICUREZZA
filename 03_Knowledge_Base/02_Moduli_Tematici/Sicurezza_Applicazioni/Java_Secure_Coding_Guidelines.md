# Java Secure Coding Guidelines

> [!Note]
> Le linee guida Java qui non sono una lista generica di best practice: vanno collegate ai concetti di weakness, controlli automatici e prevenzione di vulnerabilita' tramite regole di coding.

## Domain dependent e domain independent

- Domain dependent: dipendono dal dominio applicativo e sono difficili da controllare automaticamente.
- Domain independent: riguardano struttura del codice e proprieta' generali, quindi sono piu' adatte a static analysis.

## Strumenti

- SpotBugs.
- SonarQube.
- FindBugs.

## Linee guida principali

- Limitare la durata dei dati sensibili.
- Preferire scope locali stretti.
- Salvare hash delle password, non password in chiaro o cifrate reversibilmente.
- Evitare MD5; secondo le slide preferire SHA-256.
- Rendere classi non serializzabili quando non serve serializzazione.
- Rendere classi non deserializzabili quando non serve deserializzazione.
- Rendere classi non clonabili quando non serve clonazione.
- Gestire integer overflow.
- Usare le operazioni exact arithmetic introdotte in Java 8 quando appropriate.

## Warning SpotBugs citati

- Esposizione della rappresentazione interna.
- Password database vuota.
- Password database hardcoded.
- Campo non `final` ma che dovrebbe esserlo.

## Collegamenti

- [[Secure_Coding_Java]]
- [[Glossario_Sicurezza_Applicazioni]]

## Fonti

- SRC-008

