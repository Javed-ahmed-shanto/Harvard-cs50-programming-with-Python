
username = input("Enter username:")
print("Username is: " + username)


#formating the number and print function
price = 49
txt = "the price is {:.2f} dollars"
print(txt.format(price))

# or
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

#or I think this is the best and needed most
print("The no of Categorical Variables is: {0} in this dataset and they are: {1}" .format(len(object_cols), object_cols))


#to get the index name or coumns name who have object or text type of data
s = (X_train.dtypes == 'object')
object_cols = list(s[s].index)

print("catrgorical Variables: ")
print(object_cols)

#or better version
object_cols = [col for col in X_train.columns if X_train[col].dtype == "object"]

# Columns that can be safely ordinal encoded
good_label_cols = [col for col in object_cols if 
                   set(X_valid[col]).issubset(set(X_train[col]))]
        
# Problematic columns that will be dropped from the dataset
bad_label_cols = list(set(object_cols)-set(good_label_cols))

print('Categorical columns that will be ordinal encoded:', good_label_cols)
print('\nCategorical columns that will be dropped from the dataset:', bad_label_cols)
        



# to print unique values in a certain columns
print("Unique values in 'Condition2' column in training data:", X_train['Condition2'].unique())
print("\nUnique values in 'Condition2' column in validation data:", X_valid['Condition2'].unique())


# Get number of unique entries in each column with categorical data
object_nunique = list(map(lambda col: X_train[col].nunique(), object_cols))
d = dict(zip(object_cols, object_nunique))

# Print number of unique entries by column, in ascending order
sorted(d.items(), key=lambda x: x[1])
#result [('Street', 2), ('Utilities', 2('CentralAir', 2('LandSlope', 3('PavedDrive', 3),('LotShape', 4),('LandContour', 4), '('Neighborhood', 25)]
#For instance, the 'Street' column in the training data has two unique values: 'Grvl' and 'Pave', corresponding to a gravel road and a paved road, respectively.


#for one hot encoding
# Columns that will be one-hot encoded
low_cardinality_cols = [col for col in object_cols if X_train[col].nunique() < 10]

# Columns that will be dropped from the dataset
high_cardinality_cols = list(set(object_cols)-set(low_cardinality_cols))

print('Categorical columns that will be one-hot encoded:', low_cardinality_cols)
print('\nCategorical columns that will be dropped from the dataset:', high_cardinality_cols)


#using onehot encoder in low_cardinality_cols
from sklearn.preprocessing import OneHotEncoder

# Use as many lines of code as you need!
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)

OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[low_cardinality_cols]))
OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[low_cardinality_cols]))

# One-hot encoding removed index; put it back
OH_cols_train.index = X_train.index
OH_cols_valid.index = X_valid.index

# Remove categorical columns (will replace with one-hot encoding)
num_X_train = X_train.drop(object_cols, axis=1)
num_X_valid = X_valid.drop(object_cols, axis=1)

OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)


# using numpy linespace the_time = np.linespace(-1,1,201)
import numpy as np

the_time = np.linespace(-1,1,np.int((2/.01)+1))
print(the_time)


#all
import pandas as pd

# Read the data
data = pd.read_csv('../input/melbourne-housing-snapshot/melb_data.csv')

# Select subset of predictors
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
X = data[cols_to_use]

# Select target
y = data.Price

from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(steps=[('preprocessor', SimpleImputer()),
                              ('model', RandomForestRegressor(n_estimators=50,
                                                              random_state=0))
                             ])

from sklearn.model_selection import cross_val_score

# Multiply by -1 since sklearn calculates *negative* MAE
scores = -1 * cross_val_score(my_pipeline, X, y,
                              cv=5,
                              scoring='neg_mean_absolute_error')

print("MAE scores:\n", scores)                  

print("Average MAE score (across experiments):")
print(scores.mean())

# baki ase, best estimator, good cardinality bad cardinality, numerical alda clasifier alda
#50,100 estimation er reslut er mean or early stopping rounds
results = {}
for i in range(1,9):
    results[50*i] = get_score(50*i)
