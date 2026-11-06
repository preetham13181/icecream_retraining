# 🍦 Ice Cream Sales Predictor

A small web app that predicts how many ice creams a shop will sell in a day, based on the weather and the day of the week.

**Live app:** https://icecreamretraining-6dd7nhkdewgivcwgspacbw.streamlit.app

**GitHub repo:** https://github.com/preetham13181/icecream_retraining

## What it does

Move the controls and the app shows a predicted number of ice creams sold.

## Original model vs. updated model

This project is a retraining exercise: start with a model, add predictors, retrain, save, and redeploy.

| Version | Predictors | Status |
|---|---|---|
| **Original** | Temperature (°C) | Starting point |
| **Updated (this app)** | Temperature (°C) + **Weekend** + **Rainfall (mm)** | Retrained, saved, deployed |

### Predictors in the updated model

| Predictor | Original or new? | What it means | Why it affects sales | Effect on sales |
|---|---|---|---|---|
| Temperature (°C) | **Original** | Daily temperature (5 to 38) | Hot days make people want ice cream | About +6.6 per °C |
| Weekend | 🆕 **New** | Weekday or weekend | More people are out and free on weekends | About +44 |
| Rainfall (mm) | 🆕 **New** | Rain during the day (0 to 25) | Rain keeps people at home | About -2.3 per mm |

## How it works

1. `ice_cream_notebook.ipynb` simulates 400 days of sales data, trains a linear regression model, and saves it as `ice_cream_model.joblib`.
2. `app.py` loads the saved model and uses it to make predictions from the inputs.
3. If the saved model can't be loaded (for example, a scikit-learn version mismatch), the app retrains one automatically.

The data is simulated, so the numbers are for demonstration, not real shop sales.

## Files

| File | Purpose |
|---|---|
| `app.py` | The Streamlit web app |
| `train_model.py` | Builds the data, trains the model, saves it |
| `ice_cream_notebook.ipynb` | Notebook that walks through the data, training, and saving |
| `ice_cream_model.joblib` | The saved trained model |
| `ice_cream_data.csv` | The simulated training data |
| `requirements.txt` | Python packages needed |

## Run it locally

You need Python 3.10 or newer.

```bash
# 1. (Optional) create an environment
conda create -n icecream_prediction python=3.11 -y
conda activate icecream_prediction

# Get the code
git clone https://github.com/preetham13181/icecream_retraining.git
cd icecream_retraining

# 2. Install the packages
pip install -r requirements.txt

# 3. (Optional) retrain and re-save the model
python train_model.py

# 4. Start the app
streamlit run app.py
```

The app opens at http://localhost:8501.

## Try these examples

| Temperature | Day type | Rainfall | Expected prediction |
|---|---|---|---|
| 30 | Weekend | 0 | about 260 |
| 30 | Weekday | 0 | about 216 |
| 30 | Weekday | 15 | about 181 |

## Model results

- Model: linear regression
- Test R²: 0.97
- Average error: about 11 ice creams

## Deployed on

[Streamlit Community Cloud](https://streamlit.io/cloud), straight from this GitHub repository.



## Running Local

* Create the conda environment using the following command
* `mamba env create -f environment.yaml`
* then run the code using python 
