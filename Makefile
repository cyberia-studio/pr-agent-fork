
build-gitlab:
	docker build . -t codiumai/pr-agent:gitlab_webhook --target gitlab_webhook -f docker/Dockerfile && docker-compose up -d