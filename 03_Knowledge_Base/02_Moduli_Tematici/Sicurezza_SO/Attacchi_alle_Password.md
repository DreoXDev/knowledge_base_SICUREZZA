# Attacchi alle password

> [!Info]
> Gli attacchi alle password sfruttano sia debolezze tecniche sia scelte prevedibili degli utenti. La robustezza dipende dallo spazio di ricerca, dalla gestione del password file e dal comportamento umano.

## Strategia dell'attaccante

In ordine di complessità crescente, un aggressore proverà tipicamente:

1. password assente;
2. password uguale o derivata dallo user ID;
3. password basata su informazioni note dell'utente;
4. lista di nomi comuni;
5. breve vocabolario in una o più lingue;
6. vocabolario con maiuscole e sostituzioni, ad esempio `i = 1`, `o = 0`, `a = @`;
7. dizionario completo in una o più lingue;
8. forza bruta con numeri e lettere minuscole/maiuscole;
9. forza bruta con set completo di caratteri.

Sono possibili anche scelte mirate se l'attaccante conosce il meccanismo di generazione delle password.

## Password generate casualmente ma deboli

Anche password scelte "a caso" possono essere deboli se:

- il generatore casuale è prevedibile;
- il generatore pesca da sequenze riproducibili;
- lo spazio di generazione è limitato.

## Comportamenti scorretti degli utenti

### Password troppo semplici

Password basate su nomi, animali domestici, date o parole comuni sono facilmente individuabili con dizionari.

Un dizionario tipico può contenere anche circa 1.000.000 di entry.

### Riduzione del set di caratteri

La riduzione del set di caratteri riduce drasticamente lo spazio delle password.

Esempio per password di 6 caratteri:

```text
95^6 ~= 735 x 10^9 password possibili
26^6 ~= 309 x 10^6 password possibili
```

Usare solo lettere minuscole riduce quindi molto lo spazio di ricerca rispetto all'uso di un set più ampio.

### Scrivere o condividere la password

Scrivere o condividere la password mette a rischio la sua segretezza.

> [!Warning]
> Una password tecnicamente forte può diventare inutile se viene scritta, condivisa o riutilizzata in contesti non sicuri.

## Collegamenti

- [[Password_Hashing_Salt]]
- [[Forza_Bruta_e_Crittoanalisi]]
- [[Processo_Autenticazione_Sicuro]]

## Fonti

- SRC-004

