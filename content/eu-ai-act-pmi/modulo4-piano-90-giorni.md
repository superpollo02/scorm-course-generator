# Modulo 4: Piano 90 giorni

**Durata:** 25-30 minuti

**Obiettivi del modulo:**
- Pianificare 5 azioni concrete per la conformità AI Act nei prossimi 90 giorni
- Assegnare ruoli e responsabilità per ciascuna azione
- Valutare fornitori AI secondo criteri AI Act
- Organizzare comunicazione interna e formazione
- Produrre un mini-piano operativo di 1 pagina pronto all'uso

---

## Introduzione al Modulo

Sei arrivato all'ultimo modulo del corso. Hai imparato **cosa dice l'AI Act**, **come classificare i sistemi AI**, e **quali controlli di governance implementare**. Ora è il momento di **passare all'azione**.

Questo modulo è 100% operativo. Ti guida nella costruzione di un **piano 90 giorni** (circa 3 mesi) per avviare la conformità AI Act nella tua azienda. Non si tratta di teoria: al termine avrai un documento concreto da presentare al tuo management o da usare come roadmap personale.

**Cosa farai in questo modulo:**
- Scoprirai le **5 azioni chiave** da implementare nei primi 90 giorni
- Capirai **chi coinvolgere** (matrice ruoli RACI)
- Imparerai a **valutare i fornitori AI** con questionario pronto
- Pianificherai **comunicazione e formazione interna**
- Definirai **KPI e metriche** per monitorare progresso
- Costruirai il **tuo piano 90 giorni personalizzato** (activity builder interattivo)

**Tempo:** 12-15 minuti lezione + 10-12 minuti esercizio pratico

Iniziamo!

---

## 4.1 Roadmap 90 Giorni: le 5 Azioni Chiave

Hai 90 giorni (circa 12 settimane) per mettere le fondamenta della conformità AI Act. Non puoi fare tutto subito, ma puoi fare **5 azioni prioritarie** che ti preparano al meglio per agosto 2026.

Ecco la roadmap raccomandata:

---

### Azione 1 (Settimane 1-2): Inventory AI - Censimento sistemi AI in uso

**Cosa significa:**
Fai un **inventario completo** di tutti i tool AI che la tua azienda usa attualmente (o pianifica di usare nei prossimi mesi).

**Perché è prioritaria:**
Non puoi conformarti a ciò che non conosci. Il primo passo è sempre **mappare l'esistente**.

**Chi coinvolgere:**
- **IT / Data:** Identificano software e piattaforme AI usate (SaaS, tool interni, API)
- **Manager funzioni (HR, Marketing, Operations):** Dichiarano quali tool AI usano nei loro team
- **Legal / Compliance:** Coordinano raccolta info e classificazione rischio

**Come eseguirla (step operativi):**

**Step 1:** Manda una **survey interna** a tutti i manager di funzione con domande:
- "Quali tool basati su AI usa il tuo team?" (es. ChatGPT, software X, chatbot Y)
- "Per quale scopo?" (es. recruitment, marketing, customer service, analisi dati)
- "Chi è il fornitore?" (es. OpenAI, Microsoft, vendor Z)
- "Da quando lo usiamo?" (data attivazione)

**Step 2:** IT crea un file Excel "**Registro AI Aziendale**" (template scaricabile dal Modulo 3) con colonne:
- Nome sistema
- Fornitore
- Funzione aziendale / Responsabile
- Categoria rischio AI Act (da classificare)
- Dataset utilizzati
- Status (attivo / pianificato / disattivato)

**Step 3:** Per ciascun sistema, applica il **decision tree** (Modulo 2) per classificare categoria rischio (🔴 Proibito / 🟠 Alto / 🟡 GPAI / 🟢 Limitato/Minimo).

**Step 4:** Identifica **priorità**:
- Sistemi 🟠 **Alto Rischio** → Priorità 1 (richiedono azioni immediate)
- Sistemi 🟢 **Rischio Limitato** → Priorità 2 (azioni più leggere)
- Sistemi 🟢 **Rischio Minimo** → Priorità 3 (documentazione base)

**Output atteso:**
- File Excel "Registro AI Aziendale" completo con tutti i sistemi usati (5-20 sistemi tipicamente per una PMI)
- Identificazione 1-3 sistemi ad alto rischio che richiedono attenzione urgente
- Lista tool AI "scoperti" di cui management non era consapevole (shadow AI)

**Tempo stimato:** 6-10 ore distribuite su 2 settimane (survey + raccolta + classificazione).

**Esempio pratico:**

> **Caso: PMI manifatturiera 50 dipendenti (Brescia)**
>
> **Sistemi AI identificati:**
> 1. ChatGPT Enterprise (Marketing, contenuti) → 🟢 Rischio Limitato
> 2. Software ATS con AI screening CV (HR) → 🟠 **Alto Rischio** (priorità 1)
> 3. Chatbot sito web (Customer Service) → 🟢 Rischio Limitato
> 4. Tool AI previsioni domanda (Operations) → 🟢 Rischio Minimo
> 5. Copilot Microsoft 365 (tutti i dipendenti) → 🟢 Rischio Limitato
>
> **Azione immediata:** Focus su sistema ATS (alto rischio) → servono DPIA, human oversight, trasparenza verso candidati.

---

### Azione 2 (Settimane 2-4): AI Policy - Redigere e approvare policy aziendale

**Cosa significa:**
Scrivi il documento ufficiale che regola l'uso di AI nella tua azienda: **AI Policy** (1-2 pagine).

**Perché è prioritaria:**
La policy è la **base di governance**. Definisce chi può fare cosa, come si approvano nuovi tool, come si gestiscono rischi. Senza policy, ogni funzione fa da sé (rischio incoerenza e non-conformità).

**Chi coinvolgere:**
- **Legal / Compliance:** Redigono bozza (usando template Modulo 3)
- **CEO / Board:** Approvano formalmente
- **Manager funzioni:** Consultati per feedback (realisticità processo approvazione)
- **DPO:** Rivede coerenza con GDPR

**Come eseguirla (step operativi):**

**Step 1:** Scarica **template AI Policy** (Modulo 3) e personalizzalo:
- Inserisci nome azienda
- Adatta ruoli/responsabilità alla tua struttura (es. se non hai DPO, indica "Legal Officer")
- Definisci workflow approvazione realistico (es. se PMI piccola, approvazione CEO diretta; se media, serve comitato valutazione)

**Step 2:** Circola bozza ai **manager funzioni** per 1 settimana di consultazione:
- "Questo processo è applicabile? Ci sono criticità operative?"
- Raccogli feedback e aggiusta

**Step 3:** Presenta policy a **CEO / Board** con memo esecutivo (1 pagina):
- Perché serve (obbligo AI Act, gestione rischi)
- Cosa contiene (riassunto 5 punti chiave)
- Costi/risorse (minime se PMI, alcuni giorni/persona per setup)
- Richiesta approvazione formale

