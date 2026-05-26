# Buffer Manipulation

Un buffer e' uno spazio di memoria in cui l'applicazione conserva una certa quantita' di dati. Tipicamente e' implementato con un array di tipi primitivi o con una stringa mutabile.

## Perche' C e' rilevante

In C non e' automatico il controllo che letture e scritture restino nei limiti del buffer. Se il programma usa indici o lunghezze errate, puo' produrre accessi fuori limite.

## Overflow e overread

- Buffer overflow: scrittura fuori dai limiti del buffer.
- Buffer overread: lettura fuori dai limiti del buffer.

## Tassonomia

- CWE-664: improper control of a resource through its lifetime.
- CWE-118: incorrect access of indexable resource.
- CWE-119: improper restriction of operations within bounds of a memory buffer.
- CWE-707: improper neutralization.
- CWE-240: improper handling of inconsistent structural elements.
- CWE-130: improper handling of length parameter inconsistency.
- CAPEC-255: manipulate data structures.
- CAPEC-123: buffer manipulation.
- CAPEC-100: overflow buffers.
- CAPEC-540: overread buffers.

## Vulnerability patterns

- Uso di `gets`, che non verifica la dimensione dell'input rispetto al buffer.
- Uso di `fgets(buf, max, file)` con `max` maggiore della dimensione reale del buffer.
- Uso di input utente come parametro di lunghezza.
- Magic numbers non aggiornati dopo modifiche al buffer, invece di costanti simboliche.

## Collegamenti

- [[Buffer_Overflow]]
- [[Buffer_Overread_Heartbleed]]
- [[CWE_CAPEC_CVE]]

## Fonti

- SRC-008

