class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        # map(function, iterable, ...)  
        a_i, a_c = map(int, a[:-1].split('+'))
        b_i, b_c = map(int, b[:-1].split('+'))      
        return "{}+{}i".format(str(a_i*b_i - a_c*b_c), str(a_i*b_c + b_i*a_c))