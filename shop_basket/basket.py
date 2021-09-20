
class Basket():
    """
    Base Basket class
    """

    def __init__(self, request):
        """
        Takes in a request from user, from where it gets older session or creates new if old one does not exist
        """
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, book):
        """
        Adding users basket session data
        """
        book_id = book.id
        if book_id not in self.basket: # self.basket is from __init__ method 
            self.basket[book_id] = {'price': book.price}

        self.session.modified = True
        # tells Django we have made modification
