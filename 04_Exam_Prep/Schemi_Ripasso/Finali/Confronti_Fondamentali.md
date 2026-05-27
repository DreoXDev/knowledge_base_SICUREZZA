# Confronti Fondamentali

## Safety vs Security

| Aspetto | Safety | Security |
|---|---|---|
| Causa | Malfunzionamento | Attaccante intenzionale |
| Obiettivo | Evitare danni accidentali | Proteggere da violazioni |
| Nota | Affidabilita' operativa | Policy e minacce |

## CIA vs DAD

| CIA | Attacco DAD |
|---|---|
| Confidenzialita' | Disclosure |
| Integrita' | Alteration |
| Disponibilita' | Destruction |

## Simmetrica vs Asimmetrica

| Aspetto | Simmetrica | Asimmetrica |
|---|---|---|
| Chiavi | Una condivisa | Coppia pubblica/privata |
| Numero per `n` utenti | `n(n-1)/2` | `n` coppie |
| Pro | Efficiente | Distribuzione e firme |
| Contro | Scambio chiavi | Costosa |

## DES vs Triple DES vs AES

| Algoritmo | Stato | Nota |
|---|---|---|
| DES | Obsoleto | 56 bit effettivi |
| Triple DES | Rafforzamento storico | Piu' lento |
| AES | Standard moderno | Chiavi piu' robuste |

## Hash vs Cifratura

| Aspetto | Hash | Cifratura |
|---|---|---|
| Direzione | One-way | Reversibile con chiave |
| Output | Digest | Ciphertext |
| Uso | Integrita' | Confidenzialita' |

## Firma vs Cifratura per confidenzialita'

| Uso | Chiave usata | Verifica/lettura | Proprietà |
|---|---|---|---|
| Firma | Privata mittente | Pubblica mittente | Integrita', autenticita', non-ripudio |
| Confidenzialita' | Pubblica destinatario | Privata destinatario | Segretezza |

## Autenticazione vs Controllo Accessi

| Aspetto | Autenticazione | Controllo accessi |
|---|---|---|
| Domanda | Chi sei? | Cosa puoi fare? |
| Momento | Prima dell'accesso | Durante richiesta risorsa |
| Esempio | Password, challenge/response | ACL, MAC |

## Replay vs Reflection

| Aspetto | Replay | Reflection |
|---|---|---|
| Tecnica | Riusa messaggio valido | Riflette challenge in altra sessione |
| Difesa | Nonce | Identita' e contesto nei messaggi |

## DAC vs MAC

| Aspetto | DAC | MAC |
|---|---|---|
| Controllo | Proprietario | Sistema |
| Esempio | ACL | Bell-LaPadula, Biba |

## Bell-LaPadula vs Biba

| Aspetto | Bell-LaPadula | Biba |
|---|---|---|
| Obiettivo | Confidenzialita' | Integrita' |
| Regola chiave | No read up, no write down | No write up, no read down |

## Packet Filter vs Application Gateway

| Aspetto | Packet filter | Application gateway |
|---|---|---|
| Livello | Header rete/trasporto | Applicativo |
| Pro | Efficiente | Controllo semantico |
| Contro | Poco contesto | Specifico e costoso |

## Screened Subnet vs DMZ

| Aspetto | Screened subnet | DMZ |
|---|---|---|
| Idea | Architettura filtrata | Zona separata |
| Uso | Separare interno/esposto | Ospitare servizi pubblici |

## TLS vs IPsec

| Aspetto | TLS | IPsec |
|---|---|---|
| Livello | Sopra TCP | Livello IP |
| Protegge | Dati applicativi | Payload IP o pacchetti IP |
| Header IP visibile | Si | Dipende dalla modalita' |
| Uso tipico | HTTPS | VPN |

## IPsec Transport vs Tunnel

| Aspetto | Transport | Tunnel |
|---|---|---|
| Protegge | Payload IP | Intero pacchetto IP originale |
| Header originale | Visibile | Protetto |
| Uso | Host-to-host | VPN/gateway |

## XSS Persistent vs Reflected vs DOM-Based

| Variante | Dove nasce | Dove esegue |
|---|---|---|
| Persistent | Salvato server-side | Browser vittima |
| Reflected | Richiesta riflessa | Browser vittima |
| DOM-based | JavaScript client | Browser vittima |

## XSS vs SQL Injection

| Aspetto | XSS | SQL injection |
|---|---|---|
| Target | Browser | Database |
| Contesto | HTML/JS/DOM | SQL |
| Difesa principale | Output encoding | Prepared statements |

## Buffer Overflow vs Buffer Overread

| Aspetto | Overflow | Overread |
|---|---|---|
| Operazione | Scrittura fuori limite | Lettura fuori limite |
| Rischio | Controllo flusso/corruzione | Leak informazioni |

## Stack Overflow vs Heap Overflow

| Aspetto | Stack | Heap |
|---|---|---|
| Target tipico | Return address, frame | Strutture e puntatori |
| Scenario | Chiamate funzione | Allocazioni dinamiche |

## Canary vs ASLR vs NX/DEP

| Difesa | Scopo | Limite |
|---|---|---|
| Canary | Rilevare sovrascrittura stack | Leak puo' aggirare |
| ASLR | Randomizzare indirizzi | Leak indirizzi |
| NX/DEP | Impedire esecuzione da dati | ROP/JIT spraying |

## Weakness vs Vulnerability vs Exploit vs Attack

| Concetto | Significato |
|---|---|
| Weakness | Tipo di difetto |
| Vulnerability | Occorrenza concreta sfruttabile |
| Exploit | Tecnica di sfruttamento |
| Attack | Azione intenzionale |

