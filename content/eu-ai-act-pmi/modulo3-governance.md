# Modulo 3: Governance e controlli minimi

**Durata:** 30-35 minuti

**Obiettivi del modulo:**
- Implementare una AI policy aziendale conforme all'AI Act
- Gestire dataset e mitigare bias nei sistemi AI
- Stabilire meccanismi di trasparenza e registri AI
- Applicare human oversight e valutazioni d'impatto (DPIA/IAIA)
- Raggiungere 70% nel quiz sommativo su governance AI

---

## Introduzione al Modulo

Nei Moduli 1 e 2 hai imparato **cosa** dice l'AI Act e **come classificare** i tuoi sistemi AI. Ora è il momento di passare all'azione: **come implementare i controlli di governance minimi** richiesti dalla normativa.

Questo modulo è il più operativo del corso. Ti fornisce:
- **Template pronti all'uso** (AI policy, registri, checklist)
- **Istruzioni passo-passo** per ciascun controllo
- **Esempi già compilati** da PMI italiane fittizie

Alla fine del modulo completerai un **quiz sommativo** (10 domande, soglia 70%) che certifica la tua comprensione. Superare questo quiz è obbligatorio per accedere al Modulo 4 (Piano 90 giorni).

**Tempo di lettura:** 18-20 minuti | **Quiz finale:** 12-15 minuti

---

## 3.1 AI Policy Aziendale

### Cos'è e perché serve

Una **AI policy** è un documento interno (1-2 pagine) che definisce le regole aziendali per l'uso di intelligenza artificiale. È il tuo "manuale operativo" che risponde a domande chiave:
- Chi può approvare l'acquisto di nuovi tool AI?
- Come valutiamo i rischi di un sistema AI prima di usarlo?
- Quali principi etici guidano il nostro uso di AI?
- Cosa facciamo se un sistema AI causa un problema (incident management)?

**Perché è importante:**
- **Compliance AI Act:** Dimostra che hai un framework di governance (richiesto per sistemi ad alto rischio).
- **Gestione rischio:** Previene uso improprio di AI che potrebbe danneggiare l'azienda (legal, reputazione, operativo).
- **Chiarezza interna:** Tutti sanno cosa è permesso e cosa no (evita zona grigia).

### Cosa deve contenere (5 punti chiave)

**1. Principi etici e valori aziendali**

Dichiara i valori che guidano l'uso di AI nella tua azienda. Esempio:

> **Principi guida:**
> - **Trasparenza:** Siamo chiari con dipendenti e clienti quando usiamo AI.
> - **Fairness:** I nostri sistemi AI non discriminano persone in base a genere, età, etnia, disabilità.
> - **Privacy:** Proteggiamo i dati personali e rispettiamo GDPR in ogni uso di AI.
> - **Supervisione umana:** Le decisioni critiche su persone sono sempre prese da umani, non da AI.
> - **Responsabilità:** Identifichiamo sempre un responsabile umano per ciascun sistema AI.

**2. Ruoli e responsabilità**

Definisci chi fa cosa. Esempio tabella:

| **Ruolo**                  | **Responsabilità AI**                                                                 |
|----------------------------|---------------------------------------------------------------------------------------|
| **CEO / Board**            | Approva AI policy, budget per conformità, sponsorizza cultura AI responsabile        |
| **AI Owner / Compliance**  | Coordina conformità AI Act, mantiene registro AI, conduce valutazioni rischio        |
| **IT / Data**              | Gestisce infrastruttura AI, dataset quality, log sistemi, sicurezza                  |
| **Legal**                  | Redige policy, contratti vendor, coordina DPIA, gestisce incident legali             |
| **DPO**                    | Valuta conformità GDPR + AI Act, approva DPIA, audit privacy                         |
| **Manager funzioni**       | Responsabili uso AI nelle loro aree (HR, marketing, operations), training team       |

**3. Processo approvazione nuovi sistemi AI**

Stabilisci un workflow chiaro per introdurre nuovi tool AI. Esempio:

> **Procedura approvazione:**
> 1. **Richiesta:** Manager funzione compila "scheda proposta AI" (descrive tool, fornitore, uso previsto)
> 2. **Classificazione rischio:** IT + Compliance classificano sistema nelle 4 categorie AI Act
> 3. **Valutazione:**
>    - Se **alto rischio** → DPIA obbligatoria + approvazione CEO/Board
>    - Se **rischio limitato** → Valutazione rapida + approvazione Compliance
>    - Se **rischio minimo** → Approvazione Manager + notifica IT
> 4. **Contratto vendor:** Legal negozia clausole AI Act
> 5. **Go-live:** Solo dopo completamento step 1-4 e training utenti

**4. Gestione rischi e incidenti**

Definisci cosa fare se qualcosa va storto. Esempio:

> **Incident AI (cosa considerare incidente):**
> - Decisione AI errata che danneggia una persona (es. candidato scartato ingiustamente)
> - Bias rilevato in sistema già in uso (es. AI discrimina donne)
> - Violazione dati personali tramite sistema AI
> - Malfunzionamento tecnico con impatto operativo significativo
>
> **Procedura incident:**
> 1. Chi rileva problema notifica immediatamente AI Owner + Manager funzione
> 2. AI Owner valuta gravità (critico/medio/basso)
> 3. Se critico: sospendi uso sistema, notifica DPO/Legal, analisi root cause
> 4. Documenta incident in registro (data, sistema, descrizione, azioni correttive)
> 5. Se necessario, notifica autorità (Garante Privacy, autorità AI Act nazionale)

**5. Formazione e awareness**

Impegno a formare il personale. Esempio:

> **Piano formazione:**
> - **Tutti i dipendenti:** Awareness generale AI Act (30 min, annuale)
> - **Manager e utenti AI:** Training specifico su uso responsabile tool AI (60 min, annuale)
> - **Team compliance/IT/Legal:** Workshop approfondito su governance AI (mezza giornata, annuale)
> - **Nuovi assunti:** AI policy inclusa in onboarding

### Template policy (esempio outline 1 pagina)

```
POLICY AZIENDALE - USO INTELLIGENZA ARTIFICIALE

1. SCOPO E AMBITO
   Questa policy regola l'uso di sistemi di intelligenza artificiale in [Nome Azienda],
   garantendo conformità all'EU AI Act e promuovendo uso responsabile.

2. PRINCIPI GUIDA
   - Trasparenza
   - Fairness
   - Privacy
   - Supervisione umana
   - Responsabilità

3. RUOLI E RESPONSABILITÀ
   [Tabella come sopra]

4. PROCESSO APPROVAZIONE NUOVI SISTEMI AI
   [Workflow come sopra]

5. SISTEMI AD ALTO RISCHIO - REQUISITI SPECIALI
   - Human oversight obbligatorio
   - DPIA prima di go-live
   - Trasparenza verso utenti
   - Registro decisioni
   - Audit annuale

6. GESTIONE INCIDENTI
   [Procedura come sopra]

7. FORMAZIONE
   [Piano formazione come sopra]

8. REVISIONE POLICY
   Questa policy è rivista annualmente o quando cambiano normative/sistemi aziendali.
   Responsabile: AI Owner / Compliance

Data approvazione: [Data]
Approvata da: [CEO / Board]
Versione: 1.0
```

