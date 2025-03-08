POETRY_RUN = poetry run

DEV_APP_SOURCE = cd ./app/bot
DEV_APP_ENV = export DOTENV_PATH=$(shell pwd)
DEV_APP_RUN = python run.py

DEV_DOCKER_COMPOSE = docker compose --env-file .env.dev -f docker/docker-compose.dev.yaml

DOCKER_COMPOSE = docker compose --env-file .env -f docker/docker-compose.yaml


<<<<<<< HEAD
dev-app-start:
	${DEV_APP_ENV} && ${DEV_APP_SOURCE} && ${POETRY_RUN} ${DEV_APP_RUN}


dev-db-revision:
	${DEV_APP_ENV} && ${DEV_APP_SOURCE} && ${POETRY_RUN} alembic revision --autogenerate -m "autogenerated migration"


dev-db-migrate:
	${DEV_APP_ENV} && ${DEV_APP_SOURCE} && ${POETRY_RUN} alembic upgrade head


locale-extract:
	${DEV_APP_ENV} && ${DEV_APP_SOURCE} && ${POETRY_RUN} \
	python -m aiogram_i18n multiple-extract -i '.' -o './locales' \
=======
locale-extract:
	${DEV_APP_ENV} && ${DEV_APP_SOURCE} && ${POETRY_RUN} \
	python -m aiogram_i18n multiple-extract \
	-i './routers/' \
	-o './locales' \
>>>>>>> 01a728c (update: DDD)
	--locales "ru" \
	--locales "en" \


locale-types:
	${DEV_APP_ENV} && ${DEV_APP_SOURCE} && ${POETRY_RUN} \
<<<<<<< HEAD
	i18n stub -i "./locales/ru/_default.ftl" -o "./common/types.pyi" 


dev-db-start:
	${DEV_DOCKER_COMPOSE} up -d


dev-db-stop:
	${DEV_DOCKER_COMPOSE} down


dev-docker-ps:
=======
	i18n stub -i "./locales/ru/_default.ftl" -o "./locales/types.pyi" 


development-start:
	${DEV_DOCKER_COMPOSE} up --build -d


development-stop:
	${DEV_DOCKER_COMPOSE} down

development-logs:
	${DEV_DOCKER_COMPOSE} logs

development-ps:
>>>>>>> 01a728c (update: DDD)
	${DEV_DOCKER_COMPOSE} ps


production-start:
	${DOCKER_COMPOSE} up -d

production-stop:
	${DOCKER_COMPOSE} up -d

<<<<<<< HEAD

=======
>>>>>>> 01a728c (update: DDD)
production-logs:
	${DOCKER_COMPOSE} logs