**Step 4:** Dopo approvazione, **comunica policy** a tutti i dipendenti:
- Email CEO con allegato policy (PDF)
- Slide deck presentazione (10 slide) in riunione aziendale o town hall
- Policy caricata su intranet / drive aziendale accessibile

**Output atteso:**
- AI Policy approvata e firmata da CEO (PDF)
- Comunicazione inviata a tutti i dipendenti
- Policy disponibile su repository aziendale
- Processo approvazione nuovi tool AI operativo

**Tempo stimato:** 8-12 ore distribuite su 2-3 settimane (redazione, consultazione, approvazione, comunicazione).

**Esempio pratico:**

> **Caso: Studio commercialisti 20 persone (Milano)**
>
> **Policy AI (sintesi):**
> - **Principi:** Trasparenza, privacy, supervisione umana su decisioni clienti
> - **Ruoli:** Titolare studio = approvatore finale; Responsabile IT = valutatore tecnico; Ogni partner = responsabile uso AI nel proprio team
> - **Processo:** Chi vuole usare nuovo tool AI compila "scheda proposta" → IT valuta categoria rischio → Se rischio limitato/minimo, approvazione Responsabile IT; Se alto rischio, approvazione Titolare + consultazione DPO esterno
> - **Incident:** Segnalazione immediata a Titolare se AI causa errore verso cliente (es. report errato)
> - **Formazione:** Workshop annuale 2 ore per tutti i professionisti
>
> **Approvazione:** Titolare approva in riunione soci, policy comunicata via email.

---

### Azione 3 (Settimane 3-6): Gap Analysis - Valutare gap di conformità

**Cosa significa:**
Per ciascun sistema AI identificato (Azione 1), valuti **quanto sei distante** dalla piena conformità AI Act.

**Perché è prioritaria:**
Sai **cosa** devi fare (requisiti AI Act), ma devi capire **quanto lavoro** serve per colmare il gap. Questo ti permette di prioritizzare investimenti e risorse.

**Chi coinvolgere:**
- **Legal / Compliance:** Guidano gap analysis usando checklist AI Act
- **Manager funzioni:** Forniscono info su come usano sistemi AI oggi
- **IT / Data:** Valutano aspetti tecnici (log, dataset, sicurezza)
- **DPO:** Valuta se serve DPIA per sistemi ad alto rischio

**Come eseguirla (step operativi):**

**Step 1:** Per ogni sistema **ad alto rischio** identificato (Azione 1), usa **checklist gap analysis**:

**Checklist Gap Analysis - Sistema Alto Rischio:**

| **Requisito AI Act**              | **Implementato?** | **Gap**                                  | **Azione correttiva**                     | **Owner**  | **Deadline** |
|-----------------------------------|-------------------|------------------------------------------|-------------------------------------------|------------|--------------|
| Human oversight                   | ☐ Sì ☐ No ☐ Parziale | [Descrivi gap se No/Parziale]          | [Azione, es. "Formare recruiter a rivedere shortlist"] | [Nome]     | [Data]       |
| Trasparenza utenti                | ☐ Sì ☐ No ☐ Parziale | [Es. "Candidati non informati che AI è usata"] | [Es. "Aggiungere disclaimer in job posting"] | [Nome]     | [Data]       |
| DPIA condotta                     | ☐ Sì ☐ No         | [Es. "DPIA mai fatta"]                   | [Es. "Condurre DPIA con DPO entro 4 settimane"] | DPO/Legal  | [Data]       |
| Dataset quality audit             | ☐ Sì ☐ No         | [Es. "Dataset mai auditato per bias"]    | [Es. "Analisi demografica dataset CV"]    | IT/Data    | [Data]       |
| Registro decisioni AI             | ☐ Sì ☐ No         | [Es. "Nessun log decisioni"]             | [Es. "Configurare log sistema ATS"]       | IT         | [Data]       |
| Documentazione tecnica            | ☐ Sì ☐ No ☐ Parziale | [Es. "Vendor non ha fornito doc"]        | [Es. "Richiedere doc a vendor o cambiare vendor"] | Legal      | [Data]       |
| Diritto contestazione             | ☐ Sì ☐ No         | [Es. "Nessuna procedura contestazione"]  | [Es. "Creare processo revisione umana"]   | HR         | [Data]       |

**Step 2:** Per sistemi **rischio limitato**, checklist più leggera:

| **Requisito AI Act**              | **Implementato?** | **Gap**                                  | **Azione correttiva**                     | **Owner**  | **Deadline** |
|-----------------------------------|-------------------|------------------------------------------|-------------------------------------------|------------|--------------|
| Trasparenza (disclaimer)          | ☐ Sì ☐ No         | [Es. "Chatbot non dichiara di essere AI"]| [Es. "Aggiungere avviso chatbot"]         | Marketing  | [Data]       |
| Registro AI (tracciamento uso)    | ☐ Sì ☐ No         | [Es. "Tool non documentato"]             | [Es. "Aggiungere al registro aziendale"]  | IT         | [Data]       |

**Step 3:** Consolida tutti i gap in un **report gap analysis** (documento Word/Excel, 2-3 pagine):
- Lista sistemi AI
- Per ciascuno: stato attuale vs requisiti AI Act
- Gap prioritari (alto rischio = priorità 1)
- Piano azioni correttive con owner e deadline

**Step 4:** Presenta report a **management** con richiesta risorse (tempo, budget, persone).

**Output atteso:**
- Report gap analysis completo (2-3 pagine)
- Lista 5-10 azioni correttive prioritarie con owner e deadline
- Identificazione sistemi "non recuperabili" (se esistono tool non conformabili, decidere se discontinuare)

**Tempo stimato:** 10-16 ore distribuite su 3-4 settimane (analisi sistema per sistema, consultazione stakeholder, redazione report).

**Esempio pratico:**

> **Caso: E-commerce fashion 40 dipendenti (Roma)**
>
> **Sistema ad alto rischio identificato:** Nessuno (usano solo chatbot e ChatGPT, entrambi rischio limitato)
>
> **Gap principali (rischio limitato):**
> - **Chatbot sito web:** Non informa utenti che è AI → **Gap:** Aggiungi disclaimer entro 2 settimane (Owner: Marketing)
> - **ChatGPT (contenuti social):** Nessuna policy su cosa può/non può generare → **Gap:** Integra linee guida uso ChatGPT in AI Policy (Owner: Legal)
> - **Registro AI:** Non esiste → **Gap:** Crea registro con 3 tool usati (Owner: IT)
>
> **Azioni correttive:** 3 azioni, tutte entro 4 settimane, budget zero (solo tempo interno).

---

### Azione 4 (Settimane 4-8): Vendor Due Diligence - Valutare fornitori AI

**Cosa significa:**
Chiedi ai tuoi **fornitori di software/servizi AI** (OpenAI, Microsoft, vendor SaaS) di dimostrare che sono conformi all'AI Act. Negozi **clausole contrattuali** che ti proteggono.

