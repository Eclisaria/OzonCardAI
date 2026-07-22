from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QWidget

APP_VERSION = "0.1.0"


def create_home_page() -> QWidget:
    page = _base_page()
    layout = page.layout()

    hero = QFrame()
    hero.setObjectName("heroCard")
    hero_layout = QVBoxLayout(hero)
    hero_layout.setContentsMargins(34, 34, 34, 34)
    hero_layout.setSpacing(14)

    title = _label("OzonCardAI", "heroTitle")
    subtitle = _label(
        "Автоматическое создание карточек Ozon\n"
        "из товаров Wildberries\n"
        "с использованием искусственного интеллекта.",
        "heroSubtitle",
    )
    hero_layout.addWidget(title)
    hero_layout.addWidget(subtitle)
    layout.addWidget(hero)

    cards = QGridLayout()
    cards.setSpacing(16)
    cards.addWidget(_info_card("Статус проекта", "Создается профессиональный интерфейс приложения."), 0, 0)
    cards.addWidget(_info_card("Этап разработки", "Этап 1 — фундамент и навигация."), 0, 1)
    cards.addWidget(_info_card("Версия приложения", APP_VERSION), 1, 0)
    cards.addWidget(
        _info_card(
            "Будущие возможности",
            "Подключение WB, генерация карточек через ИИ и создание черновиков Ozon.",
        ),
        1,
        1,
    )
    layout.addLayout(cards)
    layout.addStretch()
    return page


def create_placeholder_page(title: str, description: str, button_text: str | None = None) -> QWidget:
    page = _base_page()
    layout = page.layout()

    card = QFrame()
    card.setObjectName("pageCard")
    card_layout = QVBoxLayout(card)
    card_layout.setContentsMargins(32, 32, 32, 32)
    card_layout.setSpacing(16)

    card_layout.addWidget(_label(title, "pageTitle"))
    card_layout.addWidget(_label(description, "bodyText"))

    stub = _info_card("Заглушка", "Раздел подготовлен для дальнейшего развития на следующих этапах проекта.")
    card_layout.addWidget(stub)

    if button_text:
        row = QHBoxLayout()
        button = QPushButton(button_text)
        button.setEnabled(False)
        row.addWidget(button)
        row.addStretch()
        card_layout.addLayout(row)

    card_layout.addStretch()
    layout.addWidget(card)
    layout.addStretch()
    return page


def create_about_page() -> QWidget:
    page = _base_page()
    layout = page.layout()
    card = QFrame()
    card.setObjectName("pageCard")
    card_layout = QVBoxLayout(card)
    card_layout.setContentsMargins(32, 32, 32, 32)
    card_layout.setSpacing(14)

    card_layout.addWidget(_label("О программе", "pageTitle"))
    card_layout.addWidget(_label("OzonCardAI", "sectionTitle"))
    card_layout.addWidget(_label(f"Версия: {APP_VERSION}", "bodyText"))
    card_layout.addWidget(
        _label(
            "Профессиональное desktop-приложение для автоматизации подготовки карточек Ozon "
            "на основе товаров Wildberries.",
            "bodyText",
        )
    )
    card_layout.addWidget(_label("GitHub: будет добавлен позже", "bodyText"))
    card_layout.addWidget(_label("Автор: команда OzonCardAI", "bodyText"))
    card_layout.addStretch()
    layout.addWidget(card)
    layout.addStretch()
    return page


def _base_page() -> QWidget:
    page = QWidget()
    page.setObjectName("contentArea")
    layout = QVBoxLayout(page)
    layout.setContentsMargins(28, 28, 28, 28)
    layout.setSpacing(20)
    return page


def _info_card(title: str, body: str) -> QFrame:
    card = QFrame()
    card.setObjectName("infoCard")
    layout = QVBoxLayout(card)
    layout.setContentsMargins(22, 20, 22, 20)
    layout.setSpacing(8)
    layout.addWidget(_label(title, "sectionTitle"))
    layout.addWidget(_label(body, "mutedText"))
    return card


def _label(text: str, object_name: str) -> QLabel:
    label = QLabel(text)
    label.setObjectName(object_name)
    label.setWordWrap(True)
    label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
    return label
