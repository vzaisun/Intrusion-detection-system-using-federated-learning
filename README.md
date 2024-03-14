# Intrusion-detection-system-using-federated-learning
->Used Tensorflow federated package for federating learning approach.
->The two datsets used are IEC Dataset and NSL-KDD dataset
->Train.csv and test.csv are obtained after performing certain operation on the IEC Dataset which can be referred in phase2_initail.py file.
->Similarly there is KDDTrain and KDDTest files
->Federated learning code and approach would be similar for both the datasets where only the clients or number of workers vary.
->We have chosen batch size such that number of training points(batch size * number of batches) are more than the size of dataset so each point in the dataset is processed more than once.
->For IEC Dataset we have chose 2 workers for 2 labels. Whereas for NSL-KDD dataset we have chosen 5 workers for 5 labels.
->Used DNN,LSTM,BILSTM in the model functions.
->Tried with SGD and ADAM optimizer
