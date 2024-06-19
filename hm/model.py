from pomegranate import hmm
from pomegranate.distributions import Categorical
import numpy



# Observation model for each state
sun = Categorical([[0.2,0.8]])

rain = Categorical([[0.9,0.1]])

states = [sun, rain]

# Transition model
transitions = numpy.array(
    [[0.8, 0.2], # Tomorrow's predictions if today = sun
     [0.3, 0.7]] # Tomorrow's predictions if today = rain
)

# Starting probabilities
starts = numpy.array([0.5, 0.5])

# Create the model
# hmm.DenseHMM(transitions,starts=starts,states=states)
model = HiddenMarkovModel.from_matrix(
    transitions, states, starts,
    state_names=["sun", "rain"]
)
model.bake()