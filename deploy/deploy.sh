../git checkout main
../git pull

EXIST_BLUE=$(docker ps | grep ordersvc-blue)

echo Deploy blue...

if [ -n "$EXIST_BLUE" ]; then
	sudo docker-compose stop blue
	sudo docker-compose start blue
else
	sudo docker-compose start blue
fi


EXIST_GREEN=$(docker ps | grep ordersvc-green)

echo Deploy green...

if [ -n "$EXIST_GREEN" ]; then
	sudo docker-compose stop green
	sudo docker-compose start green
else
	sudo docker-compose start green
fi

EXIST_BLUE=$(docker ps | grep ordersvc-blue)
EXIST_GREEN=$(docker ps | grep ordersvc-green)

if [ -n "$EXIST_BLUE" && -n "$EXIST_GREEN"]; then
  echo Deploy Finish!!
else
  echo Deploy Failed!!!
fi
