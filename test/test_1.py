
import sys
import os
import unittest

# Add project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import job

class TestQueueJobs(unittest.TestCase):
    def test_queue_jobs_typical(self):
        """
        Tests typical domains.txt parsing.
        """
        domains_txt = """
        prod.ex.org   www.ex.org  api.ex.org
        amy.ex.org    www.ex.org  api.ex.org
        gitlab.ex.org
        """.splitlines()

        expected = {
            "ex.org": [
                {"prod.ex.org": ["www.ex.org", "api.ex.org"]},
                {"amy.ex.org": ["www.ex.org", "api.ex.org"]},
                {"gitlab.ex.org": []}
            ]
        }

        self.assertEqual(job.queue_jobs(domains_txt), expected)

    def test_queue_jobs_whitespace_file(self):
        """
        Tests that queue_jobs returns an empty dict for a file with only whitespace.
        """
        self.assertEqual(job.queue_jobs("  \n".splitlines()), {})

if __name__ == '__main__':
    unittest.main()
