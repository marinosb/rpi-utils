set -e
for num in "$@"; do
   echo "GPIO $num"
   if [ ! -d "/sys/class/gpio/gpio$num" ]; then
      echo "Creating GPIO $num"
      echo $num > /sys/class/gpio/export
      echo out > /sys/class/gpio/gpio$num/direction
   fi
   echo 1 > "/sys/class/gpio/gpio$num/value"
done
