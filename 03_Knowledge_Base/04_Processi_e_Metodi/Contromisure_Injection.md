# Contromisure Injection

## Problema

Input non fidato viene interpretato come codice, markup, query o comando.

## Cause tipiche

- Concatenazione di stringhe per costruire output o query.
- Mancato encoding contestuale.
- Validazione assente o solo client-side.
- Confusione tra dato e linguaggio interpretabile.

## Contromisure

- Prepared statements per SQL.
- Encoding/escaping contestuale per HTML, attributi, JavaScript, URL e CSS.
- Validation server-side con allowlist quando possibile.
- Sanitization solo quando semanticamente corretta.
- Separazione tra codice e dati.

## Limiti delle contromisure

Validation generica non basta. Encoding sbagliato per contesto puo' essere inefficace. I controlli client-side possono essere aggirati.

## Collegamenti

- [[Injection_Improper_Neutralization]]
- [[Cross_Site_Scripting_XSS]]
- [[SQL_Injection]]

