# TalentBox_Task
For the Task 1 :
I have used Wikipedia as a source.

For Task 2:
(For the second Half):

I chose the Random Forest Classifier algorithm for the following reasons:

Random Forest is an ensemble learning method that combines multiple decision trees to improve the accuracy and robustness of the model.
It can capture complex non-linear relationships in the data, making it suitable for classification tasks with non-linear decision boundaries.
It provides feature importance scores, which can help identify the most influential features in the classification process.
It tends to be less prone to overfitting compared to individual decision trees, thanks to its use of bagging and random feature selection.

Different tuning methods for Random Forest include:
Number of Trees (n_estimators): The number of decision trees in the forest. Increasing the number of trees may improve the model's performance but can also increase computation time.
Maximum Depth of Trees (max_depth): The maximum depth of each decision tree. Deeper trees can capture more complex patterns but may lead to overfitting.
Minimum Samples Split (min_samples_split): The minimum number of samples required to split an internal node. Increasing this parameter can prevent overfitting.
Minimum Samples Leaf (min_samples_leaf): The minimum number of samples required to be at a leaf node. Similar to min_samples_split, increasing this parameter can prevent overfitting by controlling tree growth.
Feature Subset Size (max_features): The number of features to consider when looking for the best split. This parameter can influence the diversity of trees in the forest.

Yes, I considered other algorithms as well, such as Logistic Regression, Support Vector Machines, and Gradient Boosting Machines. However, I chose Random Forest for its simplicity, robustness, and ability to handle non-linear relationships without extensive hyperparameter tuning.

To determine the accuracy of the model, we can use metrics such as accuracy, precision, recall, F1-score, and confusion matrix. These metrics provide different perspectives on the model's performance:

Accuracy: The ratio of correctly predicted observations to the total observations. It provides an overall measure of model performance but may not be suitable for imbalanced datasets.
Precision: The ratio of true positive predictions to the total predicted positives. It measures the accuracy of positive predictions.
Recall (Sensitivity): The ratio of true positive predictions to the total actual positives. It measures the model's ability to correctly identify positive instances.
F1-score: The harmonic mean of precision and recall. It provides a balance between precision and recall.
Confusion Matrix: A table that shows the true positives, true negatives, false positives, and false negatives. It provides a detailed breakdown of model predictions.
By examining these metrics, we can gain insights into the model's performance and its ability to classify planets into different categories accurately.

The problem that I faced in task 2 is that there's an issue with how the data in the CSV file is formatted. Specifically, it seems that there are inconsistencies in the number of fields (columns) in line 53 compared to what the parser expects.
