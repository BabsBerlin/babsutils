from babsutils.lib import helloworld, sumup

def test_length_of_helloworld():   
    assert len(helloworld()) != 0
    
def test_calculation_of_sumup():
    assert sumup(3,3) == 6
    