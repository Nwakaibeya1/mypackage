from mypackage import myModule

def test_top_n():
    """making sure top_n works correctly
    """

    assert myModule.top_n([8,3,7,6,4], 3) == [8,7,6], 'incorrect'
    assert myModule.top_n([1,2,3,4,5], 5) == [5,4,3,2,1], 'incorrect'
    assert myModule.top_n([12,3,15,23,14], 2) == [23,15], 'incorrect'

