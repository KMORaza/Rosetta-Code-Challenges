# Execute a Markov algorithm
import re
rules=[
    [
    "A -> apple","B -> bag","S -> shop","T -> the",
    "the shop -> my brother","a never used -> .terminating rule"
    ],
    [
     "A -> apple","B -> bag","S -> .shop","T -> the",
     "the shop -> my brother","a never used -> .terminating rule"
    ],
    [
     "A -> apple","WWWW -> with","Bgage -> ->.*","B -> bag",
     "->.* -> money","W -> WW","S -> .shop","T -> the",
     "the shop -> my brother","a never used -> .terminating rule"
    ],
    [
     "_+1 -> _1+","1+1 -> 11+","1! -> !1",",! -> !+","_! -> _","1*1 -> x,@y","1x -> xX",
     "X, -> 1,1","X1 -> 1X","_x -> _X",",x -> ,X","y1 -> 1y","y_ -> _","1@1 -> x,@y",
     "1@_ -> @_",",@_ -> !_","++ -> +","_1 -> 1","1+_ -> 1","_+_ -> "
    ],
    [
    "A0 -> 1B","0A1 -> C01","1A1 -> C11","0B0 -> A01","1B0 -> A11",
    "B1 -> 1B","0C0 -> B01","1C0 -> B11","0C1 -> H01","1C1 -> H11"
    ]
]
data=[
    "I bought a B of As from T S.",
    "I bought a B of As from T S.",
    "I bought a B of As W my Bgage from T S.",
    "_1111*11111_",
    "000000A000000"
]
outputs=[
    "I bought a bag of apples from my brother.",
    "I bought a bag of apples from T shop.",
    "I bought a bag of apples with my money from T shop.",
    "11111111111111111111",
    "00011H1111000"
]
def apply_rules(input_str, rule_set):
    output = input_str
    for rule in rule_set:
        find, replace = rule.split(" -> ")
        output = re.sub(re.escape(find), replace, output)
    return output
for i in range(len(data)):
    transformed = apply_rules(data[i], rules[i])
    print("Transformed output for data entry", i + 1, ":", transformed)
    print("Expected output:", outputs[i])
    print("---------------------------------------------")