# Your code here


#ploting idea
import matplotlib.pyplot as plt
%matplotlib inline

plt.plot(list(results.keys()), list(results.values()))
plt.show()

#best result

n_estimators_best = min(results, key=results.get)

#checking out the weight and bias
w, b = model.weights
print("Weights\n{}\n\nBias\n{}".format(w, b))
plt.title("Weight: {:0.2f}\nBias: {:0.2f}".format(w[0][0], b[0]))

#A neural network learns by finding better values for its weights.
#we need activation function to activate more than one layers in deep learning networks for it to be non linear
# The most common is the rectifier function  max(0,x) .

# activation = relu, elu, selu, swish
#A "loss function" that measures how good the network's predictions are.
#An "optimizer" that can tell the network how to change its weights./The optimizer is an algorithm that adjusts the weights to minimize the loss.

#for regression problem the loss fucntions are: MAE, MSE, Hubber loss
stochastic gradient descent 
adam  a sekf tunig optimizer
#neural networks tend to perform best when their inputs are on a common scale.

layers.Dense(512, activation='relu'), # here, 512 is the nerons number
#Each iteration's sample of training data is called a minibatch (or often just "batch"), while a complete round of the training data is called an epoch. 

history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=256,
    epochs=10,
)

#Now we're ready to start the training! We've told Keras to feed the optimizer 256 rows of the training data at a time (the batch_size) 
# #and to do that 10 times all the way through the dataset (the epochs).


run after epoch ans

import pandas as pd

history_df = pd.DataFrame(history.history)
# Start the plot at epoch 5. You can change this to get a different view.
history_df.loc[5:, ['loss']].plot();

#Underfitting the training set is when the loss is not as low as it could be because the model hasn't learned enough signal. 
#Overfitting the training set is when the loss is not as low as it could be because the model learned too much noise.


#early stopping code from kaggle
from tensorflow import keras
from tensorflow.keras import layers, callbacks

early_stopping = callbacks.EarlyStopping(
    min_delta=0.001, # minimium amount of change to count as an improvement
    patience=20, # how many epochs to wait before stopping
    restore_best_weights=True,
)

model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=[11]),
    layers.Dense(512, activation='relu'),
    layers.Dense(512, activation='relu'),
    layers.Dense(1),
])
model.compile(
    optimizer='adam',
    loss='mae',
)

history = model.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    batch_size=256,
    epochs=500,
    callbacks=[early_stopping], # put your callbacks in a list
    verbose=0,  # turn off training log
)

history_df = pd.DataFrame(history.history)
history_df.loc[:, ['loss', 'val_loss']].plot();
print("Minimum validation loss: {}".format(history_df['val_loss'].min()))


#batch normalization and dropout
#When adding dropout, you may need to increase the number of units in your Dense layers.

from tensorflow import keras
from tensorflow.keras import layers

model = keras.Sequential([
    layers.Dense(1024, activation='relu', input_shape=[11]),
    layers.Dropout(0.3),
    layers.BatchNormalization(),
    layers.Dense(1024, activation='relu'),
    layers.Dropout(0.3),
    layers.BatchNormalization(),
    layers.Dense(1024, activation='relu'),
    layers.Dropout(0.3),
    layers.BatchNormalization(),
    layers.Dense(1),
])

#

early_stopping = callbacks.EarlyStopping(
    patience=2,
    min_delta=0.001,
    restore_best_weights=True,
)

lr_schedule = callbacks.ReduceLROnPlateau(
    patience=0,
    factor=0.2,
    min_lr=0.001,
)

#to see the exisiting libraries
!pip list -v

#splitting
N, M = map(int, input().split())
print(N, M)

# note from cs50 
x = float(input("what's x? "))
y = float(input("what's y? "))

z = round(x / y, 2)

print(z)

ans: what's x? 2
what's y? 3
0.67

or z = x /y

print(f"{z:.2f}")