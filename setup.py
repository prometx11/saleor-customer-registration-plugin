import setuptools

setuptools.setup(
    name='custom-customer-registration',
    version='0.1.8',
    description='Saleor plugin for customer registration with address.',    
    # long_description='Saleor plugin for customer registration with address.',
    # url='https://github.com/',
    author='David Janisch',
    author_email='',
    license='MIT',
    packages=['custom_customer_registration'],
    entry_points={
        'saleor.plugins': ['custom_customer_registration=custom_customer_registration.plugin:CustomCustomerRegistration'],
    },     
    # python_requires=">=3.6", 
)
