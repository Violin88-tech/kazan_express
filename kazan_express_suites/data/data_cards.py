import dataclasses


@dataclasses.dataclass
class Card:
    card_name: str
    brand_name: str
    card_article: str
    non_existent_article: str


card = Card(
    card_name='Конструктор LEGO Architecture',
    brand_name='LEGO Architecture',
    card_price='11024',
    item_name='Конструктор LEGO Architecture, 21054, &quot;Белый дом',
    non_existent_article='8944165849321186418794'
)


@dataclasses.dataclass
class Texts:
    nothing_found: str = 'Попробуйте поискать по-другому или сократить запрос'
    empty_cart: str = 'В корзине пока пусто'