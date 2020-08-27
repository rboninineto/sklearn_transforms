from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
class CreateColumns(BaseEstimator, TransformerMixin):
    def __init__(self, teste ):        
        self.teste = teste
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        
        data = pd.DataFrame.from_records( X.copy() )            
        
        cursadas = 0
                
        for index, row in X.iterrows():
                        
            cursadas = 0                   
            
            if ((data.iat[index,4]== 0.0) & (data.iat[index,0]> 0)) | (data.iat[index,4]> 0.0):
                cursadas += 1            
        
            if ((data.iat[index,5]== 0.0) & (data.iat[index,1]> 0)) | (data.iat[index,5]> 0.0):
                cursadas += 1
                            
            if ((data.iat[index,6]== 0.0) & (data.iat[index,2]> 0)) | (data.iat[index,6]> 0.0):
                cursadas += 1
                            
            if ((data.iat[index,7]== 0.0) & (data.iat[index,3]> 0)) | (data.iat[index,7]> 0.0):
                cursadas += 1                            
            
            if (cursadas>0):                                                                    
                data.iat[index,8] = ( data.iat[index,4] + data.iat[index,5] + data.iat[index,6] + data.iat[index,7] ) / cursadas
                
        return data    
