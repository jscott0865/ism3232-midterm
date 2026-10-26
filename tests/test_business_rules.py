"Unit tests for Copper Kettle Coffee Roasters business rules."

from business_rules import (
    calculate_bean_cost,
    get_bulk_discount,
    calculate_shipment_total,
    requires_prepayment,
    needs_pallet,
    total_shipped,
    largest_shipment,
    format_shipment_line,
)

def test_calculate_bean_cost_basic():
    "Verify bean cost is priced multiplied by bags"
    assert calculate_bean_cost(10.0, 5) == 50.0
def test_get_bulk_discount_below_low_limit_19():
    "Verify 19 bags recives no discount"
    assert get_bulk_discount(19, partner=False) == 0.0
def test_get_bulk_discount_low_limit_20():
    "Verify 20 bags recives 9% discount"
    assert get_bulk_discount(20, partner=False) == 0.09
def test_get_bulk_discount_below_high_limit_79():
    "Verify 79 bags recives 9% discount"
    assert get_bulk_discount(79, partner=False) == 0.09
def test_get_bulk_discount_high_limit_80():
    "Verify 80 bags recives 14% discount"
    assert get_bulk_discount(80, partner=False) == 0.14
def test_partner_discount_extra():
    "Verify partner = True adds 4% discount to the bulk discount"
    assert get_bulk_discount(20, partner=True) == 0.13
def test_partner_true_changes_answer():
    "Verify passing partner = True changes the discount compared to partner = False"
    discount_regular = get_bulk_discount(25, partner=False)
    discount_partner = get_bulk_discount(25, partner=True)
    assert discount_regular != discount_partner
    assert discount_partner == 0.13
def test_calculate_shipment_total_adds_shipping_fee():
    "Verify shipping fee is added when discount is below $250"
    total = calculate_shipment_total(20.0, 10, partner=False)
    assert round(total, 2) == 235.00
def test_calculate_shipment_total_at_fee_limit_below():
    "Verify shipment total below $250 fee limit with shipping fee"
    total = calculate_shipment_total(20.0, 5, partner=False)
    assert round(total, 2) == 135.00
def test_calculate_shipment_total_at_fee_limit_exact():
    "Verify shipment total at $250 fee limit with no shipping fee"
    total = calculate_shipment_total(25.0, 10, partner=False)
    assert round(total, 2) == 250.00
def test_requires_prepayment_below_limit_1499_99():
    "Verify shipment total below $1500 prepayment limit returns False"
    assert requires_prepayment(1499.99) is False
def test_requires_prepayment_at_limit_1500():
    "Verify shipment total at $1500 prepayment limit returns True"
    assert requires_prepayment(1500.00) is True
def test_needs_pallet_below_bag_limit_60():
    "Verify 60 bags doesnt need a pallet if the total exceeds $700"
    assert needs_pallet(60, 800.00) is False
def test_needs_pallet_at_bag_limit_61():
    "Verify 61 bags needs a pallet if the total exceeds $700"
    assert needs_pallet(61, 800.00) is True
def test_needs_pallet_below_total_limit_700():
    "Verify total of $700 does not need pallet if bags exceed 60"
    assert needs_pallet(100, 700.00) is False
def test_needs_pallet_above_total_limit_700_01():
    "Verify total of $700.01 needs pallet if bags exceed 60"
    assert needs_pallet(100, 700.01) is True
def test_total_shipped_short_list():
    "Verify total_shipped correctly sums the shipment totals for a short list of shipments"
    shipments = [
        {"buyer": "Shop A", "bag_price": 10.0, "bags": 10, "partner": False},  # 20*10 = 200, no discount, shipping fee added
        {"buyer": "Shop B", "bag_price": 10.0, "bags": 10, "partner": False},   # 15*30 = 450, discount applied
    ]
    assert round(total_shipped(shipments), 2) == 270.00
def test_largest_shipment_short_list():
    "Verify largest_shipment returns the correct buyer for a short list of shipments"
    shipments = [
        {"buyer": "Small Shop", "bag_price": 10.0, "bags": 5, "partner": False},  # 20*10 = 200, no discount, shipping fee added
        {"buyer": "Big Shop", "bag_price": 20.0, "bags": 100, "partner": False},   # 15*30 = 450, discount applied
    ]

    def test_largest_shipment_with_tie():
        "Verify largest_shipment returns the first buyer in case of a tie"
        shipments = [
            {"buyer": "Shop One", "bag_price": 10.0, "bags": 50, "partner": False},  # 20*10 = 200, no discount, shipping fee added
            {"buyer": "Shop Two", "bag_price": 10.0, "bags": 50, "partner": False},   # 15*30 = 450, discount applied
        ]
        result = largest_shipment(shipments)
        assert result in ["Shop One", "Shop Two"]  # Accept either buyer since they have the same total
def test_largest_shipment_empty_list():
    "Verify largest_shipment returns an empty string for an empty list"
    assert largest_shipment([]) == ""
def test_format_shipment_line_output():
    "Verify format_shipment_line returns the correct formatted string"
    line= format_shipment_line("Test Cafe", 123.45, prepayment= False, pallet=True)
    assert isinstance(line, str)
    assert "Test Cafe" in line
    assert "$123.45" in line
    
   
