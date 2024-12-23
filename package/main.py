"""
When we have conflex set of modules, better to use a package concept
It is must to put a empty __init__.py file in each folder inform pythons
that this folder is a package

"""
from custom_package import main_package
from custom_package.sub_package import sub_package

main_package.hello()
sub_package.hello()
