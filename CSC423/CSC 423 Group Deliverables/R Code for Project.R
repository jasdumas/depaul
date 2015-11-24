brain <- read.table("braindata.txt", header = TRUE, sep = "", na.strings="¥")
Book2 <- na.omit(brain) # remove 2 rows of missing data
# load database without empty information

# create binary variable for Gender
Book2$GenderMale = ifelse(Book2$Gender == "Male", 1, 0)

# assign variable names
y = Book2$MRI_Count
x1 = Book2$GenderMale
x2 = Book2$FSIQ
x3 = Book2$VIQ
x4 = Book2$PIQ
x5 = Book2$Weight
x6 = Book2$Height

# Run linear model - full model
basemodel = lm(y ~ x1 + x2 + x3 + x4 + x5 + x6 )
summary(basemodel)
# Run linear model - remove x2 correlation
basemodel2 = lm(y ~ x1 + x3 + x4 + x5 + x6 )
summary(basemodel2)
# Run linear model - remove x3 due to insignificance
basemodel3 = lm(y ~ x1 + x4 + x5 + x6 )
summary(basemodel3)
# Run linear model - remove x5 due to insignificance - final model
basemodel4 = lm(y ~ x1 + x4 + x6 )
summary(basemodel4)

# Create interaction variables
x1x2 = x1 * x2
x1x3 = x1 * x3
x1x4 = x1 * x4
x1x5 = x1 * x5
x1x6 = x1 * x6
x2x3 = x2 * x3
x2x4 = x2 * x4
x2x5 = x2 * x5
x2x6 = x2 * x6
x3x4 = x3 * x4
x3x5 = x3 * x5
x3x6 = x3 * x6
x4x5 = x4 * x5
x4x6 = x4 * x6
x5x6 = x5 * x6

# Run interaction linear model - full model
interactionmodel = lm(y ~ x1 + x2 + x3 + x4 + x5 + x6 + x1x2 + x1x3 + x1x4 + x1x5 + x1x6 +
                 x2x3 + x2x4 + x2x5 + x2x6 + x3x4 + x3x5 + x3x6 + x4x5 + x4x6 + x5x6)
summary(interactionmodel)

# Run interaction linear model - based on final model
interactionmodel2 = lm(y ~ x1 + x4  + x6  + x1x4  + x1x6 + x4x6 )
summary(interactionmodel2)


# Create quadratic variables
x1sq = x1 ^ 2
x2sq = x2 ^ 2
x3sq = x3 ^ 2
x4sq = x4 ^ 2
x5sq = x5 ^ 2
x6sq = x6 ^ 2

# Run quadratic model - full model
quadraticmodel = lm(y ~ x1 + x2 + x3 + x4 + x5 + x6 + x2sq + x3sq + x4sq + x5sq + x6sq )
summary(quadraticmodel)
# Run quadratic model - based on final model
quadraticmodel2 = lm(y ~ x1 + x4 + x6 + x4sq + x6sq )
summary(quadraticmodel2)


# Check residuals - Detecting lack of fit
Book2$pred = predict(basemodel4)
Book2$resid = residuals(basemodel4)
plot(x1, Book2$resid, lwd=2) # binary output as expected
plot(x4, Book2$resid, lwd=2) # no obvious inappropriate trend found
plot(x6, Book2$resid, lwd=2) # no obvious inappropriate trend found

# Check residuals - Detecting lack of fit
Book2$pred = predict(basemodel4)
Book2$resid = residuals(basemodel4)
plot(x1, Book2$resid, lwd=2) # binary output as expected
plot(x4, Book2$resid, lwd=2) # Some sign of heteroscedasticity
plot(x6, Book2$resid, lwd=2) # no obvious inappropriate trend found

# Run quadratic model - attempt to solve x4 heteroscedasticity
quadraticmodel3 = lm(y ~ x1 + x4 + x6 + x4sq )
summary(quadraticmodel3)

# transfrom y value to address x4 heteroscedasticity 
logy = log(y)
finalmodel1 = lm(logy ~ x1 + x4 + x6 )
summary(finalmodel1)

