def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = []
        sieve = [True] * (n + 1)  # Sieve of Eratosthenes optimization
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for multiple in range(i * i, n + 1, i):
                    sieve[multiple] = False

        for i in range(2, n + 1):
            if sieve[i]:
                primes.append(i)

        set_nums = list(range(1, n + 1))
        turns = 0
        while True:
            found_prime = False
            for prime in primes:
                if prime in set_nums:
                    remove_multiples = []
                    for num in set_nums:
                        if num % prime == 0:
                            remove_multiples.append(num)

                    for num_to_remove in remove_multiples:
                        set_nums.remove(num_to_remove)
                    found_prime = True
                    turns += 1
                    break

            if not found_prime:
                break

        if turns % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
