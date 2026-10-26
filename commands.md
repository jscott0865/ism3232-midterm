# My Terminal Record for Copper Kettle Coffee Roasters
mkdir ism3232-midterm
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
touch business_rules.py main.py README.md requirments.txt gitignore commands.md
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
git init
git remote add origin https://github.com/jscott0865/ism3232-midterm.git

## Virtual Enviroment
```bash
which python3
/Users/jacksonscott0865/ism3232-midterm/.venv/bin/python3
Shows where I am at and which version of Python I am in

tree -L 2
business_rules.py
commands.md
main.py
README.md
requirements.txt
tests
__init__.py
test_business_rules.py
Tree shows all of the folders that I have and the corresponding files

rg 'def '
business_rules.py:def def calculate_bean_cost
...
tests/test_business_rules.py:def test_...
Shows all of my def tests and my 21 test functions

rg -l 'print'
main.py
Only print main.py and doesnt list business_rules.py because it has no print statements

git log --oneline 
7d25799 add 21 units tests covering all rule functions
b94ca68 add main script for shipment report