**Perché è prioritaria:**
Come **deployer**, hai responsabilità anche se non sviluppi l'AI. Ma puoi (e devi) **condividere responsabilità con il fornitore** tramite contratto. Se il vendor non è conforme, sei esposto a rischi legali.

**Chi coinvolgere:**
- **Legal:** Negozia contratti e clausole AI Act
- **Procurement / Acquisti:** Gestisce relazione commerciale con vendor
- **IT:** Valuta aspetti tecnici (sicurezza, integrazione, log)
- **Manager funzione:** Utenti finali del tool, valutano funzionalità vs conformità

**Come eseguirla (step operativi):**

**Step 1:** Per ogni fornitore AI nel tuo registro (Azione 1), invia **questionario vendor AI** (template scaricabile):

**Questionario Vendor AI (10-15 domande campione):**

**Sezione A: Conformità AI Act**
1. Il vostro sistema AI è classificato come alto rischio, rischio limitato, o rischio minimo secondo l'AI Act?
2. Avete condotto una valutazione di conformità AI Act? Se sì, potete fornire documentazione?
3. (Se alto rischio) Il sistema ha marcatura CE o autocertificazione di conformità?
4. Fornite documentazione tecnica del sistema (descrizione funzionamento, dataset, accuracy)?

**Sezione B: Dataset e Bias**
5. Quali dataset avete usato per training del sistema AI?
6. Avete condotto audit per rilevare bias (genere, età, etnia)? Se sì, quali risultati?
7. Come mitigate bias nel sistema?

**Sezione C: Sicurezza e Robustezza**
8. Quali misure di sicurezza implementate per proteggere dati clienti?
9. Come gestite errori o malfunzionamenti del sistema AI?
10. Fornite log delle decisioni AI per audit clienti?

**Sezione D: Supporto Conformità Clienti**
11. Supportate i clienti (deployer) nella conduzione di DPIA?
12. Fornite template informativi per trasparenza verso utenti finali?
13. In caso di incident AI che coinvolge nostri dati/utenti, qual è la vostra procedura di notifica?

**Sezione E: Responsabilità**
14. In caso di non conformità AI Act del vostro sistema, chi è responsabile? (Vendor o cliente deployer?)
15. Siete disponibili a includere clausole contrattuali AI Act che definiscono responsabilità?

**Step 2:** Analizza risposte vendor:
- **Vendor "maturo":** Risponde a tutte le domande con documentazione, dimostra conformità → OK, procedi
- **Vendor "in progress":** Risponde parzialmente, sta lavorando su conformità → Negozia timeline e clausole di garanzia
- **Vendor "impreparato":** Non sa rispondere, non ha documentazione → **Red flag**, valuta alternative

**Step 3:** Negozia **clausole contrattuali AI Act** (5 clausole modello):

**Clausole Contrattuali AI Act (template):**

**Clausola 1 - Obbligo conformità normativa:**
> "Il Fornitore garantisce che il sistema AI fornito è conforme all'EU AI Act (Regolamento UE 2024/1689) e a tutte le normative applicabili. Il Fornitore si impegna a mantenere la conformità per tutta la durata del contratto e a notificare tempestivamente il Cliente di eventuali modifiche normative che impattano il sistema."

**Clausola 2 - Diritto audit e ispezione:**
> "Il Cliente ha diritto di richiedere audit e ispezioni del sistema AI fornito, inclusa la possibilità di verificare documentazione tecnica, log decisioni, e risultati test bias. Il Fornitore si impegna a collaborare con audit di terze parti nominati dal Cliente o da autorità competenti."

**Clausola 3 - Responsabilità in caso non conformità:**
> "In caso di non conformità del sistema AI all'AI Act rilevata da autorità o da audit Cliente, il Fornitore è responsabile per:
> - Costi di remediation (correzioni sistema)
> - Sanzioni amministrative imputabili al sistema (se causate da difetti sistema)
> - Supporto al Cliente nella gestione incident e comunicazioni autorità
> Il Cliente resta responsabile per uso conforme del sistema secondo istruzioni Fornitore."

**Clausola 4 - Supporto per DPIA/IAIA:**
> "Il Fornitore fornisce al Cliente:
> - Documentazione tecnica necessaria per condurre DPIA/IAIA (descrizione sistema, dataset, rischi noti)
> - Template informativi per trasparenza verso utenti finali
> - Supporto consulenziale (max X ore/anno) per conformità AI Act
> Il Fornitore aggiorna la documentazione entro 30 giorni da modifiche significative al sistema."

**Clausola 5 - Procedura incident e notifica:**
> "In caso di incident AI (malfunzionamento, bias rilevato, violazione dati, decisione errata grave), il Fornitore notifica il Cliente entro 24 ore. Il Fornitore conduce root cause analysis e implementa correzioni entro [X giorni]. Il Cliente ha diritto di sospendere uso del sistema fino a risoluzione incident."

**Step 4:** Aggiorna contratti esistenti o inserisci clausole in rinnovi/nuovi contratti.

**Output atteso:**
- Questionario inviato a tutti i vendor AI (5-10 fornitori tipicamente)
- Report vendor analysis: quali vendor sono "AI Act ready", quali no
- Contratti aggiornati con clausole AI Act (priorità: vendor sistemi ad alto rischio)
- Decisione su vendor non-compliant: attendere loro conformità, cambiare vendor, o discontinuare tool

**Tempo stimato:** 12-20 ore distribuite su 4-6 settimane (preparazione questionario, invio, follow-up, analisi, negoziazione clausole).

**Esempio pratico:**

> **Caso: PMI tech 100 dipendenti (Torino)**
>
> **Vendor AI usati:**
> 1. **OpenAI (ChatGPT Enterprise):** Risposta completa a questionario, documentazione fornita, clausole standard già AI Act-compliant → OK
> 2. **Vendor X (Software HR screening CV):** Risposta parziale, non hanno ancora DPIA, ma si impegnano a fornirla entro 6 mesi → Negoziata clausola "Vendor completa conformità entro 6 mesi o Cliente può recedere senza penali"
> 3. **Vendor Y (Chatbot economico):** Nessuna risposta, contratto non prevede conformità → **Decisione:** Sostituire con vendor più maturo entro 3 mesi

---

### Azione 5 (Settimane 6-12): Formazione e Comunicazione - Awareness interna

**Cosa significa:**
Formi il personale sull'AI Act e comunichi la nuova **AI Policy aziendale**. Senza awareness interna, policy e controlli restano "sulla carta".

**Perché è prioritaria:**
Il 90% dei rischi AI deriva da **uso improprio inconsapevole** (es. dipendente usa ChatGPT per dati sensibili senza capire rischi, recruiter scarta candidati basandosi solo su AI senza revisione). La formazione previene violazioni.

**Chi coinvolgere:**
- **HR:** Organizza formazione, gestisce logistica
- **Legal / Compliance:** Prepara contenuti formativi
- **CEO:** Comunica sponsorship (email, video, townhall)
- **Manager funzioni:** Facilitano partecipazione team e rinforzano messaggi

