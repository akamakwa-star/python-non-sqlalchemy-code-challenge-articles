class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be a Magazine")
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("title must be between 5 and 50 characters")
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            return  # prevent reassignment
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("author must be an Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("magazine must be a Magazine")
        self._magazine = value


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name:
            raise ValueError("name must not be empty")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            return  # prevent reassignment

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set([magazine.category for magazine in self.magazines()]))


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise TypeError("category must be a string")
        if not category:
            raise ValueError("category must not be empty")
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and (2 <= len(value) <= 16):
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and value:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author not in authors:
                authors[article.author] = 0
            authors[article.author] += 1
        result = [author for author, count in authors.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))