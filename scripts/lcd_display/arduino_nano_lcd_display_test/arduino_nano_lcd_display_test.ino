#define ENABLE (1 << 7)
#define RS     (1 << 6)

// Function prototypes

void lcdcommand(uint8_t cmd);
void lcddata(uint8_t data);
void lcdinit();
void lcdprint(const char *str);

void setup() {
  DDRD = 0xFF;  // use port B as output

  lcdinit();
  lcdcommand(0x06);   // Move cursor right
  lcdprint("Hello, World!");
  lcdcommand(0xC0);
  lcdprint("Hello, SAP");
}

void loop() {

}

void lcdcommand(uint8_t cmd) {
  // upper byte
  PORTD = ((cmd >> 4) & 0x0F);
  delayMicroseconds(3);
  PORTD = ((cmd >> 4) & 0x0F) | ENABLE;
  delayMicroseconds(3);
  PORTD = ((cmd >> 4) & 0x0F);
  delayMicroseconds(100);

  // lower byte
  PORTD = (cmd & 0x0F);
  delayMicroseconds(3);
  PORTD = (cmd & 0x0F) | ENABLE;
  delayMicroseconds(3);
  PORTD = (cmd & 0x0F);
  delayMicroseconds(100);
}

void lcddata(uint8_t data) {
  // upper byte
  PORTD = ((data >> 4) & 0x0F) | RS;
  delayMicroseconds(3);
  PORTD = ((data >> 4) & 0x0F) | RS | ENABLE;
  delayMicroseconds(3);
  PORTD = ((data >> 4) & 0x0F) | RS;
  delayMicroseconds(100);

  // lower byte
  PORTD = (data & 0x0F) | RS;
  delayMicroseconds(3);
  PORTD = (data & 0x0F) | RS | ENABLE;
  delayMicroseconds(3);
  PORTD = (data & 0x0F) | RS;
  delayMicroseconds(100);
}

void lcdprint(const char *str) {
  while(*str != '\0') {
    lcddata(*str++);
  }
}

void lcdinit() {
  delay(500);       // Wait for LCD to power up
  lcdcommand(0x28); // 4-bit mode, 2 lines, 5x8 font
  lcdcommand(0x0C); // Display ON, Cursor OFF
  lcdcommand(0x01); // Clear display
  delay(500);        // Wait for clear command to complete
}