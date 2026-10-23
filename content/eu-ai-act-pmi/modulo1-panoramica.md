# Modulo 1: Panoramica rapida e timeline AI Act

**Durata:** 20-25 minuti

**Obiettivi del modulo:**
- Spiegare cos'è l'EU AI Act e perché è rilevante per le PMI italiane
- Identificare le 4 categorie principali di sistemi AI secondo la normativa
- Riconoscere le date chiave della timeline di applicazione (2025-2027)
- Distinguere tra obblighi immediati e obblighi futuri per le PMI

---

## 1.1 Introduzione all'EU AI Act

### Cos'è l'AI Act e perché esiste

L'**EU AI Act** è la prima legge al mondo che regola l'intelligenza artificiale. È entrata ufficialmente in vigore il 1° agosto 2024.

Perché nasce? L'AI offre enormi opportunità, ma porta anche rischi concreti. Decisioni automatizzate sbagliate possono discriminare persone, violare privacy, o compromettere la sicurezza. L'AI Act vuole bilanciare innovazione e protezione dei diritti fondamentali.

La legge si applica a chi **fornisce** sistemi AI (li sviluppa e vende) e a chi li **usa** (deployer). La maggior parte delle PMI italiane rientra nella seconda categoria: utilizzate AI, non la sviluppate.

### Fornitori vs Deployer: dove ti collochi?

**Fornitore:** Sviluppi un software con AI e lo vendi a clienti. Esempio: una software house che crea un tool di analisi predittiva per e-commerce.

**Deployer (utilizzatore):** Usi strumenti AI sviluppati da altri per le tue attività aziendali. Esempio: un'azienda manifatturiera che usa ChatGPT per scrivere report tecnici, oppure un negozio online che integra un chatbot per assistenza clienti.

**La maggior parte delle PMI è deployer.** Questo significa che hai obblighi più leggeri rispetto ai fornitori, ma comunque precisi e misurabili.

### Quando una PMI "usa AI"?

Ecco alcuni esempi pratici di uso AI in una PMI italiana:

**Esempio 1 - Marketing e comunicazione:**
Una piccola azienda vinicola in Toscana usa ChatGPT per generare descrizioni prodotto sul sito e-commerce. Usa anche un chatbot per rispondere alle FAQ dei clienti. **Classificazione:** Deployer di sistemi a rischio limitato.

**Esempio 2 - Risorse umane:**
Uno studio di commercialisti a Milano usa un software AI per filtrare CV ricevuti per posizioni di stagista. Il sistema assegna un punteggio ai candidati basato su esperienza e competenze. **Classificazione:** Deployer di sistema ad alto rischio (perché impatta sul diritto al lavoro).

**Esempio 3 - Controllo qualità:**
Un'azienda manifatturiera di componentistica a Brescia usa AI per rilevare difetti visuali su pezzi meccanici. Il sistema segnala anomalie, ma l'operatore decide se scartare il pezzo. **Classificazione:** Deployer di sistema a rischio limitato o minimo (decisione finale umana).

---

## 1.2 Le 4 categorie di sistemi AI

L'AI Act classifica i sistemi AI in **4 livelli di rischio**, ciascuno con obblighi diversi. Più è alto il rischio, più stringenti sono i requisiti.

### 🔴 Sistemi Proibiti (rischio inaccettabile)

