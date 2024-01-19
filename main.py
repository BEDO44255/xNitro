import httpx
from pystyle import Col , System
from random import choice
import json

nitro_base = "https://discord.com/billing/partner-promotions/1180231712274387115/"

xNitro_art = r"""
         _   ___ __           
   _  __/ | / (_) /__________ 
  | |/_/  |/ / / __/ ___/ __ \
 _>  </ /|  / / /_/ /  / /_/ /
/_/|_/_/ |_/_/\__/_/   \____/ 
                              """

print(Col.light_blue + xNitro_art + Col.reset+"\n")
print(f" {Col.purple}[{Col.cyan}!{Col.purple}] {Col.light_red}Disclaimer : {Col.white}Remember not 100% of the nitros are valid")

number = int(input(f' {Col.purple}[{Col.cyan}?{Col.purple}] {Col.white}How much Nitros you want {Col.purple}>>{Col.reset} '))
start = input(f' {Col.purple}[{Col.cyan}!{Col.purple}] {Col.white}Press enter for launch {Col.light_blue}xNitro{Col.reset}')

System.Clear()

print(Col.light_blue + xNitro_art + Col.reset+"\n")

class xNitro :
    def __init__(self):
        self.url = "https://api.discord.gx.games/v1/direct-fulfillment"
        self.chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        self.headers = {
            "authority" : "api.discord.gx.games" , 
            "method" : "post" , 
            "path": "/v1/direct-fulfillment",
            "scheme":"https",
            "accept":"*/*",
            "Accept-Encoding":"gzip, deflate, br" ,
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7" ,
            "Content-Type":"application/json",
            "Origin":"https://www.opera.com",
            "Referer":"https://www.opera.com/",
            "Sec-Ch-Ua":'"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"' ,
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform" : "Windows",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"cross-site",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
        }

    def generate_userid(self , n) :
        return "".join(choice(self.chars) for y in range(n))

    def Post(self) : 
        partner = f"8ca69cdc-{xNitro.generate_userid(self , 4)}-{xNitro.generate_userid(self , 4)}-{xNitro.generate_userid(self , 4)}-{xNitro.generate_userid(self , 12)}"
        return json.loads(httpx.post(url=self.url , headers=self.headers , json={"partnerUserId" : partner}).text)['token']

for i in range(number) : 
    r = xNitro().Post()
    nitro_url = nitro_base+r

    if 'ey' in r :
        print(f" {Col.purple}[{Col.light_green}+{Col.purple}] {Col.light_blue}Nitro generated and saved in nitros.txt{Col.reset}")
        with open('nitros.txt' , 'a+') as f : 
            f.write(nitro_url+"\n")
    else : 
        print(f" {Col.purple}[{Col.light_red}-{Col.purple}] {Col.red}There is an error{Col.reset}")

input(f" {Col.purple}[{Col.cyan}!{Col.purple}] {Col.light_blue}Finished !!{Col.reset}")