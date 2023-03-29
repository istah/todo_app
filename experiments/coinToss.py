inputs = []
while True:
    prompt = input("Throw the coin and enter head or tail here: ")
    print(prompt)
    inputs.append(prompt)
    n_heads = inputs.count("head")
    n_tail = inputs.count("tail")
    sum = n_heads + n_tail
    percentage = n_heads / sum * 100
    print(f"Heads: {percentage}%")