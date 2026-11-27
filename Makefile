build:
	python3 infra/setup.py

up: build
	docker compose -f build/docker-compose.yml up -d --build

down:
	docker compose -f build/docker-compose.yml down

logs:
	docker compose -f build/docker-compose.yml logs -f

clean:
	docker compose -f build/docker-compose.yml down -v
	rm -rf build
