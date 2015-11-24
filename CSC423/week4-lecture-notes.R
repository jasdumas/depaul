## Lecture 4 notes

x = c(1, 2, 3, 4, 5)
y = c(2, 2, 4, 6, 6)
mean(y)
sd(y)
t = (mean(y) - 3) / (sd(y) / sqrt(5))
t

fit  = lm(y ~ x)
summary(fit)
