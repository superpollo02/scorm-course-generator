# GLOSSARIO TERMINI EU AI ACT

**Per PMI Italiane - Edizione 2024**

---

## Come Usare Questo Glossario

Questo glossario fornisce definizioni pratiche e comprensibili dei termini chiave dell'EU AI Act, specificamente pensate per professionisti PMI non tecnici.

**Organizzazione:**
- **Ordine alfabetico** per facile consultazione
- **Definizioni brevi** (2-3 frasi massimo)
- **Esempi pratici** in contesto PMI italiano
- **Riferimenti incrociati** tra termini correlati

**Convenzioni:**
- *Corsivo*: termine tecnico inglese/europeo
- **Grassetto**: concetto chiave
- 🔴🟠🟡🟢: icone categorie rischio AI Act
- → vedi: riferimento ad altro termine

---

## A

### Accuracy (Accuratezza)
Percentuale di decisioni corrette di un sistema AI. Esempio: se un AI per recruitment raccomanda 100 candidati e 85 vengono effettivamente assunti, l'accuracy è 85%. Importante: alta accuracy non garantisce assenza di bias.

### AI Act
→ vedi **EU AI Act**

### AI Owner
Ruolo aziendale (spesso Legal/Compliance) responsabile del coordinamento della conformità AI Act. Gestisce il registro AI, conduce gap analysis, coordina DPIA/IAIA. Nelle PMI piccole può essere ricoperto part-time.

### AI Policy
Documento interno (1-2 pagine) che definisce le regole aziendali per l'uso di intelligenza artificiale. Deve contenere: principi etici, ruoli/responsabilità, processo approvazione nuovi tool, gestione incident, piano formazione. Deve essere approvata da CEO/Board.

### Algoritmo
Insieme di istruzioni che un computer segue per risolvere un problema. Esempio: un algoritmo AI per credit scoring analizza reddito, storico pagamenti, età per calcolare un punteggio di affidabilità. Non tutti gli algoritmi sono AI.

### Alto Rischio
→ vedi **Sistemi ad Alto Rischio**

### Automation Bias
Tendenza umana a fidarsi ciecamente delle decisioni AI senza usare spirito critico. Esempio: un recruiter che accetta sempre le raccomandazioni AI senza rivedere CV scartati. Rischio critico per conformità AI Act (viola human oversight).

---

## B