### Chi approva la policy

**Raccomandazione:** CEO o Board (massimo livello aziendale) per dare peso e sponsorship.

**Processo:** Legal + Compliance redigono bozza → Consultazione manager funzioni → Approvazione formale CEO/Board → Comunicazione dipendenti.

### Frequenza revisione

**Minimo annuale.** Oppure quando:
- Introduci un nuovo sistema AI ad alto rischio
- Cambia la normativa (es. linee guida nazionali AI Act)
- Dopo un incident grave

---

**🔹 Domanda in-line 1:**

**Chi deve approvare formalmente la AI policy aziendale?**

**Opzioni:**
- A) Il team IT
- B) Il CEO o Board
- C) Il fornitore del software AI
- D) Ogni singolo manager di funzione

**Risposta corretta:** B

**Feedback corretto:** ✓ Giusto! La AI policy deve essere approvata al massimo livello aziendale (CEO/Board) per garantire sponsorship e autorevolezza.

**Feedback errato:** ✗ La AI policy deve essere approvata da **CEO o Board**, non da IT o manager di funzione. Questo garantisce che la policy abbia peso aziendale e risorse dedicate. IT e manager possono contribuire alla redazione, ma l'approvazione formale è top-down.

---

## 3.2 Dataset Quality e Mitigazione Bias

### Perché i dataset sono critici

L'AI Act richiede che i dataset usati per training o input di sistemi AI siano:
- **Di qualità:** Accurati, completi, aggiornati
- **Rappresentativi:** Coprono tutte le categorie rilevanti (no campioni squilibrati)
- **Privi di bias:** Non contengono discriminazioni illegali nascoste

**Esempio pratico:** Se usi AI per recruitment e il dataset contiene solo CV di uomini, l'AI impara che "candidato ideale = uomo" → discrimina donne → violazione AI Act + rischio legal.

### Come identificare bias (3 tipi con esempi)

**1. Bias nei dati storici**

**Definizione:** I dati riflettono discriminazioni del passato.

**Esempio:** Negli ultimi 10 anni la tua azienda ha assunto solo 5% di donne in ruoli tecnici (perché riceveva pochi CV femminili o per bias inconsci recruiter). Se alleni un AI su questi dati, l'AI impara che "donna = meno adatta a ruoli tecnici".

**Come rilevare:**
- Analisi demografica dataset: Conta quante donne/uomini, giovani/senior, nazionalità diverse.
- Se una categoria è sotto-rappresentata (<10-15%), rischio bias alto.

**2. Bias di selezione**

**Definizione:** Il campione di dati non rappresenta la popolazione reale.

**Esempio:** Usi AI per credit scoring allenata solo su clienti attuali (che già hanno superato approvazione umana). L'AI non ha mai visto candidati rifiutati → non sa riconoscere rischi reali → approva troppi prestiti o rifiuta troppi.

**Come rilevare:**
- Chiedi: "Il dataset copre TUTTE le situazioni che il sistema incontrerà?" Se no, bias di selezione.
- Confronta distribuzione dataset vs distribuzione popolazione target.

**3. Bias di misurazione**

**Definizione:** Usi proxy variables (variabili indirette) che correlano con categorie protette.

**Esempio:** L'AI valuta candidati in base a "università frequentata". Ma se solo università costose sono considerate top, l'AI discrimina indirettamente candidati da famiglie a basso reddito → correlazione con status socioeconomico (categoria protetta).

**Come rilevare:**
- Identifica variabili input: Quali features usa l'AI?
- Chiedi: "Questa feature può correlate con genere/etnia/disabilità/età?" Se sì, rischio bias.

### Tecniche pratiche di mitigazione (4 tecniche)

**1. Audit dataset pre-training**

**Cosa fare:**
- Prima di usare un dataset per training AI, conduci analisi statistica:
  - Distribuzione demografica (genere, età, nazionalità se rilevanti)
  - Missing data (campi vuoti, errori)
  - Outlier (valori anomali che possono distorcere AI)
- **Tool:** Excel per dataset piccoli (<1000 righe), Python (pandas) per grandi.

**Tempo:** 2-4 ore per dataset medio (1000-10000 righe).

**2. Diversificazione fonti dati**

**Cosa fare:**
- Non usare un'unica fonte. Esempio recruitment: Non solo LinkedIn (bias verso certi profili), ma anche altre piattaforme, candidature dirette, università.
- Mix dataset storici con dataset "bilanciati artificialmente" (es. aggiungi CV femminili se sotto-rappresentate).

**Attenzione:** Bilanciamento artificiale deve essere fatto con cautela per non distorcere AI in direzione opposta.

**3. Test su sottogruppi (fairness testing)**

**Cosa fare:**
- Dopo training AI, testa performance su sottogruppi demografici separati.
- Esempio: Se l'AI ha accuracy 90% su uomini ma 70% su donne, c'è bias.
- Calcola metriche fairness:
  - **Equal opportunity:** Tasso approvazione simile per tutti i gruppi (a parità di qualifiche)
  - **Calibration:** AI non sovrastima/sottostima sistematicamente un gruppo

**Tool:** Python (fairlearn, AIF360), o chiedi al vendor software di fornirti report fairness.

**Tempo:** 4-8 ore (prima volta), poi automatizzabile.

**4. Monitoraggio continuo output**

**Cosa fare:**
- Non fidarti solo del training. Monitora output AI in produzione:
  - Ogni mese, analizza decisioni AI: % approvazioni per genere, età, etc.
  - Se noti drift (es. AI inizia a scartare più donne del solito), investiga subito.
- **Alert:** Imposta soglie (es. "se % approvazioni donne scende sotto 40%, alert automatico").

**Tool:** Dashboard Excel o BI tool (Power BI, Tableau) con grafici.

### Checklist: "Il tuo dataset è AI Act-compliant?"

Usa questa checklist prima di usare un dataset per AI ad alto rischio:

- [ ] **Qualità:** Dataset aggiornato (ultimi 1-2 anni, non 10 anni fa)
- [ ] **Completezza:** Meno del 10% di dati mancanti per campi critici
- [ ] **Rappresentatività:** Copre almeno 3 categorie demografiche rilevanti (genere, età, provenienza se applicabile)
- [ ] **No bias evidente:** Nessuna categoria sotto-rappresentata (<15%) senza giustificazione
- [ ] **Fonti diverse:** Dati provengono da almeno 2 fonti indipendenti
- [ ] **Audit bias condotto:** Hai fatto analisi statistica o fairness test
- [ ] **Documentazione:** Hai documentato origine dati, pre-processing, eventuali bias noti
- [ ] **Consenso GDPR:** Se dati personali, hai consenso/base legale per uso AI

