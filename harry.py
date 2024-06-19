from logic import *

rain = Symbol("rain") # it is raining
hagrid =  Symbol("hagrid") # Harry visits Hagrid
dumbledore = Symbol("dumbledore") # Harry visits Dumbledore

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
   Not( And(hagrid,dumbledore)),
   dumbledore
) 






print(model_check(knowledge,rain))