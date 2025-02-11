"""
CostExplorer ->
   monthlyCostList(customerId)
   annualCost(customerId)

[
  {BASIC, 9.99},
  {STANDARD, 49.99}, 
  {PREMIUM, 249.99}
]

Customer -> c1
Jira
Subscription - BASIC, 5th Jan 2025
Date1: 05-01-2025
[
    Jan(27 * 9.99)
    Feb(= 9.99)
]

Date1: 05-07-2025
[
    Jan(=0)
    Feb(=0)
    July(27 * 9.99)
    September(= 9.99)
]

"""

"""
Customer (id, name)
Product(id, name)
Plan(id, name, pricing)
Subscriptions(id, customerId, productId, planId, startDate, endDate)

YTD?

"""
from abc import ABC, abstractmethod
import datetime


class SubscriptionPlan(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def price(self):
        pass


class Basic:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Standard(SubscriptionPlan):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Premium(SubscriptionPlan):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.subscriptions = []

    def addSubscriptions(self, subscription):
        self.subscriptions.append(subscription)


class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Subscription:
    def __init__(self, id, customerId, productId, planId, startDate):
        self.id = id
        self.customerId = customerId
        self.productId = productId
        self.subscriptionPlan = planId
        self.startDate = startDate


class CostExplorer:
    def __init__(self, customers, products, subcriptions, plans):
        self.months = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        self.customers = {}
        self.initilizeCustomers(customers)
        self.products = {}
        self.initilizeProducts(products)
        self.subscriptions = {}
        self.initializeSubscriptions(subcriptions)
        self.plans = {}
        self.initilizePLans(plans)

    def initilizePLans(self, plans):
        for plan in plans:
            if plan["name"] == "BASIC":
                p = Basic(plan["id"], plan["name"], plan["price"])
                self.plans[plan["id"]] = p

    def initilizeCustomers(self, customers):
        for customer in customers:
            c = Customer(customer["id"], customer["name"])
            self.customers[customer["id"]] = c

    def initilizeProducts(self, products):
        for product in products:
            p = Product(product["id"], product["name"])
            self.products[product["id"]] = p

    def initializeSubscriptions(self, subscriptions):
        for sub in subscriptions:
            s = Subscription(
                sub["id"],
                sub["customerId"],
                sub["productId"],
                sub["subscriptionPlan"],
                sub["startDate"],
            )
            self.subscriptions[sub["id"]] = s

    def monthlyCostList(self, customerId, productId=None):
        # print(self.plans, self.subscriptions, self.customers, self.products)
        customerSubscriptions = []

        for subId, sub in self.subscriptions.items():
            if sub.customerId == customerId:
                customerSubscriptions.append(sub)

        totalCost = {}
        for sub in customerSubscriptions:
            planId = sub.subscriptionPlan
            plan = self.plans[planId]
            price = plan.price
            dt = datetime.datetime.strptime(sub.startDate, "%m/%d/%y %H:%M:%S")
            days = self.months[dt.month] - dt.day + 1
            proratedPrice = (days * price) / self.months[dt.month]
            for month, days in self.months.items():
                cost = 0
                # print(dt.month, month, days)
                if month > dt.month:
                    cost = price
                elif dt.month == month:
                    cost = float(proratedPrice)
                totalCost[month] = cost

        return totalCost

    def monthlyCostListFollowUp(self, customerId, productId=None):
        # print(self.plans, self.subscriptions, self.customers, self.products)
        customerSubscriptions = []

        for subId, sub in self.subscriptions.items():
            if sub.customerId == customerId:
                customerSubscriptions.append(sub)

        totalCost = {"Jan": 0, "Feb": 0}
        for sub in customerSubscriptions:
            planId = sub.subscriptionPlan
            plan = self.plans[planId]
            price = plan.price
            startDate = datetime.datetime.strptime(sub.startDate, "%m/%d/%y %H:%M:%S")
            endDate = None
            if sub.endDate:
                endDate = datetime.datetime.strptime(sub.endDate, "%m/%d/%y %H:%M:%S")

            days = self.months[dt.month] - dt.day + 1
            proratedPrice = (days * price) / self.months[dt.month]
            for month, days in self.months.items():
                cost = 0
                print(dt.month, month, days)
                if month < dt.month:
                    pass
                elif month > dt.month:
                    cost = price
                elif dt.month == month:
                    cost = float(proratedPrice)
                totalCost[month] += cost

        return totalCost

    def annualCost(customerId, productId=None):
        pass


customers = [
    {
        "id": 1,
        "name": "John 1",
    },
    {
        "id": 2,
        "name": "John 2",
    },
]
products = [{"id": 1, "name": "Jira"}, {"id": 2, "name": "Confluence"}]

subscriptionPlans = [
    {"id": 1, "name": "BASIC", "price": 9.99},
    {"id": 1, "name": "STANDARD", "price": 49.99},
    {"id": 1, "name": "PREMIUM", "price": 249.99},
]

subscriptions = [
    {
        "id": 1,
        "customerId": 1,
        "productId": 1,
        "subscriptionPlan": 1,
        "startDate": "06/16/25 13:55:26",
        "endDate": "06/30/25 13:55:26",
    },
    {
        "id": 1,
        "customerId": 1,
        "productId": 1,
        "subscriptionPlan": 1,
        "startDate": "07/01/25 13:55:26",
        # 'startDate': '06/30/25 13:55:26',
    },
]


costExplorer = CostExplorer(customers, products, subscriptions, subscriptionPlans)
print(costExplorer.monthlyCostList(1))
