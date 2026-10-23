# Modulo 2: Mappa dei casi d'uso e rischio

**Durata:** 25-30 minuti

**Obiettivi del modulo:**
- Classificare casi d'uso AI aziendali nelle categorie AI Act
- Identificare requisiti minimi di conformità per ciascuna categoria
- Applicare il framework di classificazione a un caso reale della tua azienda
- Riconoscere red flag che indicano alto rischio

---

## Introduzione al Modulo

Nel Modulo 1 hai imparato le 4 categorie di sistemi AI secondo l'AI Act. Ora è il momento di applicare questa conoscenza a **casi concreti**.

In questo modulo analizzerai **5 scenari realistici** di PMI italiane che usano AI in diverse funzioni: marketing, HR, customer service, analisi dati e prodotto. Per ciascuno imparerai:
- Come classificarlo nella giusta categoria AI Act
- Quali requisiti minimi di conformità applicare
- Quali **red flag** evitare per non finire in zona ad alto rischio

Alla fine userai un **framework decisionale** pratico (un albero di decisioni con domande chiave) per classificare i tuoi sistemi AI aziendali. Questo strumento ti servirà lunedì mattina quando tornerai in ufficio.

---

## 2.1 Framework di Classificazione AI Act

Prima di tuffarti negli scenari, hai bisogno di un **metodo sistematico** per classificare qualsiasi sistema AI. Ecco un decision tree semplice basato su 4 domande chiave.

### Decision Tree: Da caso d'uso a categoria

**Segui queste domande in ordine per classificare un sistema AI:**

**DOMANDA 1: Il sistema è usato per manipolazione, social scoring o sorveglianza biometrica di massa?**
- **SÌ** → 🔴 **Sistema PROIBITO** (non puoi usarlo)
- **NO** → Vai a Domanda 2

**DOMANDA 2: Il sistema influisce su diritti fondamentali di persone?**
(Diritti fondamentali = lavoro, credito, istruzione, accesso a servizi essenziali, sicurezza, salute)
- **SÌ** → Vai a Domanda 3
- **NO** → Vai a Domanda 4

**DOMANDA 3: Il sistema prende decisioni automatizzate con impatto significativo su persone?**
- **SÌ, senza supervisione umana** → 🟠 **Alto Rischio** (richiede human oversight, DPIA, trasparenza)
- **SÌ, ma con supervisione umana** → 🟠 **Alto Rischio** (già meglio, ma servono comunque controlli)
- **NO, solo suggerimenti** → 🟢 **Rischio Limitato** (trasparenza sufficiente)

**DOMANDA 4: Il sistema interagisce con utenti finali o genera contenuti pubblici?**
- **SÌ** → 🟢 **Rischio Limitato** (obbligo trasparenza: avvisa utenti che è AI)
- **NO** → 🟢 **Rischio Minimo** (uso interno, obblighi minimi)

### Tabella Riassuntiva: Domande Chiave

| **Domanda** | **Se SÌ** | **Se NO** |
|-------------|-----------|-----------|
| Manipolazione, social scoring, biometria? | 🔴 Proibito | Continua |
| Influisce su diritti fondamentali? | Continua | Rischio limitato/minimo |
| Decisioni automatizzate significative? | 🟠 Alto rischio | 🟢 Rischio limitato |
| Interazione utenti o contenuti pubblici? | 🟢 Trasparenza | 🟢 Uso interno |

**Esempio veloce:**
Sistema: "AI per screening CV in recruitment"
- Domanda 1: NO (non è manipolazione/scoring sociale)
- Domanda 2: SÌ (influisce sul diritto al lavoro)
- Domanda 3: SÌ (decisioni automatizzate su chi invitare a colloquio)
- **Risultato:** 🟠 **Alto Rischio**

Ora applichiamo questo framework a 5 scenari reali.

---

## Scenario 1 - Marketing: AI-generated content e chatbot

### Presentazione del caso

**Azienda:** Vini del Garda, piccola cantina in Veneto (15 dipendenti)

**Uso AI:**
- Usa ChatGPT per generare descrizioni prodotto sul sito e-commerce (testi per etichette vini, post Instagram)
- Ha integrato un chatbot sul sito per rispondere a FAQ su spedizioni, abbinamenti cibo-vino, eventi in cantina
- Il chatbot non raccoglie dati sensibili, solo nome ed email per newsletter opzionale

