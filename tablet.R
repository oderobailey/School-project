myData<- read.table("C:/Users/odero/Downloads/tablet-computers-2014.txt", header=TRUE, sep="\t")
summary(myData)
summary(myData$Battery.life..hrs) 
myData$away<-myData$Battery.life..hrs.-8.946
write.csv(myData,'C:/Users/odero/Documents/R/tabletwritten.csv')