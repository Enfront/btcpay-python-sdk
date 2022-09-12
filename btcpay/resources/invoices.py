from btcpay.client import BTCPayClient


class Invoices(BTCPayClient):
    def __init__(self) -> None:
        super().__init__()

        self.uri = '/stores/' + self.store_id + '/invoices/'

    """
    Gets all invoices for a single store
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/Invoices_GetInvoices
    """
    @classmethod
    def get_invoices(cls):
        instance = cls()
        return instance._get_request(instance.uri)

    """
    Gets a single invoice based off the invoice id
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/Invoices_GetInvoice
    """
    @classmethod
    def get_invoice(cls, invoice_id: str):
        instance = cls()
        return instance._get_request(instance.uri + invoice_id)

    """
    Gets the available payment methods for a specific invoice
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/Invoices_GetInvoicePaymentMethods
    """
    @classmethod
    def get_invoice_payment_methods(cls, invoice_id: str, accounted: bool = True):
        instance = cls()
        altered_uri = instance.uri + invoice_id + '/payment-methods?accounted=' + str(accounted)

        return instance._get_request(altered_uri)

    """
    Creates a new invoice for a specific store
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/Invoices_CreateInvoice
    """
    @classmethod
    def create_invoice(cls, **kwargs):
        instance = cls()
        return instance._post_request(instance.uri, kwargs)

    """
    @BROKEN?
    
    Mark an invoice as invalid or settled
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/Invoices_MarkInvoiceStatus
    """
    @classmethod
    def mark_invoice_status(cls, invoice_id: str, status: str):
        if status != 'invalid' and status != 'settled':
            raise ValueError('An invoice can only be marked invalid or settled.')

        instance = cls()

        altered_uri = instance.uri + invoice_id + '/status'
        payload = {
            'status': status
        }

        return instance._post_request(altered_uri, payload)

    """
    Unarchive an archived invoice
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/Invoices_UnarchiveInvoice
    """
    @classmethod
    def unarchive_invoice(cls, invoice_id):
        instance = cls()
        altered_uri = instance.uri + invoice_id + '/unarchive'

        return instance._post_request(altered_uri, None)

    """
    Activate a payment method if you are using the lazy mode
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/Invoices_ActivatePaymentMethod
    """
    @classmethod
    def activate_payment_method(cls, invoice_id, payment_method):
        instance = cls()
        altered_uri = instance.uri + invoice_id + '/payment-methods/' + payment_method + '/activate'

        return instance._post_request(altered_uri, None)

    """
    @BROKEN
    
    Update a specific invoice
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/Invoices_UpdateInvoice
    """
    @classmethod
    def update_invoice(cls, invoice_id, metadata):
        instance = cls()
        altered_uri = instance.uri + invoice_id

        return instance._put_request(altered_uri, metadata)

    """
    Archive a specific invoice
    https://docs.btcpayserver.org/API/Greenfield/v1/#operation/Invoices_ArchiveInvoice
    """
    @classmethod
    def archive_invoice(cls, invoice_id):
        instance = cls()
        altered_uri = instance.uri + invoice_id

        return instance._delete_request(altered_uri, None)
