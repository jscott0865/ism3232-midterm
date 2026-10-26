# ISM3232 Midterm: Cooper Kettle Coffee Roasters

- Name: Jackson Scott
- Version: 1.0?
- Date: October 25th, 2026

## What this program does: This program runs the shipping processes and reporting for the company. It also calculates discounts on larger purchases, determines the shipping fees, evaluates thresholds, and identifies the pallet requirements. Lastly, it summarizes the overall metrics like total revenue, average shipment costs, and the largest buyers into a clean report. 
## Business Rules: 
1. Bean Cost- Cost of shipment which is calculated by # of bags and price per bag
2. Bulk Discounts- A discount ranging from 9-20% based on the tier of the bag, with an additional 4% for order of 20 or more bags.
3. Shipping Fees- A standard fe is added unless the discounted merch reaches a total or exceeds $250
4. Prepayment- Shipments with a total >= $1500.00
5. Pallets- Shipments > 60 bags and a total > $700 requires a pallet.
6. Summary Metrics- tracks total shipment costs, total revenue, average order value, and larger buyers

## How to Run: 
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py

## How to test:
python3 -m pytest -v
ruff check. 

## Files in this repository

business_rules.py
main.py
commands.md
README.md
requirments.txt
.gitignore
tests/__init__.py
tests/test_business_rules.py

I did not use AI