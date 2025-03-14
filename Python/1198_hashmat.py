while True:
    try:
        nums = list(map(int, input().split()))
        r = max(nums) - min(nums)
        print(r)
    except EOFError:
        break