**Punteggio:** 8/8 = Ottimo | 6-7/8 = Buono | <6 = Rischio alto, migliora prima di usare.

---

**🔹 Domanda in-line 2:**

**Il tuo dataset di recruitment include solo CV degli ultimi 5 anni, tutti da LinkedIn. Quale bias potrebbe esserci?**

**Opzioni:**
- A) Bias di misurazione (proxy variables)
- B) Bias di selezione (campione non rappresentativo)
- C) Bias nei dati storici (discriminazioni passate)
- D) Nessun bias, LinkedIn è una fonte affidabile

**Risposta corretta:** B

**Feedback corretto:** ✓ Esatto! Usare solo LinkedIn crea **bias di selezione**: LinkedIn ha demografia specifica (più uomini in tech, più senior, certe nazionalità). Non rappresenta tutti i candidati potenziali (chi non usa LinkedIn, chi usa altre piattaforme, candidati junior). Devi diversificare le fonti.

**Feedback errato:** ✗ Il problema principale è **bias di selezione**. LinkedIn non è un campione rappresentativo di tutti i candidati: ha più uomini in certi settori, più profili senior, certi background formativi. Se alleni AI solo su LinkedIn, escluderai candidati validi da altre fonti. **Soluzione:** Diversifica fonti (InfoJobs, Indeed, candidature dirette, università).

---

## 3.3 Trasparenza e Informazione Utenti

### Obbligo trasparenza per sistemi a rischio limitato

Se usi AI che **interagisce con utenti** (chatbot, assistenti virtuali) o **genera contenuti** (testi, immagini, video), devi informare gli utenti che si tratta di AI.

**Come farlo (3 esempi pratici):**

**1. Disclaimer chatbot**

Sul widget del chatbot, aggiungi testo chiaro:

> "Ciao! Sono un assistente virtuale basato su intelligenza artificiale. Sono qui per rispondere alle tue domande. Se preferisci parlare con un operatore umano, scrivimi 'operatore'."

**Dove:** Prima frase del chatbot, oppure intestazione widget.

**Tempo implementazione:** 10-15 minuti (modifica configurazione chatbot).

**2. Notice email/contenuti AI-generated**

Se usi AI per scrivere email marketing o contenuti pubblici:

**Opzione A (trasparenza totale):**
> "Questa email è stata scritta con l'assistenza di intelligenza artificiale."

**Opzione B (disclosure footer):**
> "Alcuni contenuti di questa comunicazione possono essere generati o supportati da AI."

**Dove:** Footer email, disclaimer sito web, caption social media.

**Nota:** Per email interne o documenti non critici, la disclosure è opzionale (rischio minimo). Per contenuti pubblici o marketing verso clienti, è consigliata.

**3. Watermark immagini/video AI-generated**

Se generi immagini o video con AI (Midjourney, DALL-E, Runway):

**Opzione A (watermark visivo):**
- Piccolo testo/logo in angolo: "AI-generated"

**Opzione B (metadata):**
- Inserisci tag nei metadati file: "CreatedByAI: true"

**Opzione C (caption):**
- Didascalia sotto immagine: "Immagine creata con intelligenza artificiale."

**Dove:** Prodotti, pubblicità, materiali marketing.

### Obbligo trasparenza per sistemi ad alto rischio

Per sistemi che **decidono su persone** (recruitment, credit scoring, valutazione dipendenti), la trasparenza è più rigorosa.

**Cosa devi garantire:**

**1. Spiegabilità decisioni automatizzate**

Se l'AI prende (o influenza) una decisione negativa su una persona, devi poter **spiegare perché** in linguaggio comprensibile.

**Esempio recruitment:**

> "Gentile candidato, la tua candidatura non è stata selezionata per il colloquio. Il nostro sistema di screening AI ha valutato i CV ricevuti in base a: esperienza nel settore (peso 40%), competenze tecniche (peso 30%), formazione (peso 20%), soft skills (peso 10%). Il tuo punteggio è risultato insufficiente principalmente a causa di: esperienza <2 anni (richiesta minima 3 anni) e mancanza certificazione X (preferenziale). Hai diritto a chiedere una revisione umana entro 30 giorni."

**Cosa serve tecnicamente:**
- Il sistema AI deve fornire "spiegazione" (feature importance, decision rationale).
- Se usi black box totali (es. neural network complesse), implementa tool di explainability (SHAP, LIME).

**2. Diritto a contestazione e intervento umano**

L'utente deve poter:
- **Chiedere spiegazione:** "Perché sono stato scartato?"
- **Contestare decisione:** "Penso ci sia un errore, voglio revisione umana."
- **Parlare con un umano:** Non può essere costretto a interagire solo con AI.

**Come implementarlo:**
- **Recruitment:** Inserisci in ogni email di rifiuto: "Per contestare questa decisione o chiedere revisione, contatta hr@azienda.it."
- **Credit scoring:** Offri numero verde o sportello fisico dove parlare con loan officer umano.
- **Valutazione dipendenti:** Policy interna che permette dipendente di chiedere riunione con manager per discutere valutazione AI.

**Tempi risposta:** Entro 30 giorni dalla richiesta (standard GDPR per diritti interessati).

**3. Informativa privacy specifica**

Integra la tua privacy policy (GDPR) con sezione AI:

> **USO DI INTELLIGENZA ARTIFICIALE**
> La nostra azienda utilizza sistemi di intelligenza artificiale per [recruitment/credit scoring/altra funzione]. I tuoi dati personali [specificare quali: CV, storico pagamenti, etc.] sono elaborati da algoritmi automatizzati per [scopo]. Hai diritto a:
> - Ricevere spiegazione delle decisioni automatizzate
> - Contestare decisioni e richiedere intervento umano
> - Revocare il consenso in qualsiasi momento (dove applicabile)
> Per esercitare questi diritti, contatta: [email DPO].

**Dove:** Privacy policy sito web, informative pre-contratto, disclaimer applicazioni.

---

**🔹 Domanda in-line 3 (Vero/Falso):**

**"Un chatbot sul sito deve sempre informare l'utente che è un assistente AI."**

**Vero o Falso?**

**Risposta corretta:** Vero

**Feedback corretto:** ✓ Corretto! L'AI Act richiede trasparenza per sistemi che interagiscono con utenti. Un chatbot deve dichiarare la sua natura AI (es. "Sono un assistente virtuale AI"). Questo permette all'utente di decidere consapevolmente se continuare con AI o parlare con umano.

**Feedback errato:** ✗ Falso. È **obbligatorio** informare l'utente che sta interagendo con un'AI. Questo è un requisito esplicito dell'AI Act per sistemi a rischio limitato. **Soluzione:** Aggiungi disclaimer nel primo messaggio o intestazione chatbot. Tempo implementazione: 10-15 minuti.

