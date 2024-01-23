"""
Simple application that assign static port to EPG for duplicate IP test
"""
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    """
    assign static port for duplicate IP test
    :return: None
    """
    # Login to APIC
    description = ('Simple application that logs on to the APIC'
                   ' and change speed of an interface.')
    cookie = login("https://[IP ADDRESS]:443/api/aaaLogin.json")

    if not cookie: 
        print('%% Could not login to APIC')

    # Below logic, changes the speed

    http_link="https://[IP ADDRESS]/api/node/mo/uni/tn-Terraform_Tenant/ap-test-app/epg-APP_EPG.xml"
    request_api(http_link, cookie)

def login(url):

    payload = {
        "aaaUser": {
            "attributes": {
                "name": "admin",
                "pwd": "PASSWORD"
            }
        }
    }
    headers = {'Content-Type': "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()

    # PARSE TOKEN AND SET COOKIE
    token = response['imdata'][0]['aaaLogin']['attributes']['token']
    cookie = {}
    cookie['APIC-cookie'] = token
    return cookie

def request_api(add_url, TOKEN):

    header ={'Content-Type': "text/xml",
             # "Accept": "application/json"
             # "X-Aci-Username":"admin",
             # 'X-Aci-Rbac': json.dumps({'domain': 'all', "rolesR": 0, "rolesW": 1}),
             # 'Cookie':json.dumps({'Set-Cookie': TOKEN})
             }
    body = """<fvAEPg name="APP_EPG"><fvRsPathAtt encap="vlan-970" instrImedcy="immediate" mode="regular" primaryEncap="unknown" tDn="topology/pod-1/paths-102/pathep-[eth1/7]"/></fvAEPg>"""
    req = requests.post(url=add_url, data=body, headers=header, cookies=TOKEN, verify=False)
    res = ""

    try:
        resp = json.dumps(req.json(), indent=1)
        # res = json.loads(resp)
    except ValueError as e:
        resp = req.content

    if resp:
        print(resp)
    else:
        print("Could not get data!!!")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
