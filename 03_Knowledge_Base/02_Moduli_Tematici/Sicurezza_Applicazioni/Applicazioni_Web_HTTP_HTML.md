# Applicazioni Web, HTTP e HTML

> [!Info]
> Nelle slide questa parte funziona come intermezzo di supporto: non e' il nucleo dell'esame, ma serve a capire perche' XSS e injection funzionano.

## Architettura client/server

In una web application il browser e' il client, il server espone risorse e genera risposte, spesso dinamiche. L'utente invia input tramite URL, parametri, form e richieste HTTP.

## URL, DNS e HTTP

Un URL identifica una risorsa. DNS traduce nomi in indirizzi. HTTP trasporta richieste e risposte tra client e server.

## GET e POST

- GET mette parametri tipicamente nella query string ed e' usato per recuperare risorse.
- POST invia dati nel corpo della richiesta ed e' usato spesso per form e operazioni che modificano stato.

Entrambi possono trasportare input non fidato.

## HTML, CSS e JavaScript

HTML descrive struttura tramite tag e attributi. CSS definisce presentazione. JavaScript esegue logica nel browser e puo' leggere o modificare il DOM.

## Form HTML

I form sono un canale tipico di input utente. Se il server reinserisce input in HTML senza encoding contestuale, puo' nascere [[Cross_Site_Scripting_XSS]].

## Scripting server-side e client-side

- Server-side: il server genera HTML dinamico, spesso usando dati dell'utente o del database.
- Client-side: il browser esegue JavaScript e manipola il DOM.

Questa distinzione e' centrale per distinguere XSS reflected/persistent da DOM-based XSS.

## Fonti

- SRC-007

