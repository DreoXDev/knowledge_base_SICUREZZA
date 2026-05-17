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

## Confronti importanti

- Safety vs security: la safety si concentra su danni accidentali o malfunzionamenti, la security su attacchi intenzionali e abusi.
- CIA vs DAD: la CIA Triad descrive cosa proteggere; DAD descrive famiglie di attacco contro quegli obiettivi.
- Crittografia simmetrica vs firma digitale: la simmetrica consente confidenzialità efficiente, ma non prova a terzi quale partecipante abbia generato un messaggio.
- DES vs AES: DES usa chiavi effettive da 56 bit ed è vulnerabile a forza bruta moderna; AES usa blocchi da 128 bit e chiavi più lunghe, ed è lo standard moderno.
- Simmetrica vs asimmetrica: la simmetrica è veloce ma richiede chiavi condivise; l'asimmetrica è più lenta ma rende pubblica una parte della chiave e supporta firme digitali.
- Hashing vs cifratura: l'hashing produce un digest e non è reversibile; la cifratura deve permettere il recupero del plaintext.
- Certificati vs chiavi pubbliche nude: una chiave pubblica da sola non prova l'identità del proprietario; il certificato lega chiave e identità tramite una CA.

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
