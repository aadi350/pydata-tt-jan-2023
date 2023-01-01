# Customizing Methods for Prediction

import pandas as pd

class Model:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        
        # Create a custom "predict" method for each subclass based on the input data type
        def predict(self, data):
            if isinstance(data, pd.DataFrame):
                return self._predict_df(data)
            elif isinstance(data, pd.Series):
                return self._predict_series(data)
            else:
                raise TypeError("Unsupported data type for prediction.")
        cls.predict = predict
        
        # Ensure that the subclass implements the required methods
        required_methods = ["_predict_df", "_predict_series"]
        for method in required_methods:
            if not hasattr(cls, method):
                raise NotImplementedError(f"Subclass of Model must implement the '{method}' method.")

class CustomModel(Model):
    def _predict_df(self, data):
        # Implement prediction logic for DataFrames here
        pass
    
    def _predict_series(self, data):
        # Implement prediction logic for Series here
        pass

# create an instance of the CustomModel
model = CustomModel()

# predict using DataFrame
model.predict(pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]}))

# Predict using a Series
model.predict(pd.Series([1, 2, 3]))

