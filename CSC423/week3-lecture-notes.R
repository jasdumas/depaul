#rm(list =ls())

x = c(2, 4, 6, 8)
y = c(3, 7, 5, 9)
model = lm(y~x)
summary(model) 
# beta-0 / Intercept = 2.0 AND beta-1 / x = 0.8
df = data.frame(x, y)
df
subset.val = subset(df, select = x>2)
subset.val