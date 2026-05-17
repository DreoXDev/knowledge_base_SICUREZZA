# NotebookLM Source Pack

Questo file raccogliera' progressivamente una versione compatta dei contenuti piu' importanti della knowledge base.

> [!Warning]
> Non aggiungere contenuti non supportati dalle fonti. Ogni sezione deve indicare da quali note o source ID deriva.

## Stato

Il source pack contiene il primo nucleo fondativo derivato da `SRC-001 - 00.Intro.pdf`.

## Contenuti principali

- La seconda parte del corso riguarda sicurezza informatica, con focus su crittografia, sicurezza nelle reti, sicurezza nei sistemi operativi e sicurezza nelle applicazioni.
- La distinzione tra safety engineering e security engineering è fondativa: la safety previene danni catastrofici dovuti a malfunzionamenti, mentre la security previene, difende e recupera da attacchi intenzionali.
- Una vulnerabilità può essere vista come una via alternativa non prevista dal progettista.
- La CIA Triad descrive gli obiettivi principali della sicurezza: confidenzialità, integrità e disponibilità.
- Il modello DAD descrive attacchi che compromettono la CIA Triad: Disclosure, Alteration e Destruction.
- L'analisi del rischio collega vulnerabilità, minacce e valori sensibili per decidere dove investire risorse di sicurezza.
- La crittografia protegge messaggi e dati tramite schemi di cifratura, ma non risolve da sola tutti i problemi di sicurezza: implementazione, gestione delle chiavi e contesto operativo restano decisivi.
- Gli schemi di cifratura trasformano plaintext in ciphertext tramite una chiave e devono permettere la decifratura corretta del messaggio da parte del destinatario autorizzato.
- La crittografia simmetrica usa la stessa chiave per cifrare e decifrare. È efficiente e molto utile per la confidenzialità, ma ha limiti su scambio delle chiavi, non-ripudio e attribuzione verso terze parti.
- DES è uno standard storico oggi debole per la dimensione della chiave; Triple DES aumenta la sicurezza ripetendo DES; AES è lo standard simmetrico moderno con blocchi da 128 bit e chiavi da 128, 192 o 256 bit.
- La crittografia asimmetrica usa una chiave pubblica e una chiave privata. Permette confidenzialità verso il proprietario della chiave privata e firme digitali verificabili con la chiave pubblica.
- RSA è un algoritmo asimmetrico basato sulla difficoltà di fattorizzare numeri molto grandi. È utile per chiavi, firme e piccole quantità di dati, ma è meno efficiente degli algoritmi simmetrici.
- Gli algoritmi di hashing producono message digest utili per l'integrità. MD5 e SHA1 sono contenuti storici del corso e non vanno trattati come scelte moderne per sicurezza forte; SHA2 è più robusto.
- La cifratura ibrida combina AES/DES per cifrare i dati e RSA per proteggere la chiave di sessione.
- Certificati X.509 e PKI risolvono il problema di associare in modo fidato una chiave pubblica a un'identità.
- La crittografia non è sufficiente se il threat model è incompleto: bug, dispositivi, protocolli, utenti e social engineering restano parte del rischio.
- La sicurezza nei sistemi operativi parte da autenticazione e controllo degli accessi: prima si verifica l'identità del soggetto, poi si decide se può accedere a una risorsa.
- L'autenticazione può basarsi su conoscenza, possesso o caratteristiche biometriche. Le password sono un caso di autenticazione per conoscenza.
- Le password non dovrebbero essere memorizzate in chiaro: si usano hash e salt per ridurre i danni in caso di compromissione del password file.
- Challenge/response permette di dimostrare la conoscenza di un segreto senza trasmetterlo direttamente. Il nonce impedisce replay attack.
- Reflection attack e parallel sessions attack mostrano che i protocolli devono legare crittograficamente messaggi, identità e contesto.
- Needham-Schroeder è un protocollo di autenticazione reciproca a chiave pubblica; la versione originale è vulnerabile se i messaggi non includono identità sufficienti.
- Il controllo degli accessi nei sistemi operativi stabilisce quali soggetti possono usare quali oggetti protetti e con quali diritti.
- ACL e bit Unix/Linux sono meccanismi per rappresentare diritti di accesso. Le ACL sono più flessibili; i bit Unix/Linux sono più compatti.
- Gli obiettivi del controllo accessi includono mediazione completa, prevenzione di TOC/TOU, minimi privilegi e limitazione dei covert channels.
- DAC lascia discrezionalità al proprietario della risorsa; MAC impone politiche di sicurezza definite dal sistema.
- Bell-LaPadula è orientato alla confidenzialità: no-read-up e no-write-down.
- Biba è orientato all'integrità: no-write-up e no-read-down.
- Compartimenti e need-to-know aggiungono vincoli semantici oltre ai livelli di sicurezza.
- La Muraglia Cinese gestisce conflitti di interesse tra dataset aziendali concorrenti.
- Auditing e IDS servono a registrare e analizzare eventi rilevanti per individuare intrusioni o violazioni.
- Un sistema operativo trusted deve applicare minimi privilegi, mediazione completa, deny by default, auditing, separazione utenti e semplicità d'uso.
- La sicurezza nelle reti estende CIA, autenticazione e controllo accessi a comunicazioni che attraversano nodi intermedi e protocolli diversi.
- Sniffing e wiretap passivo compromettono la confidenzialità; wiretap attivo, spoofing e creazione di traffico compromettono integrità; DoS e DDoS compromettono disponibilità.
- ARP poisoning sfrutta il comportamento stateless di ARP per inserire associazioni IP-MAC false e deviare traffico.
- Spoofing, phishing, pharming, fake public key identity e session hijacking sono attacchi basati su falsificazione o abuso di fiducia.
- Firewall, packet filtering, application gateway e DMZ sono difese perimetrali e architetturali.
- TLS protegge dati applicativi sopra TCP/IP; IPsec protegge traffico a livello IP ed è usato per VPN.

