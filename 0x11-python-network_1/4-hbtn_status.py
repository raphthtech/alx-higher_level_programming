#!/usr/bin/python3
"""
same as 0-hbtn_status with requests model
"""

if __name__ == '__main__':
    import requests
    html = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(html.text.__class__))
    print("\t- content: {}".format(html.text))
