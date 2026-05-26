# SRC-007 - Sicurezza applicazioni p1

> [!Info]
> Fonte originale: `01_Raw_Assets/slides/Sicurezza applicazioni parte 1.pdf`
> Stato: integrato nella KB
> Tipo: slide teoriche
> Modulo: Sicurezza nelle applicazioni

## Argomenti principali

- Introduzione alla sicurezza delle applicazioni.
- Glossario: security policy, weakness, vulnerabilita', exploit, attacco, attack pattern, attacker e countermeasure.
- Tassonomie e cataloghi: MITRE, NIST, WASC, OWASP, CWE, CAPEC, CVE, NVD, ATT&CK e OWASP Top Ten.
- Struttura delle applicazioni web: client/server, URL, DNS, HTTP, GET/POST, HTML, form, scripting server-side e client-side.
- Improper neutralization, XSS e SQL injection.

## Concetti chiave estratti

Le applicazioni sono bersagli naturali perche' espongono funzionalita' e risorse a utenti e reti. Un attacco puo' negare funzionalita', farle eseguire a utenti non autorizzati o accedere a risorse non concesse dalla security policy.

La fonte distingue con precisione weakness, vulnerabilita' ed exploit: la weakness e' il tipo di difetto, la vulnerabilita' e' l'occorrenza concreta sfruttabile, l'exploit e' la tecnica concreta di sfruttamento. CAPEC descrive schemi di attacco, CWE descrive weakness, CVE descrive vulnerabilita' concrete.

## Dettaglio per sezioni

### Glossario e attacchi

Gli attacchi possono essere attivi o passivi, interni o esterni, diretti o indiretti. Una countermeasure puo' eliminare, prevenire, mitigare o rilevare vulnerabilita', minacce o attacchi.

### Tassonomie

CWE include categorie come CWE-284, CWE-435, CWE-664, CWE-682, CWE-691, CWE-693, CWE-697, CWE-703, CWE-707 e CWE-710. CAPEC organizza pattern per meccanismo di attacco, tra cui injection, abuse of functionality, manipulation of resources, social engineering e altri gruppi. Le tassonomie sono utili ma non perfettamente ortogonali e talvolta confondono mistake e fault.

### Web application

Le slide usano HTTP, HTML e form come intermezzo concettuale per spiegare XSS e injection. GET e POST trasportano input utente; server-side scripting genera output dinamico; client-side scripting manipola il DOM nel browser.

### Injection, XSS, SQL injection

Improper neutralization indica il mancato trattamento di input non fidato prima dell'uso in un contesto interpretabile. XSS riguarda codice eseguito nel browser della vittima; SQL injection riguarda input che modifica query SQL. Le contromisure principali sono encoding/escaping contestuale, validation e prepared statements.

## Collegamenti alla KB

- [[Sicurezza_Applicazioni_Introduzione]]
- [[Glossario_Sicurezza_Applicazioni]]
- [[CWE_CAPEC_CVE]]
- [[Applicazioni_Web_HTTP_HTML]]
- [[Injection_Improper_Neutralization]]
- [[Cross_Site_Scripting_XSS]]
- [[SQL_Injection]]

## Possibili domande d'esame

- Spiega la differenza tra weakness, vulnerabilita', exploit e attacco.
- Spiega la differenza tra CWE, CAPEC e CVE.
- Che cos'e' improper neutralization?
- Spiega XSS e le varianti persistent, reflected e DOM-based.
- Perche' i prepared statement mitigano SQL injection?

## Flashcard derivate

- Weakness: tipo di difetto che puo' introdurre vulnerabilita'.
- Vulnerabilita': occorrenza concreta sfruttabile.
- Exploit: tecnica concreta di sfruttamento.
- CWE/CAPEC/CVE: weakness, attack pattern, vulnerabilita' concrete.
- XSS: input malevolo interpretato come codice dal browser.
- SQL injection: input che modifica una query SQL.

## Note di integrazione

La parte su web application e' marcata nella KB come supporto concettuale: serve soprattutto a capire il percorso dell'input utente fino al browser o al database.

