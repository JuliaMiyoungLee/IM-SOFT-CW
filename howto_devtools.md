# how-to :: Use the Dev Consol
---
## Overview
- You can make temporary changes to the code to test out what your changes will look like on the website.
- You can access the source code as well as view the files used in serving the webpage in an organized manner.

### Estimated Time Cost: 1 hrs

### Prerequisites:
- There may be minor variations across browsers. The current information presented is based on Chrome and has been consistent in Microsoft Edge as well.
- There are various ways to access the consol:
  - F12
  - Right click -> inspect
  - Top right of browser three dots -> More tools -> Developer tools
  - Ctrl + Shift + I

### Important Features:
- Top left mouse above a box icon / Ctrl + Shift + C: If you click on this, you can now highlight elements on the page with your mouse. Then, you will be directed to the html code that corresponds with the code that you selected.
- Device icon / ctrl + shift + M: You can change the display dimensions and the device type (desktop or mobile) which your display is created for.
  - In fact, you can choose to display the screen according to specific device models if you click on "Dimensions: Responsive" on the top right, above the display itself.

#### Elements:
This is where you will find the actual html code corresponding to what elements are being displayed on your screen. You will find that the code can be hidden and displayed according to their tags, which makes reading the code and finding specific elements much easier.

#### Style:
- All of the applied styling to your code can be found under the tab "Styles" found under your "Elements" tab and its contents.
- You're able to directly edit this style and a cool feature is that if you hover your mouse above a line of style, you can check or uncheck that line, letting you easily compare different stylings.
- The Style tab is dynamic, so it changes according to what you have selected in your Elements tab. 
 - If you select the elements within <head> </head> in your elements tab, then you will only be shown style being applied to that element.

#### Consol:
One of the most helpful uses of the consol is that it gives feedback as you run the webpage.

So, if you get the message "Did you mean: __", in the consol you will see a specific error message indicating that the initial search was redirected:
```
DevTools failed to load source map: Could not load content for https://www.google.com/_/mss/boq-search/_/ss/k=boq-search.VisualFrontendUi.U4ZuOINRIQI.L.B1.O/am=AB54H4HiAKjyf4QgEFwAAOgAEhBEMAaSCgcwAQBQEQDVRoEcYAEyJAADgAECYQAAAAAXAMkBEADYCBgAAAAAAFB45wEDAQAAAAAAAAAAIFgxAAAAAAAAIAA0CQAAAACA/d=1/ed=1/rs=AH7-fg7ik8H4K2aWERb_65-UtXEpGVcZMw/unified_viewer_view.css.map: HTTP error: status code 404, net::ERR_HTTP_RESPONSE_CODE_FAILURE
```

There is also a button called "# issues" which gives you an overview of all the feedback messages you may have gotten after running the page.

#### Sources:
- Lists all of the files your webpage is utilizing and where each of those files are located.
- For example, if you were to import fonts in your css style, those downloaded fonts could be found in Sources in whatever folder you had them downloaded in.
- Your static and templates folders along with their respective contents can also be found here if you inspect your webpage from our previous assignments.
- If you click on one of the files from the list, you will be shown a preview of what that file contains in a tab to the right of the list of files.

### Other Notes:
- Network seems fairly interesting as I believe it gives you feedback regarding how quickly each action that your webpage display request needed to go through was completed. However, my limited knowledge regarding network and speed disincline me in utilizing it. In the future, however, it can probably provide insight into what may be causing your webpage to be laggy or whatnot.

### Resources
* https://developer.chrome.com/docs/devtools/
* Observation using our own chrome browsers

---

Accurate as of (last update): 2022-10-21

#### Contributors:
The QR Code Generators  
Julia Lee, pd 2  
William V., pd 2  
Jeffery Zhou, pd 2  
