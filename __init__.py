import display
import buttons
import nvs
import mch22

def on_home_button(pressed):
  if pressed:
    mch22.exit_python()

buttons.attach(buttons.BTN_HOME, on_home_button)

t = 0

nickname = nvs.nvs_getstr("owner", "nickname")

font = "permanentmarker36"

text_width = display.getTextWidth(nickname, font)

sintab = [
    0 , 3 , 6 , 9 , 12 , 15 , 18 , 21 , 24 , 28 , 31 , 34 , 37 , 40 , 43 ,
    46 , 48 , 51 , 54 , 57 , 60 , 63 , 65 , 68 , 71 , 73 , 76 , 78 , 81 ,
    83 , 85 , 88 , 90 , 92 , 94 , 96 , 98 , 100 , 102 , 104 , 106 , 108 ,
    109 , 111 , 112 , 114 , 115 , 116 , 118 , 119 , 120 , 121 , 122 ,
    123 , 124 , 124 , 125 , 126 , 126 , 127 , 127 , 127 , 127 , 127 ,
    127 , 127 , 127 , 127 , 127 , 127 , 126 , 126 , 125 , 124 , 124 , 123
        , 122 , 121 , 120 , 119 , 118 , 117 , 115 , 114 , 112 , 111 , 109 ,
    108 , 106 , 104 , 102 , 100 , 99 , 97 , 94 , 92 , 90 , 88 , 86 , 83 ,
    81 , 78 , 76 , 73 , 71 , 68 , 65 , 63 , 60 , 57 , 54 , 52 , 49 , 46 ,
    43 , 40 , 37 , 34 , 31 , 28 , 25 , 22 , 18 , 15 , 12 , 9 , 6 , 3 ,
    0 , -2 , -6 , -9 , -12 , -15 , -18 , -21 , -24 , -27 , -30 , -33 ,
    -36 , -39 , -42 , -45 , -48 , -51 , -54 , -57 , -60 , -62 , -65 ,
    -68 , -70 , -73 , -76 , -78 , -81 , -83 , -85 , -88 , -90 , -92 ,
    -94 , -96 , -98 , -100 , -102 , -104 , -106 , -107 , -109 , -111 ,
    -112 , -114 , -115 , -116 , -118 , -119 , -120 , -121 , -122 , -123 ,
    -124 , -124 , -125 , -126 , -126 , -127 , -127 , -127 , -127 , -127 ,
    -127 , -127 , -127 , -127 , -127 , -127 , -126 , -126 , -125 , -124 ,
    -124 , -123 , -122 , -121 , -120 , -119 , -118 , -117 , -115 , -114 ,
    -113 , -111 , -109 , -108 , -106 , -104 , -103 , -101 , -99 , -97 ,
    -95 , -92 , -90 , -88 , -86 , -83 , -81 , -79 , -76 , -74 , -71 ,
    -68 , -66 , -63 , -60 , -57 , -55 , -52 , -49 , -46 , -43 , -40 ,
    -37 , -34 , -31 , -28 , -25 , -22 , -19 , -16 , -12 , -9 , -6 , -3 ,
]

def show_plasma(t):
  display.drawFill(display.BLACK)
  for j in range(240 / 8):
    for i in range(0, 320 / 8, 4):
      # manual unroll
      color = (128 + sintab[(i+t) % 256] + 128 + sintab[(j+128+sintab[t%256]) % 256]) >> 1
      r = 128 + sintab[(color + t) % 256]
      g = 128 + sintab[(color * 7 + t) % 256]
      b = 128 + sintab[(color * 2 + t) % 256]
      v = r << 16 | g << 8 | b;
      display.drawRect(i * 8, j * 8, 8, 8, True, v)

      i += 1
      color = (128 + sintab[(i+t) % 256] + 128 + sintab[(j+128+sintab[t%256]) % 256]) >> 1
      r = 128 + sintab[(color + t) % 256]
      g = 128 + sintab[(color * 7 + t) % 256]
      b = 128 + sintab[(color * 2 + t) % 256]
      v = r << 16 | g << 8 | b;
      display.drawRect(i * 8, j * 8, 8, 8, True, v)

      i += 1
      color = (128 + sintab[(i+t) % 256] + 128 + sintab[(j+128+sintab[t%256]) % 256]) >> 1
      r = 128 + sintab[(color + t) % 256]
      g = 128 + sintab[(color * 7 + t) % 256]
      b = 128 + sintab[(color * 2 + t) % 256]
      v = r << 16 | g << 8 | b;
      display.drawRect(i * 8, j * 8, 8, 8, True, v)
      
      i += 1
      color = (128 + sintab[(i+t) % 256] + 128 + sintab[(j+128+sintab[t%256]) % 256]) >> 1
      r = 128 + sintab[(color + t) % 256]
      g = 128 + sintab[(color * 7 + t) % 256]
      b = 128 + sintab[(color * 2 + t) % 256]
      v = r << 16 | g << 8 | b;
      display.drawRect(i * 8, j * 8, 8, 8, True, v)
  offset = (320 - text_width) // 2
  display.drawText(offset + 1, 120 - 18 + 1, nickname, 0xffffff, font)
  display.drawText(offset - 1, 120 - 18 - 1, nickname, 0xffffff, font)
  display.drawText(offset , 120 - 18, nickname, 0x000000, font)
  display.flush()

while True:
  show_plasma(t)
  t += 1
