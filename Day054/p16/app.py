class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            return function(*args, **kwargs)  # Function çağrısını ve sonucunu döndür
        else:
            print(f"User {args[0].name} is not authenticated.")
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("aytekin")
new_user.is_logged_in = True
create_blog_post(new_user)  # Kullanıcı oturum açmış durumda, blog postu oluşturulur

another_user = User("john")
create_blog_post(another_user)  # Kullanıcı oturum açmamış durumda, blog postu oluşturulmaz
