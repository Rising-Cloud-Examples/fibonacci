import json

# Simple Fibonacci sequence solver, provide an index and receive the number in 
# the sequence at that index
def fibonacci_val_at_index(index: int) -> int:
    
    fib = [0, 1]

    for _ in range(index-1):
        fib.append(fib[-2] + fib[-1])

    return fib[index]

def main():

    # Load request
    with open("request.json", "r") as f:
        index = json.load(f)

        print(index)
        index = index.get("index")

    if index is None:
        with open("response.json", "w") as f:
            json.dump({
                "error": "invalid input, please specify an index like so - " +
                "{\"index\": 10}"
            }, f)
        return

    # Find value of Fibonacci sequence at the rquested index
    val = fibonacci_val_at_index(index)

    # write response
    with open("response.json", "w") as f:
        json.dump({
            "index": index,
            "value": val
        }, f)

    return

if __name__ == "__main__":
    main()