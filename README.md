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
Different models where trained both using Hyperdrive and Automated ML and the best model we got using automl.

The best model used VotingEnsemble algorithm which reached to accuracy of 87.632%.
The Hyperdrive accuracy reached to 76.666%
All the columns were used for training.

Serum creatinine and ejection fraction were found to be the most relevant features and are enough to predict if a patient with heart failure will survive or not, with significant accuracy.

#### Screenshots
AutoML RunDetails
![AutoML RunDetails](https://github.com/Sara-cos/Heart_Faliure_PredictionModel/tree/main/starter_file/images/AutoML rundetails.png)

AutoMl best model
![AutoMl best model](https://github.com/Sara-cos/Heart_Faliure_PredictionModel/tree/main/starter_file/images/Best model(2).png)

AutoMl Voting Ensemble model
![AutoMl Voting Ensemble model](https://github.com/Sara-cos/Heart_Faliure_PredictionModel/tree/main/starter_file/images/AutoML model.png)

### Hyperparameter Tuning
logistic regression model with an SKLearn estimator was used in the model.
The Hyperparameters were:
1. C (Inverse of regularization strength), with a uniform range from 0.001 to 1.0. 
2. max_iter (maximun number of iterations to converge), with 3 possible values: 50, 100 and 200.

### Results

The best model reached an accuracy of 76.66% and used the following hyperparameters:
1. Regularization Strength: 0.5377086929082712
2. Max iterations: 100

#### Screenshots
Hyperdrive RunDetails
![Hyperdrive RunDetails](https://github.com/Sara-cos/Heart_Faliure_PredictionModel/tree/main/starter_file/images/Run Details Hyperdrive.png)

Hyperdrive best model
![Hyperdrive best model](https://github.com/Sara-cos/Heart_Faliure_PredictionModel/tree/main/starter_file/images/hyperdrive best model(1).png)

Hyperdrive best model in ML Studio
![Hyperdrive best model in ML Studio](https://github.com/Sara-cos/Heart_Faliure_PredictionModel/tree/main/starter_file/images/Hyperdrive model.png)

## Best Models Comparison
Auto ML - Voting Ensemble        : Accuracy 87.632%
Hyperdrive - Logistic Regression : Accuracy 76.666%

The Auto ML out performs with a almost 12% difference in accuracy than the Hyperdrive.
Voting Ensemble performed better than Logistic Regression model.

## Model Deployment
The AutoML Voting Ensemble model was deployed to an Azure Container Instance using python sdk.

Sample input:

```
{
  "data": [
    {
      "age": 36,
      "anaemia": 0,
      "creatinine_phosphokinase": 200,
      "diabetes": 0,
      "ejection_fraction": 30,
      "high_blood_pressure": 0,
      "platelets": 120000,
      "serum_creatinine": 1.1,
      "serum_sodium": 135,
      "sex": 1,
      "smoking": 0,
      "time": 7
    },
    {
      "age": 39,
      "anaemia": 0,
      "creatinine_phosphokinase": 300,
      "diabetes": 0,
      "ejection_fraction": 50,
      "high_blood_pressure": 0,
      "platelets": 200000,
      "serum_creatinine": 0.9,
      "serum_sodium": 250,
      "sex": 0,
      "smoking": 0,
      "time": 1
    }
  ]
}
```

The input can predict several data instances in parallel.
The content type should be set in the headers:
- Content-Type: 'application/json'

Also, if authentication is enabled, we should include key in the header as follows:
- Authorization: Bearer {key}

Endpoint status
![](https://github.com/Sara-cos/Heart_Faliure_PredictionModel/tree/main/starter_file/images/Endpoint running.png)



## Future Improvements 
1. The serum creatinine and ejection fraction are the most relevant. thus traing using this two attributes will lend better accuracy and better performance.
2. Consume the scoring endpoint from web or other application.
3. Deploy the best model to AKC, to provide greater scalability and performance.
4. Another improvement would be to do a model grid search, comparing Random Forest, Support Vector Machine and Logistic Regression models, for the Hyperdrive experiment.
5. The dataset can be improved for better results.

## Screen Recording
[Capstone Project by Prasansha Satpathy]
https://youtu.be/EQFYUohnBzA