**Come eseguirla (step operativi):**

**Step 1:** Definisci **piano formazione a 3 livelli**:

**Livello 1 - Awareness generale (30 minuti, tutti i dipendenti):**
- **Contenuti:**
  - Cos'è l'AI Act in 5 minuti (video o slide)
  - Perché riguarda anche te (esempi concreti per funzione)
  - La nostra AI Policy: cosa puoi/non puoi fare
  - Come segnalare problemi (contact point)
- **Formato:** Webinar live (30 min) o video on-demand + quiz 5 domande
- **Frequenza:** Una volta entro 90 giorni, poi refresh annuale

**Livello 2 - Formazione ruoli chiave (60-90 minuti, utenti AI: HR, marketing, IT, legal):**
- **Contenuti:**
  - Approfondimento AI Act per la tua funzione (es. HR → recruitment ad alto rischio, obblighi human oversight)
  - Come usare tool AI in modo conforme (esempi pratici, case study)
  - Red flag da evitare (cosa può causare incident)
  - Procedura approvazione nuovi tool
- **Formato:** Workshop interattivo (presenza o Zoom) con Q&A
- **Frequenza:** Una volta entro 90 giorni, poi refresh annuale + training on-the-job per nuovi assunti

**Livello 3 - Workshop pratico compliance team (mezza giornata, compliance/IT/legal/DPO):**
- **Contenuti:**
  - Come condurre DPIA/IAIA (pratica su caso reale)
  - Come auditare dataset per bias
  - Come gestire incident AI
  - Come negoziare contratti vendor
- **Formato:** Workshop hands-on con esercizi pratici
- **Frequenza:** Una volta entro 90 giorni, poi refresh annuale

**Step 2:** Organizza **comunicazione CEO** (strategia change management):

**Comunicazione CEO - Lancio AI Policy (template email):**

> **Oggetto:** La nostra nuova AI Policy: innovazione responsabile
>
> Cari colleghi,
>
> L'intelligenza artificiale è una grande opportunità per la nostra azienda. Usata bene, ci aiuta a lavorare meglio, più velocemente, più creativamente.
>
> Ma l'AI porta anche responsabilità. Dal 2024 l'Unione Europea ha introdotto l'**AI Act**, la prima legge al mondo che regola l'intelligenza artificiale. E anche noi, come PMI, dobbiamo conformarci.
>
> Per questo abbiamo creato la nostra **AI Policy aziendale** [link allegato]. Non è burocrazia: è una guida pratica per usare AI in modo sicuro, trasparente, ed etico.
>
> **Cosa cambia per te:**
> - Se usi strumenti AI (ChatGPT, Copilot, altri), devi rispettare alcune regole semplici
> - Se vuoi introdurre un nuovo tool AI, serve approvazione (processo rapido)
> - Se noti problemi o hai dubbi, puoi segnalare a [contact point]
>
> Nelle prossime settimane organizzeremo **formazione per tutti** (30 minuti, obbligatoria). Partecipa: ti spiegheremo tutto con esempi concreti, zero legalese.
>
> L'AI è un alleato potente. Usiamolo con intelligenza (umana!).
>
> [Nome CEO]

**Step 3:** Crea **FAQ dipendenti** (top 10 domande con risposte brevi):

**FAQ AI Act per Dipendenti (esempi):**

**Q1: Posso usare ChatGPT per scrivere documenti di lavoro?**
A: Sì, ma non inserire dati sensibili (dati personali clienti, info riservate aziendali). Rivedi sempre output AI prima di usarlo.

**Q2: Devo dire ai clienti se uso AI per rispondere alle loro email?**
A: Se usi AI per email automatizzate o chatbot, sì (obbligo trasparenza). Se usi AI come assistente per scrivere email che poi invii tu, no (sei tu a firmare).

**Q3: Come faccio a sapere se un tool AI è ad alto rischio?**
A: Chiedi a [contact point]. In generale: se il tool decide automaticamente su persone (assunzioni, valutazioni, credito), è alto rischio.

**Q4: Cosa succede se uso AI senza approvazione?**
A: Non è un licenziamento immediato (!), ma viola la policy aziendale. Prima volta: warning e formazione. Violazioni ripetute: sanzioni disciplinari.

**Q5: Ho notato che il nostro software AI sembra discriminare donne. Cosa faccio?**
A: Segnala subito a [AI Owner/Compliance]. È un incident potenzialmente grave, grazie per averlo notato.

[... altre 5 FAQ su procurement, privacy, incident, formazione, supporto ...]

**Step 4:** Monitora partecipazione formazione e **certifica** completamento (registro training).

**Output atteso:**
- Piano formazione 3 livelli definito e calendarizzato
- Email CEO inviata a tutti
- FAQ pubblicate su intranet / drive
- Webinar awareness generale erogato (100% partecipazione target)
- Workshop ruoli chiave erogati (80%+ partecipazione)
- Registro training aggiornato (chi ha fatto cosa)

**Tempo stimato:** 16-24 ore distribuite su 6-8 settimane (preparazione contenuti, organizzazione sessioni, erogazione, follow-up).

**Esempio pratico:**

