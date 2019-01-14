class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """

        result = []
        if not deck:
            return result

        # the result need to be sorted, sort it first
        outcome=sorted(deck)

        # origin operation: 
        #     result.append(deck.pop(0)) 
        #     deck.append(deck.pop(0))
        # reversed: 
        #     result.insert(0, result.pop()) 
        #     result.insert(0, outcome.pop())
        while outcome:
            if result:
                result.insert(0, result.pop())
            result.insert(0, outcome.pop())

        return result
