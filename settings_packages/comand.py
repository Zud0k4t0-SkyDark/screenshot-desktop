import requests



def ngrok_send_Telegram():
    try:
        json_request = requests.get("http://127.0.0.1:4040/api/tunnels")
        url = json_request.json()
        ngrok_url= url["tunnels"][0]["public_url"].split(":")[1].split("//")[1]
        ngrok_port = url["tunnels"][0]["public_url"].split(":")[2]


        message = "\n Take your Ip and Port\nIp\n==> {}\nPort\n==> {}".format(ngrok_url, ngrok_port)
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={message}"
        requests.get(url)
        return "Good"
    except:
        return "Invalid"
    
#ngrok_send_Telegram()