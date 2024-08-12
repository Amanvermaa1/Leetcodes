class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        t=[]
        for i in str(time) :
            t.append(str(i))
        if t[0] == '?':
            if t[1] == '?':
                t[0] = '2'
        
        if t[0] == '?':
            if t[1] >= '4':
                t[0] = '1'
            else:
                t[0] = '2'
        
        if t[1] == '?':
            if t[0] == '2':
                t[1] = '3'
            else:
                t[1] = '9'
        
        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'
        x=''
        for i in t:
            x+=i
        return x

    
    