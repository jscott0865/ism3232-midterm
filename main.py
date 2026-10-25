"Main execution for Cooper Kettle Coffee Roasters"

from business_rules import (
    calculate_shipment_total,
    requires_prepayment,
    needs_pallet,
    total_shipped,
    largest_shipment,
    format_shipment_line,
)
shipments = [
    {"buyer": "Uptown Bakery", "bag_price": 14.00, "bags": 10, "partner": False},
    {"buyer": "Vine Cafe", "bag_price": 12.50, "bags": 15, "partner": True},
    {"buyer": "Wren Hotel", "bag_price": 13.00, "bags": 40, "partner": False},
    {"buyer": "Yarrow Cafe", "bag_price": 12.00, "bags": 50, "partner": True},
    {"buyer": "Zenith Grocers", "bag_price": 11.00, "bags": 200, "partner": False},
    {"buyer": "Alder Hotel", "bag_price": 12.00, "bags": 60, "partner": False},
    {"buyer": "Birch Diner", "bag_price": 11.00, "bags": 61, "partner": False},
    {"buyer": "Cove Market", "bag_price": 13.00, "bags": 150, "partner": True},
]
def main() -> None:
    "Generate and print the Cooper Kettle Coffee Roasters shipment report"
    print("Cooper Kettle Coffee Roasters Shipment Report")
    shipment_count = 0
    prepayments_count = 0
    pallets_count = 0

    # Process each shipment
    for shipment in shipments:
        buyer = shipment["buyer"]
        bag_price = shipment["bag_price"]
        bags = shipment["bags"]
        partner = shipment.get("partner", False)

        total = calculate_shipment_total(bag_price, bags, partner)
        prepayment = requires_prepayment(total)
        pallet = needs_pallet(bags, total)

        if prepayment:
            prepayments_count += 1
        if pallet:
            pallets_count += 1

        shipment_count += 1
        print(format_shipment_line(buyer, total, prepayment, pallet))

    # Calculate metrics using functions from business_rules.py
    total_revenue = total_shipped(shipments)
    average_revenue = total_revenue / shipment_count if shipment_count > 0 else 0.0
    largest_buyer = largest_shipment(shipments)

    # Print summary metrics in exact format
    print(f"Shipments: {shipment_count}")
    print(f"Total shipped: ${total_revenue:.2f}")
    print(f"Average shipment total: ${average_revenue:.2f}")
    print(f"Largest shipment total: {largest_buyer}")
    print(f"Prepayments required: {prepayments_count}")
    print(f"Pallets needed: {pallets_count}")

if __name__ == "__main__":
    main()


  