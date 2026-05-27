# Risposte Esame Media Lunghezza

## Q-INTRO-001 - Come valuto la giusta difesa?

> [!Question]
> Come valuto la giusta difesa?

### Risposta da esame

La difesa va valutata a partire dal rischio, non solo dalla presenza astratta di vulnerabilita'. In sicurezza esiste un attaccante intenzionale che cerca strade alternative per violare la security policy, quindi bisogna considerare valori da proteggere, minacce realistiche e vulnerabilita' sfruttabili. La CIA Triad aiuta a classificare gli obiettivi: confidenzialita', integrita' e disponibilita'. La scelta della difesa deve partire dagli elementi a rischio piu' alto, secondo l'idea `Rischio = Vulnerabilita' x Minacce x Valori`, bilanciando sicurezza, costo e usabilita'.

### Punti chiave da ricordare

- CIA Triad.
- Analisi del rischio.
- Compromesso sicurezza/usabilita'.

### Collegamenti KB

- [[CIA_Triad_DAD]]
- [[Analisi_Rischio]]

### Fonti

- SRC-001
- SRC-009

## Q-CRYPTO-001 - Simmetrica vs asimmetrica

> [!Question]
> Differenza tra crittografia simmetrica e asimmetrica e relazione tra numero di chiavi e utenti.

### Risposta da esame

Nella crittografia simmetrica la stessa chiave e' condivisa da una coppia di utenti e viene usata sia per cifrare sia per decifrare. E' efficiente, ma pone un problema di distribuzione: per `n` utenti che devono comunicare privatamente a coppie servono `n(n-1)/2` chiavi. Nella crittografia asimmetrica ogni utente ha una coppia di chiavi, una pubblica e una privata; con `n` utenti servono `n` coppie. L'asimmetrica semplifica distribuzione delle chiavi, autenticazione e firme digitali, ma e' piu' costosa computazionalmente.

### Punti chiave da ricordare

- Simmetrica: una chiave condivisa per coppia.
- Asimmetrica: coppia pubblica/privata per utente.
- Numero chiavi: `n(n-1)/2` contro `n` coppie.

### Collegamenti KB

- [[Crittografia_Simmetrica]]
- [[Crittografia_Asimmetrica]]

### Fonti

- SRC-002
- SRC-003
- SRC-009
- SRC-010

## Q-CRYPTO-002 - Chiave pubblica e firme digitali

> [!Question]
> Spiega il funzionamento della crittografia a chiave pubblica e il suo uso per firme digitali.

### Risposta da esame

La crittografia a chiave pubblica usa una coppia di chiavi: la chiave pubblica puo' essere distribuita, mentre la chiave privata resta segreta. Un dato cifrato con una chiave puo' essere verificato o decifrato solo con la chiave corrispondente, secondo l'uso previsto dall'algoritmo. Per una firma digitale, il mittente usa la propria chiave privata per firmare un digest del messaggio; il destinatario usa la chiave pubblica del mittente per verificare la firma. Questo fornisce integrita', autenticita' e non-ripudio, ma non confidenzialita' se il messaggio viene inviato in chiaro.

### Punti chiave da ricordare

- Chiave pubblica distribuita, privata segreta.
- Firma: privata del mittente.
- Verifica: pubblica del mittente.

### Collegamenti KB

- [[Crittografia_Asimmetrica]]
- [[Firme_Digitali_Message_Digest]]

### Fonti

- SRC-003
- SRC-009
- SRC-011

## Q-CRYPTO-003 - Firma efficiente con message digest

> [!Question]
> Step per inviare e verificare un file firmato usando crittografia asimmetrica e message digest.

### Risposta da esame

L'utente A calcola il digest del file `F`, firma il digest con la propria chiave privata `A_priv` e invia a B il file insieme alla firma. B calcola a sua volta il digest del file ricevuto, verifica la firma usando la chiave pubblica di A e confronta i due digest. Se coincidono, il file ricevuto corrisponde al file firmato e la firma e' compatibile con la chiave privata di A. Firmare il digest e' efficiente perche' il digest ha dimensione fissa anche quando il file e' grande.

### Punti chiave da ricordare

- Hash del file.
- Firma del digest con chiave privata.
- Verifica con chiave pubblica.

### Collegamenti KB

- [[Firme_Digitali_Message_Digest]]
- [[Hashing_Message_Digest]]

### Fonti

- SRC-003
- SRC-009

## Q-CRYPTO-004 - Challenge/response

> [!Question]
> Challenge/response con chiave asimmetrica.

### Risposta da esame

In un protocollo challenge/response il verificatore invia una challenge, di solito un nonce, e il reclamante risponde con un valore calcolato crittograficamente. Con chiave asimmetrica, la risposta dimostra il possesso della chiave privata senza trasmetterla. Il nonce deve cambiare a ogni sessione per impedire replay. Nei protocolli bidirezionali bisogna includere identita' e contesto nei messaggi, altrimenti sono possibili reflection o relay attack, come mostrato dal caso Needham-Schroeder.

### Punti chiave da ricordare

- Challenge = nonce.
- Response crittografica.
- Identita' nei messaggi contro reflection attack.

### Collegamenti KB

- [[Challenge_Response_Attacchi]]
- [[Needham_Schroeder]]

### Fonti

- SRC-004
- SRC-009

## Q-CRYPTO-005 - Funzione di hash

> [!Question]
> Cosa fa una funzione di hash? Che caratteristiche deve avere?

### Risposta da esame

Una funzione di hash produce un digest di dimensione fissa a partire da un messaggio di dimensione arbitraria. In ambito crittografico deve essere facile da calcolare, ma computazionalmente difficile da invertire. Deve inoltre rendere impraticabile trovare due messaggi diversi con lo stesso digest. Non bisogna dire che il digest identifica univocamente il messaggio in senso matematico assoluto: collisioni esistono teoricamente, ma devono essere computazionalmente impraticabili.

### Punti chiave da ricordare

- Digest a dimensione fissa.
- One-way.
- Collision resistance.

### Collegamenti KB

- [[Hashing_Message_Digest]]

### Fonti

- SRC-003
- SRC-009

## Q-CRYPTO-006 - DES non sicuro

> [!Question]
> Perche' DES non e' piu' considerato sicuro? Quali modi di utilizzo migliorano la sicurezza?

### Risposta da esame

DES non e' piu' considerato sicuro soprattutto per la dimensione effettiva della chiave, 56 bit, ormai troppo piccola contro attacchi di forza bruta pratici. Triple DES aumenta la sicurezza applicando DES piu' volte con chiavi diverse, ma e' una soluzione storica e meno efficiente. AES e' lo standard moderno, supporta chiavi piu' lunghe e offre sicurezza ed efficienza migliori.

### Punti chiave da ricordare

- DES: chiave effettiva 56 bit.
- Triple DES: rafforzamento storico.
- AES: alternativa moderna.

### Collegamenti KB

- [[DES_TripleDES_AES]]

### Fonti

- SRC-002
- SRC-009

## Q-SO-001 - DAC vs MAC

> [!Question]
> Differenza tra DAC e MAC con esempio.

### Risposta da esame

Nel DAC il proprietario della risorsa puo' concedere o revocare accessi a propria discrezione; un esempio sono le ACL. Nel MAC, invece, la politica e' imposta dal sistema secondo regole non modificabili liberamente dagli utenti. Esempi di MAC sono Bell-LaPadula, orientato alla confidenzialita', e Biba, orientato all'integrita'. La differenza centrale e' quindi chi controlla la politica: il proprietario nel DAC, il sistema nel MAC.

### Punti chiave da ricordare

- DAC: discrezione del proprietario.
- MAC: politica imposta dal sistema.
- Bell-LaPadula e Biba sono MAC.

### Collegamenti KB

- [[DAC_MAC]]
- [[Bell_LaPadula]]
- [[Biba]]

### Fonti

- SRC-005
- SRC-009

## Q-SO-002 - ACL e mediazione completa

> [!Question]
> Funzionamento di una ACL e concetto di mediazione completa.

### Risposta da esame

Una ACL associa a ogni oggetto protetto l'elenco dei soggetti autorizzati e dei diritti concessi, ad esempio lettura, scrittura o esecuzione. Quando un soggetto chiede accesso a una risorsa, il sistema consulta la ACL della risorsa e decide se autorizzare l'operazione. La mediazione completa e' il principio secondo cui ogni accesso a ogni oggetto deve essere controllato. In pratica puo' esserci un compromesso con efficienza, cache e handle gia' aperti, ma il principio resta un riferimento fondamentale per sistemi sicuri.

### Punti chiave da ricordare

- ACL associata all'oggetto.
- Diritti per utenti o gruppi.
- Ogni accesso dovrebbe essere controllato.

### Collegamenti KB

- [[ACL_Mediazione_Completa]]
- [[ACL_e_Bit_Protezione]]

### Fonti

- SRC-005
- SRC-009
- SRC-011

## Q-SO-003 - ACL a 9 bit Unix/Linux

> [!Question]
> Funzionamento di una ACL basata su 9 bit di protezione Unix/Linux.

### Risposta da esame

Nei sistemi Unix/Linux classici, i permessi sono rappresentati con 9 bit divisi in tre gruppi. I primi tre indicano lettura, scrittura ed esecuzione per l'owner; i successivi tre per il group; gli ultimi tre per gli altri utenti. E' una rappresentazione compatta dei diritti, ma meno flessibile di una ACL completa perche' distingue solo owner, gruppo e world.

### Punti chiave da ricordare

- Owner, group, others.
- Read, write, execute.
- Compatta ma poco espressiva.

### Collegamenti KB

- [[ACL_Mediazione_Completa]]
- [[ACL_e_Bit_Protezione]]

### Fonti

- SRC-005
- SRC-009

## Q-SO-004 - Bell-LaPadula con compartimenti

> [!Question]
> Bell-LaPadula esteso con compartimenti; dire se e' DAC o MAC.

### Risposta da esame

Bell-LaPadula e' un modello MAC orientato alla confidenzialita'. Nella versione estesa con compartimenti, un soggetto puo' leggere un oggetto solo se il suo livello domina quello dell'oggetto e se i compartimenti dell'oggetto sono sottoinsieme dei compartimenti del soggetto. Restano valide le regole no read up e no write down. Il modello e' MAC, non DAC, perche' la politica e' imposta dal sistema e non dalla discrezione del proprietario.

### Punti chiave da ricordare

- MAC, non DAC.
- Livello soggetto >= livello oggetto.
- Compartimenti oggetto sottoinsieme dei compartimenti soggetto.

### Collegamenti KB

- [[Bell_LaPadula_Compartimenti]]
- [[Bell_LaPadula]]

### Fonti

- SRC-005
- SRC-009
- SRC-010

## Q-NET-001 - Packet filter e IP spoofing

> [!Question]
> Packet filter e protezione da IP spoofing proveniente dall'esterno.

### Risposta da esame

Un packet filter controlla pacchetti in base a campi di header, come indirizzo IP sorgente/destinazione, porte e protocollo. Le regole sono applicate in ordine e possono permettere o bloccare il traffico. Per difendere una sottorete da IP spoofing esterno, il firewall deve scartare pacchetti che arrivano dall'interfaccia esterna ma dichiarano come sorgente un indirizzo appartenente alla rete interna. Un pacchetto del genere e' incoerente con la topologia e va bloccato.

### Punti chiave da ricordare

- Filtra su header.
- Regole permit/deny.
- Anti-spoofing: bloccare sorgenti interne sull'interfaccia esterna.

### Collegamenti KB

- [[Packet_Filtering]]
- [[Firewall_Architetture]]

### Fonti

- SRC-006
- SRC-009
- SRC-011

## Q-NET-002 - Packet filter vs application gateway

> [!Question]
> Differenze tra firewall packet filter e application gateway.

### Risposta da esame

Il packet filter opera a livelli bassi e decide usando header di rete e trasporto. E' efficiente e generale, ma non comprende davvero il contenuto applicativo. L'application gateway e' un proxy applicativo: termina o intermedia la comunicazione e controlla il protocollo applicativo con maggiore consapevolezza semantica. Offre controlli piu' profondi, ma e' piu' costoso, specifico e complesso.

### Punti chiave da ricordare

- Packet filter: header.
- Application gateway: proxy applicativo.
- Trade-off tra efficienza e controllo semantico.

### Collegamenti KB

- [[Firewall_Architetture]]
- [[Application_Gateway_DMZ]]

### Fonti

- SRC-006
- SRC-009

## Q-NET-003 - Screened subnet

> [!Question]
> Che cos'e' una screened subnet?

### Risposta da esame

Una screened subnet e' un'architettura di rete che separa i servizi esposti dalla rete interna usando filtri e segmentazione. L'idea e' creare una zona intermedia controllata, cosi' un host pubblico compromesso non abbia accesso diretto alla rete interna. E' collegata al concetto di DMZ e rafforza la difesa perimetrale.

### Punti chiave da ricordare

- Segmentazione.
- Zona intermedia.
- Protezione della rete interna.

### Collegamenti KB

- [[Firewall_Architetture]]
- [[Application_Gateway_DMZ]]

### Fonti

- SRC-006
- SRC-009

## Q-NET-004 - DMZ

> [!Question]
> Che cos'e' una DMZ?

### Risposta da esame

Una DMZ e' una rete separata che ospita servizi esposti verso l'esterno, come web server o mail gateway. Serve a evitare che un servizio pubblico stia direttamente nella rete interna. I firewall regolano il traffico tra Internet, DMZ e rete interna, riducendo l'impatto di una compromissione del servizio esposto.

### Punti chiave da ricordare

- Rete separata.
- Servizi pubblici.
- Isolamento dalla rete interna.

### Collegamenti KB

- [[Application_Gateway_DMZ]]
- [[Firewall_Architetture]]

### Fonti

- SRC-006
- SRC-009

## Q-NET-005 - Pacchetto IP con TLS

> [!Question]
> Struttura di un pacchetto IP trasmesso usando SSL/TLS e protezione ottenuta.

### Risposta da esame

TLS sta sopra TCP. La struttura concettuale e': header IP, header TCP, record TLS e dati applicativi protetti. TLS cifra e autentica i dati applicativi secondo la cipher suite negoziata, ma lascia visibili header IP e TCP, quindi indirizzi IP e porte non sono nascosti. HTTPS e' HTTP trasportato dentro TLS.

### Punti chiave da ricordare

- TLS sopra TCP.
- Protegge dati applicativi.
- IP e TCP restano visibili.

### Collegamenti KB

- [[TLS_Struttura_Pacchetto]]
- [[TLS_HTTPS]]

### Fonti

- SRC-006
- SRC-009

## Q-NET-006 - IPsec tunnel mode

> [!Question]
> Struttura di un pacchetto IP con IPsec in modalita' tunneling e protezione ottenuta.

### Risposta da esame

In tunnel mode IPsec incapsula l'intero pacchetto IP originale dentro un nuovo pacchetto IP. Con ESP, la struttura concettuale e': nuovo header IP esterno, header ESP, pacchetto IP originale protetto, trailer/autenticazione ESP. Il nuovo header serve per instradare il tunnel; l'header IP originale e il payload originale sono protetti. Questa modalita' e' tipica delle VPN tra gateway e offre maggiore protezione dei metadati originali rispetto al transport mode.

### Punti chiave da ricordare

- Incapsula l'intero pacchetto IP originale.
- Nuovo header IP esterno.
- Tipico VPN gateway-to-gateway.

### Collegamenti KB

- [[IPsec_Modalita_Trasporto_Tunnel]]
- [[IPsec_VPN]]

### Fonti

- SRC-006
- SRC-009

## Q-NET-007 - IPsec transport mode

> [!Question]
> Struttura di un pacchetto IP con IPsec in modalita' trasporto e protezione ottenuta.

### Risposta da esame

In transport mode IPsec non incapsula l'intero pacchetto IP originale. L'header IP originale resta visibile e viene usato per l'instradamento; IPsec protegge il payload del pacchetto IP, cioe' tipicamente segmento TCP/UDP e dati applicativi. Con ESP si ottengono confidenzialita' del payload e integrita'/autenticazione secondo configurazione. A differenza del tunnel mode, gli indirizzi IP originali restano visibili.

### Punti chiave da ricordare

- Header IP originale visibile.
- Payload IP protetto.
- Differenza chiave rispetto al tunnel mode.

### Collegamenti KB

- [[IPsec_Modalita_Trasporto_Tunnel]]

### Fonti

- SRC-006
- SRC-010

## Q-APP-001 - XSS

> [!Question]
> Funzionamento di un attacco XSS.

### Risposta da esame

XSS avviene quando input malevolo viene inserito in una pagina e interpretato come codice dal browser della vittima. Nel persistent XSS il payload viene salvato sul server e servito a piu' utenti; nel reflected XSS viene incluso nella richiesta e riflesso nella risposta; nel DOM-based XSS e' il codice client a inserire input non fidato nel DOM. Le difese principali sono output encoding contestuale, sanitizzazione quando serve, validazione input e controlli come CSP e cookie `HttpOnly`/`SameSite`.

### Punti chiave da ricordare

- Browser come vittima.
- Persistent, reflected, DOM-based.
- Encoding contestuale.

### Collegamenti KB

- [[Cross_Site_Scripting_XSS]]
- [[Injection_Improper_Neutralization]]

### Fonti

- SRC-007
- SRC-009

## Q-APP-002 - SQL injection

> [!Question]
> Funzionamento di un attacco SQL injection.

### Risposta da esame

SQL injection e' un attacco di injection in cui input non fidato modifica la semantica di una query SQL costruita male, spesso tramite concatenazione di stringhe. L'attaccante puo' bypassare autenticazione, leggere dati sensibili, modificare o cancellare dati, o invocare funzioni del DBMS se i privilegi lo permettono. La difesa principale sono prepared statements e query parametrizzate, che separano codice SQL e dati. Validation, escaping e least privilege dell'utente DB sono difese complementari.

### Punti chiave da ricordare

- Query concatenata = rischio.
- Prepared statements.
- Least privilege DB.

### Collegamenti KB

- [[SQL_Injection]]
- [[Contromisure_Injection]]

### Fonti

- SRC-007
- SRC-009
- SRC-010

## Q-APP-003 - Buffer overflow

> [!Question]
> Funzionamento di un attacco buffer overflow.

### Risposta da esame

Un buffer overflow e' una scrittura oltre i limiti di un buffer. In C puo' sovrascrivere memoria adiacente nello stack frame, come variabili locali, base pointer o return address. Se l'attaccante controlla i dati scritti, puo' alterare il flusso di esecuzione e tentare di raggiungere shellcode, spesso usando un NOP sled. Su heap, la corruzione puo' coinvolgere strutture dati o puntatori a funzione. Difese moderne come stack canary, ASLR e NX/DEP rendono l'attacco classico piu' difficile ma non eliminano la categoria di vulnerabilita'.

### Punti chiave da ricordare

- Scrittura fuori limite.
- Return address e shellcode.
- Canary, ASLR, NX/DEP.

### Collegamenti KB

- [[Buffer_Overflow]]
- [[Contromisure_Buffer_Overflow]]

### Fonti

- SRC-008
- SRC-009
- SRC-011

