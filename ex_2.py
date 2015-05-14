import unittest

def calculate(prices_dicc,products):
    
    total = 0
    
    for product in products:
        total += prices_dicc[product]
        
    return total 

class TestAverage(unittest.TestCase):
    
    def setUp(self):
        self.prices_dicc = {"apple":1.25,"coca-cola":1.75,"kit kat":0.95,"oreo":1.10}
        
    def test_(self):
        pass
            
if __name__ == '__main__':
    unittest.main()