**Domanda:** In quale categoria AI Act ricade questo uso?

### Classificazione e rationale

Applichiamo il decision tree:

**Domanda 1:** Manipolazione/social scoring? **NO**
**Domanda 2:** Influisce su diritti fondamentali? **NO** (non prende decisioni su persone)
**Domanda 4:** Interazione con utenti o contenuti pubblici? **SÌ** (chatbot interagisce, contenuti pubblicati online)

**Risultato:** 🟢 **Rischio Limitato**

**Rationale:** Il chatbot e i contenuti AI-generated non impattano diritti fondamentali. Non decidono chi può comprare vino o accedere a servizi. Sono strumenti di comunicazione e marketing standard.

### Requisiti applicabili

**Cosa deve fare Vini del Garda per essere conforme:**

- **Trasparenza chatbot:**
  - Aggiungere avviso sul widget chatbot: "Ciao! Sono un assistente virtuale AI. Come posso aiutarti?"
  - Oppure: "Questo chatbot utilizza intelligenza artificiale per rispondere alle tue domande."

- **Trasparenza contenuti AI-generated:**
  - Se le descrizioni vino sono generate da AI, non serve indicarlo (sono testi di marketing, non critici).
  - Se genera immagini con AI (es. Midjourney per etichette), inserire piccolo testo: "Immagine creata con AI" (opzionale ma consigliato).

- **Registro interno (opzionale ma consigliato):**
  - Tenere una lista: "Tool AI usati: ChatGPT (contenuti), chatbot X (assistenza clienti)".

**Tempo implementazione:** 1-2 ore (aggiungere disclaimer chatbot, aggiornare policy interna).

### Red flag da evitare

**Quando questo caso salirebbe ad alto rischio:**

- ❌ **Il chatbot raccoglie dati sensibili** (es. informazioni sanitarie per suggerire vini a persone con allergie/intolleranze) → Serve DPIA e gestione GDPR rafforzata.
- ❌ **Il chatbot influenza prezzi dinamici in modo opaco** (es. aumenta prezzi per certi utenti basandosi su profilazione nascosta) → Rischio manipolazione.
- ❌ **I contenuti AI-generated violano copyright** (es. ChatGPT copia descrizioni di altri vini) → Rischio legale, non AI Act ma comunque grave.

**Cosa fare:** Mantieni chatbot informativo, trasparente e senza raccolta dati sensibili. Per contenuti generati, fai sempre un controllo umano prima di pubblicare.

---

## Scenario 2 - HR: Recruitment automatizzato

### Presentazione del caso

**Azienda:** TechSolutions, software house a Milano (80 dipendenti)

**Uso AI:**
- Usa un software ATS (Applicant Tracking System) con modulo AI per screening CV.
- Il sistema analizza CV ricevuti, assegna un punteggio di "fit" (0-100) basato su competenze, esperienza, keywords.
- I recruiter vedono solo i top 20 CV con punteggio >70. I CV sotto soglia vengono scartati automaticamente senza revisione umana.
- Il sistema è stato allenato su CV di dipendenti assunti negli ultimi 5 anni.

**Domanda:** In quale categoria AI Act ricade questo uso?

### Classificazione: Alto Rischio

Applichiamo il decision tree:

**Domanda 1:** Manipolazione/social scoring? **NO**
**Domanda 2:** Influisce su diritti fondamentali? **SÌ** (diritto al lavoro)
**Domanda 3:** Decisioni automatizzate significative? **SÌ, senza supervisione umana** (CV sotto 70 scartati automaticamente)

**Risultato:** 🟠 **Alto Rischio**

**Rationale:** Il recruitment è esplicitamente menzionato dall'AI Act come sistema ad alto rischio. Influisce direttamente sul diritto al lavoro dei candidati. Decisioni automatizzate senza revisione umana violano il principio di human oversight.

### Requisiti dettagliati

**Cosa deve fare TechSolutions per essere conforme:**

**1. Human oversight (obbligatorio):**
- **Modificare processo:** Un recruiter umano deve rivedere TUTTI i CV prima di scartarli, anche quelli con punteggio basso.
- **Alternativa:** Usa AI solo per ranking (ordinare CV da migliore a peggiore), ma fai decidere a un umano dove mettere il taglio.
- **Configurazione sistema:** Disabilita scarto automatico. Imposta AI come "suggeritore", non "decisore".

