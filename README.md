OBJECTIVE:
Credit-Card-Fraud Detection pipeline is an en-to-end Machine Learning project that helps in prediction of fradulent transactions for a bank.

DEISGN:

![image](https://user-images.githubusercontent.com/40231735/222939903-d4ebcb75-b792-4b22-848b-1df1d1a0e025.png)

The pipeline utilises a cassandra database for stored credit-card-fraud analysis a source for testing and training data for model. The trained models(for Kafka and REST) were deployed to make predictions from live transaction data.

Tools;
Database: Cassandra
ML: 
   Estimators: SGDClassifier, RandomForestClassifier, SVM Classifier and choosing the best estimator
   Sampling : standardscaler; Imbalanced-learn(smote, smoteenn) since the data is highly imbalanced
   Model for Kafka client and model for REST(Flask) interface


KAFKA MODEL:
   1. Simulate Kafka producer to produce kafka tx records (serialising json contents of a new transaction)
   2. Kafka consumer is subscribed to topic ('credit-card-tx')
   3. As and when kafka consumer gets a message, the transaction data is used ot predict if it is a fraud 

REST (flask) MODEL:
   1. 
   

Code flow:

![image](https://user-images.githubusercontent.com/40231735/222940725-63bd24c4-7346-4987-870d-9a8c5e09d1f5.png)


   