Questi sistemi sono **vietati** perché violano diritti fondamentali. Non puoi usarli in nessun caso (salvo eccezioni per forze dell'ordine in contesti specifici).

**Esempi di sistemi proibiti:**
- **Manipolazione comportamento:** AI che sfrutta vulnerabilità psicologiche per influenzare scelte (es. app che manipola bambini a comportamenti pericolosi).
- **Social scoring:** Sistemi che assegnano punteggi sociali ai cittadini basati su comportamento o caratteristiche personali (stile Cina).
- **Riconoscimento biometrico in tempo reale:** Uso di riconoscimento facciale in spazi pubblici per sorveglianza di massa (con limitate eccezioni per polizia).

**Per le PMI:** È molto improbabile che tu stia usando sistemi proibiti. Se usi tool standard (ChatGPT, Google AI, Microsoft Copilot), sei al sicuro.

---

### 🟠 Sistemi ad Alto Rischio

Questi sistemi **impattano diritti fondamentali** come lavoro, istruzione, accesso a servizi essenziali, o sicurezza. Hanno obblighi di conformità rigorosi.

**Quando un sistema è ad alto rischio?**
- Influisce su decisioni critiche per le persone (assunzioni, credito, accesso a servizi pubblici)
- Opera in settori regolamentati (salute, trasporti, infrastrutture critiche)
- Può discriminare o violare privacy in modo grave

**Esempi concreti per PMI italiane:**

| **Settore**          | **Caso d'uso AI**                                      | **Perché è alto rischio**                              |
|----------------------|--------------------------------------------------------|--------------------------------------------------------|
| **HR**               | Software screening CV per recruitment                  | Impatta diritto al lavoro; rischio bias discriminatori |
| **Finance**          | Credit scoring automatizzato per prestiti clienti      | Determina accesso a servizi finanziari essenziali      |
| **Manifattura**      | Sistema AI per valutazione performance operai          | Influisce su stipendio, carriera, licenziamenti        |
| **Retail**           | AI per analisi comportamento clienti in negozio fisico| Raccolta dati biometrici (movimenti, espressioni)      |

**Obblighi principali per sistemi ad alto rischio (deployer):**
- **Supervisione umana:** Un operatore deve poter intervenire e correggere decisioni AI.
- **Trasparenza:** Informare le persone che l'AI è coinvolta nella decisione.
- **Documentazione:** Tenere un registro dei sistemi AI usati e delle decisioni prese.
- **Valutazione impatto:** Condurre una DPIA (Data Protection Impact Assessment) prima di attivare il sistema.

**Esempio pratico:** Se usi un software per filtrare CV, devi assicurarti che un recruiter umano riveda sempre la shortlist prima di scartare candidati. E devi informare i candidati che un sistema AI ha partecipato alla selezione.

---

### 🟡 General Purpose AI (GPAI)

I **GPAI** sono modelli fondazionali di grandi dimensioni usabili per scopi multipli. Esempi: GPT-4 (OpenAI), Claude (Anthropic), Gemini (Google), Llama (Meta).

**Per le PMI:** Se usi ChatGPT, Microsoft Copilot, Google Bard, o altri tool basati su GPAI, **non hai obblighi diretti come deployer**. Gli obblighi ricadono sui fornitori (OpenAI, Google, Microsoft).

**Eccezione:** Se integri profondamente un GPAI in un sistema ad alto rischio (es. chatbot per credit scoring), allora devi seguire le regole per i sistemi ad alto rischio.

**In sintesi:** Usa tranquillamente ChatGPT per scrivere email o report interni. Fai attenzione se usi AI generativa per decisioni critiche su persone (HR, credito, valutazioni).

---

### 🟢 Sistemi a Rischio Limitato o Minimo

Questa categoria include la **maggior parte degli usi AI nelle PMI**: chatbot, tool di generazione contenuti, analisi dati interne, assistenti virtuali.

**Obblighi principali (molto più leggeri):**
- **Trasparenza:** Devi informare gli utenti che stanno interagendo con un'AI o che un contenuto è stato generato da AI.
- **Watermark (quando possibile):** Se generi immagini, video, o audio con AI, devi indicare che sono AI-generated.

**Esempi pratici per PMI italiane:**

| **Caso d'uso**                          | **Obbligo AI Act**                                                |
|-----------------------------------------|-------------------------------------------------------------------|
| Chatbot su sito e-commerce              | Avviso: "Stai parlando con un assistente virtuale"               |
| Email marketing generate da ChatGPT     | Non serve avviso (comunicazione interna/marketing)                |
| Immagini prodotto create con Midjourney | Indicare "Immagine generata con AI" (se pubblicata)              |
| Tool AI per previsioni vendite interne  | Nessun obbligo (decisione interna, no impatto su terzi)          |

**Esempio concreto:** Hai un e-commerce di abbigliamento e usi un chatbot per rispondere alle FAQ. Sul widget del chatbot devi scrivere: "Ciao! Sono un assistente virtuale AI. Come posso aiutarti?" Oppure: "Questo servizio utilizza intelligenza artificiale."

**Nota importante:** Se il tuo chatbot raccoglie dati sensibili (es. dati sanitari, preferenze politiche) o influenza decisioni d'acquisto in modo ingannevole, potrebbe salire a rischio più alto. Valuta caso per caso.

---

## 1.3 Timeline cruciale 2025-2027

L'AI Act entra in vigore per fasi. Alcune regole sono già attive, altre partiranno nei prossimi anni. Ecco le **date chiave** da segnare in agenda.

| **Data**           | **Cosa entra in vigore**                          | **Chi riguarda**                     | **Azioni richieste**                                      |
|--------------------|---------------------------------------------------|--------------------------------------|-----------------------------------------------------------|
| **2 febbraio 2025** | Divieto sistemi proibiti                          | Tutti (fornitori e deployer)         | Verificare di non usare AI proibite (manipolazione, social scoring, biometria di massa) |
| **2 agosto 2025**   | Obblighi per fornitori GPAI                       | OpenAI, Google, Microsoft, Anthropic | Nessuna azione diretta per PMI deployer                   |
| **2 agosto 2026**   | Obblighi per sistemi ad alto rischio              | **PMI che usano AI per HR, credit scoring, valutazione lavoratori** | Implementare human oversight, trasparenza, DPIA, registri AI |
| **2 agosto 2027**   | Piena applicazione per tutti                      | Tutti i deployer                     | Conformità completa: policy AI, registri, trasparenza, formazione |

### Data più rilevante per le PMI: 2 agosto 2026

Se la tua azienda usa (o pianifica di usare) AI per **recruitment, valutazione dipendenti, credit scoring, o decisioni automatizzate su persone**, hai **18 mesi da oggi** per prepararti.

**Cosa fare entro agosto 2026:**
1. **Mappare** tutti i sistemi AI in uso (fai un inventario).
2. **Classificare** ciascun sistema nelle 4 categorie.
3. **Implementare controlli** per i sistemi ad alto rischio: supervisione umana, registro decisioni, trasparenza verso utenti.
4. **Redigere una AI policy aziendale** che definisce chi approva nuovi sistemi AI e come gestirli.
5. **Formare il team** (HR, IT, marketing, legal) su obblighi AI Act.

**Nota pratica:** Non aspettare l'ultimo momento. Molti fornitori di software AI stanno ancora aggiornando i loro tool per conformità. Inizia ora a fare domande ai tuoi vendor e a documentare l'uso interno.

---

## 1.4 Implicazioni per funzione aziendale

L'AI Act non è solo un problema del reparto IT o Legal. Ogni funzione aziendale che usa AI ha responsabilità specifiche. Ecco una guida pratica divisa per ruolo.

### Marketing

**Cosa cambia:**
- Se usi AI per generare contenuti (testi, immagini, video), devi indicare che sono AI-generated (watermark o disclaimer).
- Se usi chatbot sul sito, devi avvisare l'utente che sta interagendo con un assistente virtuale.
- Se usi AI per segmentazione clienti o pubblicità targetizzata, verifica che non ci siano bias discriminatori (es. escludere donne da offerte di lavoro).

**Azioni concrete:**
- Aggiungi disclaimer sui chatbot: "Questo è un assistente virtuale AI."
- Etichetta contenuti AI-generated: "Immagine creata con AI" nelle descrizioni.
- Documenta tool AI usati in un registro marketing (nome tool, funzione, fornitore).

---

### HR (Risorse Umane)

**Cosa cambia:**
- L'uso di AI per recruitment è **alto rischio**. Se usi software per screening CV o video-interviste automatizzate, hai obblighi pesanti.
- Devi garantire **human oversight**: un recruiter umano deve rivedere tutte le decisioni AI prima di scartare candidati.
- Devi **informare i candidati** che un sistema AI è coinvolto nel processo di selezione.
- Devi fare una **valutazione d'impatto (DPIA)** prima di usare il sistema.

**Azioni concrete:**
- Chiedi al tuo fornitore software (es. LinkedIn Recruiter, Workday, sistemi ATS) documentazione sulla conformità AI Act.
- Inserisci clausola nel processo recruiting: "Tutte le shortlist AI devono essere validate da un recruiter umano."
- Informa i candidati nella job description o email di conferma candidatura: "Questo processo utilizza AI per screening iniziale, con validazione finale umana."

---

### Customer Service

**Cosa cambia:**
- Chatbot e assistenti virtuali sono generalmente **rischio limitato**, con obbligo di trasparenza.
- Se usi AI per scoring clienti (affidabilità, credit score, accesso a servizi premium), sale a **alto rischio**.

**Azioni concrete:**
- Chatbot: Avviso chiaro all'utente ("Assistente virtuale AI").
- Scoring/segmentazione: Verifica se influenza accesso a servizi essenziali. Se sì, implementa trasparenza e diritto a contestazione umana.
- Documenta policy escalation: quando un cliente può parlare con un operatore umano.

---

### IT e Data

**Cosa cambia:**
- Sei il custode dei **dataset** usati per AI. Devi garantire qualità, rappresentatività, assenza di bias.
- Devi mantenere un **registro dei sistemi AI** in uso aziendale (nome, fornitore, categoria rischio, funzione).
- Devi implementare **log** per sistemi ad alto rischio (tracciare input/output/decisioni).

**Azioni concrete:**
- Crea un file Excel "Registro AI aziendale" con colonne: Nome sistema, Fornitore, Funzione, Categoria rischio, Responsabile, Data attivazione.
- Per sistemi ad alto rischio: Configura log automatici (chi ha usato il sistema, quando, quale decisione ha generato).
- Audit periodico dataset: Verifica che i dati di training/input non contengano bias (es. solo CV maschili, solo clienti >50 anni).

---

### Legal e Compliance

**Cosa cambia:**
- Devi redigere una **AI policy aziendale** che regola uso, approvazione, e governance AI.
- Devi coordinare **DPIA** (valutazioni d'impatto) per sistemi ad alto rischio.
- Devi negoziare **clausole contrattuali AI Act** con i fornitori (responsabilità, audit, supporto conformità).

**Azioni concrete:**
- Redigi AI policy (1-2 pagine): principi etici, ruoli (chi approva nuovi tool AI), processo valutazione rischio, gestione incidenti.
- Integra DPIA esistente (GDPR) con sezione AI-specific per sistemi ad alto rischio.
- Rivedi contratti fornitori AI: Aggiungi clausola "Fornitore garantisce conformità AI Act e supporta PMI in DPIA/audit."

---

## Attività Interattiva - Domanda Riflessiva

**Prompt per il partecipante:**

> **Rifletti sulla tua funzione aziendale.**
>
> Quali strumenti AI usi attualmente nel tuo lavoro quotidiano? (Es. ChatGPT, software HR, chatbot, tool analisi dati)
>
> In base a quanto hai appreso in questo modulo, identifica **almeno 1 implicazione concreta dell'AI Act** per la tua funzione.
>
> Esempi:
> - "Lavoro in Marketing. Uso ChatGPT per scrivere post LinkedIn. Implicazione: devo indicare che i contenuti sono AI-generated se li pubblico a nome aziendale."
> - "Lavoro in HR. Usiamo un software per filtrare CV. Implicazione: è un sistema ad alto rischio, devo implementare human oversight e informare i candidati."
>
> **Scrivi la tua risposta nel box sottostante (max 100 parole).**

**Istruzioni:**
Questa attività non è valutata, ma ti aiuta a contestualizzare l'AI Act nella tua realtà lavorativa. Prenditi 3-5 minuti per riflettere e scrivere. Se stai seguendo il corso in gruppo, condividi la tua risposta in un forum o sessione di discussione.

---

## Quiz Formativo - Verifica Modulo 1

**Istruzioni:** Rispondi alle 6 domande seguenti. Riceverai feedback immediato dopo ogni risposta. Puoi riprovare quante volte vuoi. L'obiettivo è verificare la comprensione, non valutarti.

---

### Domanda 1 di 6

**Quale dei seguenti sistemi è PROIBITO dall'AI Act?**

**Opzioni:**
- A) Un chatbot per assistenza clienti che informa gli utenti di essere AI
- B) Un sistema di social scoring che valuta cittadini in base a comportamento sociale
- C) Un software di recruitment che filtra CV con supervisione umana
- D) Un tool AI per generare immagini di prodotto

