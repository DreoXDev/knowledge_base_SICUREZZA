# Limiti della crittografia e threat model

> [!Info]
> La crittografia riduce alcuni rischi, ma non sostituisce un threat model completo. Un sistema può restare vulnerabile anche quando i dati sono cifrati correttamente.

## La crittografia è sufficiente?

No.

La crittografia è uno strumento importante, ma la sicurezza complessiva dipende dal threat model e dalle condizioni al contorno dei dati protetti.

> [!Warning]
> Proteggere un dato con crittografia non significa automaticamente proteggere tutto il sistema.

## Threat model

Il **threat model** descrive:

- quali minacce si stanno considerando;
- quali attaccanti esistono;
- quali capacità hanno;
- quali asset vogliono compromettere;
- quali assunzioni vengono fatte sul sistema.

Se il threat model è incompleto, la crittografia può proteggere solo una parte del problema.

## Esempio: PIN del bancomat

Il PIN del bancomat può essere protetto con meccanismi crittografici.

Tuttavia, i rischi possono includere:

- bug software;
- debolezze negli algoritmi di generazione dei PIN;
- debolezze nei protocolli non software;
- intercettazioni della posta;
- attacchi sofisticati da parte di tecnici interni;
- debolezze non note dei dispositivi;
- social engineering;
- spionaggio tecnico e non tecnico;
- comportamenti inadeguati degli utenti per scarsa consapevolezza dei rischi.

## Collegamento con la gestione del rischio

Questo tema si collega direttamente all'[[Analisi_Rischio]]:

- i dati protetti sono i valori sensibili;
- gli errori di implementazione sono vulnerabilità;
- gli attaccanti e le circostanze sfavorevoli sono minacce.

> [!Summary]
> La crittografia riduce alcuni rischi, ma non sostituisce analisi del rischio, progettazione sicura, gestione degli utenti, procedure operative e difesa dell'intero sistema.

## Collegamenti

- [[Analisi_Rischio]]
- [[Crittografia_Introduzione]]
- [[Certificati_X509_PKI]]
- [[CIA_Triad_DAD]]

## Fonti

- SRC-003

