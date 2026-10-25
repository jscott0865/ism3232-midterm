"Business rules and calculations for Copper Kettle Coffee Roasters."
BAG_THRESHHOLD_LOW = 20
BAG_THRESHHOLD_HIGH = 80
DISCOUNT_LOW = 0.09
DISCOUNT_HIGH = 0.14
PARTNER_DISCOUNT_EXTRA = 0.04
SHIPPING_FEE_THRESHOLD = 250.00
SHIPPING_FEE = 35.00
PREPAYMENT_THRESHOLD = 1500.00
PALLET_BAG_THRESHOLD = 60
PALLET_TOTAL_THRESHHOLD = 700.00

def calculate_bean_cost(bag_price: float, bags:int) -> float:
    "Returns the bean cost before any discount"
    return bag_price * bags
def get_bulk_discount(bags: int, partner: bool = False) -> float:
    "Returns the discount rate as a decimal, so 9% is 0.09"
    if bags < BAG_THRESHHOLD_LOW:
        discount = 0.0
    elif bags < BAG_THRESHHOLD_HIGH:
        discount = DISCOUNT_LOW
    else:
        discount = DISCOUNT_HIGH
    if partner and bags >= BAG_THRESHHOLD_LOW:
        discount += PARTNER_DISCOUNT_EXTRA
    return discount
def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
    "Returns the shipmennt total for one shipment: the discounted cost, and the shipping fee"
    bean_cost = calculate_bean_cost(bag_price, bags)
    discount = get_bulk_discount(bags, partner)
    discounted_cost = bean_cost * (1 - discount)
    if discounted_cost < SHIPPING_FEE_THRESHOLD:
        return discounted_cost + SHIPPING_FEE
    return discounted_cost
def requires_prepayment(total: float) -> bool:
    "Returns True if it requres prepayment, False otherwise"
    return total >= PREPAYMENT_THRESHOLD
def needs_pallet(bags: int, total: float) -> bool:
    "Returns True when the shipment needs a freight pallet, False otherwise"
    return bags >= PALLET_BAG_THRESHOLD and total >= PALLET_TOTAL_THRESHHOLD
def total_shipped(shipments: list) -> float:
    "Returns the sum of the shipments totals for all of them in the list"
    total_sum = 0.0
    for shipment in shipments:
        total_sum += calulate_shipment_total(
            shipment["bag_price"],
            shipment["bags"],
            shipment.get("partner", False)      
        )
    return total_sum
def largest_shipment(shipments: list) -> str:
    "Returns the buyer the shipment with the largest total cost, or None if there are no shipments"
    if not shipments:
        return ""

    largest_buyer = ""
    max_total = -1.0
    for shipment in shipments:
        current_total = calculate_shipment_total(
            shipment["bag_price"],
            shipment["bags"],
            shipment.get("partner", False)
        )
        if current_total > max_total:
            max_total = current_total
            largest_buyer = shipment["buyer"]
    return largest_buyer    
def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str
"Returns one line of the report for a shipment."
    prepayment_str = "Yes" if prepayment else "No"
    pallet_str = "Yes" if pallet else "No"
    return f"{buyer}: ${total:.2f} | prepayment: {prepayment_str} | pallet: {pallet_str}"
 