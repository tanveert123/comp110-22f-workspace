point: 0

def main() -> None: 
    greet()
    baby()

def greet() -> str:
    global point
    point += 1

def baby() -> str:
    global point 
    print(point)

if __name__ == "__main__":
  main()