# transfrom y value to address x4 heteroscedasticity - best regression fit higher r-adjusted score
invy = 1 / y
finalmodel2 = lm(invy ~ x1 + x4 + x6 )
summary(finalmodel2)


# Checking the Normality Assumption - Not worrisom result
stdres = rstandard(finalmodel2)
hist(stdres)

# Check Outliers - 1 outliers (#6) identified (over 2 standardized residual) but not extreme enough to be removed
library(car)
outlierTest(finalmodel2) # Bonferonni p-value for most extreme obs
qqPlot(finalmodel2, main="QQ Plot") #qq plot for studentized resid 


# Check influence points - 3 points (6,8,13) identified  but extreme enough to be removed
# maybe point 6 should be removed because it is outlier and influence point
influence.measures(finalmodel2) 
summary(influence.measures(finalmodel2))
plot(rstudent(finalmodel2)~hatvalues(finalmodel2)) 

# identify D values > 4/(n-k-1) - identifies 6,13,21
cutoff <- 4/((nrow(mtcars)-length(finalmodel2$coefficients)-2)) 
plot(finalmodel2, which=4, cook.levels=cutoff)


# Autocorrelation - nothing to worry (DW = 1.776892)
library(car)
durbinWatsonTest(finalmodel2)


Book3 <- brain2[-6, ] # removed 6th outlier entry
# Run the final model
Book3$GenderMale = ifelse(Book3$Gender == "Male", 1, 0)
y = Book3$MRI_Count
x1 = Book3$GenderMale
x2 = Book3$FSIQ
x3 = Book3$VIQ
x4 = Book3$PIQ
x5 = Book3$Weight
x6 = Book3$Height

invy = 1 / y
finalmodel3 = lm(invy ~ x1 + x4 + x6 )
summary(finalmodel3)

# Checking the Normality Assumption - Not worrisom result
stdres = rstandard(finalmodel3)
hist(stdres)

# Check Outliers - 1 outliers (#5) identified (over 2 standardized residual) but not extreme enough to be removed
outlierTest(finalmodel3) # Bonferonni p-value for most extreme obs
qqPlot(finalmodel3, main="QQ Plot") #qq plot for studentized resid 


# Check influence points - 3 points (5,7,12) identified  but extreme enough to be removed
# maybe point 5 should be removed because it is outlier and influence point
influence.measures(finalmodel3) 
summary(influence.measures(finalmodel3))
plot(rstudent(finalmodel3)~hatvalues(finalmodel3)) 

# Autocorrelation - nothing to worry (DW = 1.810394)
durbinWatsonTest(finalmodel3)


#################### Newest R Code with Split Data ##################################

brain <- read.table("braindata.txt", header = TRUE, sep = "", na.strings="¥")
brain2 <- na.omit(brain) # remove 2 rows of missing data -- equivalent to Book2
brain2[6,]
brain3 <- brain2[-6, ] # removed 6th outlier entry -- equivalent to Book3

brain4 <- split(brain3, brain3$FSIQ <= 108)
brain4 <- brain4$`TRUE`
brain5 <- split(brain3, brain3$FSIQ >= 130)
brain5 <- brain5$`TRUE`

invy_low = 1 / brain4$MRI_Count
finalmodel_low <- lm(invy_low ~ Gender + PIQ + Height, data = brain4)
summary(finalmodel_low)
finalmodel_low$coefficients
############################
invy_high = 1 / brain5$MRI_Count
finalmodel_high <- lm(invy_high ~ Gender + PIQ + Height, data = brain5)
summary(finalmodel_high)
finalmodel_high$coefficients

###########################

finalmodel <- lm(brain3$MRI_Count ~ brain3$Gender + I(brain3$PIQ^2)+ brain3$Height)
summary(finalmodel)

# residual plot
plot(brain3$MRI_Count, resid(finalmodel), main = "Final Model Residual Plot", col = "blue", pch = "*")

plot(brain4$MRI_Count, resid(finalmodel_low), main = "Final Model Residual Plot - low", col = "blue", pch = "*")

plot(brain5$MRI_Count, resid(finalmodel_high), main = "Final Model Residual Plot", col = "blue", pch = "*")
