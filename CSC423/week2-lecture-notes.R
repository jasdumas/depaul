# simple regression example
# file name: week2-lecture-notes.R
setwd("/Users/jasminedumas/Desktop/depaul/CSC423") # all my work should be here

x <- c(2, 4, 6, 8) # prof. qualls calls it a tuple
y <- c(2, 6, 4, 8)
reg <- lm(y~x)
summary(reg)

# plot of the x, y
library(ggplot2)
df = data.frame(x, y)
a <- ggplot(df, aes(x, y)) +
     geom_point() +
     geom_smooth(method = "lm")