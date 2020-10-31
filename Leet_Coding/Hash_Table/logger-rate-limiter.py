"""
Approach
-------

Use a hash-table.

1. If log in hash table
1.1     Fetch it
1.2.   Check if current_timestamp - last_timestamp >= 10
1.2.1       Update its entry in hash table with current timestamp and return True.
1.2.2   Else return False
1.2 Else set the log in the Hash table and return True

Complexity
---------

Space: O(N): We can store upto N logs in the hash table. 
Time: O(1) Constant time to fetch logs from Hash table.

"""
class Logger:
	
	def __init__(self):
		self.map_log_statements_to_timestamp = {}

	def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
		if message in self.map_log_statements_to_timestamp:
			last_time_stamp = self.map_log_statements_to_timestamp[message]
			if timestamp - last_time_stamp >= 10:
				self.map_log_statements_to_timestamp[message] = timestamp
				return True
			else:
				return False

		else:
			self.map_log_statements_to_timestamp[message] = timestamp

		return True