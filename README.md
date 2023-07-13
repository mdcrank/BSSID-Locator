# BSSID-Locator
## Description
This is a BSSID Locater utilizing googles geolocation API. This was inspired by [Samy Kamkar](http://samy.pl/androidmap/) who initially found an exploit in 2011. This has since been patched, but feature still gives decent information if you have 4 or 5 nearby mac addresses. This code is a basic implementation of googles api to show what it can currently do.

## Use
In order to use this, follow [these directions](https://developers.google.com/maps/documentation/elevation/cloud-setup) to set up your google cloud account. Then replace the YOUR_API_KEY in the code with your own and test it. Then input wifi mac addresses that are nearby and the program will call the api and return back a location. If you dont input enough mac addresses, it will return your current location. 
