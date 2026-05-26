# Sicurezza Applicazioni - Context AI

## Sintesi compatta

Il modulo "Sicurezza nelle applicazioni" integra due fonti: SRC-007 e SRC-008. La parte 1 introduce lessico, tassonomie e attacchi injection in web application; la parte 2 copre buffer manipulation, null pointer dereference nel kernel e secure coding Java.

## Concetti principali

- Security policy: regole di protezione delle risorse.
- Weakness: tipo di difetto.
- Vulnerabilita': occorrenza concreta sfruttabile.
- Exploit: tecnica concreta.
- Attack pattern: schema generale di attacco.
- Countermeasure: prevenzione, mitigazione, detection o correzione.
- CWE: weakness.
- CAPEC: pattern di attacco.
- CVE: vulnerabilita' concrete.
- Improper neutralization: input non fidato usato in contesti interpretabili.
- XSS: input interpretato come script dal browser.
- SQL injection: input che modifica query SQL.
- Buffer overflow: scrittura fuori limite.
- Buffer overread: lettura fuori limite.
- Null pointer dereference: uso di NULL come puntatore valido.

## Differenze da non confondere

- Weakness non e' vulnerabilita': la prima e' categoria, la seconda e' occorrenza concreta.
- CAPEC non e' CVE: CAPEC descrive pattern, CVE descrive vulnerabilita' note.
- XSS colpisce il browser; SQL injection colpisce query e database.
- Buffer overflow scrive fuori limite; buffer overread legge fuori limite.
- Canary, ASLR ed executable space protection mitigano exploit, ma non correggono il bug.

## Esempi principali

- Query Java costruita concatenando stringhe: vulnerabile a SQL injection.
- `PreparedStatement`: separa query e parametri.
- `gets`: funzione C pericolosa perche' non verifica la dimensione del buffer.
- Heartbleed: lunghezza dichiarata maggiore del payload reale.
- CVE-2009-2692: puntatore a funzione NULL in `sock_sendpage`.
- CVE-2009-1897: null check dopo l'uso del puntatore in TUN/TAP.

## Domande probabili

1. Differenza tra weakness, vulnerabilita', exploit e attacco.
2. Differenza tra CWE, CAPEC e CVE.
3. Improper neutralization.
4. XSS e varianti.
5. SQL injection e prepared statements.
6. Buffer overflow e return address.
7. Canary, ASLR, executable space protection.
8. Heartbleed come buffer overread.
9. Null pointer dereference nel kernel.
10. CVE-2009-2692 e CVE-2009-1897.
11. Java secure coding guidelines e SpotBugs.

## Note principali

- [[Sicurezza_Applicazioni]]
- [[Cross_Site_Scripting_XSS]]
- [[SQL_Injection]]
- [[Buffer_Overflow]]
- [[Buffer_Overread_Heartbleed]]
- [[Null_Pointer_Dereference]]
- [[Java_Secure_Coding_Guidelines]]

