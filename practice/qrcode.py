import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERRORCORRECT_H,
                box_size=10,border=4)
qr.add_data("https://www,.youtbe.com/")
qr.make(fit=TRUE)
img=qr.make_image(fill_color="red",backcolor="blue")
img.save("youtube.png")
