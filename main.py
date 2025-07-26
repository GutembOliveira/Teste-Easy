def two_sum(nums, target):
    seenNumbers = {} 
    for i, num in enumerate(nums):
        secondNumber = target - num
        if secondNumber in seenNumbers:
            return [seenNumbers[secondNumber], i]
        seenNumbers[num] = i
    raise Exception("No solution found")

def main():
    nums = [2, 7, 11, 15]
    #nums = [3, 14, 11, 15,9]
    #nums = [20, 7, 11]
    target = 18

    try:
        result = two_sum(nums, target)
        print(f"Solution Indexes: {result}") 
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
