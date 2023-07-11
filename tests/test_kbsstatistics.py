import sys
import os
import unittest

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from isitkbs.ks import isitkbs

class testStatisticsKbs(unittest.TestCase):
    
    def setUp(self):
        self.ksDetector = isitkbs(model='naiveBayes')

    def testOneMashingStatistics(self):
        expectedStatistics = {
            'Total of words:': 1,
            'Total of mashings:': 1,
            'Total of non mashings:': 0,
            'Smashing percentage:': 100.0,
        }

        with open('testFile.txt', 'w') as f:
            f.write("sbfaldaxa")

        detectedStatistics = self.ksDetector.statisticsKbs('./testFile.txt')

        self.assertEqual(expectedStatistics, detectedStatistics)

    def testEmptyFileStatistics(self):
        expectedStatistics = {
            'Total of words:': 0,
            'Total of mashings:': 0,
            'Total of non mashings:': 0,
            'Smashing percentage:': 0.0,
        }
        with open('testFile.txt', 'w') as f:
            f.write("")

        detectedStatistics = self.ksDetector.statisticsKbs('./testFile.txt')

        self.assertEqual(expectedStatistics, detectedStatistics)

    def testMashingNormalStatistics(self):
        expectedStatistics = {
            'Total of words:': 20,
            'Total of mashings:': 5,
            'Total of non mashings:': 15,
            'Smashing percentage:': 25.0,
        }

        with open('testFile.txt', 'w') as f:
            f.write("The world is a ncajbc and wonderful place, but sometimes things get acaouyca and pcoalxcx, so qcagvaicx. Do you rwpofvj?")

        detectedStatistics = self.ksDetector.statisticsKbs('./testFile.txt')

        self.assertEqual(expectedStatistics, detectedStatistics)

if __name__ == '__main__':
    unittest.main()