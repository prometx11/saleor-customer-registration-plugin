from typing import Any
import logging
from saleor.plugins.base_plugin import BasePlugin, ConfigurationTypeField
from saleor.account.models import Address
from saleor.account.utils import store_user_address
from saleor.plugins.manager import get_plugins_manager 
from saleor.checkout import AddressType

logger = logging.getLogger(__name__)

class CustomCustomerRegistration(BasePlugin):
    PLUGIN_ID = "plugin.customCustomerRegistration"  # plugin identifier
    PLUGIN_NAME = "Custom Customer Registration"  # display name of plugin
    PLUGIN_DESCRIPTION = "Enables customer registration with address."
    
    def customer_created(self, customer: "User", previous_value: Any) -> Any:
        logger.info("CustomCustomerRegistration customer_updated hook invoked...")
        if customer.metadata:
            if "address" in customer.metadata:
                logger.info("customer has billing address in metadata")
                addr = Address()
                addr.first_name = customer.metadata["firstName"]
                addr.last_name=  customer.metadata["lastName"]
                addr.street_address_1 = customer.metadata["street"]
                addr.city =customer.metadata["city"]
                addr.postal_code = customer.metadata["postalCode"]
                addr.country = customer.metadata["country"]
                addr.save()                
             
                manager = get_plugins_manager()
                logger.info("storing billing address...")
                store_user_address(customer, addr, AddressType.BILLING, manager)
                logger.info("storing same address as shipping address...")  
                store_user_address(customer, addr, AddressType.SHIPPING, manager)  
                logger.info("deleting billing address metadata...")
                del customer.metadata["address"]
                del customer.metadata["firstName"]
                del customer.metadata["lastName"]
                del customer.metadata["street"]
                del customer.metadata["city"]
                del customer.metadata["postalCode"]
                del customer.metadata["country"]
                customer.save(update_fields=["metadata", "updated_at"])
                
            if "shipping_address" in customer.metadata: 
                logger.info("customer has extra shipping address metadata")                      
                sAddr = Address()
                sAddr.first_name = customer.metadata["shipping_firstName"]
                sAddr.last_name=  customer.metadata["shipping_lastName"]
                sAddr.street_address_1 = customer.metadata["shipping_street"]
                sAddr.city =customer.metadata["shipping_city"]
                sAddr.postal_code = customer.metadata["shipping_postalCode"]
                sAddr.country = customer.metadata["shipping_country"]
                sAddr.save()       
                        
                logger.info("storing shipping address...")
                manager = get_plugins_manager()
                store_user_address(customer, sAddr, AddressType.SHIPPING, manager)  
                
                logger.info("deleting shipping address metadata...")
                del customer.metadata["shipping_address"]
                del customer.metadata["shipping_firstName"]
                del customer.metadata["shipping_lastName"]
                del customer.metadata["shipping_street"]
                del customer.metadata["shipping_city"]
                del customer.metadata["shipping_postalCode"]
                del customer.metadata["shipping_country"]
                customer.save(update_fields=["metadata", "updated_at"])
                
                
        
        
    # def customer_updated(self, customer: "User", previous_value: Any) -> Any:
    #     print("CustomCustomerRegistration customer_updated hook invoked...",customer.metadata)
       
    #     if(customer.is_active): 
    #         print("customer active with metadata type", type(customer.metadata))
    #         print("address in metadata?", "address" in customer.metadata)
    #         if("address" in customer.metadata):
    #             print("customer has billing address in metadata")
    #             addr = Address()
    #             addr.first_name = customer.metadata["firstName"]
    #             addr.last_name=  customer.metadata["lastName"]
    #             addr.street_address_1 = customer.metadata["street"]
    #             addr.city =customer.metadata["city"]
    #             addr.postal_code = customer.metadata["postalCode"]
    #             addr.country = customer.metadata["country"]
    #             addr.save()
                
    #             print("storing billing address...")
    #             manager = get_plugins_manager()
    #             store_user_address(customer, addr, AddressType.BILLING, manager)  
                
    #             print("deleting billing address metadata...")
    #             del customer.metadata["address"]
    #             del customer.metadata["firstName"]
    #             del customer.metadata["lastName"]
    #             del customer.metadata["street"]
    #             del customer.metadata["city"]
    #             del customer.metadata["postalCode"]
    #             del customer.metadata["country"]
    #             customer.save(update_fields=["metadata", "updated_at"])
                
    #         if("shipping_address" in customer.metadata):
    #             print("customer has extra shipping address metadata")                      
    #             sAddr = Address()
    #             sAddr.first_name = customer.metadata["shipping_firstName"]
    #             sAddr.last_name=  customer.metadata["shipping_lastName"]
    #             sAddr.street_address_1 = customer.metadata["shipping_street"]
    #             sAddr.city =customer.metadata["shipping_city"]
    #             sAddr.postal_code = customer.metadata["shipping_postalCode"]
    #             sAddr.country = customer.metadata["shipping_country"]
    #             sAddr.save()       
                        
    #             print("storing shipping address...")
    #             manager = get_plugins_manager()
    #             store_user_address(customer, sAddr, AddressType.SHIPPING, manager)  
                
    #             print("deleting shipping address metadata...")
    #             del customer.metadata["shipping_address"]
    #             del customer.metadata["shipping_firstName"]
    #             del customer.metadata["shipping_lastName"]
    #             del customer.metadata["shipping_street"]
    #             del customer.metadata["shipping_city"]
    #             del customer.metadata["shipping_postalCode"]
    #             del customer.metadata["shipping_country"]
    #             customer.save(update_fields=["metadata", "updated_at"])
        