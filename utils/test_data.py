VALID_CREDENTIALS = {"username": "demouser", "password": "abc123"}
INVALID_CREDENTIALS = [
    {"username": "Demouser", "password": "abc123"},
    {"username": "demouser_", "password": "xyz"},
    {"username": "demouser", "password": "nananana"},
    {"username": "demouser", "password": "abc123"}
]
INVOICE_DETAILS = {
    "HotelName": "Rendezvous Hotel",
    "InvoiceDate": "14/01/2018",
    "DueDate": "15/01/2018",
    "InvoiceNumber": "110",
    "BookingCode": "0875",
    "CustomerDetails": "JOHNY SMITHR2, AVENUE DU MAROC123456",
    "Room": "Superior Double",
    "CheckIn": "14/01/2018",
    "CheckOut": "15/01/2018",
    "TotalStayCount": "1",
    "TotalStayAmount": "$150",
    "DepositNow": "USD $20.90",
    "Tax&VAT": "USD $19.00",
    "TotalAmount": "USD $209.00"
}
