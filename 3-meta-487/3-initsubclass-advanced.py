# Customizing Methods for Prediction

class Model:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # create a custom predict method for each subclass
        def predict(self, data):
            if isinstance(data, pd.DataFrame):
                return self._predict_df(data)
            if isinstance(data, pyspark.sql.DataFrame):
                return self._predict_spark(data)

        cls.predict = predict

        required_methods = ['_predict_df', 'predict_spark']
        for method in required_methods:
            if not hasattr(cls, method):
                raise NotImplementedError(f'{method} must be implemented')

class CustomModel(Model):
    def predict(self, data):
        # implements prediciton logic
        pass

    def predict_pd(self, data):
        # sklearn.predict
        pass

    def predict_spark(self, data):
        # pyspark.ml 
        pass
