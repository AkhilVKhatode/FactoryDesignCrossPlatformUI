from abc import ABC, abstractmethod
import sys

# Abstract Product Interfaces
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self):
        pass

class Window(ABC):
    @abstractmethod
    def render(self):
        pass

class Menu(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Products for Windows
class WindowsButton(Button):
    def render(self):
        return "Windows style button rendered"

    def on_click(self):
        return "Windows button click handled"

class WindowsWindow(Window):
    def render(self):
        return "Windows style window rendered"

class WindowsMenu(Menu):
    def render(self):
        return "Windows style menu rendered"

# Concrete Products for Mac
class MacButton(Button):
    def render(self):
        return "Mac style button rendered"

    def on_click(self):
        return "Mac button click handled"

class MacWindow(Window):
    def render(self):
        return "Mac style window rendered"

class MacMenu(Menu):
    def render(self):
        return "Mac style menu rendered"

# Concrete Products for Linux
class LinuxButton(Button):
    def render(self):
        return "Linux style button rendered"

    def on_click(self):
        return "Linux button click handled"

class LinuxWindow(Window):
    def render(self):
        return "Linux style window rendered"

class LinuxMenu(Menu):
    def render(self):
        return "Linux style menu rendered"

# Abstract Factory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_window(self) -> Window:
        pass
    
    @abstractmethod
    def create_menu(self) -> Menu:
        pass

# Concrete Factories
class WindowsUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_window(self) -> Window:
        return WindowsWindow()
    
    def create_menu(self) -> Menu:
        return WindowsMenu()

class MacUIFactory(UIFactory):
    def create_button(self) -> Button:
        return MacButton()
    
    def create_window(self) -> Window:
        return MacWindow()
    
    def create_menu(self) -> Menu:
        return MacMenu()

class LinuxUIFactory(UIFactory):
    def create_button(self) -> Button:
        return LinuxButton()
    
    def create_window(self) -> Window:
        return LinuxWindow()
    
    def create_menu(self) -> Menu:
        return LinuxMenu()

# Factory provider
def get_ui_factory() -> UIFactory:
    platform = sys.platform.lower()
    
    if platform.startswith('win'):
        return WindowsUIFactory()
    elif platform.startswith('darwin'):
        return MacUIFactory()
    elif platform.startswith('linux'):
        return LinuxUIFactory()
    else:
        raise NotImplementedError(f"Platform {platform} not supported")

# Client code
def main():
    factory = get_ui_factory()
    
    button = factory.create_button()
    window = factory.create_window()
    menu = factory.create_menu()
    
    print(button.render())
    print(window.render())
    print(menu.render())
    print(button.on_click())

if __name__ == "__main__":
    main()