**Risposta corretta:** B

**Feedback risposta corretta:**
✓ **Corretto!** Il social scoring è vietato perché viola diritti fondamentali e dignità umana. È uno dei sistemi proibiti dall'AI Act.

**Feedback risposta errata:**
✗ **Non corretto.** Il social scoring (valutare persone con punteggi basati su comportamento) è considerato inaccettabile e quindi proibito. Chatbot, recruitment con supervisione, e generazione immagini sono leciti con i giusti controlli. **Rivedi sezione 1.2 - Sistemi Proibiti.**

---

### Domanda 2 di 6

**Una PMI che usa ChatGPT per scrivere email interne è considerata:**

**Opzioni:**
- A) Fornitore di sistema AI
- B) Deployer di sistema AI
- C) Nessuna delle due (ChatGPT è GPAI, nessun obbligo)
- D) Soggetta a regole GPAI provider

**Risposta corretta:** B

**Feedback risposta corretta:**
✓ **Esatto!** La PMI è **deployer** (utilizzatore) di ChatGPT. OpenAI è il fornitore. Come deployer, hai obblighi leggeri (trasparenza se usi AI per decisioni su persone o contenuti pubblici).

**Feedback risposta errata:**
✗ **Non corretto.** Una PMI che usa tool AI di terzi (ChatGPT, Copilot, etc.) è **deployer**, non fornitore. I fornitori sono chi sviluppa e vende AI (OpenAI, Microsoft, Google). Come deployer, hai comunque obblighi (trasparenza, registro), ma più leggeri rispetto ai fornitori. **Rivedi sezione 1.1 - Fornitori vs Deployer.**

