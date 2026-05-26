# Contromisure Buffer Overflow

## Problema

Una scrittura fuori limite puo' corrompere memoria adiacente e alterare il flusso di esecuzione.

## Cause tipiche

- Uso di funzioni non sicure come `gets`.
- Lunghezze errate in `fgets` o `memcpy`.
- Input utente usato come dimensione.
- Magic numbers non aggiornati.

## Contromisure

- Controllare sempre bounds e lunghezze.
- Usare costanti simboliche invece di numeri magici.
- Abilitare `-fstack-protector`, `-fstack-protector-all` o `-fstack-protector-strong`.
- Usare ASLR.
- Usare executable space protection e NX/XD/XN/DEP.
- Preferire API sicure e linguaggi/runtime con controlli bounds quando possibile.

## Limiti delle contromisure

Canary e indirizzi possono essere rivelati da leak. ASLR non corregge il bug. Codice nativo in ambienti managed puo' reintrodurre il rischio.

## Collegamenti

- [[Buffer_Overflow]]
- [[Canary_vs_ASLR_vs_Executable_Space_Protection]]

