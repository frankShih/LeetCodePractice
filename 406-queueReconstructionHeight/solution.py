class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # sort by height descending & numPeople ascending O(N*log(N)), 82%
        length = len(people)

        if length<2:
            return people

        # people=sorted(people ,key=lambda l:(l[0], -l[1]), reverse=True)
        people=sorted(people ,key=lambda l:(-l[0], l[1]))

        result = []
        for person in people:
            # print(result)
            result.insert(person[1], person)

        return result