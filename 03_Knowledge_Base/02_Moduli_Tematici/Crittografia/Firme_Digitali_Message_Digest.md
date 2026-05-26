# Firme Digitali e Message Digest

Una firma digitale combina hashing crittografico e crittografia asimmetrica per garantire integrita', autenticita' e non-ripudio in modo efficiente.

## Invio di un file firmato

Se l'utente A vuole inviare un file `F` firmato a B:

1. A calcola il message digest `H(F)`.
2. A cifra il digest con la propria chiave privata `A_priv`.
3. A invia a B il file `F` e la firma digitale.

## Verifica della firma

Quando B riceve file e firma:

1. B calcola localmente `H(F)` sul file ricevuto.
2. B verifica la firma usando la chiave pubblica di A, `A_pub`, ottenendo il digest firmato da A.
3. B confronta i due digest.
4. Se coincidono, il file non e' stato alterato e la firma e' compatibile con la chiave privata di A.

## Perche' firmare il digest

Firmare direttamente file grandi e' inefficiente. Il digest ha dimensione fissa ed e' progettato per rappresentare il contenuto in modo resistente alle collisioni.

## Collegamenti

- [[Firme_Digitali]]
- [[Hashing_Message_Digest]]
- [[Crittografia_Asimmetrica]]

## Fonti

- SRC-003
- SRC-009
- SRC-011

