from .basket import Basket

def basket(request):
    """
    Returns basket data
    """
    return {'basket':Basket(request)}