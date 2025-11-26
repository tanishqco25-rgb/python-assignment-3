# Library Inventory Manager 📚

A robust command-line library management system built with Python, featuring object-oriented design, JSON persistence, and comprehensive error handling.

## 🎯 Features

- **Book Management**: Add, issue, and return books with ease
- **Advanced Search**: Search by title, author, or ISBN
- **Persistent Storage**: JSON-based data storage with automatic backups
- **Error Handling**: Comprehensive exception handling and logging
- **Statistics**: Real-time inventory statistics
- **User-Friendly CLI**: Interactive menu-driven interface
- **Unit Tests**: Complete test coverage using unittest

## 📁 Project Structure

\`\`\`
library-inventory-manager/
├── library_manager/          # Core library management package
│   ├── __init__.py          # Package initialization
│   ├── book.py              # Book class definition
│   └── inventory.py         # Inventory management logic
├── cli/                     # Command-line interface
│   └── main.py              # Main CLI application
├── tests/                   # Unit tests
│   └── test_library.py      # Test cases
├── README.md                # Project documentation
├── .gitignore              # Git ignore rules
├── requirements.txt         # Python dependencies
└── library_catalog.json     # Book catalog (auto-generated)
\`\`\`

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
\`\`\`bash
git clone https://github.com/yourusername/library-inventory-manager.git
cd library-inventory-manager
\`\`\`

2. **Install dependencies**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. **Run the application**
\`\`\`bash
python cli/main.py
\`\`\`

## 💻 Usage

### Running the Application

\`\`\`bash
python cli/main.py
\`\`\`

### Main Menu Options

1. **Add New Book**: Add a book with title, author, and ISBN
2. **Issue Book**: Mark a book as issued by ISBN
3. **Return Book**: Mark an issued book as returned
4. **View All Books**: Display complete inventory
5. **Search by Title**: Find books by title (partial match)
6. **Search by ISBN**: Find exact book by ISBN
7. **Search by Author**: Find books by author name
8. **View Statistics**: Display inventory statistics
9. **Exit**: Close the application

### Example Workflow

\`\`\`
1. Select "1" to add a new book
   - Enter title: "Python Crash Course"
   - Enter author: "Eric Matthes"
   - Enter ISBN: "9781593279288"

2. Select "2" to issue the book
   - Enter ISBN: "9781593279288"

3. Select "8" to view statistics
   - See total, available, and issued books
\`\`\`

## 🧪 Running Tests

Execute the test suite:

\`\`\`bash
python tests/test_library.py
\`\`\`

Or use pytest (if installed):

\`\`\`bash
pytest tests/ -v
\`\`\`

## 📊 Class Structure

### Book Class
- **Attributes**: title, author, isbn, status
- **Methods**: 
  - `issue()`: Mark book as issued
  - `return_book()`: Mark book as available
  - `is_available()`: Check availability
  - `to_dict()`: Serialize to dictionary

### LibraryInventory Class
- **Attributes**: books list, catalog_file path
- **Methods**:
  - `add_book()`: Add new book
  - `search_by_title()`: Search by title
  - `search_by_isbn()`: Search by ISBN
  - `search_by_author()`: Search by author
  - `issue_book()`: Issue a book
  - `return_book()`: Return a book
  - `save_catalog()`: Save to JSON
  - `load_catalog()`: Load from JSON
  - `get_statistics()`: Get inventory stats

## 🔧 Technical Details

### Technologies Used
- **Python 3**: Core programming language
- **JSON**: Data persistence
- **pathlib**: File path management
- **logging**: Application logging
- **unittest**: Testing framework

### Error Handling
- File I/O exceptions (IOError)
- JSON parsing errors (JSONDecodeError)
- Invalid user input validation
- Duplicate ISBN prevention
- Missing file handling with automatic creation

### Logging
- Log file: `library_manager.log`
- Log levels: INFO, WARNING, ERROR
- Dual output: File and console

## 📝 Code Quality

- **PEP 8 Compliant**: Follows Python style guidelines
- **Type Hints**: Included in docstrings
- **Documentation**: Comprehensive docstrings
- **Modular Design**: Separation of concerns
- **DRY Principle**: Reusable functions

## 🛡️ Exception Handling

The application handles:
- Missing or corrupted catalog files
- Invalid user inputs
- Duplicate ISBN entries
- Invalid book operations
- File permission errors

## 📈 Future Enhancements

- [ ] Add book categories/genres
- [ ] Implement due dates for issued books
- [ ] Add user management system
- [ ] Generate reports (PDF/CSV)
- [ ] Add barcode scanning support
- [ ] Web-based interface
- [ ] Database integration (SQLite/PostgreSQL)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is created for educational purposes as part of the Programming for Problem Solving using Python course.

## 👨‍💻 Author

Your Name - [Your GitHub Profile](https://github.com/yourusername)

## 📧 Contact

For queries: jyoti.yadav@krmangalam.edu.in

## 🙏 Acknowledgments

- K.R. Mangalam University
- Course: Programming for Problem Solving using Python
- Instructor: Prof. Jyoti Yadav

---

**Happy Coding! 🚀**
\`\`\`

```text file=".gitignore"
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# Project specific
library_catalog.json
library_catalog.json.backup
test_catalog.json
library_manager.log
*.backup

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
