from sklearn.base import BaseEstimator, TransformerMixin


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
        
        data = X.copy()            
        
        cursadas = 0
                
        for line in data.itertuples():
                        
            cursadas = 0            
            
            if ((data.iat[line[0],4]== 0.0) & (data.iat[line[0],0]> 0)) | (data.iat[line[0],4]> 0.0):                                
                cursadas += 1            
        
            if ((data.iat[line[0],5]== 0.0) & (data.iat[line[0],1]> 0 )) | (data.iat[line[0],5]> 0.0):
                cursadas += 1
                
            if ((data.iat[line[0],6]== 0.0) & (data.iat[line[0],2]> 0 )) | (data.iat[line[0],6]> 0.0):
                cursadas += 1
                
            if ((data.iat[line[0],7]== 0.0) & (data.iat[line[0],3]> 0 )) | (data.iat[line[0],7]> 0.0):
                cursadas += 1                            
            
            if (cursadas>0):                                                    
                data.iat[line[0],8] = ( data.iat[line[0],4] + data.iat[line[0],5] + data.iat[line[0],6] + data.iat[line[0],7] ) / cursadas                 
                
        return data    
