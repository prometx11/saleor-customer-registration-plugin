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
        
        addr = Address()
        addr.first_name = "test123"
        addr.user_addresses.add(customer)
        
        