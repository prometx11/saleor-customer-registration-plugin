from typing import Any
from saleor.plugins.base_plugin import BasePlugin, ConfigurationTypeField
from saleor.account.models import Address
from saleor.account.utils import store_user_address
from saleor.plugins.manager import get_plugins_manager 
from saleor.checkout import AddressType

class CustomCustomerRegistration(BasePlugin):
    PLUGIN_ID = "plugin.customCustomerRegistration"  # plugin identifier
    PLUGIN_NAME = "Custom Customer Registration"  # display name of plugin
    PLUGIN_DESCRIPTION = "Enables customer registration with address."
    
    def customer_updated(self, customer: "User", previous_value: Any) -> Any:
        print("CustomCustomerRegistration customer_updated hook invoked...",customer.metadata)
        # customer.first_name = "test132"
        # update_fields = ["first_name"]
        # customer.save(update_fields=update_fields)
        if(customer.is_active): 
            print("customer active with metadata type", type(customer.metadata))
            print("address in metadata?", "address" in customer.metadata)
            if("address" in customer.metadata):
                print("customer has billing address in metadata")
                addr = Address()
                addr.first_name = customer.metadata["firstName"]
                addr.last_name=  customer.metadata["lastName"]
                addr.street_address_1 = customer.metadata["street"]
                addr.city =customer.metadata["city"]
                addr.postal_code = customer.metadata["postalCode"]
                addr.country = customer.metadata["country"]
                addr.save()
                print("storing billing address...")
                manager = get_plugins_manager()
                store_user_address(customer, addr, AddressType.BILLING, manager)  
                
            if("shipping_address" in customer.metadata):
                print("customer has extra shipping address metadata")                      
                sAddr = Address()
                sAddr.first_name = customer.metadata["shipping_firstName"]
                sAddr.last_name=  customer.metadata["shipping_lastName"]
                sAddr.street_address_1 = customer.metadata["shipping_street"]
                sAddr.city =customer.metadata["shipping_city"]
                sAddr.postal_code = customer.metadata["shipping_postalCode"]
                sAddr.country = customer.metadata["shipping_country"]
                sAddr.save()               
                print("storing shipping address...")
                manager = get_plugins_manager()
                store_user_address(customer, sAddr, AddressType.SHIPPING, manager)  
        