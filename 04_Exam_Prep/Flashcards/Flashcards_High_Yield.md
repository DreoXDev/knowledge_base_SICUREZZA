# Flashcards High Yield

> [!Info]
> Flashcard ad alta priorita' per gli ultimi ripassi. Ogni carta punta a una risposta breve, non a una spiegazione completa.

## Definizioni base

1. Q: Differenza tra safety e security?  
A: Safety riguarda danni da malfunzionamento; security riguarda attacchi intenzionali contro una policy.

2. Q: Quali sono i tre elementi della CIA Triad?  
A: Confidenzialita', integrita' e disponibilita'.

3. Q: Che cosa rappresenta DAD?  
A: Disclosure, alteration e destruction: famiglie di attacchi alla CIA.

4. Q: Che cos'e' una vulnerabilita'?  
A: Occorrenza concreta di una debolezza sfruttabile per violare la security policy.

5. Q: Che cos'e' il rischio in security?  
A: Combinazione di vulnerabilita', minacce e valori da proteggere.

6. Q: Che cos'e' una security policy?  
A: Insieme di regole che stabilisce come proteggere risorse critiche e sensibili.

7. Q: Che cos'e' un threat model?  
A: Descrizione di minacce, attaccanti, capacita' e assunzioni considerate.

8. Q: Che cos'e' il principio dei minimi privilegi?  
A: Ogni soggetto deve avere solo i privilegi strettamente necessari.

## Crittografia

9. Q: Che cos'e' il plaintext?  
A: Messaggio in chiaro prima della cifratura.

10. Q: Che cos'e' il ciphertext?  
A: Messaggio cifrato prodotto dall'algoritmo.

11. Q: Che cos'e' una chiave crittografica?  
A: Parametro usato da algoritmo per cifrare o decifrare.

12. Q: Che cos'e' la crittografia simmetrica?  
A: Crittografia con la stessa chiave condivisa per cifrare e decifrare.

13. Q: Quante chiavi servono in simmetrica per `n` utenti?  
A: `n(n-1)/2` chiavi se ogni coppia comunica privatamente.

14. Q: Che cos'e' la crittografia asimmetrica?  
A: Crittografia con coppia di chiavi pubblica e privata.

15. Q: Quante chiavi servono in asimmetrica per `n` utenti?  
A: `n` coppie di chiavi.

16. Q: Perche' DES e' obsoleto?  
A: Chiave effettiva di 56 bit troppo piccola contro forza bruta.

17. Q: Che cos'e' Triple DES?  
A: Applicazione ripetuta di DES con chiavi diverse per aumentare sicurezza.

18. Q: Che cos'e' AES?  
A: Standard moderno di cifratura simmetrica a blocchi.

19. Q: Che cos'e' RSA?  
A: Algoritmo asimmetrico basato sulla difficolta' di fattorizzare grandi numeri.

20. Q: Che cos'e' una funzione one-way?  
A: Facile da calcolare, difficile da invertire.

21. Q: Che cos'e' un message digest?  
A: Riassunto crittografico a dimensione fissa di un messaggio.

22. Q: Quali proprieta' deve avere un hash crittografico?  
A: One-way e resistente alle collisioni.

23. Q: Come si firma digitalmente in modo efficiente?  
A: Si firma il digest con la chiave privata.

24. Q: Come si verifica una firma digitale?  
A: Con la chiave pubblica del mittente, confrontando i digest.

25. Q: Che cosa garantisce una firma digitale?  
A: Integrita', autenticita' e non-ripudio.

26. Q: Che cos'e' un certificato X.509?  
A: Associazione firmata tra identita' e chiave pubblica.

27. Q: Che cos'e' una PKI?  
A: Infrastruttura per certificati, chiavi pubbliche e autorita' di certificazione.

28. Q: Perche' la crittografia non basta da sola?  
A: Non protegge da errori di policy, implementazione, endpoint o threat model sbagliato.

## Sistemi operativi

29. Q: Che cos'e' autenticazione?  
A: Verifica dell'identita' dichiarata.

30. Q: Che cos'e' controllo accessi?  
A: Decisione su quali operazioni un soggetto puo' fare su un oggetto.

31. Q: Perche' le password non vanno salvate in chiaro?  
A: Se il file e' esposto, le credenziali sono subito compromesse.

32. Q: Che cos'e' il salt?  
A: Valore casuale aggiunto prima dell'hash della password.

33. Q: Che cos'e' challenge/response?  
A: Autenticazione tramite challenge variabile e risposta calcolata.

34. Q: Che cos'e' un nonce?  
A: Valore usato una sola volta.

35. Q: Perche' il nonce difende da replay?  
A: Rende vecchie risposte non riutilizzabili.

36. Q: Che cos'e' reflection attack?  
A: Uso di una sessione parallela per far risolvere una challenge alla vittima.

37. Q: Come si mitiga reflection attack?  
A: Includendo identita' e contesto nei messaggi.

38. Q: Che cos'e' Needham-Schroeder?  
A: Protocollo di autenticazione reciproca a chiave pubblica.

39. Q: Che cos'e' una ACL?  
A: Lista associata a un oggetto con soggetti e diritti.

40. Q: Che cos'e' mediazione completa?  
A: Ogni accesso a ogni oggetto protetto deve essere controllato.

41. Q: Come sono divisi i 9 bit Unix/Linux?  
A: `rwx` per owner, group e others.

42. Q: Che cos'e' DAC?  
A: Controllo accessi a discrezione del proprietario.

43. Q: Che cos'e' MAC?  
A: Controllo accessi imposto dal sistema.

44. Q: Obiettivo di Bell-LaPadula?  
A: Confidenzialita'.

