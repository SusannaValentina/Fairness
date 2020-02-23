# Fairness

Il nostro obiettivo finale è calcolare la fairness in riferimento ad un oggetto in un ranking. Presi singolarmente non si può dire se alcuni oggetti sono discriminati rispetto ad altri, ma possiamo farlo se invece questi oggetti sono raggruppati in un gruppo con attributi sensibili, che possono essere ad esempio la nazionalità, il genere, l'età.
Se raggruppiamo questi oggetti e vediamo che tutti o quasi tutti gli oggetti di uno specifico gruppo sono molto in basso nel ranking, probabilmente c'è discriminazione per quel gruppo che noi vogliamo calcolare.

Per la sperimentazione utilizziamo il dataset di YELP che contiene due file: review.json e user.json. Questi contengono le informazioni sulle review dei ristoranti e sugli utenti che scrivono le review.
Potete scaricare il dataset e vedere la documentazione da questo link 
> https://www.yelp.com/dataset.

## Obiettivo 1: aumentare i dati dell'utente

Per ottenere maggiori attributi su cui calcolare la fairness di un certo ranking, occorre aumentare i dati degli utenti ottenendo tramite tecniche di facial recognition proprietà come il genere, l'età, l'etnia ecc.
Per utilizzare i servizi di Face++ è necessario registrarsi a questo link
> https://console.faceplusplus.com/login

e generare delle API Key, richieste quando si invoca uno dei loro servizi.

Nel codice all'interno della cartella Faceplusplus trovate le mie API Key già inserite, potete decidere voi se utilizzare quelle o sostituirle con le vostre.

Qui potete testare una demo del face detection che Face++ fornisce:
> https://www.faceplusplus.com/face-detection/

Qui invece trovate la documentazione di Face++:
> https://console.faceplusplus.com/documents/5679127

Potete utilizzare Face++ per ottenere alcuni attributi e integrare il risultato con altri strumenti che trovate.

## Obiettivo 2: ottenere il ranking dalla pagina HTML di Yelp

Prendiamo in input una pagina web di Yelp, ad esempio questa:
> https://www.yelp.com/biz/noche-de-margaritas-new-york

La pagina contiene i dettagli di un business, in questo caso un ristorante, e dobbiamo riuscire ad estrarre la lista ordinata di tutte le reviews, comprese le pagine seguenti. Nel codice all'interno della cartella Scraping ho già ottenuto le reviews in modo ordinato, ma solo della prima pagina visualizzata, tramite l'utilizzo di XPath. Ovviamente potete decidere se utilizzare XPath o un altro strumento di estrazione dati da pagina web.

## Obiettivo 3: aumentare i dati delle reviews

Così come per gli utenti, abbiamo bisogno di ulteriori dati sulle reviews in modo tale da individuare attributi che possono caratterizzare e distinguere una review da un'altra. Ad esempio la lunghezza della review, il Sentiment, le Entities citate nel testo ecc. Per questo scopo potete cercare e utilizzare strumenti di Sentiment Analysis in python, che dato un testo, lo analizzano e ricavano informazioni aggiuntive. Potete inserire il codice che producete nella cartella Sentiment.

