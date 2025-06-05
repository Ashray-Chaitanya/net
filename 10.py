import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI

// Launch browser and open a test page
WebUI.openBrowser('https://www.w3schools.com')

// Textbox
WebUI.navigateToUrl('https://www.w3schools.com/html/html_forms.asp')
WebUI.setText(findTestObject('Page/input_firstname'), 'Test')

// Checkbox
WebUI.navigateToUrl('https://www.w3schools.com/howto/howto_custom_checkbox.asp')
WebUI.click(findTestObject('Page/checkbox_1'))

// Combo box
WebUI.navigateToUrl('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')
WebUI.switchToFrame(findTestObject('Page/frame_iframeResult'), 5)
WebUI.selectOptionByValue(findTestObject('Page/select_cars'), 'volvo', false)

// File upload
WebUI.navigateToUrl('https://demo.guru99.com/test/upload/')
WebUI.uploadFile(findTestObject('Page/input_upload'), 'C:\\path\\to\\file.txt')

// Alert
WebUI.navigateToUrl('https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert')
WebUI.switchToFrame(findTestObject('Page/frame_iframeResult'), 5)
WebUI.click(findTestObject('Page/button_alert'))
WebUI.acceptAlert()

// Scroll
WebUI.executeJavaScript("window.scrollTo(0, document.body.scrollHeight)", null)
WebUI.executeJavaScript("window.scrollTo(0, 0)", null)

// Screenshot
WebUI.takeScreenshot()

// Mouse hover
WebUI.navigateToUrl('https://www.w3schools.com/css/css_dropdowns.asp')
WebUI.mouseOver(findTestObject('Page/button_dropdown'))

// Drag and drop
WebUI.navigateToUrl('https://www.w3schools.com/html/html5_draganddrop.asp')
WebUI.dragAndDropToObject(findTestObject('Page/drag_source'), findTestObject('Page/drag_target'))

// Keystrokes (Google Search)
WebUI.navigateToUrl('https://www.google.com')
WebUI.setText(findTestObject('Page/input_search'), 'Katalon')
WebUI.sendKeys(findTestObject('Page/input_search'), Keys.chord(Keys.ENTER))

WebUI.closeBrowser()
