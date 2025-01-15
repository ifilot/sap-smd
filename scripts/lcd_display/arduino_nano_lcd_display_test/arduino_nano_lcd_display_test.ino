#define ENABLE (1 << 0)
#define RS     (1 << 1)
#define DELAY_SMALL 10
#define DELAY_LARGE 100

// Function prototypes

void lcdcommand(uint8_t cmd, uint8_t r = 0);
void lcddata(uint8_t data);
void lcdinit();
void lcdprint(const char *str);

void setup() {
  DDRF = 0xFF;        // use port F as output
  PORTF = 0x00;

  lcdinit();
  lcdprint("Hello, World!");
  lcdcommand(0xC0);
  lcdprint("Hello, SAP");
}

void loop() {
}

void lcdcommand(uint8_t cmd, uint8_t r) {
  // upper byte
  uint8_t ins = (cmd & 0xF0) | r;
  PORTF = ins;
  delayMicroseconds(DELAY_SMALL);
  PORTF = ins | ENABLE;
  delayMicroseconds(DELAY_SMALL);
  PORTF = ins;
  delayMicroseconds(DELAY_LARGE);

  // lower byte
  ins = ((cmd & 0x0F) << 4) | r;
  PORTF = ins;
  delayMicroseconds(DELAY_SMALL);
  PORTF = ins | ENABLE;
  delayMicroseconds(DELAY_SMALL);
  PORTF = ins;
  delayMicroseconds(DELAY_LARGE);
}

void lcddata(uint8_t cmd) {
  lcdcommand(cmd, RS);
}

void lcdprint(const char *str) {
  while(*str != '\0') {
    lcddata(*str++);
  }
}

void lcdinit() {
  lcdcommand(0x33); // set 8-bit mode
  lcdcommand(0x32); // set 4-bit mode
  lcdcommand(0x28); // 4-bit mode, 2 lines, 5x8 font
  lcdcommand(0x01); // clear display
  lcdcommand(0x06); // entry mode: moves cursor to right
  delay(5);
  lcdcommand(0x0C); // display on, cursor off
  delay(DELAY_LARGE);       // Wait for clear command to complete
}