---

## 3.4 Registri e Documentazione AI

### Cosa tracciare in registro AI (6 item)

Un **registro AI** è un file (Excel, Google Sheet, o database semplice) che elenca tutti i sistemi AI usati in azienda.

**Colonne minime:**

1. **Nome sistema/tool AI:** Es. "ChatGPT Enterprise", "Software X per recruitment", "Chatbot sito web"
2. **Fornitore:** Es. "OpenAI", "Software House Y", "Vendor Z"
3. **Categoria rischio AI Act:** 🔴 Proibito / 🟠 Alto Rischio / 🟡 GPAI / 🟢 Limitato / 🟢 Minimo
4. **Funzione aziendale e responsabile:** Es. "Marketing - Resp. Mario Rossi", "HR - Resp. Laura Bianchi"
5. **Dataset utilizzati:** Es. "Nessuno (tool generico)", "CV candidati 2020-2024", "Storico vendite 2018-2024"
6. **Log modifiche e incident:** Es. "Attivato 01/2024 | Upgrade 06/2024 | Incident bias rilevato 09/2024 (risolto)"

**Colonne opzionali aggiuntive:**
- Data attivazione / disattivazione
- Contratto vendor (link documento)
- DPIA condotta (sì/no, data)
- Audit ultimo (data)
- Note

### Template registro AI (tabella markdown)

| **Nome Sistema**       | **Fornitore** | **Categoria Rischio** | **Funzione / Responsabile**       | **Dataset**                | **Log Modifiche**                     |
|------------------------|---------------|-----------------------|-----------------------------------|----------------------------|---------------------------------------|
| ChatGPT Enterprise     | OpenAI        | 🟢 Rischio Limitato   | Marketing / Mario Rossi           | Nessuno (tool generico)    | Attivato 03/2024                      |
| Software ATS Recruiting| HRTech SRL    | 🟠 Alto Rischio       | HR / Laura Bianchi                | CV candidati 2020-2024     | Attivato 01/2024, DPIA 02/2024        |
| Chatbot sito web       | ChatBot Inc.  | 🟢 Rischio Limitato   | Customer Service / Luca Verdi     | FAQ aziendali              | Attivato 11/2023, Upgrade 05/2024     |
| AI previsioni vendite  | SalesAI       | 🟢 Rischio Minimo     | Operations / Anna Neri            | Storico vendite 2018-2024  | Attivato 06/2023                      |

**Formato file:** Excel o Google Sheet (facilita aggiornamenti collaborativi).

**Chi aggiorna:** AI Owner / Compliance (coordinatore) + Manager funzioni (notificano nuovi tool).

**Frequenza aggiornamento:** Ogni trimestre (revisione completa) + in tempo reale quando si aggiunge/rimuove un sistema.

### Documentazione tecnica per sistemi ad alto rischio

Per sistemi 🟠 **Alto Rischio**, oltre al registro, serve **documentazione tecnica dettagliata**.

**Cosa documentare:**

**1. Descrizione funzionamento (anche black box: input/output)**

Anche se non conosci l'algoritmo interno (black box del vendor), descrivi:
- **Input:** Quali dati inserisci (es. CV formato PDF, dati anagrafici, esperienze lavorative)
- **Processo:** Cosa fa il sistema (es. "Analizza CV, estrae competenze, assegna punteggio 0-100")
- **Output:** Cosa produce (es. "Lista candidati con punteggio, top 20 raccomandati")

**2. Valutazione performance e accuracy**

Documenta metriche chiave:
- **Accuracy:** Quante decisioni AI sono corrette? (es. "85% dei candidati raccomandati da AI vengono effettivamente assunti")
- **False positives/negatives:** Quanti errori fa? (es. "10% candidati scartati da AI risultano validi dopo revisione umana")
- **Bias metrics:** Differenze performance tra gruppi demografici (vedi sezione 3.2)

**Come ottenere:** Chiedi al vendor documentazione, oppure calcola internamente dopo 3-6 mesi uso.

**3. Misure sicurezza e robustezza**

Documenta:
- **Cybersecurity:** Come è protetto il sistema (encryption, accesso autenticato, backup)
- **Robustezza:** Cosa succede se AI riceve input anomalo (es. CV in lingua straniera, campi mancanti)
- **Disaster recovery:** Se sistema va offline, cosa succede? (fallback manuale)

**Formato:** File Word/PDF (5-10 pagine per sistema), salvato in repository aziendale (Sharepoint, Google Drive).

**Aggiornamento:** Annuale o quando sistema viene aggiornato significativamente.

---

**🔹 Domanda in-line 4:**

**Quale informazione NON è necessaria nel registro AI aziendale?**

**Opzioni:**
- A) Nome sistema e fornitore
- B) Categoria rischio AI Act
- C) Responsabile funzione aziendale
- D) Codice sorgente dell'algoritmo AI

**Risposta corretta:** D

**Feedback corretto:** ✓ Esatto! Il **codice sorgente** non è necessario nel registro (spesso è proprietà del vendor e non accessibile). Il registro deve contenere: nome, fornitore, categoria rischio, responsabile, dataset, log modifiche. La documentazione tecnica (per alto rischio) descrive funzionamento ma non richiede codice.

**Feedback errato:** ✗ Il registro AI NON richiede il **codice sorgente** dell'algoritmo (spesso inaccessibile per sistemi vendor). Serve: nome sistema, fornitore, categoria rischio, responsabile, dataset, log. Anche per sistemi ad alto rischio, la documentazione tecnica descrive input/output/funzionamento, ma non codice. **Rivedi template registro sezione 3.4.**

---

## 3.5 Human Oversight (Supervisione Umana)

### Definizioni: tre livelli di supervisione

**Human-in-the-loop (nel ciclo):**
- **Definizione:** Un umano rivede e approva **ogni singola decisione AI** prima che venga applicata.
- **Esempio:** Recruiter rivede ogni CV shortlist AI prima di inviare inviti a colloquio.
- **Quando:** Sistemi ad alto rischio con decisioni critiche e irreversibili (recruitment, licenziamenti, diniego credito).

**Human-on-the-loop (sul ciclo):**
- **Definizione:** Un umano **monitora** l'AI durante l'operazione e può **intervenire** se rileva anomalie.
- **Esempio:** Operatore customer service monitora chatbot, se chatbot dà risposta errata può correggerla in tempo reale.
- **Quando:** Sistemi a rischio limitato/medio dove decisioni AI sono frequenti ma non tutte critiche.

**Human-in-command (al comando):**
- **Definizione:** Un umano **controlla** il sistema AI (può disattivarlo, modificare parametri) ma non rivede ogni decisione.
- **Esempio:** IT manager può spegnere sistema AI se malfunziona, ma non controlla ogni output.
- **Quando:** Sistemi a rischio minimo o per controllo tecnico generale.

**Tabella riassuntiva:**

