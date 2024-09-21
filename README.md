# TgNotes - Telegram-Based Note Taking App

TgNotes is a feature-rich note-taking application integrated with Telegram, designed to help you stay organized with an intuitive and flexible approach. This app provides functionality for creating, sharing, and managing notes, all while leveraging Telegram's communication infrastructure.

---

## Features (Current & Planned)

### Implemented:
- **Mixed Text Editing**: Use special symbols or interface tools to format your text with ease.
- **Quick Notes**: Easily create a note with a single tap on the "+" button.
- **Note Folders**: Organize notes into customizable folders with three layout options (stack, grid, or card format).
- **Auto-Delete Notes**: Set notes to automatically delete after specific time periods (3 days, 7 days, 14 days, 30 days, 6 months, or 12 months).
- **Task Tracker**: Track deadlines with a countdown timer integrated into your notes.
- **Basic To-Do Functionality**: Use checkboxes to mark tasks as completed within your notes.
- **Telegram Integration**: Share your notes with Telegram contacts and give them permission to edit.
- **Bot Integration**: Create notes via a Telegram bot, either manually or by forwarding messages from Telegram channels.
- **Protected Folder**: Create password-protected folders to keep your sensitive notes secure.

### Planned Features:
- **Advanced Checklist Enhancements**: Refine and extend the functionality of checkboxes for to-do lists.
- **Sticker Support**: Add emojis or stickers next to your notes to enhance visual organization.
- **Enhanced Notifications**: Customizable notifications to remind you of important notes or tasks.
- **Emoji Auto-Generation**: Automatically assign emojis to folder names based on folder content or title.
- **Advanced Bot Features**: More sophisticated bot interactions, including task reminders and deeper folder integration.

---

## Tech Stack

- **Backend**: Flask, SQLAlchemy, SQLite
- **Frontend**: HTML, CSS, Bootstrap
- **Telegram Integration**: Telebot

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/tgnotes.git
    cd tgnotes
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    ```bash
    python manage.py db upgrade
    ```

4. Run the Flask application:

    ```bash
    flask run
    ```

5. Configure the Telegram bot by setting up your bot token in the `config.py` file.

---

## Usage

Once the app is up and running, you can access it via the web browser and link it to your Telegram account to begin creating and managing your notes. You can interact with the bot to automate tasks, forward notes from Telegram channels, and set reminders for important events.

---

## Contributing

Feel free to contribute by submitting pull requests, reporting bugs, or suggesting new features. We are currently working on implementing several new features and would love community support.

---

## Roadmap

- **Q4 2024**: Complete sticker and emoji integration, finalize advanced checklist functionalities.
- **Q1 2025**: Full integration of advanced bot features, including note reminders and in-depth task management.
- **Q2 2025**: Implement sharing permissions at folder level and advanced collaboration features.
