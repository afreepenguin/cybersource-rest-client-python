# Riskv1decisionsDeviceInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cookies_accepted** | **str** | Whether the customer’s browser accepts cookies. This field can contain one of the following values: - &#x60;yes&#x60;: The customer’s browser accepts cookies. - &#x60;no&#x60;: The customer’s browser does not accept cookies.  | [optional] 
**ip_address** | **str** | IP address of the customer.  | [optional] 
**network_ip_address** | **str** | Network IP address of the customer (for example, 10.1.27). A network IP address includes up to 256 IP addresses.  | [optional] 
**host_name** | **str** | DNS resolved hostname from &#x60;ipAddress&#x60;. | [optional] 
**fingerprint_session_id** | **str** | Field that contains the session ID that you send to Decision Manager to obtain the device fingerprint information. The string can contain uppercase and lowercase letters, digits, hyphen (-), and underscore (_). However, do not use the same uppercase and lowercase letters to indicate different session IDs.  The session ID must be unique for each merchant ID. You can use any string that you are already generating, such as an order number or web session ID.  The session ID must be unique for each page load, regardless of an individual’s web session ID. If a user navigates to a profiled page and is assigned a web session, navigates away from the profiled page, then navigates back to the profiled page, the generated session ID should be different and unique. You may use a web session ID, but it is preferable to use an application GUID (Globally Unique Identifier). This measure ensures that a unique ID is generated every time the page is loaded, even if it is the same user reloading the page.  | [optional] 
**http_browser_email** | **str** | Email address set in the customer’s browser, which may differ from customer email.  | [optional] 
**user_agent** | **str** | Customer’s browser as identified from the HTTP header data. For example, &#x60;Mozilla&#x60; is the value that identifies the Netscape browser.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


