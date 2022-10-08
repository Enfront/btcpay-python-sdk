from btcpay.client import BTCPayClient


class PullPayments(BTCPayClient):
    def __init__(self) -> None:
        super().__init__()

        self.management_uri = '/stores/' + self.store_id + '/pull-payments/'
        self.public_uri = '/pull-payments/'

    """
    Gets a store's pull payments
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/PullPayments_GetPullPayments
    """
    @classmethod
    def get_pull_payments(cls, include_archived: bool = False):
        instance = cls()
        altered_uri = instance.management_uri + '?includeArchived=' + str(include_archived)

        return instance._get_request(altered_uri)

    """
    Get a specific pull payment
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/PullPayments_GetPullPayment
    """
    @classmethod
    def get_pull_payment(cls, pull_payment_id: str):
        instance = cls()
        return instance._get_request(instance.public_uri + pull_payment_id)

    """
    Get a specific payout
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/PullPayments_GetPayout
    """
    @classmethod
    def get_pull_payment_payout(cls, pull_payment_id: str, payout_id: str):
        instance = cls()
        altered_uri = instance.public_uri + pull_payment_id + '/payouts/' + payout_id

        return instance._get_request(altered_uri)

    """
    Get all payouts
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/PullPayments_GetPayouts
    """
    @classmethod
    def get_pull_payment_payouts(cls, pull_payment_id: str, include_canceled: bool = False):
        instance = cls()
        altered_uri = instance.public_uri + pull_payment_id + '/payouts?includeCancelled=' + str(include_canceled)

        return instance._get_request(altered_uri)

    """
    Create a new pull payment
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/PullPayments_CreatePullPayment
    """
    @classmethod
    def create_pull_payment(cls, **kwargs):
        instance = cls()
        return instance._post_request(instance.management_uri, kwargs)

    """
    Create a pull payment payout
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/PullPayments_CreatePayout
    """
    @classmethod
    def create_pull_payment_payout(cls, pull_payment_id: str, **kwargs):
        instance = cls()
        altered_uri = instance.public_uri + pull_payment_id + '/payouts'

        return instance._post_request(altered_uri, kwargs)

    """
    Archive a pull payment - this will cancel all payouts awaiting payment
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/PullPayments_ArchivePullPayment
    """
    @classmethod
    def archive_pull_payment(cls, pull_payment_id: str):
        instance = cls()
        return instance._delete_request(instance.management_uri + pull_payment_id)