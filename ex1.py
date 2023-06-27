
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
encoder = OneHotEncoder()
data_encoded = pd.DataFrame(encoder.fit_transform(data[['whoAmI']]).toarray(), columns=encoder.get_feature_names(['whoAmI']))
data = pd.concat([data, data_encoded], axis=1)
data = data.drop('whoAmI', axis=1)
import random
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
encoder = OneHotEncoder()
data_encoded = pd.DataFrame(encoder.fit_transform(data[['whoAmI']]).toarray(), columns=encoder.get_feature_names(['whoAmI']))
data = pd.concat([data, data_encoded], axis=1)
data = data.drop('whoAmI', axis=1)
print(data)