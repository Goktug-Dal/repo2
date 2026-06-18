from dataclasses import dataclass
from typing import List
import json

@dataclass
class Account:
    id: int
    name: str
    email: str
    phone: str

class AccountService:
    _accounts = []
    _next_id = 1

    @classmethod
    def create(cls, name, email, phone):
        account = Account(cls._next_id, name, email, phone)
        cls._accounts.append(account)
        cls._next_id += 1
        return account

    @classmethod
    def list_all(cls):
        return cls._accounts

    @classmethod
    def read(cls, account_id):
        for account in cls._accounts:
            if account.id == account_id:
                return account
        return None

    @classmethod
    def update(cls, account_id, name=None, email=None, phone=None):
        account = cls.read(account_id)
        if account:
            if name:
                account.name = name
            if email:
                account.email = email
            if phone:
                account.phone = phone
        return account

    @classmethod
    def delete(cls, account_id):
        account = cls.read(account_id)
        if account:
            cls._accounts.remove(account)
        return account
