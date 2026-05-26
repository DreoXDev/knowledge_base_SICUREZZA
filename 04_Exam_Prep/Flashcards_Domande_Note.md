# Flashcards Domande Note

## Q-INTRO-001 - Giusta difesa

> [!Question]
> Come si valuta la giusta difesa?

> [!Answer]
> Si parte dal rischio: valori da proteggere, minacce realistiche e vulnerabilita' sfruttabili. La CIA Triad classifica gli obiettivi e gli interventi vanno prioritizzati sugli elementi con rischio piu' alto.

## Q-CRYPTO-001 - Simmetrica vs asimmetrica

> [!Question]
> Qual e' la differenza tra crittografia simmetrica e asimmetrica e come cambia il numero di chiavi?

> [!Answer]
> La simmetrica usa una chiave condivisa per coppia e richiede `n(n-1)/2` chiavi per `n` utenti. L'asimmetrica usa una coppia pubblica/privata per utente e richiede `n` coppie.

## Q-CRYPTO-002 - Chiave pubblica e firma

> [!Question]
> Come si usa la crittografia a chiave pubblica per firmare?

> [!Answer]
> Il mittente firma un digest con la propria chiave privata; il destinatario verifica con la chiave pubblica del mittente. Si ottengono integrita', autenticita' e non-ripudio.

## Q-CRYPTO-003 - Firma efficiente

> [!Question]
> Perche' nelle firme digitali efficienti si firma il digest e non tutto il file?

> [!Answer]
> Perche' il digest ha dimensione fissa e rappresenta crittograficamente il contenuto; firmarlo e' molto piu' efficiente che firmare direttamente file grandi.

## Q-CRYPTO-004 - Challenge/response

> [!Question]
> Perche' in challenge/response servono nonce e identificativi?

> [!Answer]
> Il nonce impedisce replay; gli identificativi legano la risposta al soggetto e al contesto, riducendo reflection e relay attack.

## Q-CRYPTO-005 - Hash

> [!Question]
> Quali proprieta' deve avere una funzione di hash crittografica?

> [!Answer]
> Deve produrre digest a dimensione fissa, essere one-way e resistente alle collisioni in modo computazionalmente pratico.

## Q-CRYPTO-006 - DES

> [!Question]
> Perche' DES non e' piu' sicuro?

> [!Answer]
> La chiave effettiva da 56 bit e' troppo breve contro forza bruta moderna. Triple DES aumenta la sicurezza storicamente, ma AES e' l'alternativa moderna.

## Q-SO-001 - DAC vs MAC

> [!Question]
> Differenza tra DAC e MAC?

> [!Answer]
> Nel DAC il proprietario gestisce gli accessi; nel MAC la politica e' imposta dal sistema. ACL e' esempio DAC; Bell-LaPadula e Biba sono esempi MAC.

## Q-SO-002 - ACL e mediazione completa

> [!Question]
> Che cos'e' una ACL e che cos'e' la mediazione completa?

> [!Answer]
> La ACL associa diritti a un oggetto per utenti o gruppi. La mediazione completa richiede che ogni accesso a ogni oggetto protetto sia controllato.

## Q-SO-003 - ACL 9 bit

> [!Question]
> Come funzionano i 9 bit Unix/Linux?

> [!Answer]
> Sono tre gruppi `rwx`: owner, group e others. Rappresentano lettura, scrittura ed esecuzione per ciascuna categoria.

## Q-SO-004 - Bell-LaPadula compartimenti

> [!Question]
> Come funziona Bell-LaPadula con compartimenti?

> [!Answer]
> Un soggetto legge un oggetto solo se domina il suo livello e possiede tutti i compartimenti dell'oggetto. E' un modello MAC orientato alla confidenzialita'.

## Q-NET-001 - Packet filter anti-spoofing

> [!Question]
> Come un packet filter blocca IP spoofing esterno?

> [!Answer]
> Scarta pacchetti in ingresso dall'esterno che dichiarano come sorgente un indirizzo appartenente alla rete interna.

## Q-NET-002 - Packet filter vs gateway

> [!Question]
> Differenza tra packet filter e application gateway?

> [!Answer]
> Il packet filter guarda header e regole di basso livello; l'application gateway agisce da proxy e controlla semanticamente il protocollo applicativo.

## Q-NET-003 - Screened subnet

> [!Question]
> Che cos'e' una screened subnet?

> [!Answer]
> Una zona intermedia filtrata che separa servizi esposti e rete interna, riducendo l'impatto di compromissioni.

## Q-NET-004 - DMZ

> [!Question]
> Che cos'e' una DMZ?

> [!Answer]
> Una rete separata per servizi pubblici, isolata dalla rete interna tramite firewall.

## Q-NET-005 - TLS packet

> [!Question]
> Cosa protegge TLS in un pacchetto IP?

> [!Answer]
> Protegge i dati applicativi nel record TLS sopra TCP; header IP e TCP restano visibili.

## Q-NET-006 - IPsec tunnel

> [!Question]
> Che cosa protegge IPsec tunnel mode?

> [!Answer]
> Incapsula e protegge l'intero pacchetto IP originale dentro un nuovo pacchetto IP esterno.

## Q-NET-007 - IPsec transport

> [!Question]
> Che cosa protegge IPsec transport mode?

> [!Answer]
> Protegge il payload del pacchetto IP; l'header IP originale resta visibile per l'instradamento.

## Q-APP-001 - XSS

> [!Question]
> Che cos'e' XSS?

> [!Answer]
> Un attacco in cui input malevolo viene interpretato come codice dal browser della vittima; puo' essere persistent, reflected o DOM-based.

## Q-APP-002 - SQL injection

> [!Question]
> Che cos'e' SQL injection?

> [!Answer]
> Input non fidato modifica una query SQL costruita male. La difesa principale sono prepared statements/query parametrizzate.

## Q-APP-003 - Buffer overflow

> [!Question]
> Perche' un buffer overflow puo' alterare il flusso di controllo?

> [!Answer]
> Una scrittura fuori limite puo' sovrascrivere return address o puntatori a funzione, portando l'esecuzione verso codice controllato dall'attaccante.

