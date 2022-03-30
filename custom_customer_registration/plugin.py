from saleor.plugins.base_plugin import BasePlugin, ConfigurationTypeField

class CustomCustomerRegistration(BasePlugin):
    PLUGIN_ID = "plugin.customCustomerRegistration"  # plugin identifier
    PLUGIN_NAME = "Custom Customer Registration"  # display name of plugin
    PLUGIN_DESCRIPTION = "Enables customer registration with address."
    
    def customer_updated(self, customer: "User"):
        print("CustomCustomerRegistration customer_updated hook invoked...",customer)
        