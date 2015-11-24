load("~/Desktop/depaul/CSC423/rdata/R/Exercises&Examples/DIESEL.Rdata")
head(DIESEL)

# convenience
fuel = paste(DIESEL$FUEL)
brand = DIESEL$BRAND
perform = DIESEL$PERFORM
  
# transform
x1 = ifelse(substr(fuel,1,2) == "F2", 1, 0)
x2 = ifelse(substr(fuel,1,2) == "F3", 1, 0)
x3 = ifelse(substr(brand,1,2) == "B2", 1, 0)
x1x3 = x1 * x3
x2x3 = x2 * x3
    
# Fit model (without interaction)
model1 = lm(perform ~ x1 + x2 + x3)
summary(model1)
      
# Fit model (with interaction)
model2 = lm(perform ~ x1 + x2 + x3 + x1x3 + x2x3)
summary(model2)
        
# Show interaction effects. See page 300, Figure 5.24
agg = aggregate(PERFORM ~ FUEL + BRAND, DIESEL, mean )
agg
interaction.plot(agg$FUEL, agg$BRAND, agg$PERFORM, main="Interaction
                             Plot",xlab="FUEL", ylab="Mean of PERFORM") 
