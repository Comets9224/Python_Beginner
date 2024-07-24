class User:
    def __init__(self,username, password):
        self.username = username
        self.password = password
    def login(self):
        if self.username == 'admin' and self.password == '<PASSWORD>':
            print('Login successful!')
        else:
            print('Login failed')
    def publish(self,article):
        print(article.author,'发表了文章',article.title)
    def show(self):
        print('Username:', self.username)
        print('Password:', self.password)