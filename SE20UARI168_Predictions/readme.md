Here, we have a time series data, with the goal being to predict the number of units sold in a week.

Step 1: (Data pre-processing)
-> We first preprocess the data to remove NA values, and outliers
-> Then we visualize the correlations between the columns, to remove redundant column
-> Then, with a little buisness logic, we realize that record_ID is superficial, and not required, so we proceed to drop that

When we continue to visualize units sold per time, we notice a seasonality present, as there are periodic peaks in the data.
Therefore, we use a SARIMAX model for our case.

We then fit the training data to the model, then using this model make the predictions for the test data.

The results are then output to "Outputs.csv"