## Definizioni importanti

- Safety engineering: prevenzione di danni catastrofici causati dal cattivo funzionamento di un sistema informatico.
- Security engineering: prevenzione, difesa e recupero rispetto ad attacchi che possono compromettere i valori rappresentati da un sistema informatico.
- Confidenzialità: protezione dell'accesso alle informazioni da parte di soggetti non autorizzati.
- Integrità: protezione da modifiche, cancellazioni, creazioni o manomissioni non autorizzate.
- Disponibilità: garanzia che utenti autorizzati possano usare risorse e servizi quando necessario.
- Rischio: possibilità di perdita o danno, modellabile come combinazione di vulnerabilità, minacce e valori.
- Plaintext: messaggio in chiaro prima della cifratura.
- Ciphertext: messaggio cifrato prodotto da un algoritmo crittografico.
- Forza bruta: attacco che prova tutte le chiavi o configurazioni possibili.
- Crittoanalisi: studio degli attacchi contro sistemi crittografici.
- Algoritmo simmetrico: algoritmo che usa la stessa chiave per cifrare e decifrare.
- Crittografia asimmetrica: classe di algoritmi con chiave pubblica e chiave privata.
- Message digest: riassunto crittografico di un messaggio.
- Firma digitale: meccanismo che garantisce integrità, autenticità e non-ripudio tramite chiave privata e verifica con chiave pubblica.
- PKI: infrastruttura per gestire certificati, chiavi pubbliche e autorità di certificazione.
- Threat model: descrizione di minacce, attaccanti, capacità e assunzioni considerate.
- Autenticazione: verifica che un soggetto sia davvero chi dichiara di essere.
- Salt: valore casuale associato a una password prima del calcolo dell'hash.
- Nonce: valore usato una sola volta in un protocollo.
- Replay attack: riuso di un messaggio valido intercettato.
- Reflection attack: riuso riflesso di una risposta valida in una sessione parallela.
- Needham-Schroeder: protocollo di autenticazione reciproca basato su chiave pubblica e nonce.
- Access Control List: lista che associa soggetti o gruppi a diritti su una risorsa.
- DAC: modello in cui il proprietario concede o modifica diritti a propria discrezione.
- MAC: modello in cui il sistema impone politiche di accesso non modificabili liberamente dagli utenti.
- Bell-LaPadula: modello per confidenzialità basato su no-read-up e no-write-down.
- Biba: modello per integrità basato su no-write-up e no-read-down.
- Covert channel: canale indiretto usato per trasferire informazioni a soggetti non autorizzati.
- IDS: sistema che analizza dati di audit per rilevare compromissioni o violazioni.
- Sniffing: intercettazione e analisi di pacchetti di rete.
- ARP poisoning: inserimento di associazioni IP-MAC false nella ARP cache.
- Spoofing: falsificazione di identità o indirizzi.
- Firewall: componente che controlla traffico tra reti secondo una security policy.
- DMZ: segmento separato che ospita servizi esposti pubblicamente.
- TLS: protocollo per proteggere privacy e integrità dei dati applicativi sopra TCP/IP.
- IPsec: meccanismo di sicurezza a livello IP per traffico tra host o gateway.
- VPN: connessione cifrata tra endpoint.

