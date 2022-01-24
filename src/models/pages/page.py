from abc import ABC, abstractmethod


class Page(ABC):

    def __init__(self):
        self.pane = None
        self.button = None

    @abstractmethod
    def get_contents(self):
        pass
