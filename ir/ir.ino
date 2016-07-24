int input;

void setup()
{
	Serial.begin(9600);
}

void loop()
{
	input = analogRead(0);
	Serial.println(input);
}