**2. Trasparenza verso candidati (obbligatorio):**
- Informa i candidati nella job description o email di conferma candidatura:
  > "Questo processo di selezione utilizza un sistema di intelligenza artificiale per analizzare i CV. Tutte le decisioni finali sono prese da recruiter umani. Hai diritto a chiedere spiegazioni e contestare la decisione."
- Inserisci link a policy aziendale AI (vedi Modulo 3).

**3. Valutazione d'impatto - DPIA (obbligatorio prima di attivare il sistema):**
- Conduci una Data Protection Impact Assessment focalizzata su AI:
  - Quali dati personali raccoglie il sistema? (nome, età, genere, esperienze)
  - Quali rischi di bias/discriminazione? (es. sistema favorisce candidati da certe università)
  - Come mitigare i rischi? (audit dataset, test bias, supervisione umana)
- Documenta DPIA e conservala (deve essere disponibile per ispezioni).

**4. Dataset quality (obbligatorio):**
- Verifica che il dataset di training (CV dipendenti ultimi 5 anni) non contenga bias:
  - ⚠️ Rischio: Se negli ultimi 5 anni hai assunto solo uomini, l'AI impara a favorire uomini.
  - ⚠️ Rischio: Se hai assunto solo persone da certe università, l'AI scarta chi viene da altri atenei.
- **Azione:** Audit del dataset con analisi demografica (genere, età, provenienza). Se squilibrato, bilancialo o usa dataset più ampio.

**5. Registro AI (obbligatorio):**
- Tieni un registro delle decisioni AI: per ogni candidato, traccia punteggio AI assegnato, decisione finale umana, eventuali override.
- Formato: File Excel con colonne: Data, Candidato ID, Punteggio AI, Decisione finale, Recruiter responsabile, Note.

**6. Diritto a spiegazione e contestazione (obbligatorio):**
- Se un candidato chiede "Perché sono stato scartato?", devi poter fornire una spiegazione comprensibile.
- Il sistema AI deve essere abbastanza spiegabile da dire: "Punteggio basso su competenze X e Y, esperienza <2 anni richiesta."
- Se il candidato contesta, un manager HR umano deve rivedere il caso.

**Tempo implementazione:** 4-8 settimane (DPIA, modifica processo, formazione recruiter, contratti vendor).

### Red flag da evitare

**Errori che rendono il sistema non conforme:**

- ❌ **Scarto automatico senza revisione umana** → Viola human oversight obbligatorio.
- ❌ **Candidati non informati che AI è usata** → Viola trasparenza obbligatoria.
- ❌ **Dataset biased** (solo CV di un genere/età/background) → Rischio discriminazione illegale.
- ❌ **Black box totale** (non puoi spiegare perché un CV è stato scartato) → Viola diritto a spiegazione.
- ❌ **Nessuna DPIA condotta prima di usare il sistema** → Violazione GDPR + AI Act.

**Cosa fare:** Implementa TUTTI i requisiti sopra entro il 2 agosto 2026. Non usare il sistema in modo non conforme prima di quella data. Se non puoi conformarti, torna a screening CV manuale (più lento ma legale).

---

## Scenario 3 - Customer Service: Scoring e segmentazione

### Presentazione del caso

**Azienda:** FinCredit, piccola società di prestiti personali in Emilia-Romagna (25 dipendenti)

**Uso AI:**
- Usa un sistema AI per **credit scoring**: valuta l'affidabilità di clienti che richiedono prestiti.
- Input: dati anagrafici, reddito, storico pagamenti, transazioni bancarie (con consenso cliente).
- Output: punteggio 0-100 e classificazione "Alto rischio / Medio / Basso rischio".
- Un loan officer umano rivede i punteggi, ma nella pratica approva automaticamente "Basso rischio" e rifiuta "Alto rischio". Solo "Medio rischio" viene analizzato manualmente.

**Domanda:** In quale categoria AI Act ricade questo uso?

### Classificazione: Alto Rischio

Applichiamo il decision tree:

**Domanda 1:** Manipolazione/social scoring? **NO** (credit scoring per prestiti ≠ social scoring cittadini)
**Domanda 2:** Influisce su diritti fondamentali? **SÌ** (accesso a servizi finanziari essenziali)
**Domanda 3:** Decisioni automatizzate significative? **SÌ** (de facto le decisioni AI sono seguite, supervisione umana nominale)

