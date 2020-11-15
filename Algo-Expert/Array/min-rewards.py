"""
Min Rewards
Input: [8, 4, 2, 1, 3, 6, 7, 9, 5]
Output: [4, 3, 2, 1, 2, 3, 4, 5, 1] // Sum 25

Assumptions
------------
1. All array elements are unique, positive integers

Approach 1:
-----------
1. Initialize a rewards array to all 1s. 
2. If previous score is less than current score, 
    current reward = previous reward + 1
3. Else if previous score is greater than current score, 
    current reward = max(current_reward, previous reward + 1)
4. Return the sum of all rewards.

Complexity 1 
------------
Time: O(N^2) Iterating through the array twice
Space: O(N) Auxillary array created for rewards.


Approach 2:
----------
1. Find the local min indices (Element in an array that's less than its previous and next element)
2. For each local min index,
2.1 Traverse to left till we don't go past the end of array and left score is greater than the current score
2.1.1  rewards[left] = max(rewards[left], rewards[left + 1] + 1)
2.2 Traverse to right, till we don't go past the right most end of the array and current score is less than the right score.
2.2.1 rewards[right] = rewards[right - 1] + 1

Complexity 2 
------------
Time: O(N) Iterating through the array once
Space: O(N) Auxillary array created for rewards.
"""

def minRewards1(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        j = i - 1
        if scores[i] > scores[j]:
            rewards[i] = rewards[j] + 1
        else:
            while j >= 0 and scores[j] > scores[j + 1]:
                rewards[j] = max(rewards[j], rewards[j + 1] + 1)
                j -= 1


    return sum(rewards)


def minRewards2(scores):
    rewards = [1 for _ in scores]
    localMinIndxs = getLocalMinIndxs(scores)
    for localMinIndx in localMinIndxs:
        leftIdx = localMinIndx - 1
        while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:
            rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
            leftIdx -= 1
        rightIdx = localMinIndx + 1
        while rightIdx < len(scores) and scores[rightIdx]> scores[rightIdx - 1]:
            rewards[rightIdx] = rewards[rightIdx - 1] + 1
            rightIdx += 1

    return sum(rewards)


def getLocalMinIndxs(scores):
    if len(scores) == 1:
		return [0]
	localMinIndxs = []
    for i in range(len(scores)):
        if i == 0 and scores[i] < scores[i + 1]:
            localMinIndxs.append(i)
        if i == len(scores) - 1 and scores[i] < scores[i - 1]:
            localMinIndxs.append(i)
        if i == 0 or i == len(scores) - 1:
            continue
        if scores[i] < scores[i - 1] and scores[i] < scores[i + 1]:
            localMinIndxs.append(i)


    return localMinIndxs



def minRewards3(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):
        if scores[i] > scores[i - 1]:
            rewards[i] = rewards[i - 1] + 1

    for i in reversed(range(len(scores) - 1)):
        if scores[i] > scores[i + 1]:
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)

    return sum(rewards)