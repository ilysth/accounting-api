import enum


class ContactTypes(str, enum.Enum):
    person = "person"
    company = "company"


class PaymentStatuses(str, enum.Enum):
    no_transaction = "no_transaction"
    pending = "pending"
    sent = "sent"
    payed = "payed"
    reminder = "reminder"
    warning = "warning"
    debt_enforcement = "debt_enforcement"