| **Livello**          | **Controllo**          | **Quando obbligatorio**               | **Esempio**                              |
|----------------------|------------------------|---------------------------------------|------------------------------------------|
| Human-in-the-loop    | Approva ogni decisione | Alto rischio (HR, credit, salute)     | Recruiter valida shortlist AI            |
| Human-on-the-loop    | Monitora e interviene  | Rischio limitato (chatbot, scoring)   | Operatore corregge chatbot se sbaglia    |
| Human-in-command     | Controllo sistema      | Tutti i sistemi (backup generale)     | IT può disattivare AI se malfunziona     |

### Quando è obbligatorio

**Human oversight è OBBLIGATORIO per sistemi 🟠 Alto Rischio.**

Livello minimo richiesto: **Human-in-the-loop** (approvazione decisioni) o **Human-on-the-loop** (monitoraggio con possibilità override).

**Non è sufficiente:** "C'è un umano da qualche parte nell'azienda che in teoria potrebbe controllare." Serve supervisione **attiva e documentata**.

### Come implementarlo (4 modalità)

**1. Decisioni critiche sempre revisionate da umano**

**Setup:**
- Configura sistema AI in modalità "suggerimento" (recommendation), non "decisione finale" (auto-decision).
- Workflow: AI analizza → Output va a umano → Umano approva/rifiuta/modifica → Decisione applicata.

**Esempio recruitment:**
- AI genera shortlist top 20 candidati
- Recruiter rivede lista, legge almeno 3-5 CV anche fuori top 20, decide finale
- Documenta eventuali override ("Ho invitato anche candidato #25 perché...")

**Tool:** Software ATS con opzione "manual approval" attivata.

**2. Possibilità override decisione AI**

**Setup:**
- L'operatore umano ha sempre un bottone "Override" o "Manual mode".
- Se AI propone decisione che sembra errata, umano può scavalcarla.

**Esempio credit scoring:**
- AI dice "Rifiuta prestito (punteggio 45/100)"
- Loan officer vede che cliente ha reddito stabile recente (non catturato da AI)
- Loan officer clicca "Override" e approva manualmente con motivazione scritta

**Tool:** Dashboard con pulsante override + campo note obbligatorio.

**3. Alert per decisioni anomale**

**Setup:**
- Sistema AI genera alert automatici per decisioni "fuori norma".
- Alert attiva revisione umana obbligatoria.

**Esempio performance evaluation:**
- AI valuta dipendente con punteggio molto basso (< 30/100)
- Alert automatico a manager: "Revisione richiesta: punteggio anomalo per dipendente X"
- Manager rivede dati manualmente prima di confermare valutazione

**Tool:** Sistema con regole alert (if score < 30 OR score > 95, trigger human review).

**4. Training operatori su limiti AI**

**Setup:**
- Forma gli operatori umani a:
  - Riconoscere quando AI può sbagliare (es. CV non standard, dati mancanti)
  - Non fidarsi ciecamente dell'AI ("automation bias")
  - Usare giudizio critico

**Esempio:**
- Training recruiter (2 ore): "L'AI favorisce candidati con CV strutturati in modo standard. Se vedi CV creativi o percorsi non lineari, valutali tu personalmente. Non scartare automaticamente chi ha punteggio basso."

**Frequenza:** Training iniziale (prima di usare AI) + refresh annuale.

---

**🔹 Domanda in-line 5 (Scenario):**

**Scenario:** Un sistema AI per credit scoring assegna punteggi ai clienti. Un loan officer rivede tutti i punteggi ma nella pratica approva sempre le decisioni AI senza analisi. Questo è human oversight conforme?**

**Opzioni:**
- A) Sì, c'è un umano nel processo
- B) No, è solo "rubber stamp" senza vera supervisione
- C) Sì, se il loan officer è formato
- D) Dipende dal punteggio AI

**Risposta corretta:** B

**Feedback corretto:** ✓ Corretto! Questo è **"rubber stamp" oversight** (supervisione nominale). L'AI Act richiede supervisione **effettiva**: il loan officer deve analizzare i casi, avere potere di override, e usarlo quando necessario. Approvare sempre in automatico senza analisi non è conforme.

**Feedback errato:** ✗ Questo è un caso di **"rubber stamp"** (timbro automatico), NON vera supervisione. L'AI Act richiede human oversight **effettivo**: l'operatore deve analizzare le decisioni, avere potere di override, e usarlo quando necessario. Se approva sempre senza pensare, è come se l'AI decidesse da sola. **Soluzione:** Il loan officer deve effettivamente analizzare almeno il 20-30% delle pratiche, override quando ha dubbi, e documentare le motivazioni.

---

## 3.6 Valutazioni d'Impatto: DPIA e IAIA

### DPIA (Data Protection Impact Assessment) per GDPR + AI

**Cos'è:** Una **valutazione d'impatto sulla privacy** richiesta dal GDPR quando tratti dati personali in modo ad alto rischio.

**Quando obbligatoria per AI:**
- Sistema AI tratta dati personali sensibili (salute, orientamento sessuale, biometria, etc.)
- Sistema AI prende decisioni automatizzate su persone (recruitment, credit scoring, profiling)
- Sistema AI monitora comportamenti su larga scala (es. videosorveglianza con analisi AI)

**Come integrarla con AI Act:**

Aggiungi sezione **"AI-specific"** alla DPIA standard:

**Template DPIA con sezione AI:**

```
DPIA - SISTEMA AI [Nome Sistema]

1. DESCRIZIONE TRATTAMENTO DATI
   - Quali dati personali raccoglie il sistema AI?
   - Finalità trattamento
   - Base legale (consenso, contratto, legittimo interesse, obblighi legali)

2. NECESSITÀ E PROPORZIONALITÀ
   - Perché serve AI per questo scopo?
   - Alternative considerate (soluzioni non-AI)?
   - Minimizzazione dati (usiamo solo dati necessari)?

3. RISCHI PER DIRITTI E LIBERTÀ
   - Rischio discriminazione (bias AI)
   - Rischio privacy (re-identificazione, inferenza dati sensibili)
   - Rischio decisioni errate (false positive/negative)
   - Rischio trasparenza (black box incomprensibile)

4. MISURE MITIGAZIONE RISCHI (AI-specific)
   - Dataset quality (audit bias condotti)
   - Human oversight implementato (livello: in-the-loop/on-the-loop)
   - Trasparenza (utenti informati che AI è usata)
   - Diritto a contestazione (processo formale esistente)
   - Accuracy testing (performance monitorata)

5. VALUTAZIONE RISCHIO RESIDUO
   - Dopo mitigazioni, rischio resta alto/medio/basso?
   - Decisione: Procedere / Non procedere / Consultare DPO/Autorità

6. APPROVAZIONE
   - Data valutazione: [Data]
   - Condotta da: [Nome, ruolo]
   - Approvata da: DPO [Nome]
   - Revisione prevista: [Data, annuale]
```

