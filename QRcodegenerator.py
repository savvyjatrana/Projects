import qrcode
from PIL import Image

upi_id=input("Enter your upi ID: ")

#UPI://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=Currency&tn=Message
#mc=merchant code


phone_pay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_pay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


def generate_qr_code(data, filename):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black" , back_colour="white")
    img.save(filename)
    img.show()
        

generate_qr_code(phone_pay_url, 'phone_pay_qr.png')
generate_qr_code(paytm_pay_url, 'paytm_pay_qr.png')
generate_qr_code(google_pay_url, 'google_pay_qr.png')








