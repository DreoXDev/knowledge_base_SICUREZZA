# Cross-Site Scripting XSS

Cross-Site Scripting e' uno schema di attacco in cui input malevolo viene interpretato come codice dal browser della vittima.

## Obiettivo

L'attaccante vuole eseguire script nel contesto della pagina visitata dalla vittima. Questo puo' permettere di leggere o modificare dati della pagina, interagire con cookie o sessione, modificare il DOM o far eseguire azioni come se fossero dell'utente.

## Perche' attaccare il browser

Il browser contiene stato applicativo, sessioni e dati visualizzati. Se uno script malevolo gira nello stesso contesto della pagina legittima, puo' abusare della fiducia che il browser assegna a quell'origine.

## Varianti

### Persistent XSS

Il payload viene salvato lato server, ad esempio in un commento o profilo, e poi servito a piu' utenti.

### Reflected XSS

Il payload arriva nella richiesta e viene riflesso nella risposta, ad esempio in un messaggio di errore o risultato di ricerca.

### DOM-based XSS

La manipolazione avviene lato client: JavaScript legge input da URL o DOM e lo inserisce in un sink pericoloso senza neutralizzazione.

## Contromisure

- Encoding/escaping contestuale dell'output.
- Validation dell'input.
- Controllo inbound e outbound.
- Separare controlli server-side e client-side: il client aiuta l'usabilita', ma il server deve restare autorevole.
- Considerare il contesto: HTML text, attributi HTML, JavaScript, URL e CSS richiedono regole diverse.

## Schema generale

1. L'attaccante prepara input con codice interpretabile.
2. L'applicazione conserva o riflette l'input senza neutralizzarlo.
3. Il browser della vittima interpreta il payload come script.
4. Lo script agisce nel contesto della pagina.

## Collegamenti

- [[Injection_Improper_Neutralization]]
- [[Persistent_vs_Reflected_vs_DOM_XSS]]
- [[XSS_vs_SQL_Injection]]

## Fonti

- SRC-007

