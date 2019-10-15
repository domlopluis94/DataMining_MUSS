library(party)
library(RWeka)
library(titanic)

m1 <- J48(Survived~., data = Titanic)
 if(require("party", quietly = TRUE)) plot(m1)

