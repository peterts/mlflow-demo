# mlflow-demo

Demo av hvordan MLFlow kan brukes for modellsporing. Presentasjonen finner du
i *notebooks/Presentation.ipynb*.

## Oppsett

Følgende må være installert på maskinen din:
- python>=3.8
- poetry
- jupyter
- (valgfritt) Make

Når dette er installert::
1. Kjør `poetry install` for å skape det virtuelle miljøet.
2. Gjør miljøet tilgjengelig som en kjerne:
    - Dersom du har Make installert: kjør `make install-kernel`
    - *Alternativ*: kopier og kjør kommandoen i *Makefile*
    - *Alternativ*: installer jupyter i poetry miljøet vha `poetry add jupyter`, og kjør jupyter fra miljøet vha `poetry run jupyter notebook`
    
    
## For å starte MLFlow guiet

Naviger til *notebooks* og kjør `poetry run mlflow ui`. Om siden ikke åpner seg automatisk
kan du gå til http://localhost:5000 for å finne guiet.