# Spawns a virtual environment
init:
	@if [ ! -d ".venv" ]; then  \
		python -m venv ./.venv; \
	fi

# Installs python tools for development
get-tools: init
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install pipreqs
	.venv/bin/pip install pytest

# Get all the packages the project needs
get-dependencies: init
	.venv/bin/pip install -r requirements.txt

# Destroys local venv
erase-venv:
	rm -rf ./.venv

# Updates the packages for the project based on imports
update-dependencies:
	.venv/bin/pipreqs ./engine --force --savepath ./requirements.txt

test:
