# Flashcards - Sicurezza SO Parte 2

## Fonte

- SRC-005

## Flashcard 1

**Domanda:** Che cos'è il controllo degli accessi?

**Risposta:**  
È il meccanismo con cui il sistema stabilisce quali soggetti possono accedere a quali oggetti protetti e con quali diritti, ad esempio lettura, scrittura o esecuzione.

## Flashcard 2

**Domanda:** Perché le password per singole risorse sono un meccanismo debole di controllo accessi?

**Risposta:**  
Perché distinguono solo tra accesso consentito e negato, sono poco flessibili, difficili da gestire, difficili da revocare e poco usabili quando le risorse sono molte.

## Flashcard 3

**Domanda:** Che cos'è una Access Control List?

**Risposta:**  
È una lista associata a una risorsa che specifica quali utenti o gruppi hanno quali diritti su quella risorsa, ad esempio ownership, read, write o execute.

## Flashcard 4

**Domanda:** Come funzionano i bit di protezione Unix/Linux?

**Risposta:**  
Sono una forma semplificata di ACL: per ogni file si definiscono i permessi read, write ed execute per owner, group e world.

## Flashcard 5

**Domanda:** Che cos'è la mediazione completa?

**Risposta:**  
È il principio secondo cui ogni accesso a ogni oggetto protetto deve essere controllato, evitando bypass e riducendo vulnerabilità come TOC/TOU.

## Flashcard 6

**Domanda:** Che cos'è un attacco TOC/TOU?

**Risposta:**  
È un attacco che sfrutta il tempo tra il controllo di autorizzazione e l'uso effettivo della risorsa, modificando il contesto o la risorsa tra i due momenti.

## Flashcard 7

**Domanda:** Che cos'è il principio dei minimi privilegi?

**Risposta:**  
È il principio secondo cui ogni utente, processo o componente deve avere solo i privilegi strettamente necessari per svolgere il proprio compito.

## Flashcard 8

**Domanda:** Che cos'è un covert channel?

**Risposta:**  
È un canale alternativo o non ovvio attraverso cui dati sensibili vengono trasmessi a soggetti non autorizzati, sfruttando file, nomi, tempi, metadati o stati osservabili.

## Flashcard 9

**Domanda:** Qual è la differenza tra DAC e MAC?

**Risposta:**  
Nel DAC il proprietario della risorsa decide a chi concedere accesso. Nel MAC è il sistema, tramite una politica obbligatoria, a imporre i diritti e limitare la discrezionalità degli utenti.

## Flashcard 10

**Domanda:** Che cos'è la sicurezza multilivello?

**Risposta:**  
È un modello in cui soggetti e oggetti sono classificati su livelli di sicurezza, e l'accesso dipende dal confronto tra livello del soggetto e livello dell'oggetto.

## Flashcard 11

**Domanda:** Qual è l'obiettivo del modello Bell-LaPadula?

**Risposta:**  
Proteggere la confidenzialità, impedendo che informazioni sensibili fluiscano verso soggetti con livello di autorizzazione insufficiente.

## Flashcard 12

**Domanda:** Cosa significa no-read-up in Bell-LaPadula?

**Risposta:**  
Significa che un soggetto non può leggere oggetti classificati a un livello superiore al proprio.

## Flashcard 13

**Domanda:** Cosa significa no-write-down in Bell-LaPadula?

**Risposta:**  
Significa che un soggetto non può scrivere oggetti classificati a un livello inferiore al proprio, per evitare fuga di informazioni verso livelli più bassi.

## Flashcard 14

**Domanda:** Qual è l'obiettivo del modello Biba?

**Risposta:**  
Proteggere l'integrità, impedendo che soggetti o dati meno affidabili modifichino o influenzino oggetti di maggiore integrità.

## Flashcard 15

**Domanda:** Cosa significa no-write-up in Biba?

**Risposta:**  
Significa che un soggetto non può modificare oggetti di classificazione o integrità più alta.

## Flashcard 16

**Domanda:** Cosa significa no-read-down in Biba?

**Risposta:**  
Significa che un soggetto non deve leggere oggetti di livello più basso, per evitare contaminazione da dati meno affidabili.

## Flashcard 17

**Domanda:** Qual è la differenza essenziale tra Bell-LaPadula e Biba?

**Risposta:**  
Bell-LaPadula protegge la confidenzialità con no-read-up e no-write-down; Biba protegge l'integrità con no-write-up e no-read-down.

## Flashcard 18

**Domanda:** Che cosa sono i compartimenti nei modelli di sicurezza?

**Risposta:**  
Sono raggruppamenti semantici, come progetti o missioni, che limitano l'accesso anche tra soggetti con lo stesso livello di sicurezza.

## Flashcard 19

**Domanda:** Che cosa significa need-to-know?

**Risposta:**  
Significa che l'accesso è consentito solo se il soggetto ha sia il livello sufficiente sia l'appartenenza al compartimento necessario.

## Flashcard 20

**Domanda:** Che cos'è il modello della Muraglia Cinese?

**Risposta:**  
È un modello di controllo accessi pensato per gestire conflitti di interesse, impedendo a un consulente di accedere a dati riservati di aziende concorrenti nella stessa classe COI.

## Flashcard 21

**Domanda:** Che cos'è l'auditing?

**Risposta:**  
È la registrazione e analisi di eventi rilevanti per la sicurezza, come accessi a file, login, logout, operazioni amministrative e operazioni privilegiate.

## Flashcard 22

**Domanda:** Che cos'è un IDS?

**Risposta:**  
Un Intrusion Detection System è un sistema che analizza dati di auditing per individuare o prevenire compromissioni, usi non autorizzati o violazioni delle politiche di sicurezza.

## Flashcard 23

**Domanda:** Quali sono alcuni principi di progettazione di un sistema operativo trusted?

**Risposta:**  
Minimi privilegi, mediazione completa, autorizzazione negata per default, multiple point of failure, separazione tra utenti, minima condivisione, protezione del riutilizzo delle risorse e auditing.

## Flashcard 24

**Domanda:** Perché la facilità d'uso è importante nei sistemi operativi trusted?

**Risposta:**  
Perché meccanismi troppo difficili da usare vengono spesso aggirati, configurati male o applicati in modo incoerente, riducendo la sicurezza reale.

