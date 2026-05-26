# Sicurezza Applicazioni - Parte 1

La prima parte introduce il lessico della sicurezza applicativa, le tassonomie usate per classificare weakness e attacchi, la struttura essenziale delle web application e due famiglie centrali di injection: XSS e SQL injection.

## Percorso di studio

1. [[Sicurezza_Applicazioni_Introduzione]]
2. [[Glossario_Sicurezza_Applicazioni]]
3. [[CWE_CAPEC_CVE]]
4. [[Applicazioni_Web_HTTP_HTML]]
5. [[Injection_Improper_Neutralization]]
6. [[Cross_Site_Scripting_XSS]]
7. [[SQL_Injection]]

## Idee guida

- Una weakness non e' ancora una vulnerabilita' concreta.
- CAPEC descrive schemi di attacco, non singoli bug.
- Nelle injection, il problema e' l'input utente usato in un contesto in cui puo' essere interpretato come codice o comando.
- XSS colpisce il browser della vittima; SQL injection colpisce la query eseguita verso il database.

## Fonti

- SRC-007

