from logic import *

colors = ["red","blue","green","yellow"]
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

knowledge = And()

for color in colors:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3")
    ),
)
    
for color in colors:
    for i in range(4):
        for j in range(4):
            if i != j:
                knowledge.add(Implication(
                    Symbol(f"{color}{i}"),
                    Not(Symbol(f"{color}{j}"))
                ),
            ),
            
for symbol in symbols:
    if model_check(knowledge,symbol):
        print(f"{symbol}")