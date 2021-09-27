def pickle_boy(path):
  import pickle
  
  with open(path, 'rb') as f:
    pickler =pickle.load(f)
  return pickler



def data_prep_and_pred(df, fit):
  df = df[['Total_Sqft', 'OverallQual', 'Neighborhood', 'BsmtQual','MSSubClass']]

  df['Total_Sqft'] = df['Total_Sqft'].fillna(df['Total_Sqft'].median())
  df['BsmtQual'] = df['BsmtQual'].fillna(df['BsmtQual'].mode()[0])

  df['MSSubClass'] = df['MSSubClass'].astype(str)

  return fit.predict(df)

