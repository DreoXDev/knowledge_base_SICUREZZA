# SQL Injection

SQL injection e' una forma di command/query injection in cui input utente modifica la query SQL eseguita dall'applicazione.

## Problema

Il programma costruisce una query concatenando stringhe e input utente. Se l'input contiene caratteri o frammenti SQL, puo' cambiare la semantica della query.

```java
String q = "SELECT * FROM utenti WHERE nome = '" + nome + "' AND password = '" + password + "'";
Statement st = conn.createStatement();
ResultSet rs = st.executeQuery(q);
```

In questo schema codice SQL e dati utente sono mescolati.

## Conseguenze

- Lettura di dati sensibili.
- Modifica o cancellazione di dati.
- Aggiramento di controlli di autenticazione.
- Amministrazione non autorizzata del database.
- Lettura di file dal filesystem del DBMS, se il DBMS e i privilegi lo permettono.

## Prepared statements

La contromisura principale e' usare query parametrizzate:

```java
PreparedStatement ps = conn.prepareStatement(
    "SELECT * FROM utenti WHERE nome = ? AND password = ?"
);
ps.setString(1, nome);
ps.setString(2, password);
ResultSet rs = ps.executeQuery();
```

Il DBMS riceve struttura della query e parametri separatamente. L'input utente resta dato, non diventa codice SQL.

## Encoding e librerie

Le slide ricordano che i linguaggi principali offrono librerie di encoding, ma per SQL injection la difesa primaria resta la parametrizzazione.

## Collegamenti

- [[Injection_Improper_Neutralization]]
- [[XSS_vs_SQL_Injection]]
- [[Contromisure_Injection]]
- [[CWE_CAPEC_CVE]]

## Fonti

- SRC-007

