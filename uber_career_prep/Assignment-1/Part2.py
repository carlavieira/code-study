'''
Part 2: Arrays & Strings

1) isStringPermutation(...)

Implement the function isStringPermutation() that takes two Strings as parameters and returns a Boolean denoting whether the first string is a permutation of the second string.
Go-Lang	func isStringPermutation(s1 string, s2 string) bool {}
Swift		func isStringPermutation(s1: String, s2: String) -> Bool {}
Python 2	def isStringPermutation(s1, s2):
Java		public boolean isStringPermutation(String s1, String s2) {}
Below are some examples:
isStringPermutation(s1: “asdf”, s2: “fsda”) == true
isStringPermutation(s1: “asdf”, s2: “fsa”) == false
isStringPermutation(s1: “asdf”, s2: “fsax”) == false
'''


def isStringPermutation(s1, s2):
    if len(s2) != len(s1): return False
    seen = {}
    for char in s1:
        seen[char] = seen[char] + 1 if char in seen else 1
    for char in s2:
        if char not in seen: return False
        seen[char] -= 1
        if seen[char] < 0: return False
    return True


'''
Complexity analysis:
  First loop (line 21-22): O(n)
      line 22: set item in dict: O(1). Complexity: O(n)*O(1) = O(n)
  Second loop (line 23-26): O(n)
      line 24: k in d in dict: O(1). Complexity: O(n)*O(1) = O(n)
      line 24: set item in dict: O(1). Complexity: O(n)*O(1) = O(n)
      line 26: get item in dict: O(1). Complexity: O(n)*O(1) = O(n)

Total Complexity: O(n)+O(n)+O(n)+O(n) = O(n)
'''


'''
2) pairsThatEqualSum(...)

Implement the function pairsThatEqualSum() that takes an array of integers and a target integer and returns an array of pairs (i.e., an array of tuples) where each pair contains two numbers from the input array and the sum of each pair equals the target integer.

Go-Lang	func pairsThatEqualSum(inputArray []int, targetSum int) []int{}
Swift		func pairsThatEqualSum(inputArray: Array<Int>, targetSum: Int) -> Array<(Int, Int)> {}
Python 2	def pairsThatEqualSum(inputArray, targetSum):
Java		public Array<(Int, Int)> pairsThatEqualSum(Array<Int> inputArray, Int targetSum) {}

Below are some examples:
pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 5) == [(1, 4), (2, 3)]
pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 1) == []
pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 7) == [(2, 5), (3, 4)]
'''


def pairsThatEqualSum(inputArray, targetSum):
    seen = set()
    ans = []
    for n in inputArray:
        complement = targetSum - n
        if complement in seen:
            ans.append((complement, n))
        seen.add(n)
    return ans


'''
Complexity analysis:
  First loop (line 63-67): O(n)
      line 64: set value: O(1). Complexity: O(n)*O(1) = O(n)
      line 65: k in d in set: O(1). Complexity: O(n)*O(1) = O(n)
      line 66: append item in list: O(1). Complexity: O(n)*O(1) = O(n)
      line 67: add item in set: O(1). Complexity: O(n)*O(1) = O(n)

Total Complexity: O(n)+O(n)+O(n)+O(n) = O(n)
'''


print("################ RUNNING TESTS ################")
print('\n1) isStringPermutation')
print(f"isStringPermutation('asdf', 'fsda') = {isStringPermutation('asdf', 'fsda')} (Expected = True)")
print(f"isStringPermutation('asdf', 'fsa') = {isStringPermutation('asdf', 'fsa')} (Expected = False)")
print(f"isStringPermutation('asdf', 'fsax') = {isStringPermutation('asdf', 'fsax')} (Expected = False)")

print('\n2) pairsThatEqualSum')
print(f"pairsThatEqualSum([1, 2, 3, 4, 5], 5) == {pairsThatEqualSum([1, 2, 3, 4, 5], 5)} (Expected = [(1, 4), (2, 3)]")
print(f"pairsThatEqualSum([1, 2, 3, 4, 5], 1) == {pairsThatEqualSum([1, 2, 3, 4, 5], 1)} (Expected = []")
print(f"pairsThatEqualSum([1, 2, 3, 4, 5], 7) == {pairsThatEqualSum([1, 2, 3, 4, 5], 7)} (Expected = [(2, 5), (3, 4)]")
