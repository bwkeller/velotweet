#define FORCE 1 //Work = Force*Distance
#define RADIUS 32 // All units will be in cgs MOTHAFUCKA
#define CIRCUM 204 // All units will be in cgs MOTHAFUCKA

unsigned long rotations;//How many times the wheel has completed one rotation
unsigned long speed;
unsigned long power;
unsigned long lasttime;

void setup()
{
	Serial.begin(9600);
	rotations = 0;
	lasttime = millis();
	attachInterrupt(0, rotated, RISING);
}

void loop()
{
	Serial.print("STATUS:");
	Serial.print("\t");
	Serial.print(speed);
	Serial.print("\t");
	Serial.print(CIRCUM*rotations);
	Serial.print("\t");
	Serial.print(power);
	Serial.print("\n");
}

void rotated()
{
	unsigned long period = millis() - lasttime;
	lasttime += period;
	rotations++;
	power = FORCE*CIRCUM/period;
	speed = CIRCUM/period;
}
