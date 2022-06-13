from random import randint, choice


class Color:
    """Класс полностью отвечает за формирование списка предметов разных цветов,
    за рандомное распределение цветов,
    за обновление цветов,
    за получение конкретного цвета,
    и за пересчет вероятности.
    """

    def __init__(self):
        self.item_list = self.do_item_list()
        self.started_probability = {'blue': 90, 'green': 96, 'red': 100}
        self.color_probability = {
            'blue': [self.item_list.count('blue') / len(self.item_list), self.item_list.count('blue')],
            'green': [self.item_list.count('green') / len(self.item_list), self.item_list.count('green')],
            'red': [self.item_list.count('red') / len(self.item_list), self.item_list.count('red')]}
        self.current_len = 99
        self.cash = {}
        self.current_color = 'blue'

    @staticmethod
    def do_color():
        """
        рандомное получение цвета, с сильным уклоном в сторону синего,
        и с учетом того что зеленого должно быть немного больше красного
        :return: str
        """
        color_status = randint(1, 100)
        if color_status <= 90:
            return 'blue'
        if 90 < color_status <= 96:
            return 'green'
        return 'red'

    def do_item_list(self):
        """
        создание списка из 100 элементов разных цветов
        :return: list
        """
        items = [self.do_color() for item in range(0, 100)]
        if items.count('green') <= items.count('red'):
            change_condition = items.count('red') - items.count('green') if items.count('red') - items.count(
                'green') else 1
            for item in range(change_condition):
                items[items.index('red')] = 'green'
        return items

    def get_color(self, index):
        """
        возвращает либо цвет из кэша если уже известен предмет под этим индексом,
        либо предположение о цыете если индекса нет в кше
        :param index: int
        :return: tuple(str, bool)
        """
        if index not in self.cash:

            max_color_value = 0
            max_color_keys = []

            # finding max probability
            for key in self.color_probability:
                if self.color_probability[key][0] >= max_color_value:
                    max_color_value = self.color_probability[key][0]
            real_color = self.item_list[index]

            # choice colors with same probability
            for key in self.color_probability:
                if self.color_probability[key][0] == max_color_value:
                    max_color_keys.append(key)
            max_color_key = choice(max_color_keys)

            # update probability
            self.color_probability[max_color_key][1] -= 1

            # cashing true color
            self.cash[index] = real_color

            # update current len
            for key in self.color_probability:
                self.color_probability[key][0] = self.color_probability[key][1] / self.current_len
            self.current_len -= 1
            if not self.current_len:
                self.current_len += 1
            self.current_color = max_color_key, True if real_color == max_color_key else False
            return max_color_key, True if real_color == max_color_key else False
        self.current_color = self.cash[index], True
        return self.cash[index], True

    def refresh(self):
        """
        обновление списка
        :return: None
        """
        self.item_list = self.do_item_list()
        self.started_probability = {'blue': 90, 'green': 96, 'red': 100}
        self.color_probability = {
            'blue': [self.item_list.count('blue') / len(self.item_list), self.item_list.count('blue')],
            'green': [self.item_list.count('green') / len(self.item_list), self.item_list.count('green')],
            'red': [self.item_list.count('red') / len(self.item_list), self.item_list.count('red')]}
        self.current_len = 99
        self.cash = {}
        self.current_color = 'blue'
