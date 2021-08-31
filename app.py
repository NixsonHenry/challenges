# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping
# calc_shipping()

from pathlib import Path

# path = Path("ecommerce")
# print(path.exists())

# Make a new path by creating a new directory
# path = Path("emails")
# print(path.mkdir())
# print(path.rmdir())

"""
path = Path()
print(path.glob('*'))  # All files in all directories
print(path.glob('*.*')) # Get aAll files that use in the current directory
print(path.glob('*.xls')) # All excel files
print(path.glob('*.py')) # All python files
"""

path = Path()
# for file in path.glob('*.py'):
#     print(file)
for file in path.glob('*'):
    print(file)
