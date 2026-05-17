# Flashcards - Crittografia Parte 2

## Fonte

- SRC-003

## Flashcard 1

**Domanda:** Che cos'è la crittografia asimmetrica?

**Risposta:**  
È una classe di algoritmi crittografici in cui ogni soggetto possiede una coppia di chiavi: una chiave pubblica, distribuibile a tutti, e una chiave privata, nota solo al proprietario.

## Flashcard 2

**Domanda:** Come si usa la crittografia asimmetrica per inviare un messaggio confidenziale ad A?

**Risposta:**  
Il mittente cifra il messaggio con la chiave pubblica di A. Solo A può decifrarlo usando la propria chiave privata.

## Flashcard 3

**Domanda:** Quante chiavi servono per `n` utenti nella crittografia asimmetrica?

**Risposta:**  
Servono `n` coppie di chiavi, una coppia per ogni utente. Questo è più scalabile rispetto alla crittografia simmetrica, che richiede `n(n-1)/2` chiavi condivise.

## Flashcard 4

**Domanda:** Perché la crittografia asimmetrica supporta il non-ripudio?

**Risposta:**  
Perché un messaggio firmato con la chiave privata può essere verificato da chiunque con la chiave pubblica corrispondente. La verifica può quindi essere fatta anche da terze parti.

## Flashcard 5

**Domanda:** Che cos'è RSA?

**Risposta:**  
RSA è un algoritmo crittografico asimmetrico inventato da Rivest, Shamir e Adleman. Si basa sulla difficoltà di fattorizzare numeri molto grandi.

## Flashcard 6

**Domanda:** Qual è l'idea matematica alla base di RSA?

**Risposta:**  
Si scelgono due grandi numeri primi `p` e `q`, si calcola `n = p * q`, e la sicurezza dipende dal fatto che, conoscendo solo `n`, è molto difficile risalire a `p` e `q`.

## Flashcard 7

**Domanda:** Quali sono i principali vantaggi di RSA?

**Risposta:**  
RSA supporta confidenzialità, integrità, autenticità e non-ripudio; permette verifica da parte di terzi; riduce il numero di chiavi necessarie; consente di scambiare chiavi pubbliche anche su canali insicuri.

## Flashcard 8

**Domanda:** Qual è il principale limite prestazionale di RSA?

**Risposta:**  
RSA è molto più lento degli algoritmi simmetrici e viene usato tipicamente per cifrare piccole quantità di dati, come chiavi di sessione o digest.

## Flashcard 9

**Domanda:** Che cos'è un message digest?

**Risposta:**  
È un riassunto crittografico del messaggio, usato per rappresentare in modo compatto il contenuto e verificare se il messaggio è stato modificato.

## Flashcard 10

**Domanda:** Quali proprietà deve avere un hash crittografico?

**Risposta:**  
Deve essere non invertibile e resistente alle collisioni, cioè deve essere difficile ricostruire un messaggio dal digest e improbabile trovare due messaggi diversi con lo stesso digest.

## Flashcard 11

**Domanda:** Gli algoritmi di hashing garantiscono confidenzialità?

**Risposta:**  
No. Gli hash non servono a cifrare messaggi o trasmettere segreti. Servono principalmente a verificare integrità.

## Flashcard 12

**Domanda:** Perché un hash da solo non garantisce autenticità?

**Risposta:**  
Perché chiunque può calcolare il digest di un messaggio. Per garantire autenticità serve legare il digest all'identità del mittente, ad esempio firmandolo digitalmente.

## Flashcard 13

**Domanda:** Come funziona una firma digitale efficiente?

**Risposta:**  
Il mittente calcola il digest del messaggio e firma il digest con la propria chiave privata. Il destinatario verifica la firma con la chiave pubblica del mittente e confronta il digest ottenuto con quello calcolato sul messaggio ricevuto.

## Flashcard 14

**Domanda:** Perché non si firma direttamente un messaggio grande con RSA?

**Risposta:**  
Perché RSA è poco efficiente su grandi quantità di dati. È più efficiente firmare solo il digest del messaggio.

## Flashcard 15

**Domanda:** Come funziona la cifratura ibrida RSA + AES?

**Risposta:**  
Il mittente genera una chiave segreta casuale, cifra il messaggio con AES usando quella chiave, poi cifra la chiave segreta con la chiave pubblica RSA del destinatario. Il destinatario decifra prima la chiave con RSA e poi il messaggio con AES.

## Flashcard 16

**Domanda:** Qual è il problema della distribuzione delle chiavi pubbliche?

**Risposta:**  
Bisogna essere sicuri che una chiave pubblica appartenga davvero all'entità che si vuole autenticare o a cui si vuole inviare un messaggio confidenziale.

## Flashcard 17

**Domanda:** Che cos'è un certificato X.509?

**Risposta:**  
È un certificato digitale che associa una chiave pubblica a un'identità, ed è firmato da un'autorità di certificazione fidata.

## Flashcard 18

**Domanda:** Che cosa contiene un certificato X.509?

**Risposta:**  
Contiene il nome dell'entità certificata, la sua chiave pubblica, il nome dell'autorità di certificazione e la firma digitale dell'autorità.

## Flashcard 19

**Domanda:** Come funziona una catena di certificati?

**Risposta:**  
La fiducia viene propagata: se A si fida di X, X certifica Y e Y certifica Z, A può verificare progressivamente i certificati fino a ottenere con fiducia la chiave pubblica di Z.

## Flashcard 20

**Domanda:** Che cos'è una PKI?

**Risposta:**  
Una Public Key Infrastructure è l'infrastruttura che gestisce chiavi pubbliche, certificati digitali e autorità di certificazione.

## Flashcard 21

**Domanda:** Perché la crittografia non è sufficiente da sola?

**Risposta:**  
Perché la sicurezza dipende anche dal threat model, dall'implementazione, dai protocolli, dai dispositivi, dagli utenti, dal social engineering e dalle condizioni operative del sistema.

## Flashcard 22

**Domanda:** Che cos'è un threat model?

**Risposta:**  
È il modello delle minacce considerate: descrive attaccanti, asset, capacità, possibili attacchi e assunzioni del sistema.

