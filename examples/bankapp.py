#!/usr/bin/env python


class BankAccount:
    def __init__(self,**kwargs):
        self.accountinfodict = kwargs


    def computebalance(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self,**kwargs):
        do some stuff here
    def computebalance(self):
        only computes balance for a savings account type
        return(self.balance)

class CurrentAccount(BankAccount):
    def __init__(self,**kwargs):
        do some stuff here
    def computebalance(self):
        only computes balances for a current account type

class PensionAccount(BankAccount)



