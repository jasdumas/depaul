# DePaul CSC423 Bill Qualls
# Review of properties of parabolas

# for a very trivial plot
x = 0
y = 0

# axes boundaries
XMIN = -6
XMAX = +2
YMIN = 0
YMAX = 10

XLIM = range(c(XMIN, XMAX))
YLIM = range(c(YMIN, YMAX))

# plot line width
LWD = 3 

# plot starts a new plot
plot(x, y, xlim=XLIM, ylim=YLIM)

# R has grid capabilities, but abline is easier
abline(v=seq(from=XMIN, to=XMAX, by=1), col="lightgray", lty="dotted")
abline(h=seq(from=YMIN, to=YMAX, by=1), col="lightgray", lty="dotted")

# build x data
x = seq(from=-6, to=6, by=.5)
x

# first graph is your basic parabola
y1 = x^2
# lines or points instruction add to existing plot
lines(x, y1, col="black", lwd=LWD) 

# watch it shift to the left
y2 = (x+3)^2
lines(x, y2, col="blue", lwd=LWD)

# watch it shift up
y3 = (x+3)^2+5
lines(x, y3, col="red", lwd=LWD)

# watch it narrow / steepen
y4 = 2*(x+3)^2+5
lines(x, y4, col="green", lwd=LWD)

# negative -2 flips the parabola upside down
y5 = -2*(x+3)^2+5
lines(x, y5, col ="purple", lwd=LWD)
