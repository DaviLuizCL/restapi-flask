APP = restapi

test:
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings


compose: 
	@docker-compose build
	@docker-compose up


prune:
	@docker container prune

heroku:
	@heroku container:push -a comunidadedevops-restapi-flask web
	@heroku container:release -a comunidadedevops-restapi-flask web
	@heroku ps:scale -a comunidadedevops-restapi-flask web=1
logs:
	@heroku logs --tail -a comunidadedevops-restapi-flask