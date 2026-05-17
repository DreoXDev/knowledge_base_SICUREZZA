# Flashcards - Sicurezza Reti

## Fonte

- SRC-006

## Flashcard 1

**Domanda:** Perché la sicurezza nelle reti è più difficile del caso single-host?

**Risposta:**  
Perché un host in rete può essere raggiunto da molti altri computer, i messaggi attraversano nodi intermedi non controllabili e gli attacchi possono essere automatizzati tramite software.

## Flashcard 2

**Domanda:** Quali requisiti di sicurezza possono essere violati in rete?

**Risposta:**  
Confidenzialità tramite intercettazione, integrità tramite modifica o creazione di traffico, disponibilità tramite Denial of Service, oltre ad autenticazione e controllo accessi.

## Flashcard 3

**Domanda:** Che cos'è lo sniffing?

**Risposta:**  
È l'acquisizione e analisi di pacchetti di rete, spesso a livello data-link, per leggere header, metadati e dati applicativi se non cifrati.

## Flashcard 4

**Domanda:** Che cos'è il promiscuous mode?

**Risposta:**  
È una modalità della scheda di rete che permette di leggere tutti i pacchetti in transito sul mezzo, non solo quelli destinati al proprio indirizzo MAC.

## Flashcard 5

**Domanda:** Perché lo sniffing è più limitato nelle reti switched?

**Risposta:**  
Perché lo switch inoltra il traffico solo verso la porta associata al MAC address di destinazione. Lo sniffer vede normalmente solo il traffico destinato al proprio host.

## Flashcard 6

**Domanda:** Che cos'è ARP poisoning?

**Risposta:**  
È un attacco che inserisce associazioni IP-MAC false nella ARP cache delle vittime, permettendo all'attaccante di ricevere o deviare traffico destinato ad altri.

## Flashcard 7

**Domanda:** Perché ARP poisoning è possibile?

**Risposta:**  
Perché ARP è stateless e può accettare ARP reply non sollecitate, salvandole in cache.

## Flashcard 8

**Domanda:** Che differenza c'è tra wiretap passivo e attivo?

**Risposta:**  
Il wiretap passivo intercetta senza modificare il traffico e viola soprattutto la confidenzialità; il wiretap attivo modifica, crea, elimina o reindirizza messaggi, compromettendo integrità e disponibilità.

## Flashcard 9

**Domanda:** Che cos'è lo spoofing?

**Risposta:**  
È la falsificazione di identità, indirizzi o chiavi per impersonare un soggetto, un host o una comunicazione legittima.

## Flashcard 10

**Domanda:** Che cos'è il phishing?

**Risposta:**  
È un attacco basato su messaggi ingannevoli che spingono l'utente a cliccare link, inserire credenziali o comunicare dati sensibili.

## Flashcard 11

**Domanda:** Che cos'è una fake public key identity?

**Risposta:**  
È un attacco in cui l'attaccante sostituisce la chiave pubblica legittima con la propria, permettendo un man-in-the-middle in protocolli crittografici.

## Flashcard 12

**Domanda:** Che cos'è un SYN flood?

**Risposta:**  
È un attacco DoS che invia molti SYN TCP senza completare l'handshake, saturando le risorse che il server mantiene per connessioni incomplete.

## Flashcard 13

**Domanda:** Che cos'è un firewall?

**Risposta:**  
È un componente di difesa perimetrale che controlla il traffico tra reti, consentendo solo ciò che è autorizzato dalla security policy e rilevando tentativi di violazione.

## Flashcard 14

**Domanda:** Qual è la differenza tra packet filter e application gateway?

**Risposta:**  
Il packet filter controlla header, indirizzi e porte, spesso in modo stateless; l'application gateway agisce da proxy e controlla semanticamente dati applicativi, spesso in modo stateful.

## Flashcard 15

**Domanda:** Che cos'è una DMZ?

**Risposta:**  
È una zona di rete separata che ospita servizi esposti pubblicamente, isolandoli dalla rete interna protetta.

## Flashcard 16

**Domanda:** Che cos'è TLS?

**Risposta:**  
TLS è il successore di SSL e protegge privacy e integrità dei dati applicativi sopra TCP/IP.

## Flashcard 17

**Domanda:** Che cos'è HTTPS?

**Risposta:**  
HTTPS è HTTP su SSL/TLS e usa tipicamente la porta TCP 443, mentre HTTP usa la porta 80.

## Flashcard 18

**Domanda:** Qual è un limite di TLS/SSL?

**Risposta:**  
Protegge i dati applicativi, ma lascia in chiaro informazioni di trasporto e rete come header TCP/IP, rendendo ancora possibili spoofing e traffic analysis.

## Flashcard 19

**Domanda:** Che cos'è IPsec?

**Risposta:**  
IPsec è un meccanismo di sicurezza a livello IP che protegge traffico tra host o gateway, spesso in modo trasparente alle applicazioni.

## Flashcard 20

**Domanda:** Quali vantaggi offre IPsec rispetto a TLS?

**Risposta:**  
IPsec protegge a livello di rete, può cifrare traffico di protocolli superiori, offre maggiore protezione da traffic analysis e autentica anche l'origine IP.

## Flashcard 21

**Domanda:** Perché può essere utile usare IPsec e TLS insieme?

**Risposta:**  
Perché TLS protegge i dati applicativi, mentre IPsec protegge il traffico a livello di rete; più livelli di crittografia rendono più difficile intercettazione e analisi.

