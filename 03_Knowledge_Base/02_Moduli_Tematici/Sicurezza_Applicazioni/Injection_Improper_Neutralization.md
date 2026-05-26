# Injection e Improper Neutralization

Improper neutralization e' una famiglia di weakness in cui input non fidato entra in un contesto dove puo' essere interpretato in modo pericoloso, perche' non e' stato trasformato, validato o codificato correttamente.

## Problema

Il dato utente non resta "dato": diventa parte di HTML, JavaScript, SQL, comandi o altri linguaggi interpretabili. L'attaccante sfrutta questa confusione per cambiare il significato dell'output o del comando.

## Mapping CWE/CAPEC

- CWE-707: Improper Neutralization.
- CWE-74: Improper Neutralization of Special Elements in Output Used by a Downstream Component.
- CWE-79: Cross-Site Scripting.
- CWE-89: SQL Injection.
- CWE-943: Improper Neutralization in Data Query Logic.
- CAPEC-152: Inject Unexpected Items.
- CAPEC-242, CAPEC-63, CAPEC-248, CAPEC-66: pattern collegati a injection e manipolazione di query/comandi.

## Validation, sanitization, encoding

- Validation: decide se un input e' accettabile rispetto a formato, tipo e range.
- Sanitization: modifica o rimuove parti pericolose.
- Encoding/escaping: rappresenta caratteri speciali in modo che siano trattati come dati nel contesto di output.

> [!Warning]
> La validazione da sola non sostituisce l'encoding contestuale: un valore valido per l'applicazione puo' comunque contenere caratteri speciali per HTML, JavaScript o SQL.

## Collegamenti

- [[Cross_Site_Scripting_XSS]]
- [[SQL_Injection]]
- [[Contromisure_Injection]]
- [[CWE_CAPEC_CVE]]

## Fonti

- SRC-007

