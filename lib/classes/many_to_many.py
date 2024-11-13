
class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")

        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)


    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not hasattr(self, '_title'):
            if isinstance(title, str) and  5 <= len(title) <= 50:
                self._title = title
            else:
                raise ValueError('Title must be between 5 and 50 characters.')
        else:
            raise AttributeError('Title cannot be changed after instantiation.')

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise ValueError('Magazine must be of type Magazine.')

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise ValueError('Author must be of type Author.')


class Author:
    all = []

    def __init__(self, name):
        
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, '_name'):
            if isinstance(name, str) and len(name) > 0:
                self._name = name
            else:
                raise ValueError('Name must be a non-empty string.')
        else:
            raise AttributeError('Name cannot be changed after initialization.')
        
    def articles(self):
        article_list = []
        for article in Article.all:
            if article.author == self:
                article_list.append(article)
        return article_list
    
    def magazines(self):
        magazine_list = set()
        for article in Article.all:
            if article.author == self:
                magazine_list.add(article.magazine)
        return list(magazine_list)
    
    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine):
           if isinstance(title, str) and 5 <= len(title) <= 50:
             new_article = Article(self, magazine, title)
             return new_article
        else:
            raise ValueError('Invalid magazine or title')
        
    def topic_areas(self):
        categories_list = set()
        for article in Article.all:
            if article.author == self:
                categories_list.add(article.magazine.category)
        return list(categories_list) if categories_list else None
    
    
class Magazine:
    all = []

    def __init__(self, name, category):
        
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError('Name must be a string between 2 and 16 characters.')

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        print(f"Setting category: {category}")
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError('Category must be a non-empty string.')
    def articles(self):
        articles_list = []
        for article in Article.all:
            if article.magazine == self:
                articles_list.append(article)
        return articles_list
    
    def contributors(self):
        author_list = set()
        for article in Article.all:
            if isinstance(article.author, Author) and article.magazine == self:
                author_list.add(article.author)
        return list(author_list)
    
    def article_titles(self):
        titles_list = []
        for article in Article.all:
            if article.magazine == self:
                titles_list.append(article.title)
        return titles_list if titles_list else None
    
    def contributing_authors(self):
        author_article_count = {}
        contributing_authors = []
        for article in Article.all:  
         if article.magazine == self:
            author = article.author
            if author in author_article_count:
                author_article_count[author] += 1
            else:
                author_article_count[author] = 1

   
        for author, count in author_article_count.items():
             if count > 2:
                 contributing_authors.append(author)

        return contributing_authors if contributing_authors else None
       
    

    def counting(self):
        counting_authors = {}
        author_list = []
        for article in Article.all:
            if isinstance(article.author, Author) and article.magazine == self:
                author = article.author
                if author in counting_authors:
                    counting_authors[author] += 1
                else:
                     counting_authors[author] = 1
        for author, count in counting_authors.items():
            if count > 2:
                author_list.append(author)
        return author_list if author_list else None
    

    # python --version
    # deactivate  # to deactivate
# pipenv shell  # to reactivate
    # pipenv --rm
# pipenv install



        







    
   

                





        







    