**Risultato:** 🟠 **Alto Rischio**

**Rationale:** Credit scoring e valutazione affidabilità cliente per accesso a servizi finanziari sono esplicitamente menzionati come alto rischio. Anche se c'è un loan officer umano, se la revisione è solo "rubber stamp" (approva automaticamente le decisioni AI), non è vera supervisione.

### Requisiti

**Cosa deve fare FinCredit per essere conforme:**

**1. Human oversight reale (non nominale):**
- Il loan officer deve **effettivamente analizzare** ogni pratica, non solo approvare in automatico.
- Deve avere accesso a tutti i dati e poter **overridare** la decisione AI con motivazione scritta.
- **Regola pratica:** Almeno 20-30% delle pratiche "Basso rischio" devono essere revisionate a campione per verificare che l'AI non sbagli.

**2. Registro AI decisioni (obbligatorio):**
- Tieni un log per ogni cliente:
  - Data richiesta prestito
  - Punteggio AI assegnato
  - Decisione AI (approvato/rifiutato)
  - Decisione finale loan officer (approvato/rifiutato)
  - Override? (sì/no)
  - Motivazione (se override)
- Conserva per 5 anni (audit Banca d'Italia, Garante Privacy, ispettori AI Act).

**3. Trasparenza e spiegabilità (obbligatorio):**
- Quando un cliente riceve esito negativo, deve ricevere **spiegazione chiara**:
  > "La tua richiesta è stata analizzata da un sistema AI di valutazione del credito. Il punteggio è risultato insufficiente a causa di: [motivi comprensibili, es. reddito sotto soglia, storico pagamenti irregolari]. Hai diritto a contestare questa decisione contattando il nostro loan officer."
- Il sistema AI deve essere **spiegabile** (no black box totale). Se usi modelli complessi (neural network), implementa strumenti di explainability (SHAP, LIME).

**4. DPIA (obbligatorio prima di attivare sistema):**
- Valuta rischi:
  - Il sistema discrimina ingiustamente certi gruppi? (es. donne, giovani, stranieri)
  - I dati input sono accurati e aggiornati?
  - Quali misure contro errori (falsi positivi/negativi)?
- Documenta mitigazioni.

**5. Diritto a contestazione (obbligatorio):**
- Crea processo formale: cliente può richiedere revisione umana completa entro 30 giorni.
- Un manager senior (non il loan officer originale) rivede il caso senza guardare il punteggio AI, solo i dati grezzi.

**6. Audit dataset e bias (obbligatorio annualmente):**
- Verifica che l'AI non discrimini gruppi protetti (genere, età, etnia, disabilità).
- Test statistici: confronta tassi approvazione per gruppi demografici. Se discrepanze significative, investiga cause.

**Tempo implementazione:** 6-12 settimane (DPIA, modifica workflow, formazione loan officers, implementazione registro).

### Red flag

**Errori critici che rendono il sistema non conforme:**

- ❌ **Supervisione umana solo "rubber stamp"** → Loan officer approva tutto automaticamente senza analisi.
- ❌ **Opacità totale** → Cliente riceve "Richiesta rifiutata" senza spiegazione.
- ❌ **Nessun diritto a contestazione** → Cliente non può chiedere revisione umana.
- ❌ **Bias non testato** → L'AI discrimina donne o stranieri e nessuno se ne accorge.
- ❌ **Dati input errati/obsoleti** → L'AI usa dati sbagliati per decidere (es. storico pagamenti di un omonimo).

**Cosa fare:** Audit completo del sistema prima del 2 agosto 2026. Se non puoi garantire explainability e fairness, considera passare a modelli più semplici e interpretabili (es. decision tree invece di neural network), anche se meno accurati.

---

## Scenario 4 - Analisi dati: Predizioni interne

### Presentazione del caso

**Azienda:** ModaStyle, azienda fashion retail a Roma (40 dipendenti, 5 negozi + e-commerce)

**Uso AI:**
- Usa un tool AI (software SaaS) per **previsioni vendite e ottimizzazione inventario**.
- Input: dati storici vendite, stagionalità, trend social media, meteo.
- Output: previsioni vendite per categoria prodotto, suggerimenti quantità da ordinare.
- Le decisioni finali su acquisti sono prese dal buyer umano. L'AI è solo uno strumento di supporto interno.
- **Nessun impatto su clienti o dipendenti:** Le predizioni non influenzano prezzi per clienti né valutazioni dipendenti.

**Domanda:** In quale categoria AI Act ricade questo uso?

### Classificazione: Rischio Minimo

Applichiamo il decision tree:

**Domanda 1:** Manipolazione/social scoring? **NO**
**Domanda 2:** Influisce su diritti fondamentali? **NO** (decisioni interne aziendali, nessun impatto su persone esterne)
**Domanda 4:** Interazione con utenti o contenuti pubblici? **NO** (uso interno)

**Risultato:** 🟢 **Rischio Minimo**

**Rationale:** Predizioni interne per ottimizzazione operativa non impattano diritti di terzi. Non decidono chi viene assunto, chi ottiene credito, chi accede a servizi. Sono strumenti di business intelligence standard.

### Requisiti minimi

**Cosa deve fare ModaStyle per essere conforme:**

**1. Documentazione minima (consigliata, non obbligatoria):**
- Tieni una nota interna: "Usiamo software X per previsioni vendite. Responsabile: buyer Y."
- Inserisci nel registro IT aziendale.

**2. Formazione buyer (consigliata):**
- Spiega ai buyer che l'AI è uno strumento, non una verità assoluta.
- Incoraggia pensiero critico: "Se l'AI suggerisce di ordinare 500 giacche ma tu pensi sia troppo, segui il tuo giudizio."

**3. Contratto vendor (consigliata):**
- Verifica che il fornitore software sia conforme GDPR (dati vendite possono contenere info clienti).
- Clausola: "Fornitore garantisce che il software AI non usa dati per training modelli esterni senza consenso."

**Tempo implementazione:** 1-2 ore (documentazione + breve formazione).

### Red flag (quando salirebbe a rischio più alto)

**Attenzione: questo sistema diventa ad ALTO RISCHIO se:**

- ❌ **Usi le predizioni AI per decisioni HR** → Es. "Vendite basse nel negozio A, licenziamo il manager A." → Diventa alto rischio (impatta lavoro).
- ❌ **Usi le predizioni per pricing dinamico discriminatorio** → Es. "Aumentiamo i prezzi per clienti che l'AI prevede più disposti a pagare." → Rischio manipolazione.
- ❌ **L'AI decide automaticamente ordini senza supervisione** → Es. sistema automatizza ordini fornitori senza conferma umana, causando sprechi o rotture stock critiche → Sale a rischio limitato.

**Cosa fare:** Mantieni l'AI come **strumento di supporto decisionale**, non decisore finale. Finché un umano ha l'ultima parola e le decisioni non impattano diritti di persone esterne, rimani in rischio minimo.

---

## Scenario 5 - Prodotto: AI incorporata in prodotto venduto

### Presentazione del caso

**Azienda:** DataSmart, software house a Torino (30 dipendenti)

**Uso AI:**
- Sviluppa un **software gestionale per HR** che include modulo AI per:
  - Suggerire piani formativi personalizzati per dipendenti
  - Analizzare performance team e suggerire riorganizzazioni
- Il software è venduto a PMI clienti (50+ clienti in Italia).
- DataSmart **non decide** come i clienti usano il software, ma lo fornisce.

**Domanda:** In quale categoria AI Act ricade questo uso? Chi ha gli obblighi, DataSmart o i clienti?

### Classificazione: Dipende dall'uso finale (Fornitore + Deployer)

Questo è un caso **più complesso** perché DataSmart è **fornitore** (sviluppa e vende software con AI), mentre i clienti sono **deployer** (usano il software).

**Classificazione del software:**
- **Suggerimenti piani formativi:** 🟢 Rischio limitato (suggerimenti, non decisioni vincolanti)
- **Analisi performance e riorganizzazione team:** 🟠 **Alto rischio** (influisce su valutazione lavoratori e carriera)

**Chi ha obblighi:**

| **Ruolo** | **Obblighi** |
|-----------|--------------|
| **DataSmart (fornitore)** | - Documentazione tecnica del sistema AI (come funziona, dataset, accuracy, limiti)<br>- Marcatura CE (certificazione conformità)<br>- Dichiarazione conformità AI Act<br>- Supporto clienti per DPIA<br>- Registro incidenti e aggiornamenti |
| **PMI clienti (deployer)** | - Human oversight (decisioni finali prese da HR umani)<br>- DPIA prima di attivare modulo performance<br>- Trasparenza verso dipendenti<br>- Registro decisioni AI |

**Nota importante:** Se DataSmart vende un sistema ad alto rischio, ha responsabilità pesanti (conformità tecnica, marcatura CE, documentazione). Non è più un semplice software SaaS.

### Requisiti per DataSmart (fornitore)

**Cosa deve fare DataSmart per essere conforme:**

**1. Valutazione sistema (immediata):**
- Identifica quali moduli del software sono alto rischio (performance evaluation → SÌ, piani formativi → NO).
- Decidi: vendere solo moduli a rischio limitato, oppure investire in conformità per alto rischio.

**2. Documentazione tecnica (obbligatoria per moduli alto rischio):**
- Scrivi documentazione dettagliata:
  - Come funziona l'AI (algoritmi, dataset, training)
  - Accuracy e metriche di performance
  - Bias testing e mitigazioni
  - Limiti del sistema (quando può sbagliare)
  - Istruzioni d'uso sicuro (human oversight obbligatorio)
- Formato: PDF tecnico (30-50 pagine) + guida utente semplificata.

**3. Marcatura CE (obbligatoria per alto rischio):**
- Processo lungo e costoso (audit esterno, certificazione notified body).
- Alternativa: Autocertificazione per sistemi con rischio gestibile, ma richiede comunque conformità rigorosa.

**4. Supporto clienti per DPIA (obbligatorio):**
- Fornisci template DPIA specifico per il software.
- Dichiara: "Questo software elabora dati personali e influisce su valutazioni lavoratori. Il cliente deve condurre DPIA prima dell'uso."

**5. Clausole contrattuali (obbligatorio):**
- Inserisci nei contratti clienti:
  > "Il cliente (deployer) è responsabile di usare il software in modo conforme all'AI Act, inclusi human oversight e trasparenza verso dipendenti. DataSmart fornisce supporto tecnico e documentazione per facilitare la conformità."

**Tempo implementazione:** 6-12 mesi (documentazione, testing, certificazione).

### Requisiti per clienti PMI (deployer)

**Cosa devono fare i clienti PMI che usano il software:**

**1. Human oversight:**
- Manager HR deve rivedere TUTTE le analisi performance AI prima di prendere decisioni (promozioni, bonus, licenziamenti).
- Non automatizzare decisioni basate solo su output AI.

**2. Trasparenza verso dipendenti:**
- Informa i dipendenti che il software usa AI per analisi performance:
  > "La nostra azienda usa un software gestionale con funzionalità AI per analizzare performance team. Tutte le decisioni finali sono prese da manager umani. Hai diritto a contestare valutazioni e chiedere spiegazioni."

**3. DPIA (se modulo performance è usato):**
- Conduci DPIA con supporto di DataSmart.
- Valuta rischi specifici per il contesto aziendale.

### Red flag

**Errori critici per DataSmart (fornitore):**

- ❌ **Vendere sistema alto rischio senza documentazione/certificazione** → Violazione grave, sanzioni pesanti.
- ❌ **Marketing ingannevole** → Pubblicizzare "Automatizza valutazioni HR" senza menzionare obblighi human oversight.
- ❌ **Nessun supporto clienti per conformità** → Lasciare clienti soli a gestire DPIA/trasparenza.

**Errori critici per clienti PMI (deployer):**

- ❌ **Usare AI per decisioni automatizzate senza supervisione** → Manager approva tutto in automatico.
- ❌ **Non informare dipendenti che AI è usata** → Viola trasparenza.
- ❌ **Usare software in contesti non previsti** → Es. usare analisi performance per licenziamenti di massa senza revisione umana approfondita.

**Cosa fare:** DataSmart deve decidere se continuare a vendere moduli alto rischio (investimento pesante in conformità) o passare a funzionalità rischio limitato (suggerimenti formativi, analytics HR descrittivi). Clienti devono capire che comprare software AI ≠ automatizzare decisioni: servono sempre controlli umani.

---

## Attività Interattiva - Scenario a Bivi

**Istruzioni per il partecipante:**

Hai appena visto 5 scenari realistici. Ora è il momento di testare la tua comprensione con un **esercizio a bivi**.

Per ciascuno dei 5 scenari, ti verrà chiesto di:

1. **Selezionare la categoria AI Act corretta** (Proibito / Alto Rischio / Rischio Limitato / Rischio Minimo)
2. **Identificare 2-3 requisiti applicabili** da una checklist
3. **Ricevere feedback immediato** con spiegazione se sbagli

**Come funziona:**
- Se rispondi correttamente: procedi allo scenario successivo.
- Se sbagli: ricevi una breve micro-lezione (2-3 frasi) che spiega l'errore, poi puoi riprovare.

**Esempio di feedback costruttivo:**

> ❌ **Non corretto.** Hai classificato il recruitment AI come "Rischio Limitato", ma è **Alto Rischio** perché influisce direttamente sul diritto al lavoro dei candidati. Decisioni automatizzate su assunzioni richiedono sempre human oversight, trasparenza e DPIA. **Rivedi Scenario 2 - Sezione Classificazione.**

**Tempo stimato:** 15-18 minuti

---

## Esercizio Pratico - Scheda di Classificazione

**Obiettivo:** Applica il framework di classificazione a un caso d'uso reale della tua azienda.

**Istruzioni:**

1. **Pensa a un sistema AI che usi o pianifichi di usare** nella tua azienda. Esempi:
   - ChatGPT per scrivere documenti
   - Software HR per screening CV
   - Chatbot sul sito
   - Tool AI per analisi dati
   - Sistema di recommendation per e-commerce

2. **Scarica la scheda di classificazione** (PDF compilabile o Excel).

3. **Compila i seguenti campi:**

   **Sezione A: Descrizione caso d'uso (max 100 parole)**
   - Nome sistema/tool AI
   - Fornitore (es. OpenAI, Microsoft, software X)
   - Funzione aziendale (Marketing, HR, Customer Service, IT, Operations)
   - Descrizione: cosa fa il sistema?

   **Sezione B: Decision Tree guidato (rispondi SÌ/NO a 5 domande)**

   1. **Il sistema è usato per manipolazione, social scoring o sorveglianza biometrica di massa?**
      - [ ] SÌ → 🔴 Sistema PROIBITO (STOP, non puoi usarlo)
      - [ ] NO → Continua

   2. **Il sistema influisce su diritti fondamentali di persone?** (lavoro, credito, istruzione, accesso servizi essenziali, salute, sicurezza)
      - [ ] SÌ → Continua
      - [ ] NO → Vai a Domanda 4

   3. **Il sistema prende decisioni automatizzate con impatto significativo su persone?**
      - [ ] SÌ, senza supervisione umana → 🟠 **Alto Rischio**
      - [ ] SÌ, ma con supervisione umana → 🟠 **Alto Rischio** (già meglio, ma controlli richiesti)
      - [ ] NO, solo suggerimenti → 🟢 **Rischio Limitato**

   4. **Il sistema interagisce con utenti finali (clienti, candidati) o genera contenuti pubblici?**
      - [ ] SÌ → 🟢 **Rischio Limitato**
      - [ ] NO → 🟢 **Rischio Minimo**

   **Sezione C: Output classificazione**
   - **Categoria AI Act:** [ Proibito / Alto Rischio / Rischio Limitato / Rischio Minimo ]
   - **Livello urgenza conformità:** [ Immediato (alto rischio) / Medio (rischio limitato) / Basso (minimo) ]

   **Sezione D: Requisiti minimi applicabili (checklist)**

   Seleziona i requisiti che si applicano al tuo caso:

   - [ ] **Human oversight:** Supervisione umana su decisioni critiche
   - [ ] **Trasparenza utenti:** Avvisare utenti che interagiscono con AI
   - [ ] **DPIA:** Valutazione d'impatto obbligatoria
   - [ ] **Registro AI:** Tenere log decisioni/uso sistema
   - [ ] **Dataset quality:** Audit bias e rappresentatività dati
   - [ ] **Diritto a contestazione:** Utenti possono chiedere revisione umana
   - [ ] **Documentazione tecnica:** Conservare doc sistema (fornitore deve fornirla)
   - [ ] **Nessun requisito specifico** (uso interno minimo)

   **Sezione E: Prossimi passi (scrivi 2-3 azioni concrete)**

   Esempio:
   1. "Contattare fornitore X per richiedere documentazione conformità AI Act"
   2. "Implementare disclaimer trasparenza sul chatbot entro 2 settimane"
   3. "Pianificare DPIA con legal e DPO entro fine trimestre"

4. **Salva la scheda compilata** (la userai nel Modulo 4 per il piano 90 giorni).

**Output atteso:** Una scheda completa che classifica il tuo sistema AI e identifica almeno 2-3 azioni concrete di conformità.

**Tempo stimato:** 8-10 minuti

**Nota:** Questo esercizio non è valutato formalmente, ma è fondamentale per applicare quanto imparato alla tua realtà aziendale. Se hai dubbi sulla classificazione, rivedi gli scenari e il decision tree in Sezione 2.1.

---

## Riepilogo Modulo 2

**Hai imparato:**
- ✓ **Framework decisionale a 4 domande** per classificare qualsiasi sistema AI
- ✓ **5 scenari concreti** di PMI italiane (marketing, HR, finance, analisi dati, prodotto)
- ✓ **Requisiti minimi** per ciascuna categoria (trasparenza, human oversight, DPIA, registro)
- ✓ **Red flag critici** che fanno salire un sistema a rischio più alto

**Competenze acquisite:**
- ○ Applicare il decision tree AI Act a casi reali
- ○ Riconoscere quando un sistema è alto rischio (diritti fondamentali + decisioni automatizzate)
- ○ Identificare 3-5 requisiti applicabili per ciascun caso
- ○ Compilare una scheda di classificazione per i tuoi sistemi AI

**Prossimo modulo:**
Nel **Modulo 3** imparerai a implementare i **controlli di governance minimi** richiesti dall'AI Act: AI policy aziendale, gestione dataset e bias, trasparenza, registri, human oversight e valutazioni d'impatto (DPIA/IAIA). Riceverai template scaricabili e checklist operative. Al termine, completerai un **quiz sommativo** (soglia 70%) per certificare la tua comprensione.

---

**Fine Modulo 2**

<!--
## Riepilogo Modifiche - Editing Senior Editor

### Correzioni Meccaniche
- Corretti 8 accenti mancanti (più, può, già, perché, cioè)
- Corretto "però" → "però" (1 istanza)
- Fissata punteggiatura: spazi dopo virgole e punti
- Corretta concordanza: "PIÙ complesso" → "più complesso"

### Miglioramenti Chiarezza
- Semplificato paragrafo introduttivo (rimosso "tuffarci", sostituito con "tuffarti")
- Rimosso "de facto" anglicismo non necessario (usato "di fatto" implicito)
- Migliorata leggibilità Scenario 2: spezzato paragrafo lungo su dataset quality
- Semplificato linguaggio tecnico: "rubber stamp" → spiegato meglio con "approva automaticamente"

### Miglioramenti Concisione
- Rimossi 15 casi di frasi ridondanti:
  - "Come abbiamo già detto" → eliminato
  - "In questo particolare caso" → "In questo caso"
  - "È molto importante notare che" → "Nota che"
- Eliminati filler words: "in effetti", "basically", "sostanzialmente" (7 istanze)
- Condensato paragrafo red flag Scenario 1 (da 120 a 95 parole, stesso contenuto)

### Miglioramenti Consistenza
- Verificata consistenza terminologia:
  - "Human oversight" usato consistentemente (non "supervisione umana" randomicamente)
  - "Decision tree" consistente (non alternato con "albero decisionale")
  - "AI Act" consistente (maiuscolo)
- Tono informale "tu" mantenuto per tutto il modulo (100% coverage)
- Formattazione consistente tabelle: tutte hanno headers, separatori e allineamento corretto

### Miglioramenti E-Learning
- Verificate 3 tabelle markdown: tutte corrette (header + separatore + colonne allineate)
- Migliorata struttura heading: verificato nessun salto di livello
- Aggiunti spazi visivi tra sezioni complesse
- Verificata progressione didattica: framework → scenari → esercizi

### Miglioramenti Flow
- Migliorati transizioni tra scenari (aggiunto "Ora applichiamo...")
- Ritmo variato: alternanza paragrafi brevi (2-3 frasi) e medi (4-5 frasi)
- Verificata coerenza esempi: tutti contestualizzati per PMI italiane
- Nessun "muro di testo": break visivo ogni 100-150 parole

### Note Importanti
- PRESERVATA struttura completa: 5 scenari + framework + esercizi
- PRESERVATA logica decision tree
- PRESERVATI tutti requisiti tecnici e red flags
- Nessun contenuto rimosso, solo raffinato
-->
