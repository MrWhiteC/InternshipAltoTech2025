# Welcome to Internship Test for Plant Energy Testing Prediction

## What happend in repo ? 

This is the fulfillment of the test assignment from AltoTech company. The goal is to model the pre-AI plant enerygy which will be used to predicted the future value and compared with post-AI plant energy in order to roughly calculate a saving value. In this repo, the model workspace and website code will be provided as submission criteria.

1.  Model Jupyter Notebook
    1. Datasets : after_ai_plant_data.csv and before_ai_plant_data.csv
    2. Model : model_workspace.ipynb
2. Dashboard Websites
    1. Dash Application : app.py 
    2. Dataset : predicted_after_ai.csv
    3. Docker Components : .Dockerfile, requirements.txt, and docker-compose.yml

## Model Jupyter Notebook

In order to create a desired model, the following step have been done to find the feature and best model:

- EDA : Observing a dataset in order to detect some pattern within the correlation between features and target.
- 
Temeperature and Plant Energy <br>
<img width="563" alt="Screenshot 2568-04-16 at 16 12 05" src="https://github.com/user-attachments/assets/bfe1d1dd-335b-4b3a-81ce-b1393bfdc9b0" /><br>

Humidity and Plant Energy<br>
<img width="566" alt="Screenshot 2568-04-16 at 16 12 15" src="https://github.com/user-attachments/assets/3b305c52-b72a-4852-abdf-cba074b903db" /><br>

Date and Plant Energy<br>
<img width="625" alt="Screenshot 2568-04-16 at 16 12 26" src="https://github.com/user-attachments/assets/f46b85db-05d8-4ef1-9808-134981ac7d90" /><br>

- Model Cross Validation and GridSearch: Pefroming a cross validation to get the best model and GridSearch for best hyperparmeter

Cross-Validation <br>
<img width="924" alt="Screenshot 2568-04-16 at 16 15 41" src="https://github.com/user-attachments/assets/28a13917-f01c-4683-8456-a800bd5d10c2" /><br>

GridSearch <br>
<img width="543" alt="Screenshot 2568-04-16 at 16 15 50" src="https://github.com/user-attachments/assets/f7c1d69e-b920-49e0-86fd-b9b60201a1e6" /><br>

- Metrices : Evaluation the metrices to understanding the performance of the model

Metrices | Value 
--- | --- |
R2 | 0.78 |
NMBE | 0.126 |
CVMSE | 0.00071 |

- Inference and Export Data : The model will be used to predict the post-AI output and compare with actual data which will be embedded in the data to export for visualization. 

## Dash Websites

In order to run the web application to visualize the final data for ploting the different between acutal and predicted plant energy, please follow the command to run locally. 

```bash
pip3 install -r requirement.txt
python3 app.py
```


```bash
docker compose up 
```

