from babsutils.lib import helloworld

def test_length_of_helloworld():   
    assert len(helloworld()) != 0
    
def test_calculation_of_sum():
    assert sum(3,3) == 6
    