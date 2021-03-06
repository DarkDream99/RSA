from typing import List
import cProfile
import sys

from tqdm import tqdm

from list.linked.linkedlist import LinkedList


sys.maxsize = 1000_000_000_000_000


class PrimeGenerator(object):

    def __init__(self, max_bound: int):
        self._max_bound = max_bound

    def generate(self) -> int:
        primes = self.primes()
        if len(primes) > 0:
            return primes[-1]

    # def primes(self) -> List[int]:
    #     is_prime = LinkedList([False, False])
    #     for i in range(self._max_bound):
    #         is_prime.add(True)
    #     primes = []
    #
    #     for num in tqdm(range(2, self._max_bound + 1)):
    #         if is_prime.get_by_index(num):
    #             primes.append(num)
    #             k = 2
    #             update_values = []
    #             while k * num <= self._max_bound + 1:
    #                 update_values.append((k * num, False))
    #                 k += 1
    #             is_prime.update_from_current(update_values)
    #
    #     return primes

    def primes(self) -> List[int]:
        is_prime = [True] * (self._max_bound + 1)
        is_prime[0] = is_prime[1] = False
        primes = []

        for num in tqdm(range(2, self._max_bound + 1)):
            if is_prime[num]:
                primes.append(num)
                k = 2
                while k * num <= self._max_bound:
                    is_prime[k * num] = False
                    k += 1

        return primes

    # def primes(self) -> List[int]:
    #     is_prime = ~0
    #     is_prime -= 0b1
    #     is_prime -= 0b10
    #     primes = []
    #
    #     for num in tqdm(range(2, self._max_bound + 1)):
    #         if is_prime & (1 << num):
    #             primes.append(num)
    #             k = 2
    #             while k * num <= self._max_bound:
    #                 if is_prime & (1 << (k * num)):
    #                     is_prime -= (1 << (k * num))
    #                 k += 1
    #
    #     return primes


if __name__ == '__main__':
    # max prime a = 999979
    # max prime b = 999983
    prime_generator = PrimeGenerator(250_000_000)
    print(prime_generator.primes())

    # cProfile.run('prime_generator.primes()')