45. Q: Regole Bell-LaPadula?  
A: No read up e no write down.

46. Q: Obiettivo di Biba?  
A: Integrita'.

47. Q: Regole Biba?  
A: No write up e no read down.

48. Q: Che cosa aggiungono i compartimenti?  
A: Vincolo need-to-know oltre al livello.

49. Q: Che cos'e' un covert channel?  
A: Canale non previsto usato per trasmettere informazioni.

50. Q: Che cos'e' auditing?  
A: Registrazione e analisi di eventi rilevanti per sicurezza.

51. Q: Che cos'e' un IDS?  
A: Sistema che rileva intrusioni o usi anomali.

## Reti

52. Q: Che cos'e' sniffing?  
A: Acquisizione e analisi di pacchetti di rete.

53. Q: Che cos'e' promiscuous mode?  
A: Modalita' scheda di rete che legge anche pacchetti non destinati al proprio MAC.

54. Q: Che cos'e' ARP poisoning?  
A: Inserimento di associazioni IP-MAC false in cache ARP.

55. Q: Che cos'e' spoofing?  
A: Falsificazione di identita' o indirizzi.

56. Q: Che cos'e' phishing?  
A: Inganno per ottenere credenziali o azioni dell'utente.

57. Q: Che cos'e' pharming?  
A: Deviazione verso host falso che impersona uno legittimo.

58. Q: Che cos'e' DoS?  
A: Attacco alla disponibilita' di un servizio.

59. Q: Che cos'e' SYN flood?  
A: DoS che satura connessioni TCP incomplete.

60. Q: Che cos'e' un firewall?  
A: Componente che filtra traffico secondo policy.

61. Q: Che cos'e' packet filtering?  
A: Filtraggio basato su header, indirizzi, porte e protocolli.

62. Q: Come si blocca IP spoofing esterno?  
A: Scartando pacchetti esterni con sorgente interna.

63. Q: Che cos'e' application gateway?  
A: Proxy che controlla traffico applicativo semanticamente.

64. Q: Che cos'e' DMZ?  
A: Rete separata per servizi esposti.

65. Q: Che cos'e' TLS?  
A: Protocollo che protegge dati applicativi sopra TCP.

66. Q: TLS nasconde header IP/TCP?  
A: No, protegge dati applicativi ma header IP/TCP restano visibili.

67. Q: Che cos'e' HTTPS?  
A: HTTP su TLS.

68. Q: Che cos'e' IPsec?  
A: Meccanismo di sicurezza a livello IP.

69. Q: IPsec transport protegge cosa?  
A: Payload IP; header IP originale resta visibile.

70. Q: IPsec tunnel protegge cosa?  
A: L'intero pacchetto IP originale incapsulato.

71. Q: Che cos'e' VPN?  
A: Connessione cifrata tra endpoint, spesso basata su IPsec.

## Applicazioni

72. Q: Che cos'e' weakness?  
A: Tipo di difetto che puo' introdurre vulnerabilita'.

73. Q: Che cos'e' exploit?  
A: Tecnica concreta di sfruttamento di una vulnerabilita'.

74. Q: CWE, CAPEC, CVE: differenza?  
A: CWE weakness, CAPEC pattern, CVE vulnerabilita' concrete.

75. Q: Che cos'e' improper neutralization?  
A: Input non neutralizzato prima di un contesto interpretabile.

76. Q: Che cos'e' XSS?  
A: Input malevolo interpretato come script dal browser.

77. Q: Varianti XSS principali?  
A: Persistent, reflected e DOM-based.

78. Q: Difesa principale contro XSS?  
A: Encoding/escaping contestuale dell'output.

79. Q: Che cos'e' SQL injection?  
A: Input che modifica la semantica di query SQL.

80. Q: Difesa principale contro SQL injection?  
A: Prepared statements/query parametrizzate.

81. Q: Che cos'e' buffer overflow?  
A: Scrittura fuori limite in un buffer.

82. Q: Perche' stack overflow e' pericoloso?  
A: Puo' sovrascrivere return address.

83. Q: Che cos'e' shellcode?  
A: Codice preparato dall'attaccante per essere eseguito.

84. Q: Che cos'e' NOP sled?  
A: Sequenza di NOP che facilita il salto allo shellcode.

85. Q: Che cos'e' canary?  
A: Valore sentinella per rilevare sovrascritture dello stack.

86. Q: Che cos'e' ASLR?  
A: Randomizzazione degli indirizzi virtuali.

87. Q: Che cos'e' NX/DEP?  
A: Difesa che impedisce esecuzione da pagine dati.

88. Q: Che cos'e' buffer overread?  
A: Lettura fuori limite che puo' esporre memoria.

89. Q: Che cos'e' Heartbleed?  
A: Overread dovuto a lunghezza dichiarata maggiore del payload reale.

90. Q: Che cos'e' null pointer dereference?  
A: Uso di NULL come puntatore valido.

91. Q: Perche' nel kernel e' grave?  
A: Puo' usare dati controllati con privilegi kernel.

92. Q: Cosa insegna CVE-2009-2692?  
A: Puntatore a funzione NULL non controllato puo' portare a privilege escalation.

93. Q: Cosa insegna CVE-2009-1897?  
A: Un null check dopo l'uso e' troppo tardi.

94. Q: Perche' limitare vita dati sensibili in Java?  
A: Riduce finestra di esposizione in memoria.

95. Q: Password in Java: cosa salvare?  
A: Hash, non password in chiaro o cifrate reversibilmente.

96. Q: Perche' usare static analysis?  
A: Per trovare pattern di weakness automaticamente.

