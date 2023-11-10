from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, constr

from app.crm import enums


class CountryTranslation(BaseModel):
    id: Optional[int] = None
    country_code: constr(max_length=255, strip_whitespace=True) = None
    locale: constr(max_length=255, strip_whitespace=True) = None
    value: constr(max_length=255, strip_whitespace=True) = None

    class Config:
        orm_mode = True


class ContactAddressBase(BaseModel):
    contact_id: Optional[int] = None
    country: constr(max_length=255, strip_whitespace=True) = None
    country_native_name: constr(max_length=255, strip_whitespace=True) = None
    country_code: constr(max_length=255, strip_whitespace=True) = None
    province: constr(max_length=255, strip_whitespace=True) = None
    city: constr(max_length=255, strip_whitespace=True) = None
    zip_code: constr(max_length=255, strip_whitespace=True) = None
    street: constr(max_length=255, strip_whitespace=True) = None
    premise: constr(max_length=255, strip_whitespace=True) = None
    po_box: constr(max_length=255, strip_whitespace=True) = None
    address_line_1: constr(strip_whitespace=True) = None
    address_line_2: constr(strip_whitespace=True) = None
    address_line_3: constr(strip_whitespace=True) = None
    crm_format: constr(strip_whitespace=True) = None
    qr_bill_format: constr(strip_whitespace=True) = None
    translations: Optional[List[CountryTranslation]] = None


class ContactAddressCreate(ContactAddressBase):
    country: constr(max_length=255, strip_whitespace=True)
    country_code: constr(max_length=255, strip_whitespace=True)
    city: constr(max_length=255, strip_whitespace=True)
    zip_code: constr(max_length=255, strip_whitespace=True)


class ContactAddress(ContactAddressBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class PaymentTermBase(BaseModel):
    name: str
    country_id: Optional[int] = 0
    description: Optional[str] = None
    credit_days: int = 0
    date_of_due: Optional[str] = None


class PaymentTerm(PaymentTermBase):
    id: int
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True


class TradeTypeBase(BaseModel):
    abbr: str
    description: str


class TradeType(TradeTypeBase):
    id: int

    class Config:
        orm_mode = True


class ContactBase(BaseModel):
    id: Optional[int] = None
    contact_type: Optional[enums.ContactTypes] = None
    name: Optional[constr(max_length=120, strip_whitespace=True)] = None
    company_id: Optional[int] = None
    address: Optional[constr(max_length=500, strip_whitespace=True)] = None
    main_telephone: Optional[constr(max_length=45, strip_whitespace=True)] = None
    direct_telephone: Optional[constr(max_length=45, strip_whitespace=True)] = None
    mobile_phone: Optional[constr(max_length=45, strip_whitespace=True)] = None
    email: Optional[constr(max_length=45, strip_whitespace=True)] = None
    direct_email: Optional[constr(max_length=45, strip_whitespace=True)] = None
    tax_id: Optional[constr(max_length=45, strip_whitespace=True)] = None
    discount: Optional[float] = None
    payment_terms: Optional[int] = -1
    payment_status: Optional[enums.PaymentStatuses] = "no_transaction"
    note: Optional[constr(strip_whitespace=True)] = None
    country_id: Optional[int] = None
    trades: List[TradeType] = []
    image: Optional[constr(max_length=250, strip_whitespace=True)] = None
    address_field: list[ContactAddress] = []


class Company(ContactBase):
    business_hours: Optional[constr(max_length=500, strip_whitespace=True)] = None
    industry: Optional[constr(max_length=120, strip_whitespace=True)] = None
    is_supplier: Optional[int] = 0
    shop_url: Optional[constr(strip_whitespace=True)] = ""
    payment_term: Optional[PaymentTerm] = None
    company: Optional["Company"] = None

    class Config:
        orm_mode = True


class Person(ContactBase):
    last_name: Optional[constr(max_length=120, strip_whitespace=True)]
    first_name: Optional[constr(max_length=120, strip_whitespace=True)]
    role: Optional[constr(max_length=120, strip_whitespace=True)] = None
    payment_term: Optional[PaymentTerm] = None
    company: Optional[Company] = None

    class Config:
        orm_mode = True


class AttachedFileBase(BaseModel):
    file_name: str
    subject: str = None
    dl_file: str = None
    contact_id: int


class AttachedFileCreate(AttachedFileBase):
    pass


class AttachedFile(AttachedFileBase):
    id: int
    date_uploaded: datetime

    class Config:
        orm_mode = True


class ContactNotes(BaseModel):
    rtf_data: str


class CSVPerson(Person):
    company_name: str

    class Config:
        orm_mode = True


class CSVContacts(Company, CSVPerson):
    last_name: Optional[constr(max_length=120, strip_whitespace=True)] = None
    first_name: Optional[constr(max_length=120, strip_whitespace=True)] = None
    role: Optional[constr(max_length=120, strip_whitespace=True)] = None
    company_name: str
    has_parent_company: bool = False
    persons: List[CSVPerson] = None

    class Config:
        orm_mode = True


class ShopAccountBase(BaseModel):
    username: str
    password: str
    user_id: int
    is_global: int


class ShopAccountCreate(ShopAccountBase):
    contact_id: int


class ShopAccount(ShopAccountBase):
    id: int

    class Config:
        orm_mode = True


class UpdateAddress(BaseModel):
    address: str
