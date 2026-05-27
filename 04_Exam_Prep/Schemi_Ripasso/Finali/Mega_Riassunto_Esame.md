# Mega Riassunto - Sicurezza e Affidabilita

> [!Info]
> Riassunto finale del secondo parziale. Da usare dopo aver letto le note KB atomiche.

## 1. Introduzione alla security

La security riguarda attacchi intenzionali contro valori protetti, mentre la safety riguarda danni causati da malfunzionamenti. Una vulnerabilita' e' una via alternativa che permette di violare una policy. La [[CIA_Triad_DAD]] organizza gli obiettivi in confidenzialita', integrita' e disponibilita'; il modello DAD descrive disclosure, alteration e destruction. La [[Analisi_Rischio]] guida le difese: rischio come combinazione di vulnerabilita', minacce e valori.

> [!Question] Domande tipiche
> - Differenza tra safety e security.
> - Definire CIA Triad e DAD.
> - Come si valuta la giusta difesa?

## 2. Crittografia

La [[Crittografia_Introduzione]] protegge dati tramite algoritmi, chiavi e assunzioni sul threat model. La [[Crittografia_Simmetrica]] usa una chiave condivisa ed e' efficiente, ma ha problemi di distribuzione; [[DES_TripleDES_AES]] mostra l'evoluzione da DES a Triple DES e AES. La [[Crittografia_Asimmetrica]] usa coppie pubblica/privata, abilita confidenzialita' verso il destinatario e firme digitali. [[RSA]] e' l'esempio centrale. [[Hashing_Message_Digest]] produce digest a dimensione fissa; [[Firme_Digitali_Message_Digest]] combina digest e chiave privata per integrita', autenticita' e non-ripudio. [[Certificati_X509_PKI]] risolve il problema della fiducia nelle chiavi pubbliche.

> [!Question] Domande tipiche
> - Simmetrica vs asimmetrica e numero di chiavi.
> - Firma digitale con message digest.
> - Perche' DES non e' piu' sicuro?

## 3. Sicurezza nei sistemi operativi

La sicurezza nei SO parte da [[Autenticazione]], password, salt e hashing. [[Challenge_Response_Attacchi]] chiarisce nonce, replay e reflection attack; [[Needham_Schroeder]] mostra perche' identita' e contesto nei messaggi contano. Il [[Controllo_Accessi_SO]] decide chi puo' usare cosa: [[ACL_Mediazione_Completa]] spiega ACL, bit Unix/Linux e mediazione completa. [[DAC_MAC]] distingue discrezione del proprietario e policy imposta dal sistema. [[Bell_LaPadula_Compartimenti]] e [[Biba]] sono modelli MAC, il primo per confidenzialita', il secondo per integrita'. Completano il quadro [[Covert_Channels]], [[Auditing_Intrusion_Detection]] e [[SO_Trusted_Principi]].

> [!Question] Domande tipiche
> - DAC vs MAC.
> - ACL e mediazione completa.
> - Bell-LaPadula con compartimenti.

## 4. Sicurezza nelle reti

Le reti ampliano la superficie d'attacco. [[Sniffing]], [[ARP_Poisoning_Spoofing]], [[Wiretap_Attivo_Passivo]] e [[Spoofing_Phishing_Pharming]] coprono intercettazione e impersonificazione. [[DoS_DDoS_SYN_Flood]] tratta disponibilita'. Le difese principali sono [[Difese_Rete_Firewall]], [[Packet_Filtering]], [[Firewall_Architetture]] e [[Application_Gateway_DMZ]]. [[TLS_Struttura_Pacchetto]] spiega che TLS protegge dati applicativi sopra TCP; [[IPsec_Modalita_Trasporto_Tunnel]] distingue transport e tunnel mode; [[IPsec_VPN]] collega IPsec alle VPN.

> [!Question] Domande tipiche
> - Packet filter e IP spoofing.
> - Packet filter vs application gateway.
> - TLS vs IPsec; IPsec transport vs tunnel.

## 5. Sicurezza nelle applicazioni

Il modulo applicazioni parte da [[Glossario_Sicurezza_Applicazioni]]: weakness, vulnerabilita', exploit, attacco e contromisura sono livelli diversi. [[CWE_CAPEC_CVE]] separa weakness, pattern e vulnerabilita' concrete. Le web application introducono input, HTTP, HTML, form e scripting: [[Injection_Improper_Neutralization]] spiega il problema comune a [[Cross_Site_Scripting_XSS]] e [[SQL_Injection]]. La parte memoria copre [[Buffer_Manipulation]], [[Buffer_Overflow]], [[Buffer_Overread_Heartbleed]] e [[Null_Pointer_Dereference]], con casi come [[CVE_2009_2692]] e [[CVE_2009_1897]]. [[Java_Secure_Coding_Guidelines]] chiude con prevenzione tramite coding rules e static analysis.

> [!Question] Domande tipiche
> - XSS e varianti.
> - SQL injection e prepared statements.
> - Buffer overflow, Heartbleed e null pointer dereference.