## Confronti importanti

- Safety vs security: la safety si concentra su danni accidentali o malfunzionamenti, la security su attacchi intenzionali e abusi.
- CIA vs DAD: la CIA Triad descrive cosa proteggere; DAD descrive famiglie di attacco contro quegli obiettivi.
- Crittografia simmetrica vs firma digitale: la simmetrica consente confidenzialità efficiente, ma non prova a terzi quale partecipante abbia generato un messaggio.
- DES vs AES: DES usa chiavi effettive da 56 bit ed è vulnerabile a forza bruta moderna; AES usa blocchi da 128 bit e chiavi più lunghe, ed è lo standard moderno.
- Simmetrica vs asimmetrica: la simmetrica è veloce ma richiede chiavi condivise; l'asimmetrica è più lenta ma rende pubblica una parte della chiave e supporta firme digitali.
- Hashing vs cifratura: l'hashing produce un digest e non è reversibile; la cifratura deve permettere il recupero del plaintext.
- Certificati vs chiavi pubbliche nude: una chiave pubblica da sola non prova l'identità del proprietario; il certificato lega chiave e identità tramite una CA.
- Autenticazione vs controllo accessi: l'autenticazione stabilisce l'identità, il controllo accessi decide i permessi.
- Password hash vs password in chiaro: l'hash riduce l'esposizione del segreto, ma deve essere accompagnato da salt e protezione del file password.
- Replay vs reflection attack: il replay riusa un messaggio vecchio; la reflection sfrutta una sessione parallela e la simmetria del protocollo.
- Bell-LaPadula vs Biba: Bell-LaPadula protegge la confidenzialità; Biba protegge l'integrità.
- DAC vs MAC: DAC è flessibile e delega al proprietario; MAC è più rigido e centralizzato.
- Multi-level vs multi-lateral: multi-level usa livelli di sicurezza; multi-lateral usa raggruppamenti semantici o conflitti di interesse.
- Sniffing vs spoofing: lo sniffing osserva traffico; lo spoofing falsifica identità o indirizzi.
- Wiretap passivo vs attivo: il passivo osserva; l'attivo modifica, crea, elimina o reindirizza traffico.
- Packet filter vs application gateway: il primo controlla header e porte; il secondo interpreta dati applicativi.
- TLS vs IPsec: TLS protegge applicazioni sopra TCP; IPsec protegge traffico a livello IP.

## Domande utili per il ripasso

- Spiega la differenza tra safety engineering e security engineering.
- Definisci CIA Triad e modello DAD.
- Che cosa significa considerare una vulnerabilità come via alternativa?
- Perché l'analisi del rischio è necessaria nell'implementazione della sicurezza?
- Perché la crittografia non è una soluzione universale?
- Quali sono le componenti di uno schema di cifratura?
- Perché la crittografia simmetrica non garantisce non-ripudio verso terze parti?
- Confronta DES, Triple DES e AES.
- Come funziona la crittografia asimmetrica?
- Perché RSA non viene usato per cifrare grandi quantità di dati?
- Come funziona una firma digitale basata su message digest?
- Quale problema risolve un certificato X.509?
- Perché un threat model incompleto può rendere insufficiente la crittografia?
- Qual è la differenza tra autenticazione e controllo degli accessi?
- Perché password file, hash e salt sono importanti?
- Come funziona challenge/response con nonce?
- Perché Needham-Schroeder originale è vulnerabile a parallel sessions attack?
- Confronta ACL e bit Unix/Linux.
- Spiega DAC e MAC.
- Confronta Bell-LaPadula e Biba.
- Che cosa sono covert channels e perché sono difficili da eliminare?
- Che cosa sono auditing e IDS?
- Spiega sniffing, ARP poisoning e spoofing.
- Qual è la differenza tra DoS e DDoS?
- Confronta firewall packet filter e application gateway.
- Confronta TLS e IPsec.