**Chi conduce:** DPO + AI Owner/Compliance + Manager funzione.

**Tempo:** 4-8 ore (prima volta per sistema nuovo), poi revisioni più rapide.

### IAIA (Impact Assessment IA) per AI Act

**Cos'è:** Una **valutazione d'impatto sui diritti fondamentali** specifica per AI, richiesta dall'AI Act per sistemi ad alto rischio.

**Quando obbligatoria:**
- Sistemi 🟠 **Alto Rischio** che influiscono su lavoro, credito, istruzione, accesso servizi essenziali, sicurezza.

**Cosa valuta (focus AI Act, non solo GDPR):**
- **Impatto su diritti fondamentali:** Non solo privacy, ma anche lavoro, non-discriminazione, dignità, accesso giustizia.
- **Fairness algoritmica:** Il sistema tratta tutti equamente?
- **Robustezza e sicurezza:** Il sistema resiste ad attacchi (adversarial AI, data poisoning)?
- **Accountability:** C'è sempre un responsabile umano identificabile?

**Template IAIA (outline):**

```
IAIA - IMPACT ASSESSMENT AI ACT [Nome Sistema]

1. CONTESTO E SCOPO
   - Descrizione sistema AI
   - Finalità uso
   - Categoria rischio AI Act: 🟠 Alto Rischio

2. DIRITTI FONDAMENTALI COINVOLTI
   - Quali diritti sono impattati? (lavoro, credito, salute, etc.)
   - Intensità impatto (alto/medio/basso)

3. RISCHI SPECIFICI AI ACT
   - Discriminazione algoritmica (bias genere/età/etnia)
   - Opacità decisionale (black box)
   - Errori sistematici (accuracy insufficiente)
   - Assenza supervisione umana

4. MISURE CONFORMITÀ AI ACT
   - Human oversight: [Descrizione implementazione]
   - Dataset quality: [Audit condotti, risultati]
   - Trasparenza: [Come informiamo utenti]
   - Explainability: [Capacità spiegare decisioni]
   - Log e registro: [Sistema tracciamento esistente]

5. CONSULTAZIONI
   - Stakeholder consultati (dipendenti, sindacati, DPO, esperti esterni)
   - Feedback ricevuto e azioni correttive

6. DECISIONE FINALE
   - Rischio residuo accettabile? SÌ / NO
   - Sistema può essere usato? SÌ / NO / SÌ CON CONDIZIONI
   - Condizioni: [es. Solo con supervisione rafforzata per primi 6 mesi]

7. MONITORAGGIO
   - KPI monitorati: [es. Tasso errori, distribuzione decisioni per genere]
   - Frequenza revisione: Trimestrale primi 12 mesi, poi annuale
```

**Chi conduce:** Legal + Compliance + DPO + Manager funzione + (opzionale) consulente esterno esperto AI.

**Tempo:** 8-16 ore (prima volta), poi revisioni annuali più rapide.

### Confronto DPIA vs IAIA

| **Aspetto**            | **DPIA (GDPR)**                        | **IAIA (AI Act)**                             |
|------------------------|----------------------------------------|-----------------------------------------------|
| **Focus**              | Privacy e protezione dati personali    | Diritti fondamentali (lavoro, credito, etc.)  |
| **Quando obbligatoria**| Trattamento dati ad alto rischio       | Sistemi AI ad alto rischio                    |
| **Chi approva**        | DPO                                    | AI Owner / Compliance (coordinamento DPO)     |
| **Contenuto chiave**   | Dati trattati, rischi privacy, mitigazioni GDPR | Diritti impattati, bias, human oversight, fairness |
| **Normativa**          | GDPR (Regolamento UE 2016/679)         | AI Act (Regolamento UE 2024/1689)             |

**Best practice:** Condurre **DPIA e IAIA insieme** per sistemi AI ad alto rischio che trattano dati personali. Usare un unico documento integrato per evitare duplicazioni.

### Chi conduce e frequenza

**Chi:**
- **DPIA:** DPO (obbligatorio) + Manager funzione + IT/Data
- **IAIA:** Legal/Compliance + DPO + AI Owner + Manager funzione + (opzionale) esperto esterno AI ethics

**Frequenza:**
- **Prima di attivare** un sistema ad alto rischio (obbligatorio)
- **Revisione annuale** (consigliato)
- **Revisione ad-hoc** quando:
  - Sistema viene aggiornato significativamente (nuove features, nuovo dataset)
  - Si verifica un incident (bias rilevato, errore grave)
  - Cambiano normative o linee guida

---

**🔹 Domanda in-line 6:**

**Qual è la differenza principale tra DPIA e IAIA?**

**Opzioni:**
- A) DPIA è solo per dati, IAIA è solo per algoritmi
- B) DPIA focalizza su privacy (GDPR), IAIA su diritti fondamentali più ampi (AI Act)
- C) DPIA è obbligatoria, IAIA è opzionale
- D) DPIA è per grandi aziende, IAIA per PMI

**Risposta corretta:** B

**Feedback corretto:** ✓ Esatto! **DPIA** (GDPR) si concentra su **privacy e protezione dati personali**. **IAIA** (AI Act) ha focus più ampio: **diritti fondamentali** (lavoro, non-discriminazione, accesso servizi, dignità). Per sistemi AI ad alto rischio, spesso servono entrambe. Best practice: documento integrato DPIA+IAIA.

**Feedback errato:** ✗ La differenza chiave è il **focus**: DPIA (GDPR) = **privacy e dati personali**. IAIA (AI Act) = **diritti fondamentali** più ampi (lavoro, non-discriminazione, accesso servizi, equità algoritmica). Entrambe possono essere obbligatorie per sistemi AI ad alto rischio. **Soluzione:** Conduci documento integrato che copre entrambi gli aspetti. **Rivedi sezione 3.6 - Confronto DPIA vs IAIA.**

---

## Quiz Sommativo - Modulo 3

**Istruzioni:**
- **10 domande** che coprono tutti i 6 topic del modulo (3.1-3.6)
- **Soglia superamento: 70%** (7/10 risposte corrette)
- **Massimo 2 tentativi**
- Riceverai feedback immediato dopo ogni domanda
- Al termine: recap errori con link a sezioni da rivedere

**Tempo stimato:** 12-15 minuti

---

### Domanda 1 di 10 (Multiple Choice)

**Quale elemento NON deve essere incluso in una AI policy aziendale?**

**Opzioni:**
- A) Principi etici e valori aziendali
- B) Ruoli e responsabilità per gestione AI
- C) Codice sorgente di tutti gli algoritmi AI usati
- D) Processo approvazione nuovi sistemi AI

**Risposta corretta:** C

**Feedback corretto:** ✓ Corretto! Una AI policy **non** include codice sorgente (spesso proprietà vendor e non accessibile). Include: principi etici, ruoli, processo approvazione, gestione incident, formazione.

