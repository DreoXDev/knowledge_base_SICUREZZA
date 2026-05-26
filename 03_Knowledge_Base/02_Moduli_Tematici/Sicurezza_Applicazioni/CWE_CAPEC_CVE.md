# CWE, CAPEC, CVE

Le tassonomie servono a dare nomi stabili a difetti, schemi di attacco e vulnerabilita' note. Sono utili per studio, analisi e comunicazione, ma non sono perfette: possono essere non ortogonali, imprecise e talvolta confondere mistake e fault.

## Organizzazioni e cataloghi

- MITRE mantiene CWE, CAPEC, CVE e ATT&CK.
- NIST mantiene NVD, il National Vulnerability Database.
- WASC propone classificazioni per web application security.
- OWASP mantiene, tra le altre risorse, OWASP Top Ten.

## Confronto essenziale

| Strumento | Cosa descrive | Esempio | Utilita' |
|---|---|---|---|
| CWE | Weakness | CWE-79 | Capire difetti da evitare |
| CAPEC | Pattern di attacco | CAPEC-63 | Capire come una weakness viene sfruttata |
| CVE | Vulnerabilita' concreta | CVE-2014-0160 | Identificare vulnerabilita' note |
| NVD | Database vulnerabilita' | CVSS, metadata | Consultazione e scoring |

## CWE

CWE cataloga weakness. Nelle slide compaiono categorie della research concept view come:

- CWE-284: improper access control;
- CWE-435: improper interaction between multiple entities;
- CWE-664: improper control of a resource through its lifetime;
- CWE-682: incorrect calculation;
- CWE-691: insufficient control flow management;
- CWE-693: protection mechanism failure;
- CWE-697: incorrect comparison;
- CWE-703: improper check or handling of exceptional conditions;
- CWE-707: improper neutralization;
- CWE-710: improper adherence to coding standards.

## CAPEC

CAPEC cataloga schemi di attacco. Per meccanismo di attacco le slide citano gruppi come CAPEC-118, CAPEC-152, CAPEC-156, CAPEC-172, CAPEC-210, CAPEC-223, CAPEC-225, CAPEC-255 e CAPEC-262.

## CVE e NVD

CVE identifica vulnerabilita' concrete in software noti. NVD aggiunge metadati, scoring e informazioni di consultazione. Heartbleed, ad esempio, e' CVE-2014-0160.

## Collegamenti

- [[Glossario_Sicurezza_Applicazioni]]
- [[Injection_Improper_Neutralization]]
- [[Buffer_Manipulation]]
- [[CWE_vs_CAPEC_vs_CVE]]

## Fonti

- SRC-007
- SRC-008

