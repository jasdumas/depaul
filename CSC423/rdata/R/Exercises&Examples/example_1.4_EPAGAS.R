# Example 1.4
## possibly write my homework in KnitR to include inputs
## and outputs with text to a PDF file!

hist(EPAGAS$MPG)
rm(list=ls())
load("~/Desktop/depaul/CSC423/rdata/R/Exercises&Examples/EPAGAS.Rdata")
View(EPAGAS)
head(EPAGAS)
View(head(EPAGAS, 10))
hist(EPAGAS$MPG)
hist(EPAGAS$MPG, breaks = 15)
hist(EPAGAS$MPG, breaks = 15, xlab="Miles per gallon", main="My Histogram")
#?hist()
hist(EPAGAS$MPG, breaks = 15, xlab="Miles per gallon", main="My Histogram", col = "purple")
savehistory("~/Desktop/depaul/CSC423/rdata/R/Exercises&Examples/example_1.4_epagas.Rhistory")
summary(EPAGAS$MPG)
#install.packages("psych") already installed!
library(psych)
describe(EPAGAS$MPG)
