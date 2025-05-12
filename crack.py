from Crypto.PublicKey import RSA

# Same PEM key
pem_data = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgCLZKwacguMDWbWf8mvm
eWFnbqizFFTDu7Jp2VldVtoKmFecx/NOMneUU+JsZv4H17W9RAQDUvnl3l+Uxco6
XIrhw04zLlSn9VqMAoM36OvFhjrpsgLt6PKLZQs71Gj9cegUJLL9rIgCMgXcE8Hf
uMZSgLByfRsHPGjEoHVPz3zbXR5pX2XwOqrs4gE0fmpXVeMs7GDLH8DW06tnTrbI
D3c2aZHJyCRvc1RHY2gCWrO9s5puuVzdWDOE9ms4Nxe3vyCkgOFYShHWxU5FgB6c
YqTVeHUE9ekp1E8MOYV7JyJsT4v65SPftOQ4o6f/Ak/upS7G3LRedEKaV9/zUMz0
NQIDAQAB
-----END PUBLIC KEY-----"""

key = RSA.import_key(pem_data)
print(f"Public exponent (e): {key.e}")
print(f"Modulus (n): {key.n}")
