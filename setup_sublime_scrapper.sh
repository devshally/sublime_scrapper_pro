#!/bin/bash

# Exit on error
set -e

# Project root
PROJECT_NAME="sublime_scrapper_pro"
mkdir -p $PROJECT_NAME && cd $PROJECT_NAME

echo "📁 Creating folder structure..."

# Core Folders
mkdir -p auth
mkdir -p modules/{apollo,snovio,lusha,rocketreach,sales_navigator}
mkdir -p engine
mkdir -p outputs
mkdir -p gui
mkdir -p updater
mkdir -p jobs
mkdir -p utils
mkdir -p tests
mkdir -p configs
mkdir -p logs
mkdir -p plugins
mkdir -p scheduler
mkdir -p api_mode

# Init files for each folder
find . -type d -exec touch {}/__init__.py \;

# Core Python files
touch main.py
touch run.py
touch README.md
touch .gitignore
touch requirements.txt

echo "🧱 Creating boilerplate core files..."
# Example module files
touch auth/browser_auth.py
touch auth/api_auth.py

touch engine/scraper_manager.py
touch engine/thread_manager.py
touch engine/proxy_manager.py
touch engine/rate_limiter.py
touch engine/captcha_solver.py
touch engine/field_mapper.py
touch engine/logger.py
touch engine/data_validator.py
touch engine/error_handler.py

touch gui/main_window.py
touch gui/updater_ui.py
touch gui/job_configurator.py
touch gui/progress_panel.py
touch gui/authentication_ui.py

touch updater/update.py
touch updater/license_manager.py

touch jobs/job_runner.py
touch jobs/template_loader.py

touch utils/plugin_loader.py
touch utils/file_writer.py
touch utils/session_storage.py

touch configs/default_settings.json
touch configs/job_templates.json
touch logs/app.log

touch api_mode/server.py
touch scheduler/job_scheduler.py

echo "📦 Initializing virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "📜 Installing dependencies..."
pip install --upgrade pip
pip install playwright PySide6 requests pandas openpyxl reportlab aiohttp python-dotenv beautifulsoup4

# Optional: Install 2captcha SDK
pip install twocaptcha

# Optional: install PyInstaller for packaging
pip install pyinstaller

# Add basic requirements.txt
cat > requirements.txt <<EOL
playwright
PySide6
requests
pandas
openpyxl
reportlab
aiohttp
python-dotenv
beautifulsoup4
twocaptcha
pyinstaller
EOL

echo "📥 Installing Playwright browsers..."
playwright install

echo "✅ Setup complete. Project ready at ./$PROJECT_NAME"
