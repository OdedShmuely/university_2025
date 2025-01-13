import time
from Angry import Angry
from Furious import Furious
from Explosive import Explosive
from Chill import Chill
from Calm import Calm
from TypeA import TypeA
from TypeB import TypeB


class Customer:
    def __init__(self, name, mood, personality, initial_patience=100, arrive_time=None):
        self.name = name
        self.__mood = mood
        self.personality = personality
        self.initial_patience = initial_patience
        self.__patience = initial_patience
        if arrive_time is None:
            self.arrive_time = int(time.time())
        else:
            self.arrive_time = arrive_time

    def get_mood(self):
        return self.__mood

    def get_waiting_time(self, current_time=None):
        """
        :param current_time: current time
        :return: the time passed from the beginning
        """
        if current_time is None:
            current_time = int(time.time())
        return current_time-self.arrive_time

    def get_patience(self):
        return round(self.__patience,2)

    def update(self, waiting_time=None):
        """
        update patience and then update the mood of customer
        :param waiting_time: if None --> get the waiting time to be the current time
        :return: None
        """
        if waiting_time is None:
            waiting_time = self.get_waiting_time()
        self.__patience -= self.__mood.get_patience_factor(waiting_time)
        self.__mood = self.personality.adjust_mood(self.__mood,waiting_time)


    def __repr__(self):
        categories = [f'name: {self.name}',f'mood: {self.__mood.__name__}',f'personality: {self.personality.__name__}',f'patience: {self.__patience}']
        counter = [len(counter) for counter in categories]
        max_len = max(counter)
        str_to_print = f'{(max_len + 4) * "*"}\n'
        for line in categories:
            str_to_print = f'{str_to_print}* {line}{(max_len-len(line))*" "} *\n'
        str_to_print += f'{(max_len + 4) * "*"}'
        return str_to_print


my_customer = Customer('oded',Calm,TypeA)
print(my_customer)
# time.sleep(1)
my_customer.update(my_customer.get_waiting_time())
print(my_customer)