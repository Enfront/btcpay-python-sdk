import btcpay

btcpay.api_key = 'API_KEY'  # change this
btcpay.host_url = 'HOST_URL'  # change this
btcpay.store_id = 'STORE_ID'  # change this


def test_get_pull_payments():
    response = btcpay.PullPayments.get_pull_payments()
    assert len(response) != 0


def test_get_pull_payment():
    response = btcpay.PullPayments.get_pull_payment('4SwE88rEw7k8RKQXmgqd81xDPaBP')
    assert len(response) != 0


def test_get_pull_payment_payout():
    response = btcpay.PullPayments.get_pull_payment_payout(
        '2pcLAajAhq9dYZTBouodGopxrWpD',
        '3DNz5WcUTwpvP5SDqhbHtfneeG6G'
    )

    assert len(response) != 0


def test_get_pull_payment_payouts():
    response = btcpay.PullPayments.get_pull_payment_payouts('2pcLAajAhq9dYZTBouodGopxrWpD', include_canceled=True)
    assert len(response) != 0


def test_create_pull_payment():
    test_data = {
        'name': 'Payout for Peter Pettigrew',
        'amount': '0.01',
        'currency': 'BTC',
        'autoApproveClaims': True,
        'paymentMethods': [
            'BTC'
        ]
    }

    response = btcpay.PullPayments.create_pull_payment(**test_data)
    assert len(response) != 0
    
    
def test_create_pull_payment_payout():
    test_data = {
        'destination': '2N9v1EbWL7BjhCSUa3GSc7XVwrHU8Nv4pgN',
        'amount': "0.000099",
        'paymentMethod': 'BTC'
    }

    response = btcpay.PullPayments.create_pull_payment_payout('3uDqpZiPzesEKyQQzEZqaWC4hB4F', **test_data)
    assert len(response) != 0


def test_archive_pull_payment():
    response = btcpay.PullPayments.archive_pull_payment('2tAN3WgG4GGo9fVVQ92qvkLBUCXj')
    assert response is None
