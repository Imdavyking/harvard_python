from constraint import *


problem = Problem()
problem.addVariables(
    ["A","B","C","D","E","F","G"],
    ["Monday","Tuesday","Wednesday"]
)

CONSTRAINTS = [
    ("A","B"),
    ("A","C"),
    ("B","C"),
    ("B","D"),
    ("B","E"),
    ("C","E"),
    ("C","F"),
    ("D","E"),
    ("E","F"),
    ("E","G"),
    ("F","G"),
]

