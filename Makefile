APP = comunidadedevops-restapi-flask

test:
	@flake8 . --exclude .venv
	@pytest -v --disable-warnings


compose: 
	@docker-compose build
	@docker-compose up


prune:
	@docker container prune

heroku:
	@heroku container:login
	@heroku container:push -a $(APP) web
	@heroku container:release -a $(APP) web
	@heroku ps:scale -a $(APP) web=1
logs:
	@heroku logs --tail -a $(APP)