**Feedback errato:** ✗ Il **codice sorgente** non appartiene alla policy (spesso inaccessibile per sistemi vendor). La policy include: principi etici, ruoli/responsabilità, workflow approvazione, gestione rischi/incident, piano formazione. **Rivedi sezione 3.1.**

---

### Domanda 2 di 10 (Multiple Choice)

**Quale tipo di bias si verifica quando il dataset contiene solo candidati già assunti (e non include rifiutati)?**

**Opzioni:**
- A) Bias nei dati storici
- B) Bias di selezione
- C) Bias di misurazione
- D) Bias di conferma

**Risposta corretta:** B

**Feedback corretto:** ✓ Esatto! **Bias di selezione**: il campione non rappresenta la popolazione reale. Se l'AI vede solo assunti, non impara a riconoscere candidati da rifiutare → decisioni distorte.

**Feedback errato:** ✗ Questo è **bias di selezione**. Il dataset include solo un sottogruppo (assunti) e non rappresenta l'intera popolazione (tutti i candidati). L'AI non ha mai visto esempi negativi → non sa distinguere bene. **Soluzione:** Include anche candidati rifiutati nel training (se possibile e legale). **Rivedi sezione 3.2.**

---

### Domanda 3 di 10 (Multiple Response - 2 risposte corrette)

**Quali sono obblighi trasparenza per un chatbot su e-commerce? (Seleziona 2)**

**Opzioni:**
- A) Informare utente che è un assistente AI
- B) Condurre DPIA prima di attivarlo
- C) Consentire opzione parlare con umano
- D) Pubblicare codice sorgente chatbot

**Risposte corrette:** A, C

**Feedback corretto:** ✓ Corretto! Un chatbot (rischio limitato) deve: **A) Informare l'utente che è AI** e **C) Permettere escalation a umano** (best practice, non sempre obbligatorio ma consigliato). DPIA è solo per alto rischio. Pubblicare codice non è richiesto.

**Feedback errato:** ✗ Le risposte corrette sono **A e C**. Un chatbot deve **informare utente che è AI** (obbligo trasparenza) e **permettere parlare con umano** (best practice). DPIA è solo per sistemi ad alto rischio. Pubblicare codice non è mai richiesto. **Rivedi sezione 3.3.**

---

### Domanda 4 di 10 (Multiple Choice)

**Quale informazione è obbligatoria nel registro AI aziendale?**

**Opzioni:**
- A) Nome sistema e fornitore
- B) Prezzo pagato per licenza software
- C) Nome tutti i dipendenti che lo usano
- D) Codice fiscale del fornitore

**Risposta corretta:** A

**Feedback corretto:** ✓ Esatto! Il registro deve contenere almeno: **nome sistema, fornitore, categoria rischio, funzione/responsabile, dataset, log modifiche**. Prezzo e dettagli fiscali non sono richiesti.

**Feedback errato:** ✗ Il registro AI deve tracciare: **nome sistema, fornitore, categoria rischio, responsabile, dataset, log modifiche**. Prezzo, elenco completo utenti, e dati fiscali vendor non sono necessari. **Rivedi sezione 3.4 - Template Registro.**

---

### Domanda 5 di 10 (Vero/Falso)

**"Human-in-the-loop significa che un umano monitora il sistema AI ma non rivede ogni singola decisione."**

**Vero o Falso?**

**Risposta corretta:** Falso

**Feedback corretto:** ✓ Corretto! È **FALSO**. **Human-in-the-loop** significa che un umano **approva ogni decisione** prima che venga applicata. Quello che monitorare senza approvare tutte le decisioni è **human-on-the-loop**.

**Feedback errato:** ✗ È **FALSO**. **Human-in-the-loop** = umano approva **ogni singola decisione**. **Human-on-the-loop** = monitora e può intervenire (ma non rivede tutto). Per sistemi ad alto rischio serve almeno human-in-the-loop. **Rivedi sezione 3.5 - Definizioni.**

---

### Domanda 6 di 10 (Multiple Response - 2 risposte corrette)

**Quali tecniche aiutano a mitigare bias nei dataset AI? (Seleziona 2)**

**Opzioni:**
- A) Diversificare fonti dati
- B) Usare solo dati degli ultimi 10 anni
- C) Test fairness su sottogruppi demografici
- D) Aumentare dimensione dataset senza controllare bias

**Risposte corrette:** A, C

**Feedback corretto:** ✓ Perfetto! **A) Diversificare fonti** (non solo LinkedIn, mix canali) e **C) Test fairness** (verificare che AI funzioni equamente per tutti i gruppi) sono tecniche efficaci. Usare solo dati vecchi (B) o aumentare volume senza controllo (D) non risolve bias.

**Feedback errato:** ✗ Le risposte corrette sono **A e C**. **Diversificare fonti** riduce bias di selezione. **Test fairness** rileva se AI discrimina gruppi. Usare solo dati vecchi (B) può perpetuare bias storici. Aumentare volume senza audit (D) non risolve bias, lo amplifica. **Rivedi sezione 3.2 - Tecniche Mitigazione.**

---

### Domanda 7 di 10 (Scenario - Multiple Choice)

**Scenario:** Un sistema AI per credit scoring rifiuta il 60% delle richieste di donne ma solo il 30% di uomini (a parità di reddito). Cosa devi fare immediatamente?

**Opzioni:**
- A) Continuare a usare il sistema, è solo casualità statistica
- B) Sospendere il sistema, condurre audit bias, correggere dataset
- C) Informare solo il DPO, ma continuare uso
- D) Cambiare solo la soglia di approvazione per bilanciare

**Risposta corretta:** B

**Feedback corretto:** ✓ Corretto! Un bias così evidente (discriminazione di genere) è **illegale** (GDPR + AI Act + leggi anti-discriminazione). Devi **sospendere immediatamente** il sistema, condurre audit approfondito, correggere dataset/algoritmo, e ripartire solo dopo fix verificato.

**Feedback errato:** ✗ Questo è un caso grave di **discriminazione di genere** (illegale). Non puoi ignorarlo (A) o solo informare DPO continuando uso (C). Cambiare soglia senza capire causa (D) è "patch" insufficiente. **Azione corretta:** **B) Sospendi sistema, audit bias, correggi dataset/algoritmo, testa fairness, riattiva solo dopo fix**. **Rivedi sezione 3.2 - Identificare Bias.**

---

### Domanda 8 di 10 (Multiple Choice)

**Quando è obbligatoria una DPIA per sistemi AI?**

**Opzioni:**
- A) Per tutti i sistemi AI senza eccezioni
- B) Solo per sistemi AI che costano più di 50.000 euro
- C) Per sistemi AI che trattano dati personali ad alto rischio (es. decisioni automatizzate su persone)
- D) Solo per aziende con più di 250 dipendenti

**Risposta corretta:** C

