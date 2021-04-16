# Heart_Faliure_PredictionModel
The cardiovascular diseases are the section of diseases which are major cause of death anually. About 17.9 million people die from CVD amounting 31% annual death trolls. It is estimated that up to 90% of CVD may be preventable. 
The objective of this ML model is predicting the possiblity of demise accordance with the data available of possible patient. Understanding the pattern of possiblity of demise is important.

## Dataset

### Overview
The Heart Failure Prediction dataset was downloaded from Kaggle. However, the dataset was originally collected from the Faisalabad Institute of Cardiology and at the Allied Hospital in Faisalabad (Punjab, Pakistan), during April–December 2015.

The CVD in population is caused due to various factors. In CVD, heart failure is a common event and this dataset contains 12 features that can be used to predict mortality by heart failure.

### Task
People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management where in a machine learning model can be of great help.

The dataset contains data based on these attributes:-
1. age
2. anaemia [whether the person had anaemia or not]
3. creatinine phosphorus [Level of CPK enszyme in the blood]
4. diabetes [whether thr person has diabetes or not]
5. ejection fraction [Percentage of blood leaving the heart at each contraction]
6. high blood preassure [whether had HBP]
7. platelets [kiloplatelets/ml]
8. serum creatinine [mg/dL]
9. serum sodium [mEq/L]
10. sex
11. smoking [weather the person smokes or not]
12. time [days]
13. death event [if the person surcumbed due to heart failure]

### Access

The dataset CSV file is hosted in the Github repository. Thus, the dataset is accessed raw, whose URL is "https://raw.githubusercontent.com/Sara-cos/Heart_Faliure_PredictionModel/main/starter_file/heart_failure_clinical_records_dataset.csv". 
Then in the Azure Dataset library to download and convert the csv file to a dataset that can be used by the notebook.

## Automated ML

Settings and configurations
1. experiment_timeout_minutes: 20
2. concurrent iterations at max: 4
3. Primary metric: Accuracy
4. Targetcolumn : Death_Event
5. The algorithm used : classification
6. Early stopping : Enabled
7. VM_size : Standard_D2_V2, 4 nodes

### Results










