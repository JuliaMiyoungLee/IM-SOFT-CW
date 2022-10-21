# How to use the Dev Console
## Team QR Code Generators: Julia Lee, William V., Jeffery Zhou
#### How to access:
##### [From the POV of a Windows User. Tested on Microsoft Edge and Chrome]
- F12
- Right click -> inspect
- Top right of browser three dots -> More tools -> Developer tools
- Ctrl + Shift + I

#### Advantages:
- You can make temporary changes to the code to test out what your changes will look like on the website.
- You can access the source code as well as view the files used in serving the webpage in an organized manner.

### Important Features:
- Top left mouse above a box icon / Ctrl + Shift + C: If you click on this, you can now highlight elements on the page with your mouse. Then, you will be directed to the html code that corresponds with the code that you selected.
- Device icon / ctrl + shift + M: You can change the display dimensions and the device type (desktop or mobile) which your display is created for.

#### Elements:
This is where you will find the actual html code corresponding to what elements are being displayed on your screen. You will find that the code can be hidden and displayed according to their tags, which makes reading the code and finding specific elements much easier.

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
