load("~/Desktop/depaul/CSC423/BQAPPLE.Rdata")
head(BQAPPLE)

plot( BQAPPLE$INCOME, BQAPPLE$APPLE)

BQAPPLE = BQAPPLE[order(BQAPPLE$INCOME),]
options(scipen=3)
plot(APPLE ~ INCOME, data=BQAPPLE, lwd=2)
