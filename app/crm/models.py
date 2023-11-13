from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Table,
    Text,
)
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import object_session, relationship

from app.crm import enums, schemas
from sqlalchemy.ext.declarative import declarative_base
from app.base import Base

contact_relationships = Table(
    "crm_employee_employer_relationships",
    Base.metadata,
    Column("empr_id", ForeignKey("crm_contacts.id")),
    Column("empe_id", ForeignKey("crm_contacts.id")),
)


contact_trades = Table(
    "crm_graph_companies_trades_edges",
    Base.metadata,
    Column("company_id", ForeignKey("crm_contacts.id")),
    Column("trade_type_id", ForeignKey("crm_company_trade_types.id")),
)


class Contact(Base):
    __tablename__ = "crm_contacts"

    id = Column(Integer, primary_key=True, index=True)
    contact_type = Column(Enum(enums.ContactTypes))
    country_id = Column(Integer)
    note = Column(Text, nullable=True)
    name = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    industry = Column(String, nullable=True)
    role = Column(String, nullable=True)
    address = Column(String, nullable=True)
    main_telephone = Column(String, nullable=True)
    direct_telephone = Column(String, nullable=True)
    mobile_phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    direct_email = Column(String, nullable=True)
    business_hours = Column(String, nullable=True)
    tax_id = Column(String, nullable=True)
    image = Column(String, nullable=True)
    shop_url = Column(Text, nullable=True)
    is_supplier = Column(Integer, default=0)
    discount = Column(Numeric, nullable=True)
    payment_terms = Column(Integer, ForeignKey(
        "crm_payment_terms.id"), nullable=True)
    payment_status = Column(Enum(enums.PaymentStatuses), nullable=True)
    company_id = Column(Integer, ForeignKey("crm_contacts.id"), nullable=True)

    attached_files = relationship(
        "AttachedFile", backref="contacts", cascade="all, delete-orphan"
    )

    journal = relationship("accounting.models.Journal",
                           backref="crm_contacts.id")

    trades = relationship("TradeType", secondary=contact_trades)

    company = relationship("Contact", remote_side=[id])

    sub_contacts = relationship(
        "Contact",
        backref="super_contacts",
        secondary=contact_relationships,
        primaryjoin=id == contact_relationships.c.empr_id,
        secondaryjoin=id == contact_relationships.c.empe_id,
    )

    payment_term = relationship("PaymentTerm")


class PaymentTerm(Base):
    __tablename__ = "crm_payment_terms"

    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer, nullable=True, default=0)
    name = Column(String(191), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    credit_days = Column(Integer, nullable=False)
    date_of_due = Column(Text, nullable=True)
    is_deleted = Column(Boolean, nullable=False, server_default="0")


class AttachedFile(Base):
    __tablename__ = "crm_attached_files"

    id = Column(Integer, primary_key=True, index=True)
    file_name = Column(String(250))
    subject = Column(String(100))
    date_uploaded = Column(DateTime)
    dl_file = Column(String(250))
    contact_id = Column(Integer, ForeignKey("crm_contacts.id"))


class TradeType(Base):
    __tablename__ = "crm_company_trade_types"

    id = Column(Integer, primary_key=True, index=True)
    abbr = Column(String(9))
    description = Column(Text)


class ShopAccount(Base):
    __tablename__ = "crm_shop_accounts"

    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    password = Column(String(100))
    user_id = Column(Integer)
    contact_id = Column(Integer, ForeignKey("crm_contacts.id"))
    shop_url = Column(String(2048))
    is_global = Column(Boolean)

    contacts = relationship(Contact, backref="shop_url_accounts")


class Address(Base):
    __tablename__ = "crm_addresses"

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, ForeignKey("crm_contacts.id"))
    country = Column(String(255))
    country_native_name = Column(String(255))
    country_code = Column(String(255))
    province = Column(String(255))
    city = Column(String(255))
    zip_code = Column(String(255))
    premise = Column(String(255))
    street = Column(String(255))
    po_box = Column(String(255))
    address_line_1 = Column(Text)
    address_line_2 = Column(Text)
    address_line_3 = Column(Text)
    crm_format = Column(Text)
    qr_bill_format = Column(Text)

    contact = relationship("Contact", backref="address_field")
    translations = relationship(
        "CountryTranslation",
        primaryjoin="Address.country_code==CountryTranslation.country_code",
        lazy="joined",
    )


class CountryTranslation(Base):
    __tablename__ = "crm_country_translations"

    id = Column(Integer, primary_key=True)
    country_code = Column(String(255), ForeignKey(
        "crm_addresses.country_code"))
    locale = Column(String(255))
    value = Column(String(255))
