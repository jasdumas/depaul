library(scatterplot3d)

seeds <- read.table("/Users/jasminedumas/desktop/depaul/IS467/seeds.txt", header = T)

with(seeds, {
  scatterplot3d(area,   # x axis
                perimeter,     # y axis
                width_of_kernal,    # z axis
                main="3-D Scatterplot of 3 Most Important Variables")
})


# create column indicating point color
seeds$pcolor[seeds$class==1] <- "red"
seeds$pcolor[seeds$class==2] <- "blue"
seeds$pcolor[seeds$class==3] <- "darkgreen"

with(seeds, {
  s3d <- scatterplot3d(area, perimeter, width_of_kernal,        # x y and z axis
                       color=pcolor, pch=19,        # circle color indicates no. of cylinders
                       type="h", lty.hplot=2,       # lines to the horizontal plane
                       scale.y=.75)          # lines to the horizontal plane
  
  s3d.coords <- s3d$xyz.convert(area, perimeter, width_of_kernal) # convert 3D coords to 2D projection
  text(s3d.coords$x, s3d.coords$y,             # x and y coordinates
       labels=seeds$class,               # text to plot
       cex=.5, pos=4)  
  # add the legend
  legend("topleft", inset=.05,      # location and inset
         bty="n", cex=.5,              # suppress legend box, shrink text 50%
         title="Important Parameters",
         c("1", "2", "3"), fill=c("red", "blue", "darkgreen"))
  
})

pairs(seeds[, 1:7], col=seeds$pcolor)

# linear model
fit <- lm(class ~ area + perimeter + compactness + 
            length_of_kernal + width_of_kernal + 
            asymmetry_coefficient + length_of_kernal_grove, data = seeds) 
summary(fit)

# forward selection
min.model = lm(class ~ 1, data=seeds)          # aka intercept only model
biggest = formula(lm(class ~ area + perimeter + compactness + 
                       length_of_kernal + width_of_kernal + 
                       asymmetry_coefficient + length_of_kernal_grove, data = seeds) )   # the full model
model = step(min.model, direction='forward', scope=biggest)
summary(model)

