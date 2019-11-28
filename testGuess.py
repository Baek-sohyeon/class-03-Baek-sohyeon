import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass


    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('k')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('A')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('s')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u d ')
        self.g1.guess('k')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u d k')
        self.g1.guess('s')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u d k s')

    def testReturnFinished(self):
        self.g1.guess('d')
        self.assertEqual(self.g1.finished(), False)
        self.g1.guess('e')
        self.assertEqual(self.g1.finished(), False)
        self.g1.guess('f')
        self.assertEqual(self.g1.finished(), False)
        self.g1.guess('a')
        self.assertEqual(self.g1.finished(), False)
        self.g1.guess('u')
        self.assertEqual(self.g1.finished(), False)
        self.g1.guess('l')
        self.assertEqual(self.g1.finished(), False)
        self.g1.guess('t')
        self.assertEqual(self.g1.finished(), True)

    def testReturnGuessed(self):
        self.assertEqual(self.g1.guess('e'), True)
        self.assertEqual(self.g1.guess('f'), True)
        self.assertEqual(self.g1.guess('a'), True)
        self.assertEqual(self.g1.guess('A'), False)
        self.assertEqual(self.g1.guess('t'), True)
        self.assertEqual(self.g1.guess('l'), True)
        self.assertEqual(self.g1.guess('u'), True)
        self.assertEqual(self.g1.guess('d'), True)
        self.assertEqual(self.g1.guess('k'), False)

if __name__ == '__main__':
    unittest.main()
