from dataclasses import dataclass

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QSplitter,
    QStackedWidget,
    QToolBar,
)

from app.ui.pages import (
    create_about_page,
    create_home_page,
    create_placeholder_page,
)
from app.ui.styles import APP_STYLE


@dataclass(frozen=True)
class NavigationItem:
    title: str
    status_message: str


class MainWindow(QMainWindow):
    """Main application window for OzonCardAI."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("OzonCardAI")
        self.resize(1200, 800)
        self.setMinimumSize(1000, 680)
        self.setStyleSheet(APP_STYLE)

        self._navigation_items = [
            NavigationItem("🏠 Главная", "Главная страница"),
            NavigationItem("📦 Товары Wildberries", "Раздел товаров Wildberries"),
            NavigationItem("📝 Черновики Ozon", "Раздел черновиков Ozon"),
            NavigationItem("🤖 Искусственный интеллект", "Раздел искусственного интеллекта"),
            NavigationItem("📊 История операций", "Раздел истории операций"),
            NavigationItem("⚙ Настройки", "Раздел настроек"),
            NavigationItem("ℹ О программе", "Информация о приложении"),
        ]

        self.navigation = QListWidget()
        self.pages = QStackedWidget()

        self._create_menu_bar()
        self._create_toolbar()
        self._create_status_bar()
        self._create_central_layout()

        self._select_page(0)

    def _create_menu_bar(self) -> None:
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("Файл")
        file_menu.addAction(self._create_action("Главная", lambda: self._select_page(0)))
        file_menu.addSeparator()
        file_menu.addAction(self._create_action("Выход", self.close))

        settings_menu = menu_bar.addMenu("Настройки")
        settings_menu.addAction(
            self._create_action("Открыть настройки", lambda: self._select_page(5))
        )

        help_menu = menu_bar.addMenu("Помощь")
        help_menu.addAction(
            self._create_action("О программе", lambda: self._select_page(6))
        )

    def _create_toolbar(self) -> None:
        toolbar = QToolBar("Главная панель", self)
        toolbar.setMovable(False)

        toolbar.addAction(self._create_action("Главная", lambda: self._select_page(0)))
        toolbar.addAction(self._create_action("WB товары", lambda: self._select_page(1)))
        toolbar.addAction(self._create_action("Ozon", lambda: self._select_page(2)))
        toolbar.addAction(self._create_action("AI", lambda: self._select_page(3)))

        self.addToolBar(toolbar)

    def _create_status_bar(self) -> None:
        self.statusBar().showMessage("Готово")

    def _create_central_layout(self) -> None:
        self._configure_navigation()
        self._populate_pages()

        splitter = QSplitter(Qt.Orientation.Horizontal, self)

        splitter.addWidget(self.navigation)
        splitter.addWidget(self.pages)

        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        splitter.setSizes([260, 940])
        splitter.setChildrenCollapsible(False)

        self.setCentralWidget(splitter)

    def _configure_navigation(self) -> None:
        self.navigation.setObjectName("navigationList")
        self.navigation.setFixedWidth(260)
        self.navigation.setSpacing(4)

        for item in self._navigation_items:
            self.navigation.addItem(QListWidgetItem(item.title))

        self.navigation.currentRowChanged.connect(self._select_page)

    def _populate_pages(self) -> None:
        pages = [
            create_home_page(),
            create_placeholder_page(
                "Товары Wildberries",
                "Здесь появится список товаров продавца после подключения официального Wildberries API.",
                "Подключение будет реализовано позже",
            ),
            create_placeholder_page(
                "Черновики Ozon",
                "В этом разделе будут отображаться подготовленные черновики карточек для Ozon Seller API.",
                "Подключение будет реализовано позже",
            ),
            create_placeholder_page(
                "Искусственный интеллект",
                "Будущий центр генерации названий, описаний, SEO, характеристик и атрибутов карточек.",
            ),
            create_placeholder_page(
                "История операций",
                "Журнал будущих действий: импорт товаров, генерация контента и создание черновиков.",
            ),
            create_placeholder_page(
                "Настройки",
                "Позже здесь появятся настройки приложения без реализации токенов и авторизации на текущем этапе.",
            ),
            create_about_page(),
        ]

        for page in pages:
            self.pages.addWidget(page)

    def _select_page(self, index: int) -> None:
        if index < 0 or index >= self.pages.count():
            return

        self.pages.setCurrentIndex(index)

        if self.navigation.currentRow() != index:
            self.navigation.setCurrentRow(index)

        self.statusBar().showMessage(
            self._navigation_items[index].status_message
        )

    def _create_action(self, title: str, slot) -> QAction:
        action = QAction(title, self)
        action.triggered.connect(slot)
        return action