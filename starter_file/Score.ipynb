{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import logging\n",
    "import os\n",
    "import pickle\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import azureml.core.model import Model\n",
    "from inference_schema.schema_decorators import input_schema, output_schema\n",
    "from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType\n",
    "from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "input_sample = pd.DataFrame({\"age\": pd.Series([0.0], dtype=\"float64\"), \"anaemia\": pd.Series([0.0], dtype=\"float64\"), \"creatinine_phosphokinase\": pd.Series([0.0], dtype=\"float64\"), \"diabetes\": pd.Series([0.0], dtype=\"float64\"), \"ejection_fraction\": pd.Series([0.0], dtype=\"float64\"), \"high_blood_pressure\": pd.Series([0.0], dtype=\"float64\"), \"platelets\": pd.Series([0.0], dtype=\"float64\"), \"serum_creatinine\": pd.Series([0.0], dtype=\"float64\"), \"serum_sodium\": pd.Series([0.0], dtype=\"float64\"), \"sex\": pd.Series([0.0], dtype=\"float64\"), \"smoking\": pd.Series([0.0], dtype=\"float64\"), \"time\": pd.Series([0.0], dtype=\"float64\")})\n",
    "output_sample = np.array([0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def init():\n",
    "    global model\n",
    "    # This name is model.id of model that we want to deploy deserialize the model file back into a sklearn model\n",
    "    model_path = Model.get_model_path(\"heart-failure-prediction-automl-model\")\n",
    "    print(model_path)\n",
    "    path = os.path.normpath(model_path)\n",
    "    path_split = path.split(os.sep)\n",
    "    try:\n",
    "        model = joblib.load(model_path)\n",
    "    except Exception as e:\n",
    "        raise\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "@input_schema('data', PandasParameterType(input_sample))\n",
    "@output_schema(NumpyParameterType(output_sample))\n",
    "def run(data):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " try:\n",
    "        result = model.predict(data)\n",
    "        return json.dumps({\"result\": result.tolist()})\n",
    "except Exception as e:\n",
    "        result = str(e)\n",
    "        return json.dumps({\"error\": result})"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
