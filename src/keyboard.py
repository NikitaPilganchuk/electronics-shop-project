from src.item import Item


class MixinLang:
    LANGUAGES = 'EN'

    def __init__(self):
        self.__language = self.LANGUAGES

    def change_lang(self):
        if self.language == 'EN':
            self.__language = 'RU'
        elif self.language == 'RU':
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLang):
    pass
