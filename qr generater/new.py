# import qrcode as qr
# img=qr.make("6203824530")
# img.save(" Sachin's number.png")

import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("JHUK KE REHNA PADEGA ..🤣🤣😅😂 ")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="pink")
img.save("sachin 2.png")