# DAC e MAC

> [!Info]
> DAC e MAC sono due famiglie di controllo accessi: nel DAC decide il proprietario della risorsa, nel MAC decide una politica imposta dal sistema.

## Discretionary Access Control

Nel **Discretionary Access Control** o **DAC**, il proprietario di una risorsa può concedere, modificare o revocare diritti di accesso ad altri utenti a sua discrezione.

Esempio tipico:

- Access Control List;
- permessi gestiti dal proprietario.

## Vantaggio del DAC

È flessibile e adatto ad ambienti in cui gli utenti devono collaborare e condividere risorse.

## Limite del DAC

Il sistema lascia molta discrezionalità agli utenti.

Questo può essere un problema se l'obiettivo è impedire che informazioni sensibili vengano propagate in modo non controllato.

## Mandatory Access Control

Nel **Mandatory Access Control** o **MAC**, il sistema impone un modello che limita e controlla la discrezionalità degli utenti nell'assegnare diritti di accesso.

Le regole sono definite da una politica di sicurezza e non possono essere modificate liberamente dai proprietari delle risorse.

## Confronto

| Modello | Chi decide i diritti? | Caratteristica principale |
|---|---|---|
| DAC | proprietario della risorsa | flessibilità |
| MAC | sistema/politica di sicurezza | controllo forte e centralizzato |

## Collegamenti

- [[ACL_e_Bit_Protezione]]
- [[Modelli_Multilivello]]
- [[Bell_LaPadula]]
- [[Biba]]

## Fonti

- SRC-005

