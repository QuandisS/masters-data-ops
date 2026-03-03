include .env
export

MIGRATIONS_DIR = ./migrations

YOYO_DB := postgresql://$(DB_USER):$(DB_PASSWORD)@$(DB_HOST):$(DB_PORT)/$(DB_NAME)
export YOYO_DB

dev.install:
	pip install -r requirements.txt

db.migration.new:
	yoyo new -m "$(name)" $(MIGRATIONS_DIR)

db.migrate:
	yoyo apply --database $(YOYO_DB)  $(MIGRATIONS_DIR)

db.rollback:
	yoyo rollback --database $(YOYO_DB) $(MIGRATIONS_DIR)
