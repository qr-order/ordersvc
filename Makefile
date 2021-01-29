default: build

build:
		docker-compose build
		docker-compose -f docker-compose-test.yml build
run:
		docker-compose run app
test:
		docker-compose -f docker-compose-test.yml run test
