git checkout main
git pull

EXIST_BLUE=$(docker ps | grep ordersvc-blue)

echo Deploy blue...

if [ -n "$EXIST_BLUE" ]; then
	docker-compose stop blue
	docker-compose start blue
else
	docker-compose start blue
fi


EXIST_GREEN=$(docker ps | grep ordersvc-green)

echo Deploy green...

if [ -n "$EXIST_GREEN" ]; then
	docker-compose stop green
	docker-compose start green
else
	docker-compose start green
fi

echo Deploy Finish!!
