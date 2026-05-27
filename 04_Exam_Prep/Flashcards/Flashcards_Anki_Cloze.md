# Flashcards Anki Cloze - Domande Note

La giusta difesa si valuta a partire dal {{c1::rischio}}, considerando {{c2::vulnerabilita', minacce e valori}}.

La crittografia simmetrica richiede {{c1::n(n-1)/2}} chiavi per `n` utenti se ogni coppia deve comunicare privatamente.

Nella crittografia asimmetrica ogni utente possiede {{c1::una coppia di chiavi}}, una {{c2::pubblica}} e una {{c3::privata}}.

In una firma digitale efficiente si firma {{c1::il message digest}} del file con {{c2::la chiave privata del mittente}}.

La verifica di una firma digitale usa {{c1::la chiave pubblica del mittente}} e confronta {{c2::i digest}}.

In challenge/response il {{c1::nonce}} impedisce replay attack.

Nei protocolli challenge/response bidirezionali gli {{c1::identificativi}} aiutano a evitare reflection attack.

Una funzione di hash crittografica deve essere {{c1::one-way}} e {{c2::collision resistant}}.

DES e' debole soprattutto per la chiave effettiva da {{c1::56 bit}}.

Nel {{c1::DAC}} il proprietario concede diritti; nel {{c2::MAC}} la politica e' imposta dal sistema.

La mediazione completa richiede che {{c1::ogni accesso a ogni oggetto protetto}} sia controllato.

I permessi Unix/Linux classici sono tre gruppi {{c1::rwx}} per {{c2::owner, group, others}}.

Bell-LaPadula con compartimenti richiede che i compartimenti dell'oggetto siano {{c1::sottoinsieme}} dei compartimenti del soggetto.

Un packet filter anti-spoofing blocca pacchetti esterni con sorgente {{c1::appartenente alla rete interna}}.

TLS protegge {{c1::i dati applicativi}} ma lascia visibili {{c2::header IP e TCP}}.

IPsec tunnel mode protegge {{c1::l'intero pacchetto IP originale}} incapsulandolo in {{c2::un nuovo pacchetto IP}}.

IPsec transport mode protegge {{c1::il payload IP}} ma lascia visibile {{c2::l'header IP originale}}.

XSS puo' essere {{c1::persistent}}, {{c2::reflected}} o {{c3::DOM-based}}.

La difesa principale contro SQL injection sono {{c1::prepared statements/query parametrizzate}}.

Un buffer overflow su stack puo' sovrascrivere {{c1::il return address}} e alterare {{c2::il flusso di esecuzione}}.

Nel modello Bell-LaPadula la proprieta' semplice e' {{c1::no-read-up}}, mentre la proprieta' di confinamento e' {{c2::no-write-down}}.

Nel modello Biba la regola semplice e' {{c1::no-write-up}}, mentre la regola di confinamento e' {{c2::no-read-down}}.

TLS opera {{c1::sopra TCP}} e protegge {{c2::i dati applicativi}}.

IPsec opera a {{c1::livello IP}} e puo' lavorare in modalita' {{c2::transport}} o {{c3::tunnel}}.

In XSS la vittima principale e' {{c1::il browser dell'utente}}, mentre in SQL injection il contesto colpito e' {{c2::la query/database}}.