### Bias (Discriminazione Algoritmica)
Quando un sistema AI discrimina sistematicamente certi gruppi di persone (genere, età, etnia, disabilità). Può essere **nei dati storici** (l'AI impara discriminazioni passate), **di selezione** (dataset non rappresentativo), o **di misurazione** (proxy variables che correlano con categorie protette).

**Esempio:** AI per recruitment allenata solo su CV maschili impara che "donna = meno adatta" → bias di genere illegale.

### Bias di Conferma
→ vedi **Automation Bias**

### Bias di Misurazione
Tipo di bias causato dall'uso di **proxy variables** (variabili indirette) che correlano con categorie protette. Esempio: usare "università frequentata" per valutare candidati discrimina indirettamente status socioeconomico (università costose = famiglie ricche).

### Bias di Selezione
Tipo di bias quando il dataset non rappresenta la popolazione reale. Esempio: AI per credit scoring allenata solo su clienti attuali (già approvati) non impara a riconoscere rischi reali perché non ha mai visto candidati rifiutati.

### Bias nei Dati Storici
Tipo di bias quando i dati riflettono discriminazioni del passato. Esempio: se negli ultimi 10 anni hai assunto solo 5% donne in ruoli tecnici, l'AI impara che "donna = meno adatta ruoli tecnici" → perpetua la discriminazione.

### Black Box
Sistema AI il cui funzionamento interno non è trasparente o comprensibile. Esempio: reti neurali profonde. Problema per AI Act: se non puoi spiegare perché l'AI ha scartato un candidato, violi il diritto a spiegazione. Soluzione: tool di explainability (SHAP, LIME).

---

## C

### Calibration (Calibrazione)
In fairness testing, verifica che l'AI non sovrastimi o sottostimi sistematicamente un gruppo demografico. Esempio: se l'AI prevede 70% successo per donne ma solo 50% ha effettivamente successo (mentre per uomini prevede 70% e 70% ha successo), non è calibrata.

### Categoria Rischio
L'AI Act classifica i sistemi AI in 4 categorie in base al rischio per diritti fondamentali: 🔴 **Proibito**, 🟠 **Alto Rischio**, 🟡 **GPAI**, 🟢 **Rischio Limitato/Minimo**. Ogni categoria ha obblighi diversi.

### Chatbot
Assistente virtuale che interagisce con utenti tramite testo (es. chatbot su sito e-commerce). Secondo AI Act, è generalmente **rischio limitato** con obbligo di trasparenza: devi informare l'utente che sta parlando con un'AI.

### Clausole Contrattuali AI Act
Clausole specifiche da inserire nei contratti con fornitori AI per condividere responsabilità conformità. Devono includere: obbligo conformità normativa, diritto audit, responsabilità in caso incident, supporto DPIA, procedura notifica modifiche.

### Compliance
Conformità alle normative. Nel contesto AI Act: implementare tutti i controlli richiesti per la categoria di rischio del proprio sistema AI (policy, registri, trasparenza, human oversight, DPIA, ecc.).

### Credit Scoring
Valutazione automatizzata dell'affidabilità creditizia di una persona tramite AI. Esempio: sistema che analizza reddito, storico pagamenti, età per decidere se approvare un prestito. Secondo AI Act è **alto rischio** perché impatta accesso a servizi finanziari essenziali.

---

## D

### Dataset
Insieme di dati usati per "allenare" (training) un sistema AI o come input per decisioni AI. Esempio: un dataset di recruitment contiene 1000 CV di candidati passati. Qualità del dataset è critica: dataset biased → AI biased.

### Decision Tree (Albero Decisionale)
Strumento per classificare sistemi AI nelle categorie AI Act rispondendo a domande sequenziali. Esempio del corso: 4 domande chiave → determina se sistema è proibito, alto rischio, o rischio limitato/minimo.

### Deployer (Utilizzatore)
Chi **usa** sistemi AI sviluppati da altri per le proprie attività aziendali. Esempio: PMI che usa ChatGPT, chatbot, software HR con AI. **La maggior parte delle PMI è deployer, non fornitore**. Ha obblighi più leggeri ma comunque precisi.

### DPIA (Data Protection Impact Assessment)
Valutazione d'impatto sulla privacy richiesta dal GDPR quando tratti dati personali ad alto rischio. Per sistemi AI è obbligatoria se: tratti dati sensibili, prendi decisioni automatizzate su persone, o monitori comportamenti su larga scala. Deve essere approvata dal DPO.

### DPO (Data Protection Officer)
Responsabile della protezione dati personali in azienda (obbligatorio GDPR se oltre certe soglie). Per AI Act: approva DPIA, rivede AI policy per coerenza GDPR, consulenza su privacy + AI. PMI piccole (<50 dipendenti) possono usare DPO esterno part-time.

### Diritto a Contestazione
Per sistemi ad alto rischio, l'utente deve poter contestare una decisione AI negativa e richiedere revisione umana completa. Esempio: candidato scartato da AI recruitment può chiedere che un recruiter umano riveda il suo CV. Risposta entro 30 giorni (standard GDPR).

### Diritto a Spiegazione
Per sistemi ad alto rischio, se l'AI prende una decisione negativa su una persona, devi poter spiegare **perché** in linguaggio comprensibile. Esempio: "CV scartato perché esperienza <2 anni (richiesta 3) e mancanza certificazione X". Richiede sistemi AI spiegabili (no black box totali).

---

## E

### Equal Opportunity (Pari Opportunità)
In fairness testing, verifica che il tasso di approvazione AI sia simile per tutti i gruppi demografici a parità di qualifiche. Esempio: se donne e uomini con stesso reddito/esperienza hanno tassi approvazione prestito molto diversi, l'AI viola equal opportunity.

### EU AI Act
Regolamento UE 2024/1689, prima legge al mondo che regola l'intelligenza artificiale. Entrata in vigore 1° agosto 2024, applicazione per fasi 2025-2027. Obiettivo: bilanciare innovazione e protezione diritti fondamentali. Si applica a fornitori e deployer di sistemi AI.

### Explainability (Spiegabilità)
Capacità di un sistema AI di fornire spiegazioni comprensibili per le sue decisioni. Obbligatoria per sistemi ad alto rischio (diritto a spiegazione). Tool: SHAP, LIME. Esempio: "Punteggio basso perché esperienza insufficiente (peso 40%) e mancanza skill X (peso 30%)".

---

## F

### Fairness (Equità)
Principio che l'AI deve trattare tutti i gruppi di persone equamente, senza discriminazioni. Si misura con **fairness testing**: confrontare accuracy, tassi approvazione, errori tra gruppi demografici. Se discrepanze significative → bias da correggere.

### Fairness Testing
Test statistici per rilevare bias in sistemi AI. Metodi: confrontare performance AI su sottogruppi demografici (genere, età, etnia). Metriche: equal opportunity, calibration, disparate impact. Tool: Python (fairlearn, AIF360) o report vendor.

### False Negative
Errore AI: classificare come "negativo" qualcosa che è "positivo". Esempio recruitment: scartare un candidato valido (l'AI dice "no" ma il candidato sarebbe stato bravo). Costo: perdere talenti. Da monitorare con human oversight.

### False Positive
Errore AI: classificare come "positivo" qualcosa che è "negativo". Esempio recruitment: raccomandare un candidato inadatto (l'AI dice "sì" ma il candidato non è bravo). Costo: tempo perso in colloqui. Meno grave di false negative per diritti fondamentali.

### Feature (Caratteristica)
Variabile che l'AI usa per prendere decisioni. Esempio credit scoring: reddito, età, storico pagamenti sono "features". Importante verificare che features non siano proxy variables che discriminano categorie protette (es. codice postale = proxy per etnia).

### Feature Importance
In explainability, indica quanto ciascuna feature influenza la decisione AI. Esempio: "Esperienza lavorativa pesa 40%, formazione 30%, soft skills 20%, altro 10%". Utile per diritto a spiegazione in sistemi ad alto rischio.

### Fornitore (Provider)
Chi **sviluppa e vende** sistemi AI a clienti. Esempio: OpenAI (fornisce ChatGPT), software house che crea tool AI per PMI. Ha obblighi pesanti: documentazione tecnica, marcatura CE (se alto rischio), dichiarazione conformità, supporto deployer per DPIA.

---

## G

### Gap Analysis
Analisi per identificare la distanza tra stato attuale e piena conformità AI Act. Per ciascun sistema AI: confronti requisiti AI Act vs cosa hai implementato → identifichi gap → pianifichi azioni correttive. Output: report con lista gap + owner + deadline.

### GDPR (General Data Protection Regulation)
Regolamento UE 2016/679 sulla protezione dati personali. Complementare all'AI Act: GDPR protegge privacy, AI Act protegge diritti fondamentali più ampi (lavoro, equità, accesso servizi). Molti obblighi si sovrappongono (es. DPIA).

### General Purpose AI (GPAI)
→ vedi **GPAI**

### Governance
Insieme di policy, processi, ruoli e controlli per gestire l'uso di AI in azienda. Elementi chiave: AI policy, registro AI, RACI matrix, processo approvazione nuovi tool, gestione incident, formazione. Obiettivo: uso responsabile e conforme di AI.

### GPAI (General Purpose AI)
Modelli fondazionali di grandi dimensioni usabili per scopi multipli. Esempi: GPT-4 (OpenAI), Claude (Anthropic), Gemini (Google), Llama (Meta). Per PMI deployer: se usi ChatGPT/Copilot non hai obblighi diretti (ricadono sui fornitori), a meno che non integri GPAI in sistema ad alto rischio.

---

## H

### Human-in-command (al comando)
Livello base di supervisione umana: un umano può disattivare o modificare il sistema AI ma non rivede ogni decisione. Esempio: IT manager può spegnere AI se malfunziona. Minimo per tutti i sistemi (backup generale).

### Human-in-the-loop (nel ciclo)
Livello massimo di supervisione umana: un umano rivede e approva **ogni singola decisione** AI prima che venga applicata. Esempio: recruiter valida ogni shortlist CV prima di inviare inviti. **Obbligatorio per sistemi ad alto rischio con decisioni critiche** (recruitment, licenziamenti, diniego credito).

### Human-on-the-loop (sul ciclo)
Livello intermedio di supervisione umana: un umano monitora l'AI e può intervenire se rileva anomalie. Esempio: operatore customer service corregge chatbot se dà risposta errata. Per sistemi a rischio limitato/medio.

### Human Oversight (Supervisione Umana)
Obbligo per sistemi ad alto rischio: un operatore umano deve poter monitorare, intervenire e correggere decisioni AI. Non è sufficiente "c'è un umano da qualche parte": serve supervisione **attiva e documentata**. Livelli: in-the-loop, on-the-loop, in-command.

---

## I

### IAIA (Impact Assessment IA Act)
Valutazione d'impatto sui diritti fondamentali specifica per AI, richiesta dall'AI Act per sistemi ad alto rischio. Focus: non solo privacy (come DPIA), ma anche lavoro, non-discriminazione, accesso servizi, dignità, equità algoritmica, robustezza. Best practice: documento integrato DPIA+IAIA.

### Incident AI
Evento problematico causato da un sistema AI. Esempi: decisione AI errata che danneggia una persona, bias rilevato in produzione, violazione dati tramite AI, malfunzionamento tecnico grave. Deve essere documentato in registro incident e, se grave, notificato ad autorità (Garante Privacy, autorità AI Act).

### Inventory AI (Censimento AI)
Primo passo conformità: mappare tutti i sistemi AI usati in azienda. Output: registro AI con nome tool, fornitore, funzione, categoria rischio, responsabile, dataset, status. Identifica anche "shadow AI" (tool usati senza consapevolezza management).

---

## K

### KPI (Key Performance Indicator)
Metriche per monitorare progresso conformità AI Act. Esempi: % sistemi AI censiti (target 100%), AI policy approvata (sì/no), DPIA completate per alto rischio (N°), vendor valutati (%), dipendenti formati (%). Da tracciare in dashboard Excel/BI.

---

## L

### LMS (Learning Management System)
Piattaforma e-learning (es. Moodle, Canvas, Blackboard) dove si caricano corsi SCORM. Per importare corso AI Act: vai a "Aggiungi attività" → "Pacchetto SCORM" → carica ZIP → fatto.

### Log (Registro Decisioni)
Per sistemi ad alto rischio, tracciamento di tutte le decisioni AI: data, utente, input, output, decisione finale umana, eventuali override. Formato: Excel con colonne (Data, Sistema, Utente, Input, Output AI, Decisione finale, Note). Conservare 5 anni per audit.

---

## M

### Manipolazione Comportamento
Sistema AI che sfrutta vulnerabilità psicologiche per influenzare scelte (es. app che manipola bambini verso comportamenti pericolosi). **Proibito** dall'AI Act (rischio inaccettabile). Molto improbabile che PMI usi sistemi del genere.

### Marcatura CE
Certificazione europea di conformità. Per fornitori di sistemi AI ad alto rischio è obbligatoria (processo lungo: audit esterno, notified body). Per PMI deployer non è richiesta (obbligo ricade sui fornitori).

### Modello Fondazionale
→ vedi **GPAI**

---

## N

### Neural Network (Rete Neurale)
Tipo di algoritmo AI ispirato al cervello umano. Ottimo per accuracy ma spesso **black box** (difficile spiegare perché decide così). Problema per alto rischio: se non puoi spiegare decisioni, violi diritto a spiegazione. Soluzione: reti più semplici o tool explainability.

---

## O

### Opacità
→ vedi **Black Box**

### Override
Quando un operatore umano scavalca una decisione AI prendendo decisione diversa. Esempio: AI dice "rifiuta prestito" ma loan officer vede informazioni aggiuntive e approva manualmente. Deve essere documentato con motivazione. Indicatore chiave di human oversight effettivo (se override = 0% sempre, è "rubber stamp").

---

## P

### Profilazione
Uso di AI per valutare aspetti di una persona (performance, comportamento, affidabilità). Esempio: credit scoring, valutazione dipendenti. Se automatizzata e impatta diritti fondamentali, è **alto rischio** (richiede human oversight, DPIA, trasparenza).

### Proxy Variable (Variabile Indiretta)
Feature che correla con una categoria protetta anche se non la misura direttamente. Esempio: "codice postale" può essere proxy per etnia (certi quartieri = certe etnie), "università frequentata" per status socioeconomico. Causa **bias di misurazione**.

---

## R

### RACI Matrix
Matrice per assegnare ruoli e responsabilità. RACI = Responsible (chi esegue), Accountable (chi approva), Consulted (chi consulti), Informed (chi informi). Utile per piano 90 giorni: chiarisce chi fa cosa per conformità AI Act.

### Registro AI
File (Excel/Google Sheet) che elenca tutti i sistemi AI usati in azienda. Colonne minime: Nome sistema, Fornitore, Categoria rischio, Funzione/Responsabile, Dataset, Log modifiche. Deve essere aggiornato trimestralmente + in tempo reale quando aggiungi/rimuovi sistemi.

### Riconoscimento Biometrico
AI che identifica persone tramite caratteristiche fisiche (volto, impronte, voce). Riconoscimento facciale in tempo reale in spazi pubblici per sorveglianza di massa è **proibito** (salvo limitate eccezioni forze ordine). Riconoscimento per unlock smartphone è OK (non pubblico).

### Rischio Inaccettabile
→ vedi **Sistemi Proibiti**

### Rischio Limitato / Rischio Minimo
🟢 Categoria AI Act per la **maggioranza degli usi AI nelle PMI**: chatbot, tool generazione contenuti, analisi dati interne, assistenti virtuali. Obblighi leggeri: trasparenza (informare utenti che è AI), watermark contenuti AI-generated. Esempi: ChatGPT per email, chatbot e-commerce, previsioni vendite interne.

### Rubber Stamp
Supervisione umana solo "nominale": l'operatore approva automaticamente tutte le decisioni AI senza analisi reale. **Non è conforme** all'AI Act. Esempio: loan officer che clicca "approva" su tutte le pratiche suggerite da AI senza leggerle. Serve supervisione **effettiva**, non formale.

---

## S

### SCORM (Shareable Content Object Reference Model)
Standard e-learning per pacchetti didattici compatibili con tutti gli LMS. SCORM 1.2 (usato nel corso) è il più universale (dal 2001). Funziona su Moodle, Canvas, Blackboard, tutti i principali LMS.

### Shadow AI
Tool AI usati in azienda senza consapevolezza del management. Esempio: marketing usa Midjourney per immagini senza informare IT/Legal. Rischio: non conformità, violazione policy. L'inventory AI serve a scoprire shadow AI.

### SHAP / LIME
Tool tecnici per explainability: rendono comprensibili decisioni di AI complesse (black box). SHAP = SHapley Additive exPlanations, LIME = Local Interpretable Model-agnostic Explanations. Usati da data scientist per analizzare feature importance e fornire spiegazioni.

### Sistemi ad Alto Rischio
🟠 Sistemi AI che impattano diritti fondamentali: lavoro, credito, istruzione, accesso servizi essenziali, sicurezza, salute. Esempi PMI: recruitment AI, credit scoring, valutazione performance dipendenti. **Obblighi pesanti:** human oversight, trasparenza, DPIA, registri, dataset quality audit, diritto contestazione.

### Sistemi Proibiti
🔴 Sistemi AI vietati perché violano diritti fondamentali (rischio inaccettabile). Esempi: manipolazione comportamento, social scoring cittadini, riconoscimento biometrico di massa in pubblico. **Non puoi usarli in nessun caso** (salvo eccezioni forze ordine). Molto improbabile che PMI usi sistemi proibiti.

### Social Scoring
Sistemi che assegnano punteggi sociali ai cittadini basati su comportamento o caratteristiche personali (modello Cina). **Proibito** dall'AI Act. Diverso da credit scoring (che è specifico per prestiti e lecito con controlli).

### Spiegabilità
→ vedi **Explainability**

### Supervisione Umana
→ vedi **Human Oversight**

---

## T

### Timeline AI Act
Applicazione per fasi:
- **2 febbraio 2025:** Divieto sistemi proibiti
- **2 agosto 2025:** Obblighi fornitori GPAI
- **2 agosto 2026:** 🔴 **Data cruciale PMI:** Obblighi sistemi ad alto rischio (HR, credit scoring, valutazione lavoratori)
- **2 agosto 2027:** Piena applicazione per tutti

### Training (Allenamento)
Processo di "insegnare" a un sistema AI analizzando dati storici (dataset). Esempio: AI recruitment è "allenata" su 1000 CV di candidati passati per imparare pattern di successo. Qualità training dipende da qualità dataset: dataset biased → AI biased.

### Trasparenza
Obbligo di informare utenti che stanno interagendo con AI o che un contenuto è stato generato da AI. Per **rischio limitato** (chatbot): disclaimer "Sono un assistente virtuale AI". Per **alto rischio** (recruitment): informare candidati che AI è coinvolta + spiegare decisioni negative.

---

## V

### Valutazione d'Impatto
→ vedi **DPIA** e **IAIA**

### Vendor (Fornitore)
→ vedi **Fornitore**

### Vendor Due Diligence
Processo di valutazione dei fornitori AI per verificare conformità AI Act. Include: questionario 15 domande (conformità, dataset, bias, sicurezza, supporto), analisi risposte, negoziazione clausole contrattuali. Output: report vendor (maturo/in progress/impreparato) + contratti aggiornati.

---

## W

### Watermark
Etichetta su contenuti AI-generated (immagini, video, audio) che indica sono creati da AI. Può essere: testo visivo ("AI-generated"), metadata nascosti, o caption. Obbligatorio per rischio limitato quando pubblichi contenuti AI verso utenti esterni.

---

## Note Finali

**Data versione:** Ottobre 2024
**Prossimo aggiornamento:** Quando evolvono normative o terminologia

**Termini mancanti?** Se incontri un termine AI Act non presente nel glossario, contatta [email supporto] per richiesta aggiunta.

**Approfondimenti:** Per definizioni legali ufficiali, consulta il [testo integrale EU AI Act su EUR-Lex](https://eur-lex.europa.eu/).

---

**Fine Glossario**
