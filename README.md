# BTCPay Python SDK
BTCPay had a Python SDK, but it was using the old legacy API, meaning the way to connect was outdated as well as the
API responses it was giving. This library uses the Greenfield API and will follow the
[documentation](https://docs.btcpayserver.org/API/Greenfield/v1/) provided by the BTCPay Server team.

> As of right now, this is a work in progress and will be updated to add more API calls

## Installation
You don't need this source code unless you want to modify the package. If you just want to use the package, run the 
command:

```sh
pip install btcpay-python-sdk
```

Install from source with:

```sh
python setup.py install
```

### Dependencies
 - Python 2.7+
 - Requests
 - Setuptools

## Usage
The library needs to be configured with your stores api key, store id, and host url.

> To generate an API key, you need to log in to your BTCPay instance, click "Account" in the lower left corner, click 
> "Manage Account", click the "API Keys" tab, and then generate your key.

```python
import btcpay

btcpay.api_key = 'API_KEY_HERE'  # should use an env variable
btcpay.host_url = 'HOST_URL'
btcpay.store_id = 'STORE_ID'

# get all invoices
invoices = btcpay.Invoices.get_invoices()
print(invoices)
```