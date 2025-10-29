docker-local-build-run:
	docker build -t dai-mcp .
	docker run -p 8000:8000 dai-mcp:latest

install-dev:
	uv run python3 -m uv pip install -e .
 

all: install-dev  