---

### Domanda 3 di 6

**Entro quale data le PMI devono conformarsi per i sistemi ad alto rischio?**

**Opzioni:**
- A) 2 febbraio 2025
- B) 2 agosto 2025
- C) 2 agosto 2026
- D) 2 agosto 2027

**Risposta corretta:** C

**Feedback risposta corretta:**
✓ **Perfetto!** Il **2 agosto 2026** è la data cruciale per sistemi ad alto rischio (HR, credit scoring, valutazione lavoratori). Hai 18 mesi da oggi per prepararti.

**Feedback risposta errata:**
✗ **Non corretto.** La data chiave è il **2 agosto 2026**. Prima (febbraio/agosto 2025) entrano in vigore solo divieti e obblighi per fornitori GPAI. Per deployer di sistemi ad alto rischio, il 2 agosto 2026 è la deadline. **Rivedi sezione 1.3 - Timeline.**

---

### Domanda 4 di 6

**Quale funzione aziendale gestisce un sistema ad alto rischio?**

**Opzioni:**
- A) Marketing che usa ChatGPT per scrivere post social
- B) HR che usa software AI per screening CV senza supervisione umana
- C) IT che usa AI per previsioni vendite interne
- D) Customer service che usa chatbot informativo sul sito

**Risposta corretta:** B

**Feedback risposta corretta:**
✓ **Corretto!** Il recruitment automatizzato è ad alto rischio perché impatta il diritto al lavoro. Senza supervisione umana, viola l'AI Act. HR deve implementare human oversight obbligatorio.

**Feedback risposta errata:**
✗ **Non corretto.** Il recruitment automatizzato (screening CV con AI) è classificato **alto rischio** perché influisce sui diritti fondamentali delle persone (accesso al lavoro). Gli altri esempi sono rischio limitato o minimo. **Rivedi sezione 1.2 - Sistemi ad Alto Rischio e sezione 1.4 - Implicazioni HR.**

---

### Domanda 5 di 6 (Scenario-based)

**Scenario:** Un'azienda di e-commerce usa un chatbot sul sito per assistenza clienti. Il chatbot risponde a domande su spedizioni, resi, disponibilità prodotti. A volte il chatbot non riesce a rispondere e passa la conversazione a un operatore umano.

**Cosa deve fare l'azienda per essere conforme all'AI Act?**

**Opzioni:**
- A) Nulla, i chatbot non sono regolati
- B) Condurre una DPIA prima di attivare il chatbot
- C) Informare l'utente che sta interagendo con un assistente virtuale AI
- D) Implementare human oversight per ogni risposta del chatbot

