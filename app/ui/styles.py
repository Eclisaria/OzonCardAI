APP_STYLE = """
QMainWindow {
    background: #f3f6fb;
}
QMenuBar {
    background: #ffffff;
    color: #1f2937;
    padding: 4px 10px;
    border-bottom: 1px solid #e5e7eb;
}
QMenuBar::item {
    padding: 6px 12px;
    border-radius: 6px;
}
QMenuBar::item:selected {
    background: #eef4ff;
    color: #1d4ed8;
}
QMenu {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    padding: 6px;
}
QMenu::item {
    padding: 8px 24px;
    border-radius: 6px;
}
QMenu::item:selected {
    background: #eef4ff;
    color: #1d4ed8;
}
QToolBar {
    background: #ffffff;
    border-bottom: 1px solid #e5e7eb;
    spacing: 8px;
    padding: 8px 12px;
}
QToolButton {
    background: #f8fafc;
    color: #1f2937;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 8px 12px;
}
QToolButton:hover {
    background: #eef4ff;
    border-color: #bfdbfe;
    color: #1d4ed8;
}
QStatusBar {
    background: #ffffff;
    color: #64748b;
    border-top: 1px solid #e5e7eb;
}
QListWidget#navigationList {
    background: #111827;
    color: #cbd5e1;
    border: none;
    padding: 14px 10px;
    outline: none;
    font-size: 15px;
}
QListWidget#navigationList::item {
    min-height: 42px;
    padding: 8px 12px;
    border-radius: 10px;
    margin: 3px 0;
}
QListWidget#navigationList::item:hover {
    background: #1f2937;
    color: #ffffff;
}
QListWidget#navigationList::item:selected {
    background: #2563eb;
    color: #ffffff;
}
QWidget#contentArea {
    background: #f3f6fb;
}
QFrame#pageCard, QFrame#infoCard, QFrame#heroCard {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
}
QLabel#heroTitle {
    color: #0f172a;
    font-size: 44px;
    font-weight: 800;
}
QLabel#heroSubtitle {
    color: #475569;
    font-size: 22px;
    line-height: 1.4;
}
QLabel#pageTitle {
    color: #0f172a;
    font-size: 30px;
    font-weight: 700;
}
QLabel#sectionTitle {
    color: #0f172a;
    font-size: 18px;
    font-weight: 700;
}
QLabel#bodyText {
    color: #475569;
    font-size: 15px;
    line-height: 1.45;
}
QLabel#mutedText {
    color: #64748b;
    font-size: 14px;
}
QPushButton {
    background: #2563eb;
    color: #ffffff;
    border: none;
    border-radius: 10px;
    padding: 11px 16px;
    font-size: 14px;
    font-weight: 600;
}
QPushButton:hover {
    background: #1d4ed8;
}
QPushButton:pressed {
    background: #1e40af;
}
"""
