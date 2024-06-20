# Pulizia e Preparazione dati PNRR 🔍🛠️💾
Repo creata per manutenere il codice di aggiornamento della base dati per la [app di monitoraggio PNRR](https://public.tableau.com/app/profile/period.thinktank/viz/webapp-attempt_newbase/Home) di Period Think Tank

![draft](docs/draft.png)
*Draft Pipeline di Estrazione del Dato finale DA AGGIORNARE*

## Risorse Utili 📝
* [Link](https://docs.google.com/document/d/1HaHIbAhVGqhypHSc_gMIXG6Z4ioIH56mi-BsnI2Ty1w/edit#heading=h.r13rq9c3hkqr) ad analisi funzionale realizzata da @lalafrufru e @alessandrapomella  
* [Notebooks](notebooks/data_prep_old) di collezionamento e preparazione del dataset finale prodotti da @alessandrapomella per la [precedente iterazione](https://github.com/PeriodThinkTank/analisi-dati-pnrr) della web app. 


## Recap delle fonti dati 💾
| ID | Descrizione | Formato | Fonte | Ultima Estrazione | Ultimo Aggiornamento | Freq. Aggiornamento | Commenti |  
|:---------|:------|:--------|:------------------|:---------|:---------|:------|:----|
| P01 | **Associazione CIG-CUP** | `.csv`| [ANAC](https://dati.anticorruzione.it/opendata/dataset/cup) | 22/01/2024 | 03/06/2024 | Mensile | NA |
| P02 | **Anagrafica CUP** | `.csv` | [OpenCup](https://www.opencup.gov.it/portale/documents/21195/299152/)| 08/12/2023 | 02/2024 | NA | NA |
| P03 | **Premialità** | `.csv` to `.xlsx` | [ANAC](https://dati.anticorruzione.it/opendata/dataset/misurepremiali-pnrrpnc) | 08/01/2024 | 03/06/2024 | Mensile | NA |
| P04 | **Quote e Deroghe** | `.csv` to `.xlsx` | [ANAC](https://dati.anticorruzione.it/opendata/dataset/indicatori-pnrrpnc) | 08/01/2024 | 03/06/2024 | Mensile| NA |
| P05 | **Anagrafica CIG** (2023) | `.csv` | [ANAC](https://dati.anticorruzione.it/opendata/dataset/cig-2023) | 08/01/2024 | 18/01/2024 | in attesa di aggiornamento 2024| NA |
| Comuni | **Elenco Comuni Italiani** | `.csv` | Istat | NA | NA | NA | NA |
| Missioni | **Elenco missioni/sottomissioni PNRR** | `.json`| NA | NA | NA | NA | NA |
| Indicatori PNRR | **Mappatura indicatori comuni del PNRR** | `.csv` | [ItaliaDomani](https://www.italiadomani.gov.it/content/sogei-ng/it/it/catalogo-open-data/mappatura-indicatori-comuni.html) | NA | 18/04/24 (v6) | NA | Dataset citato nell'articolo di [inGenere](https://www.ingenere.it/) |
| Target PNRR | **Indicatori Target del PNRR** | `.csv` | [ItaliaDomani](https://www.italiadomani.gov.it/content/sogei-ng/it/it/catalogo-open-data/indicatori-target-del-pnrr--dati-validati-.html) | NA | 15/03/2024 | NA | NA |
| Indicatori PNRR & SDGS | **Monitoraggio delle misure del PNRR attraverso gli indicatori di sviluppo sostenibile (SDGs) e dell'Agenda 2030** | `.csv` | [ItaliaDomani](https://www.italiadomani.gov.it/content/sogei-ng/it/it/catalogo-open-data/monitoraggio-delle-misure-del-pnrr-attraverso-gli-indicatori-di-.html) | NA | 19/06/2024 (v5) | NA | Dataset di interesse per alcune misure presenti che potrebbero impattare direttamente sul genere e inclusività |


## Note Metodologiche 📕
* I dataset Comuni e Missioni vengono presi come dati e non aggiornati. 
* Per il resto delle fonti dati, al fine di popolare la dashboard di frontend con informazioni rilevanti e aggiornate, Period Think Tank effettuerà l'aggiornamento con frequenza adeguata.

## Punti Aperti 👀

#### Ricostruzione P05
Descrizione del processo di creazione di P05 per come ci è stata spiegata da [Andrea Borruso](https://www.linkedin.com/in/andreaborruso/?locale=it_IT):

    - Scarica tutti i csv zippati con i delta aggiornamenti di CIG bandi gara (ANAC, 23, dicembre compreso)
    - Decomprime e converte in gzip così sono accessibili in stream
    - Tra tutti i file scaricati, filtra soltanto quelli con flag PNRR uguale a 1
    - Per CIG duplicati, preso il più recente
    - Merge di tutti i file in uno solo

Nostro processo di ricostruzione del dato:  
* Scarica tutti i csv zippati con i CIG bandi gara mensili (ANAC, 2023, dicembre compreso)  
* Unzip i csv, trasforma in pandas dataframe e concatena i dataset mensili in un unico dataset annuale  