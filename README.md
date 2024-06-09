# Pulizia e Preparazione dati PNRR 🔍🛠️💾
Repo creata per manutenere il codice di aggiornamento della base dati per la [app di monitoraggio PNRR](https://public.tableau.com/app/profile/period.thinktank/viz/webapp-attempt_newbase/Home) di Period Think Tank

![draft](docs/draft.png)

## Risorse Utili 📝
* [Link](https://docs.google.com/document/d/1HaHIbAhVGqhypHSc_gMIXG6Z4ioIH56mi-BsnI2Ty1w/edit#heading=h.r13rq9c3hkqr) ad analisi funzionale realizzata da @lalafrufru e @alessandrapomella


## Recap delle fonti dati 💾
| ID | Descrizione | Formato | Fonte | Ultima Estrazione | Ultimo Aggiornamento | Freq. Aggiornamento | Commenti |  
|:---------|:------|:--------|:------------------|:---------|:---------|:------|:----|
| P01 | **Associazione CIG-CUP** | `.csv`| [ANAC](https://dati.anticorruzione.it/opendata/dataset/cup) | 22/01/2024 | 03/06/2024 | Mensile | NA |
| P02 | **Anagrafica CUP** | `.csv` | [OpenCup](https://www.opencup.gov.it/portale/documents/21195/299152/)| 08/12/2023 | 02/2024 | NA | NA |
| P03 | **Premialità** | `.csv` to `.xlsx` | [ANAC](https://dati.anticorruzione.it/opendata/dataset/misurepremiali-pnrrpnc) | 08/01/2024 | 03/06/2024 | Mensile | NA |
| P04 | **Quote e Deroghe** | `.csv` to `.xlsx` | [ANAC](https://dati.anticorruzione.it/opendata/dataset/indicatori-pnrrpnc) | 08/01/2024 | 03/06/2024 | Mensile| NA |
| P05 | **Anagrafica CIG** (2023) | `.csv` | [ANAC](https://dati.anticorruzione.it/opendata/dataset/cig-2023) | 08/01/2024 | 18/01/2024 | in attesa di aggiornamento 2024| NA |
| Comuni | **Elenco Comuni Italiani** | `.csv` | Istat | NA | NA | NA |
| Missioni | **Elenco missioni/sottomissioni PNRR** | `.json`| NA | NA | NA |
