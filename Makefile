default: build

build:
		docker-compose build
		docker-compose -f docker-compose-test.yml build
run:
		docker-compose up
test:
		docker-compose -f docker-compose-test.yml run test --rm
down:
		docker-compose down
		docker-compose -f docker-compose-test.yml down
