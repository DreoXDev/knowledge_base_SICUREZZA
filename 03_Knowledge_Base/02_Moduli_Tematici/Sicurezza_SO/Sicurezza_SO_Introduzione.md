# Sicurezza nei sistemi operativi

> [!Info]
> Il sistema operativo è il livello che media tra applicazioni e hardware. Per questo è un punto centrale della sicurezza: gestisce risorse, identità, oggetti e regole di accesso.

## Organizzazione di un sistema informatico

Un sistema informatico può essere visto come una struttura a livelli:

1. utenti;
2. applicazioni;
3. sistema operativo;
4. hardware;
5. dispositivi di I/O, memoria, CPU e bus.

Il sistema operativo si trova tra applicazioni e hardware: fornisce astrazioni, gestisce risorse e media l'accesso a oggetti e dispositivi.

## Funzioni del sistema operativo

Le principali funzioni rilevanti per la sicurezza sono:

- **multitasking**: uso contemporaneo della CPU da parte di più processi;
- **gestione della memoria**: segmentazione, paginazione e memoria virtuale;
- **device driver**: astrazione dell'accesso ai dispositivi;
- **file system**: organizzazione delle informazioni sulle memorie di massa;
- **interprete dei comandi**: interazione uomo/macchina tramite shell;
- **protocolli di rete**: comunicazione tra applicazioni remote.

## Aree di interesse per la sicurezza

Le aree principali sono:

- autenticazione degli utenti;
- protezione della memoria;
- controllo degli accessi;
- protezione di file;
- protezione di periferiche di I/O;
- protezione di oggetti generici;
- controllo della condivisione tra utenti;
- protezione dei dati di protezione del sistema operativo.

## Due problemi centrali

| Problema | Significato |
|---|---|
| Autenticazione | stabilire un'identità e autenticare il richiedente |
| Controllo degli accessi | decidere se un soggetto autenticato può accedere a oggetti protetti |

> [!Important]
> Prima si autentica il soggetto, poi si applicano le regole di controllo accessi.

## Collegamenti

- [[Autenticazione]]
- [[CIA_Triad_DAD]]
- [[Analisi_Rischio]]

## Fonti

- SRC-004