> **Caso: Agenzia marketing 30 persone (Bologna)**
>
> **Piano formazione:**
> - **Awareness generale:** Webinar live 30 min (venerdì 14:30, tutta l'agenzia) + video registrato per assenti → Partecipazione 95%
> - **Formazione team marketing/content:** Workshop 90 min su uso ChatGPT/Midjourney conforme (trasparenza, watermark, non copiare) → Partecipazione 100% (obbligatorio)
> - **Workshop compliance (CEO + 2 manager):** Mezza giornata con consulente esterno su DPIA e contratti vendor → Completato
>
> **Comunicazione:**
> - Email CEO con video messaggio (2 min)
> - FAQ su Notion aziendale (aggiornate settimanalmente con nuove domande team)
> - Slack channel #ai-act per domande veloci
>
> **Risultato:** Zero incident AI nei primi 3 mesi post-lancio policy.

---

## 4.2 Matrice Ruoli e Responsabilità

Hai visto le 5 azioni. Ma **chi fa cosa**? Ecco una matrice RACI (Responsible, Accountable, Consulted, Informed) per chiarire ruoli.

### RACI Matrix: Conformità AI Act

| **Azione / Deliverable**           | **CEO/Board** | **Legal/Compliance** | **IT/Data** | **HR**  | **Marketing** | **DPO** |
|------------------------------------|---------------|----------------------|-------------|---------|---------------|---------|
| **Inventory AI (Azione 1)**         | I             | A                    | R           | C       | C             | C       |
| **AI Policy (Azione 2)**            | A             | R                    | C           | C       | C             | C       |
| **Gap Analysis (Azione 3)**         | I             | A                    | R           | C       | C             | C       |
| **Vendor Due Diligence (Azione 4)** | I             | R/A                  | C           | I       | I             | C       |
| **Formazione (Azione 5)**           | A (sponsor)   | R (contenuti)        | C           | R (logistica) | C   | C       |
| **DPIA sistemi alto rischio**       | I             | C                    | C           | R (se HR AI) | I  | A       |
| **Human oversight (sistemi HR)**    | I             | C                    | C           | A/R     | I             | C       |
| **Registro AI (manutenzione)**      | I             | C                    | A/R         | C       | C             | I       |
| **Gestione incident AI**            | A (decision)  | R (coordinamento)    | R (tecnico) | C       | C             | C       |

**Legenda:**
- **R = Responsible** (chi esegue il lavoro)
- **A = Accountable** (chi approva e ha responsabilità finale)
- **C = Consulted** (chi viene consultato per input)
- **I = Informed** (chi viene informato dei risultati)

### Descrizione Ruoli per Funzione

**CEO / Board:**
- **Responsabilità principali:**
  - Approva AI policy e budget conformità
  - Sponsorizza cultura AI responsabile (comunicazione top-down)
  - Decide su rischi strategici (es. discontinuare un sistema AI non conformabile)
- **Tempo stimato:** 4-6 ore nei 90 giorni (approvazioni, comunicazione, decisioni strategiche)

**Legal / Compliance (o AI Owner se ruolo dedicato):**
- **Responsabilità principali:**
  - Coordina tutte le 5 azioni (project manager conformità)
  - Redige AI policy, contratti vendor, clausole
  - Conduce gap analysis
  - Prepara contenuti formativi
  - Gestisce incident AI (coordinamento)
- **Tempo stimato:** 40-60 ore nei 90 giorni (ruolo più impegnato)

**IT / Data:**
- **Responsabilità principali:**
  - Crea e mantiene registro AI
  - Classifica sistemi AI (supporto tecnico)
  - Audit dataset per bias
  - Configura log e sicurezza sistemi
  - Supporto tecnico vendor due diligence
- **Tempo stimato:** 20-30 ore nei 90 giorni

**HR:**
- **Responsabilità principali:**
  - Implementa human oversight per sistemi HR (recruitment, valutazione)
  - Conduce DPIA per sistemi HR ad alto rischio
  - Organizza formazione (logistica, calendario, tracking)
  - Comunica policy a dipendenti
- **Tempo stimato:** 16-24 ore nei 90 giorni

**Marketing:**
- **Responsabilità principali:**
  - Implementa trasparenza per chatbot e contenuti AI-generated
  - Aggiorna disclaimer e watermark
  - Usa tool AI secondo policy
- **Tempo stimato:** 8-12 ore nei 90 giorni

**DPO (Data Protection Officer):**
- **Responsabilità principali:**
  - Approva DPIA (obbligatorio per GDPR)
  - Rivede AI policy per coerenza GDPR
  - Consulenza su privacy + AI Act
  - Audit conformità annuale
- **Tempo stimato:** 12-16 ore nei 90 giorni

**Nota:** Se PMI piccola (<50 dipendenti) senza DPO, il ruolo può essere coperto da Legal o consulente esterno part-time.

---

## 4.3 Vendor AI Due Diligence

Hai già visto l'Azione 4 (vendor due diligence) nella roadmap. Qui approfondiamo con checklist operativa.

### Checklist Negoziazione Contratti AI

Usa questa checklist quando negozi/rinnovi un contratto con vendor AI:

- [ ] **Questionario vendor compilato:** Hai ricevuto risposte a tutte le 15 domande (sezione 4.1)
- [ ] **Documentazione conformità AI Act fornita:** Vendor ha condiviso DPIA, certificazioni, audit bias
- [ ] **Categoria rischio AI Act dichiarata:** Vendor ha classificato il sistema (alto/limitato/minimo)
- [ ] **Clausola conformità normativa inserita:** Contratto include obbligo vendor di rispettare AI Act
- [ ] **Clausola diritto audit inserita:** Puoi richiedere ispezioni o audit terzi
- [ ] **Clausola responsabilità incident inserita:** Chiaro chi paga/fa cosa in caso incident
- [ ] **Clausola supporto DPIA inserita:** Vendor fornisce doc tecnica per tue DPIA
- [ ] **Clausola notifica modifiche inserita:** Vendor ti avvisa se cambia sistema AI significativamente
- [ ] **SLA incident definito:** Tempo massimo risposta vendor in caso problema (es. 24h notifica, 7 giorni fix)
- [ ] **Exit strategy definita:** Se vendor non rispetta conformità, puoi recedere senza penali (o con penali ridotte)

**Punteggio:** 10/10 = Contratto AI Act-proof | 7-9/10 = Buono | <7/10 = Rivedi contratto

---

## 4.4 Comunicazione Interna e Change Management

Hai già visto l'Azione 5 (formazione e comunicazione). Qui aggiungiamo tone e best practices.

### Tone e Messaggi Chiave

**Tone giusto per comunicazione AI Act:**
- ✅ **Opportunità, non minaccia:** "L'AI Act ci aiuta a usare AI meglio, non a usarla meno."
- ✅ **Pratico, non teorico:** "Ecco cosa cambia per te lunedì mattina."
- ✅ **Rassicurante, non allarmista:** "Non è complesso, ci siamo preparati."
- ✅ **Inclusivo, non top-down:** "Tutti contribuiamo alla conformità, non solo legal."

**Tone sbagliato (da evitare):**
- ❌ **Burocratico:** "Conformemente al Regolamento UE 2024/1689..."
- ❌ **Punitivo:** "Chi viola la policy sarà sanzionato..."
- ❌ **Vago:** "Dobbiamo essere più attenti all'AI..."
- ❌ **Passivo:** "L'AI Act ci obbliga a..." → Preferisci: "Abbiamo scelto di..."

### Template Comunicazione (slide deck outline)

**Slide Deck AI Policy - 10 Slide (per townhall aziendale):**

**Slide 1: Titolo**
- "AI Responsabile: La Nostra Politica AI"
- [Logo azienda]

**Slide 2: Perché parliamo di AI oggi?**
- L'AI è già qui: [X]% di noi usa ChatGPT, Copilot, tool AI ogni giorno
- Grandi opportunità: efficienza, creatività, competitività
- Ma serve responsabilità: privacy, equità, trasparenza

**Slide 3: Cos'è l'AI Act (in 60 secondi)**
- Prima legge mondiale su AI (UE, 2024)
- Obiettivo: Bilanciare innovazione e protezione diritti
- Riguarda anche noi (PMI): Obblighi leggeri ma chiari

**Slide 4: Le 4 categorie AI Act (visual con icone colorate)**
- 🔴 Proibito (non possiamo usare)
- 🟠 Alto Rischio (serve controlli rigorosi)
- 🟡 GPAI (fornitori responsabili, noi deployer)
- 🟢 Limitato/Minimo (trasparenza sufficiente)

**Slide 5: I nostri sistemi AI (esempi concreti azienda)**
- Tool X (Marketing) → 🟢 Rischio Limitato
- Tool Y (HR) → 🟠 Alto Rischio
- Tool Z (Operations) → 🟢 Rischio Minimo
- [Visual: registro AI semplificato]

**Slide 6: La nostra AI Policy - 5 Principi**
- Trasparenza
- Fairness
- Privacy
- Supervisione umana
- Responsabilità
- [Visual: icona per ciascun principio]

**Slide 7: Cosa cambia per te (pratico)**
- ✅ Puoi usare ChatGPT/Copilot per lavoro (con regole)
- ⚠️ Non inserire dati sensibili clienti/aziendali
- ✅ Nuovi tool AI? Chiedi approvazione (processo veloce)
- ✅ Noti problemi AI? Segnala a [contact point]

**Slide 8: Formazione obbligatoria**
- **Tutti:** Webinar 30 min [data] → Segna in agenda
- **Utenti AI (HR/Marketing/IT):** Workshop 90 min [date]
- **Compliance team:** Training approfondito [data]
- Certificato partecipazione rilasciato

**Slide 9: Supporto disponibile**
- **Domande?** FAQ su [intranet/drive]
- **Dubbi operativi?** Slack #ai-act o email [contact point]
- **Incident?** Procedura segnalazione [link]

**Slide 10: Messaggio finale**
- "L'AI è un alleato, se usato con intelligenza (umana!)."
- "Grazie per contribuire a un uso responsabile dell'AI."
- [Logo azienda + claim]

---

## 4.5 Metriche e Monitoraggio

Non puoi migliorare ciò che non misuri. Ecco i **KPI chiave** per monitorare la conformità AI Act.

### KPI Conformità AI Act (5 KPI con target)

| **KPI**                                    | **Metrica**                          | **Target**              | **Frequenza** | **Owner**         |
|--------------------------------------------|--------------------------------------|-------------------------|---------------|-------------------|
| **1. Copertura inventory AI**              | % sistemi AI censiti / totali stimati| 100% entro 90 giorni    | Mensile       | IT/Compliance     |
| **2. AI Policy approvata**                 | Sì/No + data approvazione            | Approvata entro 30 gg   | One-time      | Legal             |
| **3. DPIA completate (alto rischio)**      | N° DPIA condotte / N° sistemi alto rischio | 100% entro 90 giorni | Mensile       | DPO/Legal         |
| **4. Vendor AI valutati**                  | % vendor che hanno risposto questionario / totale vendor | 80% entro 60 giorni | Mensile | Legal/Procurement |
| **5. Dipendenti formati**                  | % dipendenti che hanno completato awareness / totale | 100% entro 90 giorni | Settimanale | HR                |

**KPI aggiuntivi (opzionali ma consigliati):**
- **Incident AI:** N° incident rilevati / risolti (target: <2 incident/trimestre, 100% risolti entro 30 gg)
- **Gap di conformità chiusi:** % gap correttivi completati / totale gap (target: 70% entro 90 giorni)
- **Contratti vendor aggiornati:** N° contratti con clausole AI Act / totale contratti vendor AI (target: 100% entro 6 mesi)

### Dashboard Monitoraggio (template Excel)

**Dashboard KPI Conformità AI Act (Excel con grafici):**

**Tab 1: Overview**

| **KPI**                        | **Target**       | **Attuale**  | **Status**       | **Prossima Milestone**       |
|--------------------------------|------------------|--------------|------------------|------------------------------|
| Inventory AI                   | 100%             | 85%          | 🟡 In progress   | Completare entro 15/11       |
| AI Policy                      | Approvata        | Approvata    | 🟢 OK            | -                            |
| DPIA (alto rischio)            | 2/2 completate   | 1/2          | 🟡 In progress   | DPIA sistema HR entro 20/11  |
| Vendor valutati                | 80%              | 60%          | 🟡 In progress   | Sollecito vendor X entro 10/11|
| Dipendenti formati             | 100%             | 75%          | 🟡 In progress   | Webinar recovery 18/11       |

**Tab 2: Dettaglio Azioni (Gantt semplificato)**

[Tabella con colonne: Azione | Owner | Start | End | Status | % Completamento | Note]

**Tab 3: Incident Log**

[Tabella con colonne: Data | Sistema AI | Descrizione | Gravità | Owner | Status | Data Risoluzione | Azioni Correttive]

**Grafici suggeriti:**
- **Grafico a torta:** % sistemi AI per categoria rischio (🔴🟠🟡🟢)
- **Grafico barre:** % completamento 5 azioni chiave (Inventory, Policy, Gap, Vendor, Formazione)
- **Grafico linea:** Trend formazione dipendenti (% settimanale)

### Frequency Review

**Primi 6 mesi (fase setup):**
- **Review mensile** con compliance team (1 ora, revisionare dashboard, sbloccare criticità)
- **Report mensile a CEO/Board** (1 pagina, highlight progress + eventuali escalation)

**Dopo 6 mesi (fase run):**
- **Review trimestrale** (verifica KPI, audit sistemi ad alto rischio, aggiornamento policy se necessario)
- **Report semestrale a CEO/Board**

**Audit annuale completo:**
- Revisione registro AI (sistemi aggiunti/rimossi)
- DPIA refresh per sistemi ad alto rischio
- Audit bias dataset (campionamento)
- Formazione refresh (tutti i dipendenti)
- Aggiornamento contratti vendor

---

## Attività Interattiva - Activity Builder

**Obiettivo:** Costruisci il tuo piano 90 giorni personalizzato selezionando azioni, assegnando ruoli, e definendo timeline.

**Istruzioni:**

**Step 1: Seleziona le tue 5 azioni prioritarie**

Ti vengono proposte **8-10 azioni** tra cui scegliere le **5 più rilevanti** per la tua azienda. Le 5 azioni standard (Inventory, Policy, Gap, Vendor, Formazione) sono sempre consigliate, ma puoi personalizzare.

**Azioni disponibili (scegli 5):**
1. ✅ **Inventory AI** (obbligatorio, sempre consigliato)
2. ✅ **AI Policy** (obbligatorio, sempre consigliato)
3. ✅ **Gap Analysis** (obbligatorio per sistemi alto rischio)
4. ✅ **Vendor Due Diligence** (obbligatorio se usi vendor esterni)
5. ✅ **Formazione e Comunicazione** (obbligatorio)
6. **DPIA per sistema alto rischio specifico** (se hai identificato sistema HR/credit scoring/etc.)
7. **Configurare log e registro decisioni** (per sistemi alto rischio, tecnico)
8. **Audit bias dataset** (se hai sistemi con dataset proprietari)
9. **Revisione contratti vendor esistenti** (se hai già contratti da aggiornare)
10. **Implementare human oversight per sistema X** (se hai sistema alto rischio senza supervisione)

**Suggerimenti basati su profilo:**
- **PMI manifatturiera (50 dip., usa AI per controllo qualità + HR):** Scegli 1, 2, 3, 4, 5 (+ 6 per sistema HR)
- **PMI servizi (20 dip., usa solo ChatGPT/Copilot):** Scegli 1, 2, 4, 5 (+ azione leggera come configurare registro)
- **PMI tech (100 dip., sviluppa software con AI):** Scegli 1, 2, 3, 4, 5 (+ azioni tecniche come audit bias, human oversight)

**Step 2: Assegna owner (responsabile) per ciascuna azione**

Dropdown per ciascuna azione:
- CEO/Board
- Legal/Compliance
- IT/Data
- HR
- Marketing
- DPO
- Consulente esterno

**Nota:** Alcuni owner sono pre-popolati (es. AI Policy → Legal/Compliance), ma puoi cambiare.

**Step 3: Definisci timeline (drag & drop su calendario 12 settimane)**

Visual calendar: 12 settimane (asse X) con 5 righe (azioni selezionate).

**Esempio drag & drop:**
- Inventory AI: Settimana 1-2 (trascina barra su settimane 1-2)
- AI Policy: Settimana 2-4
- Gap Analysis: Settimana 3-6
- Vendor Due Diligence: Settimana 4-8
- Formazione: Settimana 6-12

**Controllo conflitti:** Sistema avvisa se due azioni con stesso owner si sovrappongono troppo (rischio sovraccarico).

**Step 4: Stima risorse (ore/persona, budget se applicabile)**

Per ciascuna azione, inserisci:
- **Ore/persona stimate:** [Campo numerico] (il sistema suggerisce range basato su azione)
- **Budget stimato (opzionale):** [Campo numerico] (es. consulente esterno, software, formazione)

**Esempio:**
- Inventory AI: 8 ore (IT + Compliance)
- AI Policy: 12 ore (Legal) + €0 (interno)
- Formazione: 20 ore (HR + Legal) + €1500 (consulente esterno per workshop livello 3)

**Step 5: Visualizza il tuo piano 90 giorni**

Output automatico:

**Gantt semplificato:** Visual con 5 azioni su timeline 12 settimane, colori per owner.

**Tabella riassuntiva:**

| **Azione**              | **Owner**         | **Settimane** | **Ore** | **Budget** | **Output Atteso**                         |
|-------------------------|-------------------|---------------|---------|------------|-------------------------------------------|
| Inventory AI            | IT + Compliance   | 1-2           | 8       | €0         | Registro AI con 10 sistemi classificati   |
| AI Policy               | Legal             | 2-4           | 12      | €0         | Policy approvata e comunicata             |
| Gap Analysis            | Legal + IT        | 3-6           | 14      | €0         | Report gap + 5 azioni correttive          |
| Vendor Due Diligence    | Legal             | 4-8           | 16      | €0         | Questionari + clausole contratti          |
| Formazione              | HR + Legal        | 6-12          | 20      | €1500      | 100% dipendenti formati                   |
| **TOTALE**              |                   | 12 settimane  | **70**  | **€1500**  |                                           |

**Alert automatici:**
- ⚠️ "Legal ha 42 ore assegnate nei primi 30 giorni. Considera di distribuire o delegare alcune attività."
- ⚠️ "Budget totale €1500. Confermi? [Sì/Rivedi]"

**Step 6: Scarica il tuo piano**

**Formato download:**
- **PDF** (1-2 pagine, pronto per presentazione management)
- **Excel** (con formule, modificabile, include dashboard KPI)
- **Google Sheet** (condivisibile con team)

**Contenuto PDF:**
- Intestazione: [Nome azienda] - Piano 90 Giorni Conformità AI Act
- Gantt visual
- Tabella azioni
- Milestone chiave (es. "Fine mese 1: Policy approvata", "Fine mese 2: DPIA completata", "Fine mese 3: 100% dipendenti formati")
- Owner e contact points
- Prossimi step (azioni settimana 1)

**Tempo attività:** 12-15 minuti

---

## Compito Opzionale - Mini-Piano 1 Pagina

**Obiettivo:** Compila un template strutturato per creare il tuo piano operativo di 1 pagina.

**Quando usarlo:**
- Se l'activity builder non è disponibile (corso PDF o stampa)
- Se preferisci scrivere manualmente
- Se vuoi un documento formale da presentare a CEO/Board

**Template Mini-Piano 1 Pagina (Word/PDF compilabile):**

---

**PIANO 90 GIORNI - CONFORMITÀ AI ACT**

**Azienda:** [Nome azienda]
**Settore:** [Es. Manifattura, Servizi, Tech, Retail]
**Dimensione:** [N° dipendenti]
**Data piano:** [Data]
**Responsabile piano:** [Nome, ruolo]

---

**SEZIONE 1: CONTESTO AZIENDA (max 100 parole)**

Descrivi brevemente:
- Quali sistemi AI usi attualmente (nome tool, funzione)
- Quale categoria rischio AI Act (alto/limitato/minimo)
- Principale driver conformità (es. "Usiamo AI per recruitment, sistema alto rischio, deadline agosto 2026")

[Campo testo libero, max 100 parole]

---

**SEZIONE 2: 5 AZIONI CON OWNER, DEADLINE, DELIVERABLE**

| **Azione**              | **Owner (Nome/Ruolo)** | **Deadline** | **Deliverable**                           | **Risorse (ore/budget)** |
|-------------------------|------------------------|--------------|-------------------------------------------|--------------------------|
| 1. [Es. Inventory AI]   | [Es. Mario Rossi, IT]  | [15/11/2024] | [Registro AI con 8 sistemi classificati]  | [8 ore, €0]              |
| 2. [Es. AI Policy]      | [Laura Bianchi, Legal] | [30/11/2024] | [Policy approvata CEO]                    | [12 ore, €0]             |
| 3. [Es. Gap Analysis]   | [...]                  | [...]        | [...]                                     | [...]                    |
| 4. [Es. Vendor DD]      | [...]                  | [...]        | [...]                                     | [...]                    |
| 5. [Es. Formazione]     | [...]                  | [...]        | [...]                                     | [...]                    |

---

**SEZIONE 3: RISCHI E MITIGAZIONI**

Identifica 2-3 rischi principali che potrebbero far deragliare il piano, e come mitigarli.

| **Rischio**                                  | **Probabilità (A/M/B)** | **Impatto (A/M/B)** | **Mitigazione**                                    |
|----------------------------------------------|-------------------------|---------------------|----------------------------------------------------|
| [Es. Vendor non risponde a questionario]     | M                       | A                   | [Escalation a livello commerciale, deadline formale] |
| [Es. Budget formazione non approvato]        | B                       | M                   | [Formazione interna, zero consulenti esterni]      |
| [Es. IT sovraccarico, non completa inventory]| M                       | A                   | [Delegare parte inventory a compliance]            |

---

**SEZIONE 4: KPI E MILESTONES**

**KPI principali:**
- [ ] Inventory AI completato (100% sistemi censiti)
- [ ] AI Policy approvata e comunicata
- [ ] DPIA completate per sistemi alto rischio (N°: [X])
- [ ] Vendor AI valutati (% target: [Y]%)
- [ ] Dipendenti formati (% target: 100%)

**Milestones chiave (date):**
- **Fine Mese 1:** [Es. Policy approvata, inventory completato]
- **Fine Mese 2:** [Es. Gap analysis completata, vendor valutati]
- **Fine Mese 3:** [Es. Formazione completata, 100% dipendenti certificati]

---

**FIRMA E APPROVAZIONE**

Piano redatto da: _________________________ [Nome, ruolo] Data: _______

Approvato da: _________________________ [CEO / Board] Data: _______

---

**Istruzioni compilazione (inline nel template):**
- **Sezione 1:** Scrivi in modo conciso, focus su "qual è il problema" (es. "Usiamo software HR ad alto rischio, serve conformità urgente").
- **Sezione 2:** 5 azioni concrete. Owner deve essere persona specifica (non "team IT" ma "Mario Rossi, IT Manager"). Deliverable deve essere misurabile (non "fare policy" ma "policy approvata CEO").
- **Sezione 3:** Pensa a cosa può andare storto (vendor lento, budget tagliato, persone sovraccariche) e come prevenire/mitigare.
- **Sezione 4:** KPI devono essere S.M.A.R.T. (specifici, misurabili, raggiungibili, rilevanti, temporizzati).

**Rubrica valutazione (se corso con tutorship):**

| **Criterio**            | **Peso** | **Descrizione Eccellente (25/25)**                                                                 |
|-------------------------|----------|----------------------------------------------------------------------------------------------------|
| **Completezza**         | 25%      | Tutte le 4 sezioni compilate, nessun campo vuoto, deliverable chiari per tutte le 5 azioni        |
| **Fattibilità**         | 25%      | Timeline realistiche (azioni non sovrapposte eccessivamente), risorse (ore/budget) coerenti con dimensione azienda |
| **Allineamento AI Act** | 25%      | Azioni coprono requisiti chiave AI Act (inventory, policy, gap/DPIA, vendor, formazione), focus su sistemi ad alto rischio se presenti |
| **Chiarezza**           | 25%      | Deliverable misurabili, responsabilità chiare (owner nominati), milestones specifiche con date     |

**Punteggio:** 80-100 = Eccellente | 60-79 = Buono | 40-59 = Sufficiente (rivedi alcune sezioni) | <40 = Insufficiente

**Upload opzionale:** Se il corso prevede tutorship, carica il mini-piano compilato per feedback personalizzato da un esperto.

---

## Riepilogo Modulo 4

**Hai imparato:**
- ✓ **Le 5 azioni chiave per i primi 90 giorni:** Inventory AI, AI Policy, Gap Analysis, Vendor Due Diligence, Formazione
- ✓ **Matrice RACI ruoli e responsabilità:** Chi fa cosa (CEO, Legal, IT, HR, Marketing, DPO)
- ✓ **Come valutare fornitori AI:** Questionario 15 domande + 5 clausole contrattuali modello
- ✓ **Strategia comunicazione e change management:** Email CEO, FAQ, piano formazione 3 livelli, tone giusto
- ✓ **KPI e metriche:** 5 KPI chiave + dashboard monitoraggio + frequency review

**Competenze acquisite:**
- ○ Pianificare roadmap 90 giorni con azioni concrete, owner, deadline, deliverable
- ○ Assegnare ruoli e coordinare team multifunzionale (Legal, IT, HR)
- ○ Negoziare con vendor AI e inserire clausole contrattuali AI Act
- ○ Comunicare policy AI internamente con linguaggio chiaro e non-tecnico
- ○ Monitorare progresso con KPI e dashboard operativa

**Materiali scaricabili (disponibili al termine del modulo):**
- Template Piano 90 Giorni (Excel con Gantt automatico)
- RACI Matrix vuota (Excel, personalizzabile)
- Questionario Vendor AI (Word/PDF, 15 domande)
- Clausole Contrattuali AI Act (Word, 5 clausole modello pronte per legal)
- Template Comunicazione Interna:
  - Email CEO (Word)
  - Slide Deck AI Policy (PowerPoint, 10 slide)
  - FAQ Dipendenti (Word, 15 Q&A)
- Dashboard KPI Conformità (Excel con grafici)
- Template Mini-Piano 1 Pagina (Word/PDF compilabile)

---

## Conclusione del Corso

**Complimenti! Hai completato il corso "EU AI Act: essentials e azioni pratiche per PMI".**

**Cosa hai imparato nei 4 moduli:**

**Modulo 1:** Panoramica AI Act, 4 categorie sistemi, timeline 2025-2027, implicazioni per funzione
**Modulo 2:** Framework classificazione, 5 scenari concreti PMI, requisiti per categoria, red flag
**Modulo 3:** AI policy, dataset quality/bias, trasparenza, registri, human oversight, DPIA/IAIA
**Modulo 4:** Piano 90 giorni (5 azioni), ruoli RACI, vendor due diligence, comunicazione, KPI

**Sei ora in grado di:**
- ✓ Distinguere sistemi AI proibiti, alto rischio, e rischio limitato
- ✓ Classificare i tuoi casi d'uso aziendali nelle categorie AI Act
- ✓ Implementare controlli di governance minimi (policy, registri, trasparenza, human oversight)
- ✓ Pianificare e coordinare conformità AI Act nei prossimi 90 giorni
- ✓ Comunicare AI Act al tuo team e management con linguaggio pratico

**Prossimi step (lunedì mattina):**

1. **Scarica tutti i template** da questo corso (policy, registri, questionari, clausole, dashboard)
2. **Avvia Azione 1:** Manda survey interna per inventory AI (tempo: 2 ore setup)
3. **Pianifica meeting kickoff:** 1 ora con Legal/IT/HR per condividere piano 90 giorni
4. **Presenta al management:** Usa mini-piano 1 pagina o slide deck per richiedere sponsorship e risorse
5. **Calendario azioni:** Blocca in agenda le deadline chiave (policy entro 30 giorni, DPIA entro 60 giorni, formazione entro 90 giorni)

**Ricorda:**
- La deadline AI Act per sistemi ad alto rischio è **2 agosto 2026** (20 mesi da oggi)
- Iniziare ora ti dà vantaggio competitivo e riduce stress last-minute
- Conformità AI Act non è solo obbligo legale: è gestione rischio e reputazione

**Certificato Completamento (se applicabile):**
Hai completato tutte le attività e superato il quiz Modulo 3 (≥70%). Scarica il certificato nominativo:
- Nome partecipante
- Titolo corso: "EU AI Act: essentials e azioni pratiche per PMI"
- Data completamento
- Punteggio quiz: [X]/10

**Supporto post-corso (opzionale se previsto):**
- Forum community: [Link]
- Office hours con esperti: [Calendario]
- Aggiornamenti normativi via email (newsletter)

---

**Grazie per aver partecipato. Buona conformità AI Act!**

**Domande?** Contatta: [email supporto]

---

**Fine Modulo 4**

**Fine Corso**
