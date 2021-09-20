from .models import Category

def categories(request):
    """
    Returns all category information that will be available throught the site
    """
    # we accomplish having this available throughout the whole site by adding
    # this view to the context_processors
    return {
        'categories': Category.objects.all()
    }
