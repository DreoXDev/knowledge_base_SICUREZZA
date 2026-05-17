# Forza bruta e crittoanalisi

> [!Info]
> La forza bruta prova tutte le chiavi possibili; la crittoanalisi cerca invece debolezze più profonde o informazioni indirette per violare un sistema crittografico.

## Attacchi di forza bruta

Un attacco di **forza bruta** consiste nel provare tutte le istanze possibili di un insieme finito di schemi o chiavi crittografiche, fino a trovare quella corretta.

Esempio:

> Provare tutte le possibili chiavi di `N` caratteri.

## Esempio numerico

Se una chiave ha 8 caratteri e ogni carattere è scelto tra 26 lettere minuscole, il numero di chiavi possibili è:

$$
26^8
$$

Se ogni prova richiede `1 microsecondo`, il tempo totale nel caso peggiore è:

$$
26^8 \times 10^{-6} \text{ secondi}
$$

Questo esempio serve a mostrare che la resistenza alla forza bruta dipende da:

- dimensione dello spazio delle chiavi;
- tempo necessario per provare ogni chiave;
- capacità computazionale disponibile;
- possibilità di parallelizzare l'attacco.

> [!Warning]
> Molti algoritmi assumono l'infattibilità degli attacchi di forza bruta, ma il set di attacchi possibili deve sempre essere analizzato con attenzione.

## Crittoanalisi

La **crittoanalisi** studia gli attacchi che tentano di violare la crittografia tramite l'analisi di messaggi cifrati, algoritmi, chiavi o contesto di utilizzo.

Possibili obiettivi:

- decifrare un singolo messaggio;
- scoprire debolezze di un algoritmo crittografico;
- scoprire debolezze dell'ambiente di funzionamento;
- scoprire la chiave usata per cifrare un insieme di messaggi;
- dedurre significati segreti senza decifrare il contenuto, ad esempio osservando frequenza o lunghezza dei messaggi.

## Crittografia vs crittoanalisi

| Termine | Significato |
|---|---|
| Crittografia | costruzione di metodi per codificare in modo sicuro i messaggi |
| Crittoanalisi | studio dei modi per violare o aggirare tali metodi |

## Collegamenti

- [[Schemi_di_Cifratura]]
- [[Algoritmi_Crittografici]]
- [[DES_TripleDES_AES]]
- [[Analisi_Rischio]]

## Fonti

- SRC-002

