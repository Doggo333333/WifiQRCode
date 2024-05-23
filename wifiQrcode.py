import qrcode

def generate_wifi_qr(ssid, password, encryption = "WPA"):
    wifi_info = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(wifi_info)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(f'{ssid}_wifi_qr.png')

Your_SSID = input("Enter the SSID (name of wifi)")
Your_Password = input("Enter password")

generate_wifi_qr(Your_SSID, Your_Password)

