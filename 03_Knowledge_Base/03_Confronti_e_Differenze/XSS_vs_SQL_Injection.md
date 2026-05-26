# XSS vs SQL Injection

| Aspetto | XSS | SQL injection |
|---|---|---|
| Contesto colpito | Browser/HTML/JavaScript | Database/query SQL |
| Vittima tipica | Utente che visita la pagina | Applicazione e database |
| Effetto | Script nel browser | Query alterata |
| Difesa principale | Encoding contestuale output | Prepared statements |

## Punto comune

Entrambe sono injection causate da improper neutralization: input non fidato viene usato in un contesto interpretabile.

## Collegamenti

- [[Cross_Site_Scripting_XSS]]
- [[SQL_Injection]]
- [[Injection_Improper_Neutralization]]

## Fonti

- SRC-007

