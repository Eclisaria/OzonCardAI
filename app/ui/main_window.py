from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QLabel, QMainWindow, QToolBar, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    """Main application window for OzonCardAI."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("OzonCardAI")
        self.resize(1200, 800)

        self._create_menu_bar()
        self._create_toolbar()
        self._create_status_bar()
        self._create_central_area()

    def _create_menu_bar(self) -> None:
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("Файл")
        file_menu.addAction(self._create_action("Выход", self.close))

        menu_bar.addMenu("Настройки")
        menu_bar.addMenu("Помощь")

    def _create_toolbar(self) -> None:
        toolbar = QToolBar("Главная панель", self)
        toolbar.setMovable(False)
        toolbar.addAction(self._create_action("Выход", self.close))
        self.addToolBar(toolbar)

    def _create_status_bar(self) -> None:
        self.statusBar().showMessage("Готово")

    def _create_central_area(self) -> None:
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("OzonCardAI")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setObjectName("titleLabel")

        subtitle = QLabel(
            "Автоматическое создание карточек Ozon\n"
            "из товаров Wildberries\n"
            "с использованием искусственного интеллекта."
        )
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setObjectName("subtitleLabel")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        self.setCentralWidget(central_widget)
        self._apply_styles()

    def _create_action(self, title: str, slot) -> QAction:
        action = QAction(title, self)
        action.triggered.connect(slot)
        return action

    def _apply_styles(self) -> None:
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #f6f7fb;
            }
            QMenuBar, QToolBar, QStatusBar {
                background-color: #ffffff;
                color: #1f2937;
            }
            QMenuBar::item:selected, QMenu::item:selected {
                background-color: #e8eefc;
            }
            QLabel#titleLabel {
                color: #111827;
                font-size: 42px;
                font-weight: 700;
            }
            QLabel#subtitleLabel {
                color: #4b5563;
                font-size: 22px;
                line-height: 1.4;
                margin-top: 16px;
            }
            """
        )
