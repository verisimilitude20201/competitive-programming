"""
Complexity:
---------

Logger1
-------
Time: O(1)
Space: O(M) Where M is the number of distinct log messages received till date

Logger2
-------
Time: O(N)
Space: O(N) 

"""

from collections import deque
class Logger1:

    def __init__(self):
        self._msg_time = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self._msg_time:
            self._msg_time[message] = timestamp
            return True
        if timestamp - self._msg_time[message] >= 10:
            self._msg_time[message] = timestamp
            return True
        return False



class Logger2:

    def __init__(self):
        self._Q = deque([])
        self._seen_msgs = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while len(self._Q):
            msg, ts = self._Q[0]
            if timestamp - ts >= 10:
                self._seen_msgs.remove(msg)
                self._Q.popleft()
            else:
               break
            
        if message not in self._seen_msgs:
            self._seen_msgs.add(message)
            self._Q.append((message, timestamp))
            return True
        
        return False