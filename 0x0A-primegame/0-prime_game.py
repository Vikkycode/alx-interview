def isWinner(x, nums):
    if not nums or x <= 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        available_numbers = list(range(1, n + 1))
        turns = 0

        while True:
            prime_found = False
            for p in range(2, n + 1):
                is_prime = True
                for i in range(2, int(p**0.5) + 1):
                    if p % i == 0:
                        is_prime = False
                        break
                if is_prime and p in available_numbers:

                    nums_to_remove = []
                    for num in available_numbers:
                        if num % p == 0:
                            nums_to_remove.append(num)

                    for num in nums_to_remove:
                        available_numbers.remove(num)

                    prime_found = True
                    turns += 1
                    break  # Move on to next player's turn

            if not prime_found:
                break

        if turns % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
