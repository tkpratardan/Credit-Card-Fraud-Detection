from cassandra_rw import CassandraReadWriteDb
from TxInfo import TxInfoModel
from ml_model import BuildMlPipeline
from sklearn.model_selection import train_test_split

if '__name__' == '__main__':

    cass_rw = CassandraReadWriteDb(ip_addrs=['172.17.0.2'],keypsace = "emp")
    
    #load data in cassandra
    cass_rw.sync_class_table(TxInfoModel)
    cass_rw.write_file_table('creditcard.csv')
    
    #cassandra to pandas
    credit_data = cass_rw.get_pandas_from_cassandra()
    
    print ('Data Loaded into Dataframe')
    
    #model creation
   
    ml_pipeline = BuildMlPipeline()
    ml_pipeline.set_estimators('svc','randomForestClassifier')
    ml_pipeline.set_scalers('standardscaler')
    ml_pipeline.set_samplers('smote','smoteenn')
    ml.pipleline.create_pipleline()
    
    
    params_dict = {}
    params_dict['smote'] = {'smote_k_neighbours':[5,10,15]}
    params_dict['smoteenn'] = {'smoteenn_sampling_strategy':['auto','all','not majority']}
    params_dict['randomforestclassifier'] = {'randomforestclassifier_n_estimators':[8,12]}
    params_dict['svc'] = {'svc_kernel':['linear','rbf','poly'],'svc_C':[.1,1,10]}
    
    ml_pipeline.set_hyperparameters(params_dict)
   
    X = credit_data.drop['tx_id','Time','C'], axis=1)
    y = credit_data.C
    trainX, testX, trainY, testY = train_test_split(X,y)
    
    print ("Model Training")
    
    #model training
    ml_pipeline.fit(trainX, trainY)
    
    #model performance
    ml_pipeline.score(testX, testY)
