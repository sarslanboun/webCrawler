import abc


class BaseProductMethods(abc.ABC):

    @abc.abstractmethod
    def title(self):
        pass

    @abc.abstractmethod
    def price(self):
        pass

    @abc.abstractmethod
    def price_without_discount(self):
        pass

    @abc.abstractmethod
    def main_image_url(self):
        pass

    @abc.abstractmethod
    def image_urls(self):
        pass

    @abc.abstractmethod
    def rating_score(self):
        pass

    @abc.abstractmethod
    def rating_count(self):
        pass

    @abc.abstractmethod
    def review_count(self):
        pass