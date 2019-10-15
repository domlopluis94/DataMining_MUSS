library(party)
library(RWeka)
library(titanic)

m1 <- J48(Survived~ ., data = Titanic)
## print and summary
m1
summary(m1) # calls evaluate_Weka_classifier()
table(Titanic$Survived, predict(m1)) # by hand

## visualization
## use partykit package
if(require("partykit", quietly = TRUE)) plot(m1)
## or Graphviz
write_to_dot(m1)
## or Rgraphviz
## Not run: 
library("Rgraphviz")
ff <- tempfile()
write_to_dot(m1, ff)
plot(agread(ff))

