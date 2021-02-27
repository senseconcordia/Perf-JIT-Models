logistic regression
  ############model
  file <- paste("hadoop_prediction_", i, sep="")
  file <- paste(file, ".csv", sep="")

  form=as.formula(paste("contains_bug>0~",paste(names(after_redun),collapse="+")))
  rf.fit=glm(formula=form, data=log10(trainingset+1), family = binomial(link = "logit"))
  
  rf_predictions <- predict(rf.fit, log10(testset+1),type="response")

  TP_rf = sum((rf_predictions=="TRUE") & (testset$contains_bug>0))
  FP_rf = sum((rf_predictions=="TRUE") & (testset$contains_bug==0))
  
  precision_rf[i] = TP_rf / sum((rf_predictions=="TRUE"))
  recall_rf[i] = TP_rf / sum(testset$contains_bug>0)
  
  x <- data.frame(rf_predictions)
  write.table(x, file, sep = ",", append = TRUE, quote = FALSE, col.names=c("Prediction"), row.names = FALSE)

randomForest

file <- paste("hadoop_prediction_", i, sep="")
  file <- paste(file, ".csv", sep="")

  
  rf.fit= randomForest(x=log10(after_redun+1), y=as.factor(trainingset$contains_bug>0), ntree=100, type='classification', importance=TRUE)
  rf_predictions <- predict(rf.fit, log10(testset+1),type="response")
  
  rf_predictions_bool <- predict(rf.fit, log10(testset+1),type="response")
  rf_predictions <- predict(rf.fit, log10(testset+1),type="prob")
  
  TP_rf = sum((rf_predictions=="TRUE") & (testset$contains_bug>0))
  FP_rf = sum((rf_predictions=="TRUE") & (testset$contains_bug==0))
  
  precision_rf[i] = TP_rf / sum((rf_predictions=="TRUE"))
  recall_rf[i] = TP_rf / sum(testset$contains_bug>0)
  
  x <- data.frame(rf_predictions_bool, rf_predictions)
  #write.csv(rf_predictions, file, row.names = FALSE)
  write.table(x, file, sep = ",", append = TRUE, quote = FALSE, col.names=c("Prediction","False","True"), row.names = FALSE)
  
  decision tree
  ############model
  file <- paste("hadoop_prediction_", i, sep="")
  file <- paste(file, ".csv", sep="")
  
  form=as.formula(paste("contains_bug>0~",paste(names(after_redun),collapse="+")))
  rf.fit=rpart(formula=form, data=log10(trainingset+1),method='class')
  
  rf_predictions <- predict(rf.fit, log10(testset+1),type="class")
  
  TP_rf = sum((rf_predictions=="TRUE") & (testset$contains_bug>0))
  FP_rf = sum((rf_predictions=="TRUE") & (testset$contains_bug==0))
  
  precision_rf[i] = TP_rf / sum((rf_predictions=="TRUE"))
  recall_rf[i] = TP_rf / sum(testset$contains_bug>0)
  
  x <- data.frame(rf_predictions)
  
  write.table(x, file, sep = ",", append = TRUE, quote = FALSE, col.names=c("Prediction"), row.names = FALSE)

  SVM
############model
  file <- paste("hadoop_prediction_", i, sep="")
  file <- paste(file, ".csv", sep="")
  
  form=as.formula(paste("contains_bug>0~",paste(names(after_redun),collapse="+")))
  rf.fit=svm(formula=form, data=log10(trainingset+1),type="C-classification")
  
  rf_predictions <- predict(rf.fit, log10(testset+1),type="class")
  
  TP_rf = sum((rf_predictions=="TRUE") & (testset$contains_bug>0))
  FP_rf = sum((rf_predictions=="TRUE") & (testset$contains_bug==0))
  
  precision_rf[i] = TP_rf / sum((rf_predictions=="TRUE"))
  recall_rf[i] = TP_rf / sum(testset$contains_bug>0)
  
  x <- data.frame(rf_predictions)
  
  write.table(x, file, sep = ",", append = TRUE, quote = FALSE, col.names=c("Prediction"), row.names = FALSE)

############model

  file <- paste("cassandra_prediction_", i, sep="")
  file <- paste(file, ".csv", sep="")
  form=as.formula(paste("contains_bug>0~",paste(names(after_redun),collapse="+")))
  model=glm(formula=form, data=log10(trainingset+1), family = binomial(link = "logit"))
  predictions <- predict(model, log10(testset+1) ,type="response")
  x <- data.frame(predictions)
  write.table(x, file, sep = ",", append = TRUE, quote = FALSE, col.names=c("Prediction"), row.names = FALSE)