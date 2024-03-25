# Platform Mapper

The platform mapper is used as an abstract class builder to provide unified multi-platform service functionality.

Methods available to custom and generic classes:

- get_nist_urls()

Here are a few examples showing how you would use this in your python code.

```python

from netutils.platform_mapper import os_platform_object_builder

# Create the platform objects to get NIST query URL(s) for.
cisco_ios = os_platform_object_builder("Cisco", "IOS", "15.5(2)S1c")
juniper_junos = os_platform_object_builder("Juniper", "JunOS", "10.2R2.11")

# Get NIST URL for the Cisco IOS object
cisco_ios.get_nist_urls()
# ['https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:cisco:ios:15.5\\(2\\)s1c:*']

# Get NIST URL(s) for the Juniper JunOS object
juniper_junos.get_nist_urls()
# ['https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:juniper:junos:10.2r2:*:*:*:*:*:*:*', 'https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:juniper:junos:10.2:r2:*:*:*:*:*:*']
```

## Custom Parsers

As stated above, this mapper is meant to provided unified utility usage between different platforms/services.  In order to do this, custom parsers are needed so that data can be normalized into values that the services need.  There are two parts **potentially** needed for this to work.
- Version Parsing - Document: [netutils.os_version](lib_use_cases_os_version.md)
- Service Ready Output

### Service Ready Output

"Service Ready Output" means that the utility is providing a readily usable value for the service it is meant to use.  

Using NIST as the example, the URL building utility responsible for "Service Ready Output" is `netutils.nist`. Some popular vendors do not follow NIST standards in regard to how their CPE are defined using delimiters of `:`.

- **Cisco IOS CPE String** - `cpe:2.3:o:cisco:ios:15.5\\(2\\)s1c:*`
    - `15.5\\(2\\)s1c:*` - As seen here, Cisco uses CPE strings that do not include the `:` delimiter, which can be queried using escape characters in the search string.  This is the format of ALL "generic" OS/Other platforms that do not have their own custom NIST URL builder when querying NIST.
    - Service Ready Output - `'https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:cisco:ios:15.5\\(2\\)s1c:*'`

- **Juniper JunOS CPE String** - `cpe:2.3:o:juniper:junos:10.2:r2:*:*:*:*:*:*` 
    - `10.2:r2:*:*:*:*:*:*` - As noted here, one of the provided URLs to query for this Juniper JunOS OS platform includes additional values that follow NIST delimiter structures.  In the case where the parser provides multiple URLs, they will both be evaluated and the CVE from both will be added and associated.
    - Service Ready Output - `['https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:juniper:junos:10.2r2:*:*:*:*:*:*:*', 'https://services.nvd.nist.gov/rest/json/cves/2.0?virtualMatchString=cpe:2.3:o:juniper:junos:10.2:r2:*:*:*:*:*:*']`

## Important Notes
Please see [here](lib_use_cases_nist.md) for documentation on using the NIST utility on its own, as well as information on additional requirements such as obtaining an API Key.
