from pomegranate import *
from pomegranate.distributions import *
from pomegranate.markov_chain import MarkovChain

start = Categorical(
    [
        [0.5,0.5],
    ]
)


transitions = ConditionalCategorical(
    [
        [
            [0.8, 0.2],
            [0.3, 0.7]
        ],
    ]
)

model = MarkovChain([start,transitions])

print(model.sample(50))