**Feedback corretto:** ✓ Esatto! DPIA è obbligatoria quando tratti **dati personali ad alto rischio**, inclusi sistemi AI che prendono **decisioni automatizzate su persone** (recruitment, credit scoring, profiling). Non dipende da costo o dimensione azienda.

**Feedback errato:** ✗ DPIA (GDPR) è obbligatoria per **trattamento dati personali ad alto rischio**, inclusi sistemi AI con decisioni automatizzate su persone (recruitment, scoring, profiling). Non dipende da costo sistema (B) o dimensione azienda (D). Non serve per TUTTI i sistemi (A), solo alto rischio. **Rivedi sezione 3.6 - DPIA.**

---

### Domanda 9 di 10 (Multiple Choice)

**Qual è il focus principale della IAIA (Impact Assessment AI Act) rispetto alla DPIA?**

**Opzioni:**
- A) IAIA si concentra solo su privacy, DPIA su diritti fondamentali
- B) IAIA valuta impatto su diritti fondamentali ampi (lavoro, equità), DPIA su privacy
- C) Sono identiche, solo nomi diversi
- D) IAIA è per AI generativa, DPIA per AI predittiva

**Risposta corretta:** B

**Feedback corretto:** ✓ Perfetto! **IAIA** (AI Act) valuta impatto su **diritti fondamentali ampi**: lavoro, non-discriminazione, accesso servizi, dignità, fairness algoritmica. **DPIA** (GDPR) focalizza su **privacy e dati personali**. Per sistemi AI ad alto rischio servono spesso entrambe.

**Feedback errato:** ✗ La risposta corretta è **B**. **IAIA** = diritti fondamentali ampi (lavoro, equità, accesso servizi). **DPIA** = privacy e protezione dati. Non sono identiche (C), e la distinzione non è per tipo AI (D). **Rivedi sezione 3.6 - Confronto DPIA vs IAIA.**

---

### Domanda 10 di 10 (Scenario - Multiple Response - 3 risposte corrette)

**Scenario:** Vuoi implementare un sistema AI per valutazione performance dipendenti (sistema ad alto rischio). Quali azioni sono obbligatorie? (Seleziona 3)**

**Opzioni:**
- A) Human oversight (manager rivede valutazioni AI)
- B) DPIA prima di attivare sistema
- C) Trasparenza verso dipendenti (informarli che AI è usata)
- D) Pubblicare AI policy sul sito web pubblico
- E) Assumere un data scientist a tempo pieno

**Risposte corrette:** A, B, C

**Feedback corretto:** ✓ Eccellente! Per un sistema ad alto rischio (valutazione dipendenti) sono obbligatori: **A) Human oversight** (manager approva valutazioni), **B) DPIA** (valutazione impatto privacy + diritti), **C) Trasparenza** (informare dipendenti). Pubblicare policy pubblicamente (D) e assumere data scientist (E) non sono obbligatori.

**Feedback errato:** ✗ Le risposte corrette sono **A, B, C**. Per sistemi ad alto rischio (valutazione dipendenti) servono: **Human oversight** (manager rivede valutazioni AI), **DPIA** (obbligatoria per decisioni automatizzate su persone), **Trasparenza** (informare dipendenti). Pubblicare policy pubblicamente e assumere data scientist non sono obblighi legali (anche se possono essere utili). **Rivedi sezioni 3.5 (Human Oversight) e 3.6 (DPIA).**

---

## Feedback Finale Quiz

**Se hai totalizzato 7-10/10 (≥70%):**
> 🎉 **Complimenti! Hai superato il quiz sommativo del Modulo 3.**
>
> Hai dimostrato di comprendere i controlli di governance minimi richiesti dall'AI Act: AI policy, dataset quality, trasparenza, registri, human oversight, e valutazioni d'impatto.
>
> **Prossimo passo:** Accedi al **Modulo 4 - Piano 90 giorni** per pianificare le azioni concrete di conformità nella tua azienda.
>
> **Punteggio registrato:** [X]/10 | **Status:** SUPERATO ✓

**Se hai totalizzato <7/10 (<70%):**
> ⚠️ **Non hai ancora raggiunto la soglia del 70%.**
>
> **Punteggio:** [X]/10 | **Soglia:** 7/10
>
> **Tentativi:** [1 o 2]/2
>
> **Aree da rivedere:**
> [Lista automatica delle sezioni con errori, es. "Hai sbagliato 2 domande su Human Oversight (3.5) e 1 su DPIA (3.6). Ti consigliamo di rivedere queste sezioni."]
>
> **Cosa fare ora:**
> - **Se è il tuo 1° tentativo:** Rivedi le sezioni indicate sopra (10-15 min) e riprova il quiz.
> - **Se è il tuo 2° tentativo:** Rivedi tutto il Modulo 3 (20-25 min) prima di procedere. Puoi comunque accedere al Modulo 4, ma ti consigliamo di consolidare le basi di governance prima di pianificare azioni concrete.

---

## Riepilogo Modulo 3

**Hai imparato:**
- ✓ **Cosa deve contenere una AI policy aziendale** (5 elementi chiave: principi, ruoli, processo approvazione, gestione incident, formazione)
- ✓ **Come identificare e mitigare bias nei dataset** (3 tipi bias + 4 tecniche mitigazione)
- ✓ **Obblighi trasparenza** per rischio limitato (disclaimer chatbot, watermark) e alto rischio (spiegabilità, diritto contestazione)
- ✓ **Come tenere registri AI** (6 colonne minime) e documentazione tecnica per alto rischio
- ✓ **3 livelli human oversight** (in-the-loop, on-the-loop, in-command) e quando è obbligatorio
- ✓ **Differenza tra DPIA e IAIA** e quando condurle

**Competenze acquisite:**
- ○ Redigere una AI policy aziendale (usando template fornito)
- ○ Condurre audit dataset per rilevare bias
- ○ Implementare trasparenza verso utenti (disclaimer, spiegazioni)
- ○ Creare un registro AI aziendale completo
- ○ Configurare human oversight per sistemi ad alto rischio
- ○ Pianificare e condurre DPIA/IAIA per sistemi AI

**Materiali scaricabili (disponibili al termine del modulo):**
- Template AI Policy (Word, 2 pagine)
- Checklist Dataset Quality (PDF, 10 item)
- Template Registro AI (Excel)
- Template DPIA integrata con AI (Word, 5 pagine)
- Checklist IAIA (PDF, 15 item)
- Guida Human Oversight (PDF, 3 pagine con esempi)

**Prossimo modulo:**
Nel **Modulo 4** metterai in pratica tutto quello che hai imparato costruendo un **piano operativo 90 giorni** per la tua azienda. Identificherai 5 azioni prioritarie, assegnerai ruoli e responsabilità, valuterai fornitori AI, organizzerai comunicazione interna, e definirai KPI di monitoraggio. Alla fine avrai un piano concreto pronto da presentare al tuo management.

---

**Fine Modulo 3**
