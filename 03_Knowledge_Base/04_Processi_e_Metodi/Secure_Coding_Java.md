# Secure Coding Java

## Problema

Weakness evitabili possono entrare nel codice Java tramite gestione errata di dati sensibili, serializzazione, clonazione, overflow interi o esposizione di rappresentazione interna.

## Cause tipiche

- Scope troppo ampio per dati sensibili.
- Password in chiaro o cifrate reversibilmente.
- Uso di algoritmi deboli come MD5.
- Classi serializzabili, deserializzabili o clonabili senza necessita'.
- Mancata gestione di integer overflow.

## Contromisure

- Limitare durata e scope dei dati sensibili.
- Salvare hash delle password.
- Secondo le slide, preferire SHA-256 a MD5.
- Rendere classi non serializzabili/deserializzabili/clonabili quando non necessario.
- Usare exact arithmetic di Java 8.
- Usare SpotBugs, SonarQube o FindBugs.

## Limiti delle contromisure

Gli strumenti statici aiutano soprattutto su regole domain independent. Le regole domain dependent richiedono conoscenza del dominio applicativo.

## Collegamenti

- [[Java_Secure_Coding_Guidelines]]

