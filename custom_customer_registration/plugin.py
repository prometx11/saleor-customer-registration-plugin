from typing import Any
from saleor.plugins.base_plugin import BasePlugin, ConfigurationTypeField
from saleor.account.models import Address

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
            print("customer activate")
            if("billing_address" in customer.metadata):
                print("customer has billing address metadata")                      
                addr = Address()
                addr.first_name = "firstname"
                addr.last_name= "lastname"
                addr.street_address_1 = "test street"
                addr.city = "test city"
                addr.postal_code = "1223"
                addr.country = "AT"
                addr.save()
                
                addr.user_addresses.add(customer)
                customer.addresses.add(addr)
        