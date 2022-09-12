import btcpay

btcpay.api_key = 'API_KEY'  # change this
btcpay.host_url = 'HOST_URL'  # change this
btcpay.store_id = 'STORE_ID'  # change this


def test_get_invoices():
    response = btcpay.Invoices.get_invoices()
    assert len(response) != 0


def test_get_invoice():
    response = btcpay.Invoices.get_invoice('MohTqVADdWP9CUXJ7Ubd9v')
    assert len(response) != 0


def test_get_invoice_payment_methods():
    response = btcpay.Invoices.get_invoice_payment_methods('MohTqVADdWP9CUXJ7Ubd9v')
    assert len(response) != 0


def test_create_invoice():
    test_data = {
        "metadata": {
            "orderId": "03ea7e71-2e3a-4ed6-859f-781241784357"
        },
        "checkout": {
            "speedPolicy": "MediumSpeed",
            "defaultPaymentMethod": "BTC",
            "expirationMinutes": 90,
            "monitoringMinutes": 90,
            "paymentTolerance": 0,
            "redirectAutomatically": True,
            "requiresRefundEmail": True
        },
        "amount": "5.00",
        "currency": "USD"
    }

    response = btcpay.Invoices.create_invoice(**test_data)
    assert len(response) != 0


# will most likely fail due to the invoice not being under the right circumstances
def test_mark_invoice_status():
    response = btcpay.Invoices.mark_invoice_status('MohTqVADdWP9CUXJ7Ubd9v', 'invalid')
    assert len(response) != 0


def test_activate_payment_method():
    response = btcpay.Invoices.activate_payment_method('MohTqVADdWP9CUXJ7Ubd9v', 'BTC')
    assert response is None


# broken api method
def test_update_invoice():
    test_data = {
        "metadata": {
            "orderId": 'test_id',
            "orderUrl": 'https://test.com'
        }
    }

    response = btcpay.Invoices.update_invoice('MohTqVADdWP9CUXJ7Ubd9v', test_data)
    assert len(response) != 0


def test_archive_invoice():
    response = btcpay.Invoices.activate_payment_method('MohTqVADdWP9CUXJ7Ubd9v', 'BTC')
    assert response is None
