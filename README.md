## Deutsche Bahn API

This project is **not affiliated with, endorsed by, or sponsored by Deutsche Bahn AG or any of its subsidiaries**.  

It is a non-commercial hobby project for private use. The project retrieves timetable and departure information from the official **DB API Marketplace – Timetables API** and formats the returned data for display.  

### API access

To use the project, you need your own credentials for the DB API Marketplace.  

1. Create or use a DB customer account and register for the DB API Marketplace.  
2. Create an application in the Marketplace.  
3. Subscribe your application to the **Timetables** API.  
4. Use the Client ID and Client Secret (API Key) provided for your application.  

You can access the DB API Marketplace here:  

https://developers.deutschebahn.com/db-api-marketplace/apis/product  

The DB API Marketplace documentation states that the Timetables API provides information about arrivals, departures, and train journeys. The API is subject to the applicable DB API Marketplace terms and the specific license and usage conditions of the Timetables API.  

**Do not publish your Client Secret / API Key.** Store your credentials locally or in environment variables and do not commit them to this repository.  

### Data and attribution

Timetable data is provided through the Deutsche Bahn Timetables API. The Timetables API documentation specifies that the dataset is provided under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.  

Please refer to the official DB API Marketplace documentation and applicable terms for the current conditions of use:  

https://developers.deutschebahn.com/db-api-marketplace/apis/product/timetables  

https://developers.deutschebahn.com/db-api-marketplace/apis/nutzungsbedingungen  
