from abc import ABC, abstractmethod

class StatusBar(ABC):
    def __init__(self, system):
        self._system = system

    @abstractmethod
    def create(self):
        pass

class MainMenu(ABC):
    def __init__(self, system):
        self._system = system

    @abstractmethod
    def create(self):
        pass

class MainWindow(ABC):
    def __init__(self, system):
        self._system = system

    @abstractmethod
    def create(self):
        pass


class WindowsStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print('Created main menu for {}'.format(self._system))

class WindowsMainMenu(MainMenu):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print('Created main menu for {}'.format(self._system))

class WindowsMainWindow(MainWindow):
    def __init__(self):
        super().__init__("Windows")

    def create(self):
        print('Created MainWindow for {}'.format(self._system))

class LinuxStatusBar(StatusBar):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print('Created status bar for {}'.format(self._system))

class LinuxMainMenu(MainMenu):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print('Created main menu for {}'.format(self._system))

class LinuxMainWindow(MainWindow):
    def __init__(self):
        super().__init__("Linux")

    def create(self):
        print('Created MainWindow for {}'.format(self._system))

class GuiAbstractFactory(ABC):
    @abstractmethod
    def getStatusBar(self) -> StatusBar:
        pass
    
    @abstractmethod
    def getMainMenu(self) -> MainMenu:
        pass

    @abstractmethod
    def getMainWindow(self) -> MainWindow:
        pass

class WindowsGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return WindowsStatusBar()

    def getMainMenu(self) -> MainMenu:
        return WindowsMainMenu()

    def getMainWindow(self) -> MainWindow:
        return WindowsMainWindow()

class LinuxGuiFactory(GuiAbstractFactory):
    def getStatusBar(self) -> StatusBar:
        return LinuxStatusBar()
    
    def getMainMenu(self) -> MainMenu:
        return LinuxMainMenu()

    def getMainWindow(self) -> MainWindow:
        return LinuxMainWindow()

class Application:
    def __init__(self, factory: GuiAbstractFactory):
        self._gui_factory = factory

    def create_gui(self):
        mainwindow = self._gui_factory.getMainWindow()
        status_bar = self._gui_factory.getStatusBar()
        main_menu = self._gui_factory.getMainMenu()
        mainwindow.create()
        main_menu.create()
        status_bar.create()

def create_factory(system_name) -> GuiAbstractFactory:
    factory_dict = {"Windows": WindowsGuiFactory,"Linux": LinuxGuiFactory}
    return factory_dict[system_name]()

if __name__ == '__main__':
    print("we have two operating systems Windows and Linux")
    system_name = input("system_name:")
    ui = create_factory(system_name)
    app = Application(ui)
    app.create_gui()