**Risposta corretta:** C

**Feedback risposta corretta:**
✓ **Esatto!** Il chatbot è rischio limitato. L'obbligo principale è **trasparenza**: devi avvisare l'utente che sta parlando con un'AI. Non servono DPIA o supervisione umana costante per chatbot informativi.

**Feedback risposta errata:**
✗ **Non corretto.** Un chatbot per assistenza clienti è classificato **rischio limitato**. L'obbligo principale è **trasparenza**: informare l'utente che sta interagendo con un assistente AI. DPIA e human oversight sono obbligatori solo per sistemi ad alto rischio. **Rivedi sezione 1.2 - Sistemi a Rischio Limitato e sezione 1.4 - Customer Service.**

---

### Domanda 6 di 6 (Vero/Falso)

**Affermazione:** "Le PMI che usano solo ChatGPT o Microsoft Copilot per attività interne (scrivere report, analizzare dati) non hanno nessun obbligo dall'AI Act."

**Vero o Falso?**

**Risposta corretta:** Falso

**Feedback risposta corretta:**
✓ **Corretto!** Anche per usi interni di GPAI, le PMI sono considerate deployer e devono rispettare obblighi base: tenere un registro dei sistemi AI usati, garantire trasparenza se l'AI genera contenuti pubblici o decisioni su persone, e formare il personale sui limiti dell'AI. Gli obblighi sono leggeri, ma esistono.

**Feedback risposta errata:**
✗ **Non corretto. L'affermazione è FALSA.** Anche se usi solo ChatGPT/Copilot internamente, sei comunque un deployer AI. Hai obblighi minimi ma importanti:
- Tenere un registro dei tool AI usati
- Formare i dipendenti su uso responsabile
- Garantire trasparenza se l'AI genera contenuti pubblici o decisioni
- Valutare rischi se usi AI per decisioni su persone

**Rivedi sezione 1.1 e 1.2 per comprendere gli obblighi base per deployer.**

---

## Riepilogo Modulo 1

**Hai imparato:**
- ✓ **Cos'è l'AI Act** e perché regola l'intelligenza artificiale in Europa
- ✓ **La differenza tra fornitore e deployer** (la maggior parte delle PMI è deployer)
- ✓ **Le 4 categorie di sistemi AI**: proibiti 🔴, alto rischio 🟠, GPAI 🟡, rischio limitato/minimo 🟢
- ✓ **Le date chiave**: 2 agosto 2026 è la deadline per sistemi ad alto rischio (HR, credit scoring)
- ✓ **Le implicazioni concrete per la tua funzione** (Marketing, HR, Customer Service, IT, Legal)

**Competenze acquisite:**
- ○ Distinguere tra sistemi AI permessi, regolati, e proibiti
- ○ Identificare quali tool AI usi nella tua funzione rientrano nell'AI Act
- ○ Conoscere la timeline di conformità e quando agire

**Prossimo modulo:**
Nel **Modulo 2** esplorerai **5 scenari concreti di uso AI** nelle PMI italiane. Imparerai a classificare ciascun caso nelle categorie AI Act e a identificare i requisiti minimi di conformità. Userai un framework decisionale pratico applicabile ai tuoi sistemi aziendali.

**Collegamenti utili:**
- [Testo ufficiale EU AI Act (EUR-Lex)](https://eur-lex.europa.eu/)
- [Guida Garante Privacy italiano su AI e GDPR](https://www.garanteprivacy.it/)
- [FAQ Commissione Europea su AI Act](https://ec.europa.eu/ai)

---

**Fine Modulo 1**
