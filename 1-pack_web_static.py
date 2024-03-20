import unittest
import MySQLdb

class TestMySQLFunctionality(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
	# Connect to the MySQL database
	cls.db = MySQLdb.connect(host="localhost",
				user="hbnb_test",
				password="hbnb_test_pwd",
				db="hbnb_test_db")
	cls.cursor = cls.db.cursor()

	@classmethod
	def tearDownClass(cls):
	# Close the database connection
	cls.db.close()

	def test_create_state(self):
	# Get the initial count of records in the states table
	self.cursor.execute("SELECT COUNT(*) FROM states")
	initial_count = self.cursor.fetchone()[0]

	# Execute the console command (assuming it's a function in your codebase)
	# For example: create_state("California")
	create_state_command = ... # Your code to execute the command

        # Get the count of records again
        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]

	# Assert that the count has increased by 1
	self.assertEqual(final_count, initial_count + 1)

if __name__ == '__main__':
    unittest.main()
