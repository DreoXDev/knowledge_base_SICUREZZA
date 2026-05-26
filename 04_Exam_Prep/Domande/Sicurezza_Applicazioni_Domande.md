# Domande - Sicurezza Applicazioni

## Fonte

- SRC-007
- SRC-008

## Domande e risposte

### 1. Spiega differenza tra weakness, vulnerabilita', exploit e attacco.

Una weakness e' una categoria di difetto nel progetto, implementazione o operazione. Una vulnerabilita' e' l'occorrenza concreta di una weakness in un sistema specifico. Un exploit e' la tecnica concreta per sfruttarla. L'attacco e' l'azione intenzionale che usa o segue un pattern per violare la security policy.

### 2. Spiega differenza tra CWE, CAPEC e CVE.

CWE cataloga weakness, CAPEC cataloga attack pattern e CVE cataloga vulnerabilita' concrete in software noti.

### 3. Quali sono i problemi delle tassonomie CWE/CAPEC?

Sono utili ma non perfette: non sempre ortogonali, talvolta sovrapposte, imprecise e capaci di confondere errore umano, difetto e pattern di sfruttamento.

### 4. Spiega la struttura base di una web application e perche' serve per capire XSS.

Una web application ha browser client, server, richieste HTTP, HTML generato dinamicamente e spesso JavaScript lato client. Serve per capire XSS perche' l'input utente puo' rientrare nell'HTML o nel DOM ed essere interpretato dal browser come codice.

### 5. Che cos'e' improper neutralization?

E' una weakness in cui input non fidato non viene neutralizzato correttamente prima di essere usato in un contesto interpretabile, come HTML, JavaScript o SQL.

### 6. Spiega XSS e le sue varianti persistent/reflected/DOM-based.

XSS esegue script malevolo nel browser della vittima. Persistent salva il payload lato server. Reflected lo include nella richiesta e lo riflette nella risposta. DOM-based nasce da codice client che manipola il DOM usando input non fidato.

### 7. Quali sono le contromisure contro XSS?

Encoding/escaping contestuale dell'output, validation dell'input, controlli server-side, attenzione ai diversi contesti HTML, attributi, JavaScript, URL e CSS.

### 8. Spiega SQL injection e perche' le query concatenate sono pericolose.

SQL injection avviene quando input utente modifica una query SQL. Le query concatenate mescolano codice SQL e dati, permettendo all'input di cambiare struttura o condizioni della query.

### 9. Perche' i prepared statement mitigano SQL injection?

Separano struttura della query e parametri. Il database tratta i valori utente come dati, non come frammenti di codice SQL.

### 10. Che cos'e' buffer overflow?

E' una scrittura fuori dai limiti di un buffer. In C puo' sovrascrivere memoria adiacente perche' non sempre esistono controlli bounds automatici.

### 11. Come puo' un buffer overflow alterare il flusso di controllo?

Su stack puo' sovrascrivere il return address; quando la funzione termina, il processore salta all'indirizzo scelto dall'attaccante invece che al chiamante legittimo.

### 12. Spiega shellcode e NOP sled.

Lo shellcode e' codice preparato dall'attaccante. Il NOP sled e' una sequenza di NOP che amplia l'area in cui puo' cadere un salto impreciso prima di raggiungere lo shellcode.

### 13. Differenza tra stack buffer overflow e heap buffer overflow.

Nello stack l'obiettivo tipico e' sovrascrivere variabili locali, base pointer o return address. Nell'heap si corrompono strutture dati, metadati o puntatori a funzione.

### 14. Spiega canary values, ASLR ed executable space protection.

I canary rilevano sovrascritture dello stack. ASLR randomizza indirizzi per renderli meno prevedibili. Executable space protection impedisce esecuzione da pagine dati come stack o heap.

### 15. Che cos'e' JIT spraying?

E' una tecnica che abusa della generazione just-in-time di codice per ottenere molte sequenze eseguibili utili, riducendo l'efficacia di alcune difese sull'esecuzione della memoria.

### 16. Perche' i linguaggi managed non eliminano del tutto il problema dei buffer overflow?

Perche' possono interagire con codice nativo, librerie o runtime scritti in linguaggi senza controlli bounds automatici.

### 17. Che cos'e' buffer overread?

E' una lettura oltre i limiti del buffer. Non corrompe memoria, ma puo' rivelare dati sensibili.

### 18. Spiega Heartbleed.

Heartbleed sfrutta una lunghezza dichiarata nel heartbeat TLS maggiore del payload reale. Il server copia in risposta piu' byte di quelli ricevuti e rivela memoria adiacente.

### 19. Che cos'e' null pointer dereference?

E' l'uso di un puntatore NULL come se puntasse a un oggetto valido. Spesso causa crash, ma nel kernel puo' essere sfruttabile.

### 20. Come puo' una null pointer dereference diventare sfruttabile nel kernel?

Se l'attaccante mappa o controlla pagina NULL/indirizzi bassi, il kernel puo' usare dati o puntatori controllati dall'attaccante con privilegi kernel.

### 21. Spiega CVE-2009-2692.

E' una vulnerabilita' Linux kernel in `sock_sendpage`: un puntatore a funzione non controllato puo' essere NULL. Tramite `sendfile` e mapping della pagina 0, l'attaccante puo' redirigere esecuzione e ottenere privilegi.

### 22. Spiega CVE-2009-1897.

Riguarda TUN/TAP: il puntatore `tun` viene usato prima del null check. Il controllo tardivo puo' essere eliminato dal compilatore, consentendo sfruttamento con pagina NULL controllata.

### 23. Quali sono alcune linee guida Java per il secure coding?

Limitare durata dei dati sensibili, salvare hash password, evitare MD5 secondo la fonte, controllare serializzazione/deserializzazione/clonazione, gestire integer overflow e usare strumenti come SpotBugs.

### 24. Perche' bisogna limitare la vita dei dati sensibili?

Meno a lungo un dato sensibile resta in memoria o in scope ampio, minore e' la finestra in cui puo' essere letto, loggato o esposto.

### 25. Perche' conviene salvare hash delle password e non password in chiaro/crittografate reversibilmente?

Le password in chiaro sono immediatamente compromesse. Quelle cifrate reversibilmente dipendono dalla protezione della chiave. Gli hash riducono l'impatto, soprattutto se progettati per password.

### 26. Perche' serializzazione, deserializzazione e clonazione possono essere rischiose?

Possono esporre stato interno, creare oggetti inattesi o aggirare invarianti se abilitate senza necessita' e senza controlli.

### 27. Come si gestisce integer overflow in Java?

Si usano controlli espliciti e, quando appropriato, le funzioni di exact arithmetic introdotte in Java 8, che segnalano overflow invece di lasciarlo silenzioso.

### 28. Qual e' il ruolo di SpotBugs/SonarQube/FindBugs?

Sono strumenti di static analysis che individuano pattern di codice potenzialmente vulnerabili, soprattutto regole domain independent come esposizione di rappresentazione interna o password hardcoded.

