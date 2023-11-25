  GNU nano 7.2                                                                                                        blink.c                                                                                                                 
#include <bcm2835.h>
#define LED RPI_GPIO_P1_11
int main(int argc, char **argv) {
        if (!bcm2835_init()) return 1;
        bcm2835_gpio_fsel(LED, BCM2835_GPIO_FSEL_OUTP);
        unsigned int delay = 300;
        while(1) {
        bcm2835_gpio_write(LED, HIGH);
        bcm2835_delay(delay);
        bcm2835_gpio_write(LED, LOW);
        bcm2835_delay(delay);
        }
        bcm2835_close();
        return 0;
}



